---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient
title: Class CatalogServiceClient (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:51.801372+00:00
---

# Class CatalogServiceClient (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CatalogServiceClient (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dataplex/google-cloud-dataplex/src/main/java/com/google/cloud/dataplex/v1/CatalogServiceClient.java)| [Product Reference](https://cloud.google.com/dataplex)| [REST Documentation](https://cloud.google.com/dataplex/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dataplex/docs/reference/rpc)  
---|---|---|---  
  
Service Description: The primary resources offered by this service are EntryGroups, EntryTypes, AspectTypes, Entries and EntryLinks. They collectively let data administrators organize, manage, secure, and catalog data located across cloud projects in their organization in a variety of storage systems, including Cloud Storage and BigQuery.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryTypeName name = EntryTypeName.of("[PROJECT]", "[LOCATION]", "[ENTRY_TYPE]");
       EntryType response = catalogServiceClient.getEntryType(name);
     }
     

Note: close() needs to be called on the CatalogServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateEntryType |  Creates an EntryType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEntryTypeAsync(CreateEntryTypeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createEntryTypeAsync(LocationName parent, EntryType entryType, String entryTypeId) 
  * createEntryTypeAsync(String parent, EntryType entryType, String entryTypeId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEntryTypeOperationCallable() 
  * createEntryTypeCallable() 

  
UpdateEntryType |  Updates an EntryType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEntryTypeAsync(UpdateEntryTypeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateEntryTypeAsync(EntryType entryType, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEntryTypeOperationCallable() 
  * updateEntryTypeCallable() 

  
DeleteEntryType |  Deletes an EntryType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEntryTypeAsync(DeleteEntryTypeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteEntryTypeAsync(EntryTypeName name) 
  * deleteEntryTypeAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEntryTypeOperationCallable() 
  * deleteEntryTypeCallable() 

  
ListEntryTypes |  Lists EntryType resources in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEntryTypes(ListEntryTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEntryTypes(LocationName parent) 
  * listEntryTypes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEntryTypesPagedCallable() 
  * listEntryTypesCallable() 

  
GetEntryType |  Gets an EntryType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEntryType(GetEntryTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEntryType(EntryTypeName name) 
  * getEntryType(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEntryTypeCallable() 

  
CreateAspectType |  Creates an AspectType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAspectTypeAsync(CreateAspectTypeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createAspectTypeAsync(LocationName parent, AspectType aspectType, String aspectTypeId) 
  * createAspectTypeAsync(String parent, AspectType aspectType, String aspectTypeId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAspectTypeOperationCallable() 
  * createAspectTypeCallable() 

  
UpdateAspectType |  Updates an AspectType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAspectTypeAsync(UpdateAspectTypeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAspectTypeAsync(AspectType aspectType, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAspectTypeOperationCallable() 
  * updateAspectTypeCallable() 

  
DeleteAspectType |  Deletes an AspectType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAspectTypeAsync(DeleteAspectTypeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAspectTypeAsync(AspectTypeName name) 
  * deleteAspectTypeAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAspectTypeOperationCallable() 
  * deleteAspectTypeCallable() 

  
ListAspectTypes |  Lists AspectType resources in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAspectTypes(ListAspectTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAspectTypes(LocationName parent) 
  * listAspectTypes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAspectTypesPagedCallable() 
  * listAspectTypesCallable() 

  
GetAspectType |  Gets an AspectType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAspectType(GetAspectTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAspectType(AspectTypeName name) 
  * getAspectType(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAspectTypeCallable() 

  
CreateEntryGroup |  Creates an EntryGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEntryGroupAsync(CreateEntryGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createEntryGroupAsync(LocationName parent, EntryGroup entryGroup, String entryGroupId) 
  * createEntryGroupAsync(String parent, EntryGroup entryGroup, String entryGroupId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEntryGroupOperationCallable() 
  * createEntryGroupCallable() 

  
UpdateEntryGroup |  Updates an EntryGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEntryGroupAsync(UpdateEntryGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateEntryGroupAsync(EntryGroup entryGroup, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEntryGroupOperationCallable() 
  * updateEntryGroupCallable() 

  
DeleteEntryGroup |  Deletes an EntryGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEntryGroupAsync(DeleteEntryGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteEntryGroupAsync(EntryGroupName name) 
  * deleteEntryGroupAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEntryGroupOperationCallable() 
  * deleteEntryGroupCallable() 

  
ListEntryGroups |  Lists EntryGroup resources in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEntryGroups(ListEntryGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEntryGroups(LocationName parent) 
  * listEntryGroups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEntryGroupsPagedCallable() 
  * listEntryGroupsCallable() 

  
GetEntryGroup |  Gets an EntryGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEntryGroup(GetEntryGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEntryGroup(EntryGroupName name) 
  * getEntryGroup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEntryGroupCallable() 

  
CreateEntry |  Creates an Entry. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEntry(CreateEntryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createEntry(EntryGroupName parent, Entry entry, String entryId) 
  * createEntry(String parent, Entry entry, String entryId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEntryCallable() 

  
UpdateEntry |  Updates an Entry. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEntry(UpdateEntryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateEntry(Entry entry, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEntryCallable() 

  
DeleteEntry |  Deletes an Entry. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEntry(DeleteEntryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteEntry(EntryName name) 
  * deleteEntry(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEntryCallable() 

  
ListEntries |  Lists Entries within an EntryGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEntries(ListEntriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEntries(EntryGroupName parent) 
  * listEntries(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEntriesPagedCallable() 
  * listEntriesCallable() 

  
GetEntry |  Gets an Entry. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEntry(GetEntryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEntry(EntryName name) 
  * getEntry(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEntryCallable() 

  
LookupEntry |  Looks up an entry by name using the permission on the source system. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * lookupEntry(LookupEntryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * lookupEntryCallable() 

  
ModifyEntry |  Modifies an entry using the permission on the source system. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * modifyEntry(ModifyEntryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * modifyEntryCallable() 

  
SearchEntries |  Searches for Entries matching the given query and scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchEntries(SearchEntriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * searchEntries(LocationName name, String query) 
  * searchEntries(String name, String query) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchEntriesPagedCallable() 
  * searchEntriesCallable() 

  
CreateMetadataJob |  Creates a metadata job. For example, use a metadata job to import metadata from a third-party system into Dataplex Universal Catalog. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMetadataJobAsync(CreateMetadataJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createMetadataJobAsync(LocationName parent, MetadataJob metadataJob, String metadataJobId) 
  * createMetadataJobAsync(String parent, MetadataJob metadataJob, String metadataJobId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMetadataJobOperationCallable() 
  * createMetadataJobCallable() 

  
GetMetadataJob |  Gets a metadata job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMetadataJob(GetMetadataJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMetadataJob(MetadataJobName name) 
  * getMetadataJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMetadataJobCallable() 

  
ListMetadataJobs |  Lists metadata jobs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMetadataJobs(ListMetadataJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMetadataJobs(LocationName parent) 
  * listMetadataJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMetadataJobsPagedCallable() 
  * listMetadataJobsCallable() 

  
CancelMetadataJob |  Cancels a metadata job.  If you cancel a metadata import job that is in progress, the changes in the job might be partially applied. We recommend that you reset the state of the entry groups in your project by running another metadata job that reverts the changes from the canceled job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelMetadataJob(CancelMetadataJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelMetadataJob(MetadataJobName name) 
  * cancelMetadataJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelMetadataJobCallable() 

  
CreateEntryLink |  Creates an Entry Link. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEntryLink(CreateEntryLinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createEntryLink(EntryGroupName parent, EntryLink entryLink, String entryLinkId) 
  * createEntryLink(String parent, EntryLink entryLink, String entryLinkId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEntryLinkCallable() 

  
UpdateEntryLink |  Updates an Entry Link. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEntryLink(UpdateEntryLinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateEntryLink(EntryLink entryLink) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEntryLinkCallable() 

  
DeleteEntryLink |  Deletes an Entry Link. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEntryLink(DeleteEntryLinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteEntryLink(EntryLinkName name) 
  * deleteEntryLink(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEntryLinkCallable() 

  
LookupEntryLinks |  Looks up Entry Links referencing the specified Entry. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * lookupEntryLinks(LookupEntryLinksRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * lookupEntryLinksPagedCallable() 
  * lookupEntryLinksCallable() 

  
LookupContext |  Looks up LLM Context for the specified resources. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * lookupContext(LookupContextRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * lookupContextCallable() 

  
GetEntryLink |  Gets an Entry Link. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEntryLink(GetEntryLinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEntryLink(EntryLinkName name) 
  * getEntryLink(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEntryLinkCallable() 

  
CreateMetadataFeed |  Creates a MetadataFeed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMetadataFeedAsync(CreateMetadataFeedRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createMetadataFeedAsync(LocationName parent, MetadataFeed metadataFeed, String metadataFeedId) 
  * createMetadataFeedAsync(String parent, MetadataFeed metadataFeed, String metadataFeedId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMetadataFeedOperationCallable() 
  * createMetadataFeedCallable() 

  
GetMetadataFeed |  Gets a MetadataFeed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMetadataFeed(GetMetadataFeedRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMetadataFeed(MetadataFeedName name) 
  * getMetadataFeed(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMetadataFeedCallable() 

  
ListMetadataFeeds |  Retrieve a list of MetadataFeeds. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMetadataFeeds(ListMetadataFeedsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMetadataFeeds(LocationName parent) 
  * listMetadataFeeds(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMetadataFeedsPagedCallable() 
  * listMetadataFeedsCallable() 

  
DeleteMetadataFeed |  Deletes a MetadataFeed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteMetadataFeedAsync(DeleteMetadataFeedRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteMetadataFeedAsync(MetadataFeedName name) 
  * deleteMetadataFeedAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteMetadataFeedOperationCallable() 
  * deleteMetadataFeedCallable() 

  
UpdateMetadataFeed |  Updates a MetadataFeed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateMetadataFeedAsync(UpdateMetadataFeedRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateMetadataFeedAsync(MetadataFeed metadataFeed, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateMetadataFeedOperationCallable() 
  * updateMetadataFeedCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of CatalogServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CatalogServiceSettings catalogServiceSettings =
         CatalogServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CatalogServiceClient catalogServiceClient = CatalogServiceClient.create(catalogServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CatalogServiceSettings catalogServiceSettings =
         CatalogServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CatalogServiceClient catalogServiceClient = CatalogServiceClient.create(catalogServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CatalogServiceSettings catalogServiceSettings =
         CatalogServiceSettings.newHttpJsonBuilder().build();
     CatalogServiceClient catalogServiceClient = CatalogServiceClient.create(catalogServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CatalogServiceClient

## Static Methods 

### create()
    
    
    public static final CatalogServiceClient create()

Constructs an instance of CatalogServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CatalogServiceSettings settings)
    
    
    public static final CatalogServiceClient create(CatalogServiceSettings settings)

Constructs an instance of CatalogServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CatalogServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CatalogServiceStub stub)
    
    
    public static final CatalogServiceClient create(CatalogServiceStub stub)

Constructs an instance of CatalogServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CatalogServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CatalogServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.CatalogServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient)` |   
  
## Constructors 

### CatalogServiceClient(CatalogServiceSettings settings)
    
    
    protected CatalogServiceClient(CatalogServiceSettings settings)

Constructs an instance of CatalogServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CatalogServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceSettings)`  
  
  
### CatalogServiceClient(CatalogServiceStub stub)
    
    
    protected CatalogServiceClient(CatalogServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CatalogServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.CatalogServiceStub)`  
  
  
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
  
### cancelMetadataJob(@Nullable MetadataJobName name)
    
    
    public final void cancelMetadataJob(@Nullable MetadataJobName name)

Cancels a metadata job.

If you cancel a metadata import job that is in progress, the changes in the job might be partially applied. We recommend that you reset the state of the entry groups in your project by running another metadata job that reverts the changes from the canceled job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       MetadataJobName name = MetadataJobName.of("[PROJECT]", "[LOCATION]", "[METADATAJOB]");
       catalogServiceClient.cancelMetadataJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.MetadataJobName`  
Required. The resource name of the job, in the format `projects/{project_id_or_number}/locations/{location_id}/metadataJobs/{metadata_job_id}`  
  
### cancelMetadataJob(CancelMetadataJobRequest request)
    
    
    public final void cancelMetadataJob(CancelMetadataJobRequest request)

Cancels a metadata job.

If you cancel a metadata import job that is in progress, the changes in the job might be partially applied. We recommend that you reset the state of the entry groups in your project by running another metadata job that reverts the changes from the canceled job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CancelMetadataJobRequest request =
           CancelMetadataJobRequest.newBuilder()
               .setName(MetadataJobName.of("[PROJECT]", "[LOCATION]", "[METADATAJOB]").toString())
               .build();
       catalogServiceClient.cancelMetadataJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelMetadataJobRequest)`  
The request object containing all of the parameters for the API call.  
  
### cancelMetadataJob(String name)
    
    
    public final void cancelMetadataJob(String name)

Cancels a metadata job.

If you cancel a metadata import job that is in progress, the changes in the job might be partially applied. We recommend that you reset the state of the entry groups in your project by running another metadata job that reverts the changes from the canceled job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = MetadataJobName.of("[PROJECT]", "[LOCATION]", "[METADATAJOB]").toString();
       catalogServiceClient.cancelMetadataJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the job, in the format `projects/{project_id_or_number}/locations/{location_id}/metadataJobs/{metadata_job_id}`  
  
### cancelMetadataJobCallable()
    
    
    public final UnaryCallable<CancelMetadataJobRequest,Empty> cancelMetadataJobCallable()

Cancels a metadata job.

If you cancel a metadata import job that is in progress, the changes in the job might be partially applied. We recommend that you reset the state of the entry groups in your project by running another metadata job that reverts the changes from the canceled job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CancelMetadataJobRequest request =
           CancelMetadataJobRequest.newBuilder()
               .setName(MetadataJobName.of("[PROJECT]", "[LOCATION]", "[METADATAJOB]").toString())
               .build();
       ApiFuture<Empty> future =
           catalogServiceClient.cancelMetadataJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelMetadataJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### close()
    
    
    public final void close()

### createAspectTypeAsync(@Nullable LocationName parent, AspectType aspectType, String aspectTypeId)
    
    
    public final OperationFuture<AspectType,OperationMetadata> createAspectTypeAsync(@Nullable LocationName parent, AspectType aspectType, String aspectTypeId)

Creates an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       AspectType aspectType = AspectType.newBuilder().build();
       String aspectTypeId = "aspectTypeId-423030675";
       AspectType response =
           catalogServiceClient.createAspectTypeAsync(parent, aspectType, aspectTypeId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the AspectType, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
`aspectType` | `[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType)`  
Required. AspectType Resource.  
`aspectTypeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. AspectType identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createAspectTypeAsync(CreateAspectTypeRequest request)
    
    
    public final OperationFuture<AspectType,OperationMetadata> createAspectTypeAsync(CreateAspectTypeRequest request)

Creates an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateAspectTypeRequest request =
           CreateAspectTypeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAspectTypeId("aspectTypeId-423030675")
               .setAspectType(AspectType.newBuilder().build())
               .setValidateOnly(true)
               .build();
       AspectType response = catalogServiceClient.createAspectTypeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateAspectTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createAspectTypeAsync(String parent, AspectType aspectType, String aspectTypeId)
    
    
    public final OperationFuture<AspectType,OperationMetadata> createAspectTypeAsync(String parent, AspectType aspectType, String aspectTypeId)

Creates an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       AspectType aspectType = AspectType.newBuilder().build();
       String aspectTypeId = "aspectTypeId-423030675";
       AspectType response =
           catalogServiceClient.createAspectTypeAsync(parent, aspectType, aspectTypeId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the AspectType, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
`aspectType` | `[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType)`  
Required. AspectType Resource.  
`aspectTypeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. AspectType identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createAspectTypeCallable()
    
    
    public final UnaryCallable<CreateAspectTypeRequest,Operation> createAspectTypeCallable()

Creates an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateAspectTypeRequest request =
           CreateAspectTypeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAspectTypeId("aspectTypeId-423030675")
               .setAspectType(AspectType.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.createAspectTypeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateAspectTypeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAspectTypeOperationCallable()
    
    
    public final OperationCallable<CreateAspectTypeRequest,AspectType,OperationMetadata> createAspectTypeOperationCallable()

Creates an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateAspectTypeRequest request =
           CreateAspectTypeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAspectTypeId("aspectTypeId-423030675")
               .setAspectType(AspectType.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<AspectType, OperationMetadata> future =
           catalogServiceClient.createAspectTypeOperationCallable().futureCall(request);
       // Do something.
       AspectType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateAspectTypeRequest),[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createEntry(@Nullable EntryGroupName parent, Entry entry, String entryId)
    
    
    public final Entry createEntry(@Nullable EntryGroupName parent, Entry entry, String entryId)

Creates an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryGroupName parent = EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]");
       Entry entry = Entry.newBuilder().build();
       String entryId = "entryId-1591558867";
       Entry response = catalogServiceClient.createEntry(parent, entry, entryId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EntryGroupName`  
Required. The resource name of the parent Entry Group: `projects/{project}/locations/{location}/entryGroups/{entry_group}`.  
`entry` | `[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)`  
Required. Entry resource.  
`entryId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Entry identifier. It has to be unique within an Entry Group. Entries corresponding to Google Cloud resources use an Entry ID format based on [full resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name). The format is a full resource name of the resource without the prefix double slashes in the API service name part of the full resource name. This allows retrieval of entries using their associated resource name. For example, if the full resource name of a resource is `//library.googleapis.com/shelves/shelf1/books/book2`, then the suggested entry_id is `library.googleapis.com/shelves/shelf1/books/book2`. It is also suggested to follow the same convention for entries corresponding to resources from providers or systems other than Google Cloud. The maximum size of the field is 4000 characters.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### createEntry(CreateEntryRequest request)
    
    
    public final Entry createEntry(CreateEntryRequest request)

Creates an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateEntryRequest request =
           CreateEntryRequest.newBuilder()
               .setParent(EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
               .setEntryId("entryId-1591558867")
               .setEntry(Entry.newBuilder().build())
               .build();
       Entry response = catalogServiceClient.createEntry(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### createEntry(String parent, Entry entry, String entryId)
    
    
    public final Entry createEntry(String parent, Entry entry, String entryId)

Creates an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString();
       Entry entry = Entry.newBuilder().build();
       String entryId = "entryId-1591558867";
       Entry response = catalogServiceClient.createEntry(parent, entry, entryId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent Entry Group: `projects/{project}/locations/{location}/entryGroups/{entry_group}`.  
`entry` | `[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)`  
Required. Entry resource.  
`entryId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Entry identifier. It has to be unique within an Entry Group. Entries corresponding to Google Cloud resources use an Entry ID format based on [full resource names](https://cloud.google.com/apis/design/resource_names#full_resource_name). The format is a full resource name of the resource without the prefix double slashes in the API service name part of the full resource name. This allows retrieval of entries using their associated resource name. For example, if the full resource name of a resource is `//library.googleapis.com/shelves/shelf1/books/book2`, then the suggested entry_id is `library.googleapis.com/shelves/shelf1/books/book2`. It is also suggested to follow the same convention for entries corresponding to resources from providers or systems other than Google Cloud. The maximum size of the field is 4000 characters.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### createEntryCallable()
    
    
    public final UnaryCallable<CreateEntryRequest,Entry> createEntryCallable()

Creates an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateEntryRequest request =
           CreateEntryRequest.newBuilder()
               .setParent(EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
               .setEntryId("entryId-1591558867")
               .setEntry(Entry.newBuilder().build())
               .build();
       ApiFuture<Entry> future = catalogServiceClient.createEntryCallable().futureCall(request);
       // Do something.
       Entry response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryRequest),[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)>` |   
  
### createEntryGroupAsync(@Nullable LocationName parent, EntryGroup entryGroup, String entryGroupId)
    
    
    public final OperationFuture<EntryGroup,OperationMetadata> createEntryGroupAsync(@Nullable LocationName parent, EntryGroup entryGroup, String entryGroupId)

Creates an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       EntryGroup entryGroup = EntryGroup.newBuilder().build();
       String entryGroupId = "entryGroupId1228924712";
       EntryGroup response =
           catalogServiceClient.createEntryGroupAsync(parent, entryGroup, entryGroupId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the entryGroup, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
`entryGroup` | `[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup)`  
Required. EntryGroup Resource.  
`entryGroupId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. EntryGroup identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createEntryGroupAsync(CreateEntryGroupRequest request)
    
    
    public final OperationFuture<EntryGroup,OperationMetadata> createEntryGroupAsync(CreateEntryGroupRequest request)

Creates an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateEntryGroupRequest request =
           CreateEntryGroupRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setEntryGroupId("entryGroupId1228924712")
               .setEntryGroup(EntryGroup.newBuilder().build())
               .setValidateOnly(true)
               .build();
       EntryGroup response = catalogServiceClient.createEntryGroupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createEntryGroupAsync(String parent, EntryGroup entryGroup, String entryGroupId)
    
    
    public final OperationFuture<EntryGroup,OperationMetadata> createEntryGroupAsync(String parent, EntryGroup entryGroup, String entryGroupId)

Creates an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       EntryGroup entryGroup = EntryGroup.newBuilder().build();
       String entryGroupId = "entryGroupId1228924712";
       EntryGroup response =
           catalogServiceClient.createEntryGroupAsync(parent, entryGroup, entryGroupId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the entryGroup, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
`entryGroup` | `[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup)`  
Required. EntryGroup Resource.  
`entryGroupId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. EntryGroup identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createEntryGroupCallable()
    
    
    public final UnaryCallable<CreateEntryGroupRequest,Operation> createEntryGroupCallable()

Creates an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateEntryGroupRequest request =
           CreateEntryGroupRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setEntryGroupId("entryGroupId1228924712")
               .setEntryGroup(EntryGroup.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.createEntryGroupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEntryGroupOperationCallable()
    
    
    public final OperationCallable<CreateEntryGroupRequest,EntryGroup,OperationMetadata> createEntryGroupOperationCallable()

Creates an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateEntryGroupRequest request =
           CreateEntryGroupRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setEntryGroupId("entryGroupId1228924712")
               .setEntryGroup(EntryGroup.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<EntryGroup, OperationMetadata> future =
           catalogServiceClient.createEntryGroupOperationCallable().futureCall(request);
       // Do something.
       EntryGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryGroupRequest),[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createEntryLink(@Nullable EntryGroupName parent, EntryLink entryLink, String entryLinkId)
    
    
    public final EntryLink createEntryLink(@Nullable EntryGroupName parent, EntryLink entryLink, String entryLinkId)

Creates an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryGroupName parent = EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]");
       EntryLink entryLink = EntryLink.newBuilder().build();
       String entryLinkId = "entryLinkId-1349584441";
       EntryLink response = catalogServiceClient.createEntryLink(parent, entryLink, entryLinkId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EntryGroupName`  
Required. The resource name of the parent Entry Group: `projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}`.  
`entryLink` | `[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)`  
Required. Entry Link resource.  
`entryLinkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Entry Link identifier 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the EntryGroup. 

  
**Returns**  
---  
**Type** | **Description**  
`[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)` |   
  
### createEntryLink(CreateEntryLinkRequest request)
    
    
    public final EntryLink createEntryLink(CreateEntryLinkRequest request)

Creates an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateEntryLinkRequest request =
           CreateEntryLinkRequest.newBuilder()
               .setParent(EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
               .setEntryLinkId("entryLinkId-1349584441")
               .setEntryLink(EntryLink.newBuilder().build())
               .build();
       EntryLink response = catalogServiceClient.createEntryLink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryLinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)` |   
  
### createEntryLink(String parent, EntryLink entryLink, String entryLinkId)
    
    
    public final EntryLink createEntryLink(String parent, EntryLink entryLink, String entryLinkId)

Creates an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString();
       EntryLink entryLink = EntryLink.newBuilder().build();
       String entryLinkId = "entryLinkId-1349584441";
       EntryLink response = catalogServiceClient.createEntryLink(parent, entryLink, entryLinkId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent Entry Group: `projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}`.  
`entryLink` | `[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)`  
Required. Entry Link resource.  
`entryLinkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Entry Link identifier 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the EntryGroup. 

  
**Returns**  
---  
**Type** | **Description**  
`[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)` |   
  
### createEntryLinkCallable()
    
    
    public final UnaryCallable<CreateEntryLinkRequest,EntryLink> createEntryLinkCallable()

Creates an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateEntryLinkRequest request =
           CreateEntryLinkRequest.newBuilder()
               .setParent(EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
               .setEntryLinkId("entryLinkId-1349584441")
               .setEntryLink(EntryLink.newBuilder().build())
               .build();
       ApiFuture<EntryLink> future =
           catalogServiceClient.createEntryLinkCallable().futureCall(request);
       // Do something.
       EntryLink response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryLinkRequest),[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)>` |   
  
### createEntryTypeAsync(@Nullable LocationName parent, EntryType entryType, String entryTypeId)
    
    
    public final OperationFuture<EntryType,OperationMetadata> createEntryTypeAsync(@Nullable LocationName parent, EntryType entryType, String entryTypeId)

Creates an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       EntryType entryType = EntryType.newBuilder().build();
       String entryTypeId = "entryTypeId-1105721081";
       EntryType response =
           catalogServiceClient.createEntryTypeAsync(parent, entryType, entryTypeId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the EntryType, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
`entryType` | `[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType)`  
Required. EntryType Resource.  
`entryTypeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. EntryType identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createEntryTypeAsync(CreateEntryTypeRequest request)
    
    
    public final OperationFuture<EntryType,OperationMetadata> createEntryTypeAsync(CreateEntryTypeRequest request)

Creates an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateEntryTypeRequest request =
           CreateEntryTypeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setEntryTypeId("entryTypeId-1105721081")
               .setEntryType(EntryType.newBuilder().build())
               .setValidateOnly(true)
               .build();
       EntryType response = catalogServiceClient.createEntryTypeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEntryTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createEntryTypeAsync(String parent, EntryType entryType, String entryTypeId)
    
    
    public final OperationFuture<EntryType,OperationMetadata> createEntryTypeAsync(String parent, EntryType entryType, String entryTypeId)

Creates an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       EntryType entryType = EntryType.newBuilder().build();
       String entryTypeId = "entryTypeId-1105721081";
       EntryType response =
           catalogServiceClient.createEntryTypeAsync(parent, entryType, entryTypeId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntryType, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
`entryType` | `[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType)`  
Required. EntryType Resource.  
`entryTypeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. EntryType identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createEntryTypeCallable()
    
    
    public final UnaryCallable<CreateEntryTypeRequest,Operation> createEntryTypeCallable()

Creates an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateEntryTypeRequest request =
           CreateEntryTypeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setEntryTypeId("entryTypeId-1105721081")
               .setEntryType(EntryType.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.createEntryTypeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEntryTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryTypeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEntryTypeOperationCallable()
    
    
    public final OperationCallable<CreateEntryTypeRequest,EntryType,OperationMetadata> createEntryTypeOperationCallable()

Creates an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateEntryTypeRequest request =
           CreateEntryTypeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setEntryTypeId("entryTypeId-1105721081")
               .setEntryType(EntryType.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<EntryType, OperationMetadata> future =
           catalogServiceClient.createEntryTypeOperationCallable().futureCall(request);
       // Do something.
       EntryType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateEntryTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEntryTypeRequest),[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createMetadataFeedAsync(@Nullable LocationName parent, MetadataFeed metadataFeed, String metadataFeedId)
    
    
    public final OperationFuture<MetadataFeed,OperationMetadata> createMetadataFeedAsync(@Nullable LocationName parent, MetadataFeed metadataFeed, String metadataFeedId)

Creates a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       MetadataFeed metadataFeed = MetadataFeed.newBuilder().build();
       String metadataFeedId = "metadataFeedId1633421160";
       MetadataFeed response =
           catalogServiceClient.createMetadataFeedAsync(parent, metadataFeed, metadataFeedId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the parent location, in the format `projects/{project_id_or_number}/locations/{location_id}`  
`metadataFeed` | `[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed)`  
Required. The metadata job resource.  
`metadataFeedId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The metadata job ID. If not provided, a unique ID is generated with the prefix `metadata-job-`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createMetadataFeedAsync(CreateMetadataFeedRequest request)
    
    
    public final OperationFuture<MetadataFeed,OperationMetadata> createMetadataFeedAsync(CreateMetadataFeedRequest request)

Creates a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateMetadataFeedRequest request =
           CreateMetadataFeedRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMetadataFeed(MetadataFeed.newBuilder().build())
               .setMetadataFeedId("metadataFeedId1633421160")
               .setValidateOnly(true)
               .build();
       MetadataFeed response = catalogServiceClient.createMetadataFeedAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateMetadataFeedRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createMetadataFeedAsync(String parent, MetadataFeed metadataFeed, String metadataFeedId)
    
    
    public final OperationFuture<MetadataFeed,OperationMetadata> createMetadataFeedAsync(String parent, MetadataFeed metadataFeed, String metadataFeedId)

Creates a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       MetadataFeed metadataFeed = MetadataFeed.newBuilder().build();
       String metadataFeedId = "metadataFeedId1633421160";
       MetadataFeed response =
           catalogServiceClient.createMetadataFeedAsync(parent, metadataFeed, metadataFeedId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent location, in the format `projects/{project_id_or_number}/locations/{location_id}`  
`metadataFeed` | `[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed)`  
Required. The metadata job resource.  
`metadataFeedId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The metadata job ID. If not provided, a unique ID is generated with the prefix `metadata-job-`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createMetadataFeedCallable()
    
    
    public final UnaryCallable<CreateMetadataFeedRequest,Operation> createMetadataFeedCallable()

Creates a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateMetadataFeedRequest request =
           CreateMetadataFeedRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMetadataFeed(MetadataFeed.newBuilder().build())
               .setMetadataFeedId("metadataFeedId1633421160")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.createMetadataFeedCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateMetadataFeedRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createMetadataFeedOperationCallable()
    
    
    public final OperationCallable<CreateMetadataFeedRequest,MetadataFeed,OperationMetadata> createMetadataFeedOperationCallable()

Creates a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateMetadataFeedRequest request =
           CreateMetadataFeedRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMetadataFeed(MetadataFeed.newBuilder().build())
               .setMetadataFeedId("metadataFeedId1633421160")
               .setValidateOnly(true)
               .build();
       OperationFuture<MetadataFeed, OperationMetadata> future =
           catalogServiceClient.createMetadataFeedOperationCallable().futureCall(request);
       // Do something.
       MetadataFeed response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateMetadataFeedRequest),[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createMetadataJobAsync(@Nullable LocationName parent, MetadataJob metadataJob, String metadataJobId)
    
    
    public final OperationFuture<MetadataJob,OperationMetadata> createMetadataJobAsync(@Nullable LocationName parent, MetadataJob metadataJob, String metadataJobId)

Creates a metadata job. For example, use a metadata job to import metadata from a third-party system into Dataplex Universal Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       MetadataJob metadataJob = MetadataJob.newBuilder().build();
       String metadataJobId = "metadataJobId-2021530679";
       MetadataJob response =
           catalogServiceClient.createMetadataJobAsync(parent, metadataJob, metadataJobId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the parent location, in the format `projects/{project_id_or_number}/locations/{location_id}`  
`metadataJob` | `[MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob)`  
Required. The metadata job resource.  
`metadataJobId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The metadata job ID. If not provided, a unique ID is generated with the prefix `metadata-job-`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createMetadataJobAsync(CreateMetadataJobRequest request)
    
    
    public final OperationFuture<MetadataJob,OperationMetadata> createMetadataJobAsync(CreateMetadataJobRequest request)

Creates a metadata job. For example, use a metadata job to import metadata from a third-party system into Dataplex Universal Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateMetadataJobRequest request =
           CreateMetadataJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMetadataJob(MetadataJob.newBuilder().build())
               .setMetadataJobId("metadataJobId-2021530679")
               .setValidateOnly(true)
               .build();
       MetadataJob response = catalogServiceClient.createMetadataJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateMetadataJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createMetadataJobAsync(String parent, MetadataJob metadataJob, String metadataJobId)
    
    
    public final OperationFuture<MetadataJob,OperationMetadata> createMetadataJobAsync(String parent, MetadataJob metadataJob, String metadataJobId)

Creates a metadata job. For example, use a metadata job to import metadata from a third-party system into Dataplex Universal Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       MetadataJob metadataJob = MetadataJob.newBuilder().build();
       String metadataJobId = "metadataJobId-2021530679";
       MetadataJob response =
           catalogServiceClient.createMetadataJobAsync(parent, metadataJob, metadataJobId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent location, in the format `projects/{project_id_or_number}/locations/{location_id}`  
`metadataJob` | `[MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob)`  
Required. The metadata job resource.  
`metadataJobId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The metadata job ID. If not provided, a unique ID is generated with the prefix `metadata-job-`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createMetadataJobCallable()
    
    
    public final UnaryCallable<CreateMetadataJobRequest,Operation> createMetadataJobCallable()

Creates a metadata job. For example, use a metadata job to import metadata from a third-party system into Dataplex Universal Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateMetadataJobRequest request =
           CreateMetadataJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMetadataJob(MetadataJob.newBuilder().build())
               .setMetadataJobId("metadataJobId-2021530679")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.createMetadataJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateMetadataJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createMetadataJobOperationCallable()
    
    
    public final OperationCallable<CreateMetadataJobRequest,MetadataJob,OperationMetadata> createMetadataJobOperationCallable()

Creates a metadata job. For example, use a metadata job to import metadata from a third-party system into Dataplex Universal Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CreateMetadataJobRequest request =
           CreateMetadataJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMetadataJob(MetadataJob.newBuilder().build())
               .setMetadataJobId("metadataJobId-2021530679")
               .setValidateOnly(true)
               .build();
       OperationFuture<MetadataJob, OperationMetadata> future =
           catalogServiceClient.createMetadataJobOperationCallable().futureCall(request);
       // Do something.
       MetadataJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateMetadataJobRequest),[MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteAspectTypeAsync(@Nullable AspectTypeName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAspectTypeAsync(@Nullable AspectTypeName name)

Deletes an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       AspectTypeName name = AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]");
       catalogServiceClient.deleteAspectTypeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.AspectTypeName`  
Required. The resource name of the AspectType: `projects/{project_number}/locations/{location_id}/aspectTypes/{aspect_type_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteAspectTypeAsync(DeleteAspectTypeRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAspectTypeAsync(DeleteAspectTypeRequest request)

Deletes an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteAspectTypeRequest request =
           DeleteAspectTypeRequest.newBuilder()
               .setName(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setEtag("etag3123477")
               .build();
       catalogServiceClient.deleteAspectTypeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteAspectTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteAspectTypeAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAspectTypeAsync(String name)

Deletes an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString();
       catalogServiceClient.deleteAspectTypeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the AspectType: `projects/{project_number}/locations/{location_id}/aspectTypes/{aspect_type_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteAspectTypeCallable()
    
    
    public final UnaryCallable<DeleteAspectTypeRequest,Operation> deleteAspectTypeCallable()

Deletes an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteAspectTypeRequest request =
           DeleteAspectTypeRequest.newBuilder()
               .setName(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.deleteAspectTypeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteAspectTypeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAspectTypeOperationCallable()
    
    
    public final OperationCallable<DeleteAspectTypeRequest,Empty,OperationMetadata> deleteAspectTypeOperationCallable()

Deletes an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteAspectTypeRequest request =
           DeleteAspectTypeRequest.newBuilder()
               .setName(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           catalogServiceClient.deleteAspectTypeOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteAspectTypeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteEntry(@Nullable EntryName name)
    
    
    public final Entry deleteEntry(@Nullable EntryName name)

Deletes an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryName name = EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]");
       Entry response = catalogServiceClient.deleteEntry(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EntryName`  
Required. The resource name of the Entry: `projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}`.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### deleteEntry(DeleteEntryRequest request)
    
    
    public final Entry deleteEntry(DeleteEntryRequest request)

Deletes an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteEntryRequest request =
           DeleteEntryRequest.newBuilder()
               .setName(
                   EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]").toString())
               .build();
       Entry response = catalogServiceClient.deleteEntry(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEntryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### deleteEntry(String name)
    
    
    public final Entry deleteEntry(String name)

Deletes an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]").toString();
       Entry response = catalogServiceClient.deleteEntry(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Entry: `projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}`.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### deleteEntryCallable()
    
    
    public final UnaryCallable<DeleteEntryRequest,Entry> deleteEntryCallable()

Deletes an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteEntryRequest request =
           DeleteEntryRequest.newBuilder()
               .setName(
                   EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]").toString())
               .build();
       ApiFuture<Entry> future = catalogServiceClient.deleteEntryCallable().futureCall(request);
       // Do something.
       Entry response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEntryRequest),[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)>` |   
  
### deleteEntryGroupAsync(@Nullable EntryGroupName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEntryGroupAsync(@Nullable EntryGroupName name)

Deletes an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryGroupName name = EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]");
       catalogServiceClient.deleteEntryGroupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EntryGroupName`  
Required. The resource name of the EntryGroup: `projects/{project_number}/locations/{location_id}/entryGroups/{entry_group_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteEntryGroupAsync(DeleteEntryGroupRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEntryGroupAsync(DeleteEntryGroupRequest request)

Deletes an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteEntryGroupRequest request =
           DeleteEntryGroupRequest.newBuilder()
               .setName(EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
               .setEtag("etag3123477")
               .build();
       catalogServiceClient.deleteEntryGroupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEntryGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteEntryGroupAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEntryGroupAsync(String name)

Deletes an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString();
       catalogServiceClient.deleteEntryGroupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntryGroup: `projects/{project_number}/locations/{location_id}/entryGroups/{entry_group_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteEntryGroupCallable()
    
    
    public final UnaryCallable<DeleteEntryGroupRequest,Operation> deleteEntryGroupCallable()

Deletes an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteEntryGroupRequest request =
           DeleteEntryGroupRequest.newBuilder()
               .setName(EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.deleteEntryGroupCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEntryGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEntryGroupOperationCallable()
    
    
    public final OperationCallable<DeleteEntryGroupRequest,Empty,OperationMetadata> deleteEntryGroupOperationCallable()

Deletes an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteEntryGroupRequest request =
           DeleteEntryGroupRequest.newBuilder()
               .setName(EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           catalogServiceClient.deleteEntryGroupOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEntryGroupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteEntryLink(@Nullable EntryLinkName name)
    
    
    public final EntryLink deleteEntryLink(@Nullable EntryLinkName name)

Deletes an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryLinkName name =
           EntryLinkName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY_LINK]");
       EntryLink response = catalogServiceClient.deleteEntryLink(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EntryLinkName`  
Required. The resource name of the Entry Link: `projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entryLinks/{entry_link_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)` |   
  
### deleteEntryLink(DeleteEntryLinkRequest request)
    
    
    public final EntryLink deleteEntryLink(DeleteEntryLinkRequest request)

Deletes an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteEntryLinkRequest request =
           DeleteEntryLinkRequest.newBuilder()
               .setName(
                   EntryLinkName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY_LINK]")
                       .toString())
               .build();
       EntryLink response = catalogServiceClient.deleteEntryLink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEntryLinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)` |   
  
### deleteEntryLink(String name)
    
    
    public final EntryLink deleteEntryLink(String name)

Deletes an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name =
           EntryLinkName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY_LINK]").toString();
       EntryLink response = catalogServiceClient.deleteEntryLink(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Entry Link: `projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entryLinks/{entry_link_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)` |   
  
### deleteEntryLinkCallable()
    
    
    public final UnaryCallable<DeleteEntryLinkRequest,EntryLink> deleteEntryLinkCallable()

Deletes an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteEntryLinkRequest request =
           DeleteEntryLinkRequest.newBuilder()
               .setName(
                   EntryLinkName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY_LINK]")
                       .toString())
               .build();
       ApiFuture<EntryLink> future =
           catalogServiceClient.deleteEntryLinkCallable().futureCall(request);
       // Do something.
       EntryLink response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEntryLinkRequest),[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)>` |   
  
### deleteEntryTypeAsync(@Nullable EntryTypeName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEntryTypeAsync(@Nullable EntryTypeName name)

Deletes an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryTypeName name = EntryTypeName.of("[PROJECT]", "[LOCATION]", "[ENTRY_TYPE]");
       catalogServiceClient.deleteEntryTypeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EntryTypeName`  
Required. The resource name of the EntryType: `projects/{project_number}/locations/{location_id}/entryTypes/{entry_type_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteEntryTypeAsync(DeleteEntryTypeRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEntryTypeAsync(DeleteEntryTypeRequest request)

Deletes an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteEntryTypeRequest request =
           DeleteEntryTypeRequest.newBuilder()
               .setName(EntryTypeName.of("[PROJECT]", "[LOCATION]", "[ENTRY_TYPE]").toString())
               .setEtag("etag3123477")
               .build();
       catalogServiceClient.deleteEntryTypeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEntryTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEntryTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteEntryTypeAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEntryTypeAsync(String name)

Deletes an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = EntryTypeName.of("[PROJECT]", "[LOCATION]", "[ENTRY_TYPE]").toString();
       catalogServiceClient.deleteEntryTypeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntryType: `projects/{project_number}/locations/{location_id}/entryTypes/{entry_type_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteEntryTypeCallable()
    
    
    public final UnaryCallable<DeleteEntryTypeRequest,Operation> deleteEntryTypeCallable()

Deletes an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteEntryTypeRequest request =
           DeleteEntryTypeRequest.newBuilder()
               .setName(EntryTypeName.of("[PROJECT]", "[LOCATION]", "[ENTRY_TYPE]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.deleteEntryTypeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEntryTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEntryTypeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEntryTypeOperationCallable()
    
    
    public final OperationCallable<DeleteEntryTypeRequest,Empty,OperationMetadata> deleteEntryTypeOperationCallable()

Deletes an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteEntryTypeRequest request =
           DeleteEntryTypeRequest.newBuilder()
               .setName(EntryTypeName.of("[PROJECT]", "[LOCATION]", "[ENTRY_TYPE]").toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           catalogServiceClient.deleteEntryTypeOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteEntryTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEntryTypeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteMetadataFeedAsync(@Nullable MetadataFeedName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteMetadataFeedAsync(@Nullable MetadataFeedName name)

Deletes a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       MetadataFeedName name = MetadataFeedName.of("[PROJECT]", "[LOCATION]", "[METADATA_FEED]");
       catalogServiceClient.deleteMetadataFeedAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.MetadataFeedName`  
Required. The resource name of the metadata feed, in the format `projects/{project_id_or_number}/locations/{location_id}/MetadataFeeds/{metadata_feed_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteMetadataFeedAsync(DeleteMetadataFeedRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteMetadataFeedAsync(DeleteMetadataFeedRequest request)

Deletes a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteMetadataFeedRequest request =
           DeleteMetadataFeedRequest.newBuilder()
               .setName(MetadataFeedName.of("[PROJECT]", "[LOCATION]", "[METADATA_FEED]").toString())
               .build();
       catalogServiceClient.deleteMetadataFeedAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteMetadataFeedRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteMetadataFeedAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteMetadataFeedAsync(String name)

Deletes a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = MetadataFeedName.of("[PROJECT]", "[LOCATION]", "[METADATA_FEED]").toString();
       catalogServiceClient.deleteMetadataFeedAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the metadata feed, in the format `projects/{project_id_or_number}/locations/{location_id}/MetadataFeeds/{metadata_feed_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteMetadataFeedCallable()
    
    
    public final UnaryCallable<DeleteMetadataFeedRequest,Operation> deleteMetadataFeedCallable()

Deletes a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteMetadataFeedRequest request =
           DeleteMetadataFeedRequest.newBuilder()
               .setName(MetadataFeedName.of("[PROJECT]", "[LOCATION]", "[METADATA_FEED]").toString())
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.deleteMetadataFeedCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteMetadataFeedRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteMetadataFeedOperationCallable()
    
    
    public final OperationCallable<DeleteMetadataFeedRequest,Empty,OperationMetadata> deleteMetadataFeedOperationCallable()

Deletes a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       DeleteMetadataFeedRequest request =
           DeleteMetadataFeedRequest.newBuilder()
               .setName(MetadataFeedName.of("[PROJECT]", "[LOCATION]", "[METADATA_FEED]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           catalogServiceClient.deleteMetadataFeedOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteMetadataFeedRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### getAspectType(@Nullable AspectTypeName name)
    
    
    public final AspectType getAspectType(@Nullable AspectTypeName name)

Gets an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       AspectTypeName name = AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]");
       AspectType response = catalogServiceClient.getAspectType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.AspectTypeName`  
Required. The resource name of the AspectType: `projects/{project_number}/locations/{location_id}/aspectTypes/{aspect_type_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType)` |   
  
### getAspectType(GetAspectTypeRequest request)
    
    
    public final AspectType getAspectType(GetAspectTypeRequest request)

Gets an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetAspectTypeRequest request =
           GetAspectTypeRequest.newBuilder()
               .setName(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .build();
       AspectType response = catalogServiceClient.getAspectType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetAspectTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType)` |   
  
### getAspectType(String name)
    
    
    public final AspectType getAspectType(String name)

Gets an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString();
       AspectType response = catalogServiceClient.getAspectType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the AspectType: `projects/{project_number}/locations/{location_id}/aspectTypes/{aspect_type_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType)` |   
  
### getAspectTypeCallable()
    
    
    public final UnaryCallable<GetAspectTypeRequest,AspectType> getAspectTypeCallable()

Gets an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetAspectTypeRequest request =
           GetAspectTypeRequest.newBuilder()
               .setName(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .build();
       ApiFuture<AspectType> future =
           catalogServiceClient.getAspectTypeCallable().futureCall(request);
       // Do something.
       AspectType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetAspectTypeRequest),[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType)>` |   
  
### getEntry(@Nullable EntryName name)
    
    
    public final Entry getEntry(@Nullable EntryName name)

Gets an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryName name = EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]");
       Entry response = catalogServiceClient.getEntry(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EntryName`  
Required. The resource name of the Entry: `projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}`.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### getEntry(GetEntryRequest request)
    
    
    public final Entry getEntry(GetEntryRequest request)

Gets an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetEntryRequest request =
           GetEntryRequest.newBuilder()
               .setName(
                   EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]").toString())
               .setView(EntryView.forNumber(0))
               .addAllAspectTypes(new ArrayList<String>())
               .addAllPaths(new ArrayList<String>())
               .build();
       Entry response = catalogServiceClient.getEntry(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEntryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### getEntry(String name)
    
    
    public final Entry getEntry(String name)

Gets an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]").toString();
       Entry response = catalogServiceClient.getEntry(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Entry: `projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}`.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### getEntryCallable()
    
    
    public final UnaryCallable<GetEntryRequest,Entry> getEntryCallable()

Gets an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetEntryRequest request =
           GetEntryRequest.newBuilder()
               .setName(
                   EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]").toString())
               .setView(EntryView.forNumber(0))
               .addAllAspectTypes(new ArrayList<String>())
               .addAllPaths(new ArrayList<String>())
               .build();
       ApiFuture<Entry> future = catalogServiceClient.getEntryCallable().futureCall(request);
       // Do something.
       Entry response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEntryRequest),[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)>` |   
  
### getEntryGroup(@Nullable EntryGroupName name)
    
    
    public final EntryGroup getEntryGroup(@Nullable EntryGroupName name)

Gets an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryGroupName name = EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]");
       EntryGroup response = catalogServiceClient.getEntryGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EntryGroupName`  
Required. The resource name of the EntryGroup: `projects/{project_number}/locations/{location_id}/entryGroups/{entry_group_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup)` |   
  
### getEntryGroup(GetEntryGroupRequest request)
    
    
    public final EntryGroup getEntryGroup(GetEntryGroupRequest request)

Gets an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetEntryGroupRequest request =
           GetEntryGroupRequest.newBuilder()
               .setName(EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
               .build();
       EntryGroup response = catalogServiceClient.getEntryGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEntryGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup)` |   
  
### getEntryGroup(String name)
    
    
    public final EntryGroup getEntryGroup(String name)

Gets an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString();
       EntryGroup response = catalogServiceClient.getEntryGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntryGroup: `projects/{project_number}/locations/{location_id}/entryGroups/{entry_group_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup)` |   
  
### getEntryGroupCallable()
    
    
    public final UnaryCallable<GetEntryGroupRequest,EntryGroup> getEntryGroupCallable()

Gets an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetEntryGroupRequest request =
           GetEntryGroupRequest.newBuilder()
               .setName(EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
               .build();
       ApiFuture<EntryGroup> future =
           catalogServiceClient.getEntryGroupCallable().futureCall(request);
       // Do something.
       EntryGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEntryGroupRequest),[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup)>` |   
  
### getEntryLink(@Nullable EntryLinkName name)
    
    
    public final EntryLink getEntryLink(@Nullable EntryLinkName name)

Gets an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryLinkName name =
           EntryLinkName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY_LINK]");
       EntryLink response = catalogServiceClient.getEntryLink(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EntryLinkName`  
Required. The resource name of the Entry Link: `projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entryLinks/{entry_link_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)` |   
  
### getEntryLink(GetEntryLinkRequest request)
    
    
    public final EntryLink getEntryLink(GetEntryLinkRequest request)

Gets an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetEntryLinkRequest request =
           GetEntryLinkRequest.newBuilder()
               .setName(
                   EntryLinkName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY_LINK]")
                       .toString())
               .build();
       EntryLink response = catalogServiceClient.getEntryLink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEntryLinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)` |   
  
### getEntryLink(String name)
    
    
    public final EntryLink getEntryLink(String name)

Gets an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name =
           EntryLinkName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY_LINK]").toString();
       EntryLink response = catalogServiceClient.getEntryLink(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Entry Link: `projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entryLinks/{entry_link_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)` |   
  
### getEntryLinkCallable()
    
    
    public final UnaryCallable<GetEntryLinkRequest,EntryLink> getEntryLinkCallable()

Gets an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetEntryLinkRequest request =
           GetEntryLinkRequest.newBuilder()
               .setName(
                   EntryLinkName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY_LINK]")
                       .toString())
               .build();
       ApiFuture<EntryLink> future = catalogServiceClient.getEntryLinkCallable().futureCall(request);
       // Do something.
       EntryLink response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEntryLinkRequest),[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)>` |   
  
### getEntryType(@Nullable EntryTypeName name)
    
    
    public final EntryType getEntryType(@Nullable EntryTypeName name)

Gets an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryTypeName name = EntryTypeName.of("[PROJECT]", "[LOCATION]", "[ENTRY_TYPE]");
       EntryType response = catalogServiceClient.getEntryType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EntryTypeName`  
Required. The resource name of the EntryType: `projects/{project_number}/locations/{location_id}/entryTypes/{entry_type_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType)` |   
  
### getEntryType(GetEntryTypeRequest request)
    
    
    public final EntryType getEntryType(GetEntryTypeRequest request)

Gets an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetEntryTypeRequest request =
           GetEntryTypeRequest.newBuilder()
               .setName(EntryTypeName.of("[PROJECT]", "[LOCATION]", "[ENTRY_TYPE]").toString())
               .build();
       EntryType response = catalogServiceClient.getEntryType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEntryTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEntryTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType)` |   
  
### getEntryType(String name)
    
    
    public final EntryType getEntryType(String name)

Gets an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = EntryTypeName.of("[PROJECT]", "[LOCATION]", "[ENTRY_TYPE]").toString();
       EntryType response = catalogServiceClient.getEntryType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntryType: `projects/{project_number}/locations/{location_id}/entryTypes/{entry_type_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType)` |   
  
### getEntryTypeCallable()
    
    
    public final UnaryCallable<GetEntryTypeRequest,EntryType> getEntryTypeCallable()

Gets an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetEntryTypeRequest request =
           GetEntryTypeRequest.newBuilder()
               .setName(EntryTypeName.of("[PROJECT]", "[LOCATION]", "[ENTRY_TYPE]").toString())
               .build();
       ApiFuture<EntryType> future = catalogServiceClient.getEntryTypeCallable().futureCall(request);
       // Do something.
       EntryType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEntryTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEntryTypeRequest),[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = catalogServiceClient.getIamPolicy(request);
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
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = catalogServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = catalogServiceClient.getLocation(request);
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
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = catalogServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getMetadataFeed(@Nullable MetadataFeedName name)
    
    
    public final MetadataFeed getMetadataFeed(@Nullable MetadataFeedName name)

Gets a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       MetadataFeedName name = MetadataFeedName.of("[PROJECT]", "[LOCATION]", "[METADATA_FEED]");
       MetadataFeed response = catalogServiceClient.getMetadataFeed(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.MetadataFeedName`  
Required. The resource name of the metadata feed, in the format `projects/{project_id_or_number}/locations/{location_id}/MetadataFeeds/{metadata_feed_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed)` |   
  
### getMetadataFeed(GetMetadataFeedRequest request)
    
    
    public final MetadataFeed getMetadataFeed(GetMetadataFeedRequest request)

Gets a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetMetadataFeedRequest request =
           GetMetadataFeedRequest.newBuilder()
               .setName(MetadataFeedName.of("[PROJECT]", "[LOCATION]", "[METADATA_FEED]").toString())
               .build();
       MetadataFeed response = catalogServiceClient.getMetadataFeed(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetMetadataFeedRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed)` |   
  
### getMetadataFeed(String name)
    
    
    public final MetadataFeed getMetadataFeed(String name)

Gets a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = MetadataFeedName.of("[PROJECT]", "[LOCATION]", "[METADATA_FEED]").toString();
       MetadataFeed response = catalogServiceClient.getMetadataFeed(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the metadata feed, in the format `projects/{project_id_or_number}/locations/{location_id}/MetadataFeeds/{metadata_feed_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed)` |   
  
### getMetadataFeedCallable()
    
    
    public final UnaryCallable<GetMetadataFeedRequest,MetadataFeed> getMetadataFeedCallable()

Gets a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetMetadataFeedRequest request =
           GetMetadataFeedRequest.newBuilder()
               .setName(MetadataFeedName.of("[PROJECT]", "[LOCATION]", "[METADATA_FEED]").toString())
               .build();
       ApiFuture<MetadataFeed> future =
           catalogServiceClient.getMetadataFeedCallable().futureCall(request);
       // Do something.
       MetadataFeed response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetMetadataFeedRequest),[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed)>` |   
  
### getMetadataJob(@Nullable MetadataJobName name)
    
    
    public final MetadataJob getMetadataJob(@Nullable MetadataJobName name)

Gets a metadata job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       MetadataJobName name = MetadataJobName.of("[PROJECT]", "[LOCATION]", "[METADATAJOB]");
       MetadataJob response = catalogServiceClient.getMetadataJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.MetadataJobName`  
Required. The resource name of the metadata job, in the format `projects/{project_id_or_number}/locations/{location_id}/metadataJobs/{metadata_job_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob)` |   
  
### getMetadataJob(GetMetadataJobRequest request)
    
    
    public final MetadataJob getMetadataJob(GetMetadataJobRequest request)

Gets a metadata job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetMetadataJobRequest request =
           GetMetadataJobRequest.newBuilder()
               .setName(MetadataJobName.of("[PROJECT]", "[LOCATION]", "[METADATAJOB]").toString())
               .build();
       MetadataJob response = catalogServiceClient.getMetadataJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetMetadataJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob)` |   
  
### getMetadataJob(String name)
    
    
    public final MetadataJob getMetadataJob(String name)

Gets a metadata job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = MetadataJobName.of("[PROJECT]", "[LOCATION]", "[METADATAJOB]").toString();
       MetadataJob response = catalogServiceClient.getMetadataJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the metadata job, in the format `projects/{project_id_or_number}/locations/{location_id}/metadataJobs/{metadata_job_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob)` |   
  
### getMetadataJobCallable()
    
    
    public final UnaryCallable<GetMetadataJobRequest,MetadataJob> getMetadataJobCallable()

Gets a metadata job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetMetadataJobRequest request =
           GetMetadataJobRequest.newBuilder()
               .setName(MetadataJobName.of("[PROJECT]", "[LOCATION]", "[METADATAJOB]").toString())
               .build();
       ApiFuture<MetadataJob> future =
           catalogServiceClient.getMetadataJobCallable().futureCall(request);
       // Do something.
       MetadataJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetMetadataJobRequest),[MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable CatalogServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.CatalogServiceSettings` |   
  
### getStub()
    
    
    public CatalogServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.CatalogServiceStub)` |   
  
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
  
### listAspectTypes(@Nullable LocationName parent)
    
    
    public final CatalogServiceClient.ListAspectTypesPagedResponse listAspectTypes(@Nullable LocationName parent)

Lists AspectType resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (AspectType element : catalogServiceClient.listAspectTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the AspectType location, of the form: `projects/{project_number}/locations/{location_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListAspectTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListAspectTypesPagedResponse)` |   
  
### listAspectTypes(ListAspectTypesRequest request)
    
    
    public final CatalogServiceClient.ListAspectTypesPagedResponse listAspectTypes(ListAspectTypesRequest request)

Lists AspectType resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListAspectTypesRequest request =
           ListAspectTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (AspectType element : catalogServiceClient.listAspectTypes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAspectTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAspectTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListAspectTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListAspectTypesPagedResponse)` |   
  
### listAspectTypes(String parent)
    
    
    public final CatalogServiceClient.ListAspectTypesPagedResponse listAspectTypes(String parent)

Lists AspectType resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (AspectType element : catalogServiceClient.listAspectTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the AspectType location, of the form: `projects/{project_number}/locations/{location_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListAspectTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListAspectTypesPagedResponse)` |   
  
### listAspectTypesCallable()
    
    
    public final UnaryCallable<ListAspectTypesRequest,ListAspectTypesResponse> listAspectTypesCallable()

Lists AspectType resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListAspectTypesRequest request =
           ListAspectTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAspectTypesResponse response =
             catalogServiceClient.listAspectTypesCallable().call(request);
         for (AspectType element : response.getAspectTypesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAspectTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAspectTypesRequest),[ListAspectTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAspectTypesResponse)>` |   
  
### listAspectTypesPagedCallable()
    
    
    public final UnaryCallable<ListAspectTypesRequest,CatalogServiceClient.ListAspectTypesPagedResponse> listAspectTypesPagedCallable()

Lists AspectType resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListAspectTypesRequest request =
           ListAspectTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<AspectType> future =
           catalogServiceClient.listAspectTypesPagedCallable().futureCall(request);
       // Do something.
       for (AspectType element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAspectTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAspectTypesRequest),[ListAspectTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListAspectTypesPagedResponse)>` |   
  
### listEntries(@Nullable EntryGroupName parent)
    
    
    public final CatalogServiceClient.ListEntriesPagedResponse listEntries(@Nullable EntryGroupName parent)

Lists Entries within an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryGroupName parent = EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]");
       for (Entry element : catalogServiceClient.listEntries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EntryGroupName`  
Required. The resource name of the parent Entry Group: `projects/{project}/locations/{location}/entryGroups/{entry_group}`.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListEntriesPagedResponse)` |   
  
### listEntries(ListEntriesRequest request)
    
    
    public final CatalogServiceClient.ListEntriesPagedResponse listEntries(ListEntriesRequest request)

Lists Entries within an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListEntriesRequest request =
           ListEntriesRequest.newBuilder()
               .setParent(EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Entry element : catalogServiceClient.listEntries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEntriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListEntriesPagedResponse)` |   
  
### listEntries(String parent)
    
    
    public final CatalogServiceClient.ListEntriesPagedResponse listEntries(String parent)

Lists Entries within an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString();
       for (Entry element : catalogServiceClient.listEntries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent Entry Group: `projects/{project}/locations/{location}/entryGroups/{entry_group}`.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListEntriesPagedResponse)` |   
  
### listEntriesCallable()
    
    
    public final UnaryCallable<ListEntriesRequest,ListEntriesResponse> listEntriesCallable()

Lists Entries within an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListEntriesRequest request =
           ListEntriesRequest.newBuilder()
               .setParent(EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListEntriesResponse response = catalogServiceClient.listEntriesCallable().call(request);
         for (Entry element : response.getEntriesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEntriesRequest),[ListEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEntriesResponse)>` |   
  
### listEntriesPagedCallable()
    
    
    public final UnaryCallable<ListEntriesRequest,CatalogServiceClient.ListEntriesPagedResponse> listEntriesPagedCallable()

Lists Entries within an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListEntriesRequest request =
           ListEntriesRequest.newBuilder()
               .setParent(EntryGroupName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Entry> future = catalogServiceClient.listEntriesPagedCallable().futureCall(request);
       // Do something.
       for (Entry element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEntriesRequest),[ListEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListEntriesPagedResponse)>` |   
  
### listEntryGroups(@Nullable LocationName parent)
    
    
    public final CatalogServiceClient.ListEntryGroupsPagedResponse listEntryGroups(@Nullable LocationName parent)

Lists EntryGroup resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (EntryGroup element : catalogServiceClient.listEntryGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the entryGroup location, of the form: `projects/{project_number}/locations/{location_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListEntryGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListEntryGroupsPagedResponse)` |   
  
### listEntryGroups(ListEntryGroupsRequest request)
    
    
    public final CatalogServiceClient.ListEntryGroupsPagedResponse listEntryGroups(ListEntryGroupsRequest request)

Lists EntryGroup resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListEntryGroupsRequest request =
           ListEntryGroupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (EntryGroup element : catalogServiceClient.listEntryGroups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEntryGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEntryGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListEntryGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListEntryGroupsPagedResponse)` |   
  
### listEntryGroups(String parent)
    
    
    public final CatalogServiceClient.ListEntryGroupsPagedResponse listEntryGroups(String parent)

Lists EntryGroup resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (EntryGroup element : catalogServiceClient.listEntryGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the entryGroup location, of the form: `projects/{project_number}/locations/{location_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListEntryGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListEntryGroupsPagedResponse)` |   
  
### listEntryGroupsCallable()
    
    
    public final UnaryCallable<ListEntryGroupsRequest,ListEntryGroupsResponse> listEntryGroupsCallable()

Lists EntryGroup resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListEntryGroupsRequest request =
           ListEntryGroupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListEntryGroupsResponse response =
             catalogServiceClient.listEntryGroupsCallable().call(request);
         for (EntryGroup element : response.getEntryGroupsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntryGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEntryGroupsRequest),[ListEntryGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEntryGroupsResponse)>` |   
  
### listEntryGroupsPagedCallable()
    
    
    public final UnaryCallable<ListEntryGroupsRequest,CatalogServiceClient.ListEntryGroupsPagedResponse> listEntryGroupsPagedCallable()

Lists EntryGroup resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListEntryGroupsRequest request =
           ListEntryGroupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<EntryGroup> future =
           catalogServiceClient.listEntryGroupsPagedCallable().futureCall(request);
       // Do something.
       for (EntryGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntryGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEntryGroupsRequest),[ListEntryGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListEntryGroupsPagedResponse)>` |   
  
### listEntryTypes(@Nullable LocationName parent)
    
    
    public final CatalogServiceClient.ListEntryTypesPagedResponse listEntryTypes(@Nullable LocationName parent)

Lists EntryType resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (EntryType element : catalogServiceClient.listEntryTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the EntryType location, of the form: `projects/{project_number}/locations/{location_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListEntryTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListEntryTypesPagedResponse)` |   
  
### listEntryTypes(ListEntryTypesRequest request)
    
    
    public final CatalogServiceClient.ListEntryTypesPagedResponse listEntryTypes(ListEntryTypesRequest request)

Lists EntryType resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListEntryTypesRequest request =
           ListEntryTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (EntryType element : catalogServiceClient.listEntryTypes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEntryTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEntryTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListEntryTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListEntryTypesPagedResponse)` |   
  
### listEntryTypes(String parent)
    
    
    public final CatalogServiceClient.ListEntryTypesPagedResponse listEntryTypes(String parent)

Lists EntryType resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (EntryType element : catalogServiceClient.listEntryTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the EntryType location, of the form: `projects/{project_number}/locations/{location_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListEntryTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListEntryTypesPagedResponse)` |   
  
### listEntryTypesCallable()
    
    
    public final UnaryCallable<ListEntryTypesRequest,ListEntryTypesResponse> listEntryTypesCallable()

Lists EntryType resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListEntryTypesRequest request =
           ListEntryTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListEntryTypesResponse response =
             catalogServiceClient.listEntryTypesCallable().call(request);
         for (EntryType element : response.getEntryTypesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntryTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEntryTypesRequest),[ListEntryTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEntryTypesResponse)>` |   
  
### listEntryTypesPagedCallable()
    
    
    public final UnaryCallable<ListEntryTypesRequest,CatalogServiceClient.ListEntryTypesPagedResponse> listEntryTypesPagedCallable()

Lists EntryType resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListEntryTypesRequest request =
           ListEntryTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<EntryType> future =
           catalogServiceClient.listEntryTypesPagedCallable().futureCall(request);
       // Do something.
       for (EntryType element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEntryTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEntryTypesRequest),[ListEntryTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListEntryTypesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final CatalogServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : catalogServiceClient.listLocations(request).iterateAll()) {
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
`[CatalogServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = catalogServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,CatalogServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           catalogServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListLocationsPagedResponse)>` |   
  
### listMetadataFeeds(@Nullable LocationName parent)
    
    
    public final CatalogServiceClient.ListMetadataFeedsPagedResponse listMetadataFeeds(@Nullable LocationName parent)

Retrieve a list of MetadataFeeds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (MetadataFeed element : catalogServiceClient.listMetadataFeeds(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the parent location, in the format `projects/{project_id_or_number}/locations/{location_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListMetadataFeedsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListMetadataFeedsPagedResponse)` |   
  
### listMetadataFeeds(ListMetadataFeedsRequest request)
    
    
    public final CatalogServiceClient.ListMetadataFeedsPagedResponse listMetadataFeeds(ListMetadataFeedsRequest request)

Retrieve a list of MetadataFeeds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListMetadataFeedsRequest request =
           ListMetadataFeedsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (MetadataFeed element : catalogServiceClient.listMetadataFeeds(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMetadataFeedsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataFeedsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListMetadataFeedsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListMetadataFeedsPagedResponse)` |   
  
### listMetadataFeeds(String parent)
    
    
    public final CatalogServiceClient.ListMetadataFeedsPagedResponse listMetadataFeeds(String parent)

Retrieve a list of MetadataFeeds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (MetadataFeed element : catalogServiceClient.listMetadataFeeds(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent location, in the format `projects/{project_id_or_number}/locations/{location_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListMetadataFeedsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListMetadataFeedsPagedResponse)` |   
  
### listMetadataFeedsCallable()
    
    
    public final UnaryCallable<ListMetadataFeedsRequest,ListMetadataFeedsResponse> listMetadataFeedsCallable()

Retrieve a list of MetadataFeeds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListMetadataFeedsRequest request =
           ListMetadataFeedsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListMetadataFeedsResponse response =
             catalogServiceClient.listMetadataFeedsCallable().call(request);
         for (MetadataFeed element : response.getMetadataFeedsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMetadataFeedsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataFeedsRequest),[ListMetadataFeedsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataFeedsResponse)>` |   
  
### listMetadataFeedsPagedCallable()
    
    
    public final UnaryCallable<ListMetadataFeedsRequest,CatalogServiceClient.ListMetadataFeedsPagedResponse> listMetadataFeedsPagedCallable()

Retrieve a list of MetadataFeeds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListMetadataFeedsRequest request =
           ListMetadataFeedsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<MetadataFeed> future =
           catalogServiceClient.listMetadataFeedsPagedCallable().futureCall(request);
       // Do something.
       for (MetadataFeed element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMetadataFeedsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataFeedsRequest),[ListMetadataFeedsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListMetadataFeedsPagedResponse)>` |   
  
### listMetadataJobs(@Nullable LocationName parent)
    
    
    public final CatalogServiceClient.ListMetadataJobsPagedResponse listMetadataJobs(@Nullable LocationName parent)

Lists metadata jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (MetadataJob element : catalogServiceClient.listMetadataJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the parent location, in the format `projects/{project_id_or_number}/locations/{location_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListMetadataJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListMetadataJobsPagedResponse)` |   
  
### listMetadataJobs(ListMetadataJobsRequest request)
    
    
    public final CatalogServiceClient.ListMetadataJobsPagedResponse listMetadataJobs(ListMetadataJobsRequest request)

Lists metadata jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListMetadataJobsRequest request =
           ListMetadataJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (MetadataJob element : catalogServiceClient.listMetadataJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMetadataJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListMetadataJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListMetadataJobsPagedResponse)` |   
  
### listMetadataJobs(String parent)
    
    
    public final CatalogServiceClient.ListMetadataJobsPagedResponse listMetadataJobs(String parent)

Lists metadata jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (MetadataJob element : catalogServiceClient.listMetadataJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent location, in the format `projects/{project_id_or_number}/locations/{location_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListMetadataJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListMetadataJobsPagedResponse)` |   
  
### listMetadataJobsCallable()
    
    
    public final UnaryCallable<ListMetadataJobsRequest,ListMetadataJobsResponse> listMetadataJobsCallable()

Lists metadata jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListMetadataJobsRequest request =
           ListMetadataJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListMetadataJobsResponse response =
             catalogServiceClient.listMetadataJobsCallable().call(request);
         for (MetadataJob element : response.getMetadataJobsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMetadataJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataJobsRequest),[ListMetadataJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataJobsResponse)>` |   
  
### listMetadataJobsPagedCallable()
    
    
    public final UnaryCallable<ListMetadataJobsRequest,CatalogServiceClient.ListMetadataJobsPagedResponse> listMetadataJobsPagedCallable()

Lists metadata jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListMetadataJobsRequest request =
           ListMetadataJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<MetadataJob> future =
           catalogServiceClient.listMetadataJobsPagedCallable().futureCall(request);
       // Do something.
       for (MetadataJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMetadataJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataJobsRequest),[ListMetadataJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.ListMetadataJobsPagedResponse)>` |   
  
### lookupContext(LookupContextRequest request)
    
    
    public final LookupContextResponse lookupContext(LookupContextRequest request)

Looks up LLM Context for the specified resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LookupContextRequest request =
           LookupContextRequest.newBuilder()
               .setName("name3373707")
               .addAllResources(new ArrayList<String>())
               .setContext("context951530927")
               .putAllOptions(new HashMap<String, String>())
               .build();
       LookupContextResponse response = catalogServiceClient.lookupContext(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[LookupContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupContextRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LookupContextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupContextResponse)` |   
  
### lookupContextCallable()
    
    
    public final UnaryCallable<LookupContextRequest,LookupContextResponse> lookupContextCallable()

Looks up LLM Context for the specified resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LookupContextRequest request =
           LookupContextRequest.newBuilder()
               .setName("name3373707")
               .addAllResources(new ArrayList<String>())
               .setContext("context951530927")
               .putAllOptions(new HashMap<String, String>())
               .build();
       ApiFuture<LookupContextResponse> future =
           catalogServiceClient.lookupContextCallable().futureCall(request);
       // Do something.
       LookupContextResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[LookupContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupContextRequest),[LookupContextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupContextResponse)>` |   
  
### lookupEntry(LookupEntryRequest request)
    
    
    public final Entry lookupEntry(LookupEntryRequest request)

Looks up an entry by name using the permission on the source system.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LookupEntryRequest request =
           LookupEntryRequest.newBuilder()
               .setName("name3373707")
               .setView(EntryView.forNumber(0))
               .addAllAspectTypes(new ArrayList<String>())
               .addAllPaths(new ArrayList<String>())
               .setEntry(
                   EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]").toString())
               .build();
       Entry response = catalogServiceClient.lookupEntry(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[LookupEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupEntryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### lookupEntryCallable()
    
    
    public final UnaryCallable<LookupEntryRequest,Entry> lookupEntryCallable()

Looks up an entry by name using the permission on the source system.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LookupEntryRequest request =
           LookupEntryRequest.newBuilder()
               .setName("name3373707")
               .setView(EntryView.forNumber(0))
               .addAllAspectTypes(new ArrayList<String>())
               .addAllPaths(new ArrayList<String>())
               .setEntry(
                   EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]").toString())
               .build();
       ApiFuture<Entry> future = catalogServiceClient.lookupEntryCallable().futureCall(request);
       // Do something.
       Entry response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[LookupEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupEntryRequest),[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)>` |   
  
### lookupEntryLinks(LookupEntryLinksRequest request)
    
    
    public final CatalogServiceClient.LookupEntryLinksPagedResponse lookupEntryLinks(LookupEntryLinksRequest request)

Looks up Entry Links referencing the specified Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LookupEntryLinksRequest request =
           LookupEntryLinksRequest.newBuilder()
               .setName("name3373707")
               .setEntry(
                   EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]").toString())
               .addAllEntryLinkTypes(new ArrayList<String>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (EntryLink element : catalogServiceClient.lookupEntryLinks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[LookupEntryLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupEntryLinksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.LookupEntryLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.LookupEntryLinksPagedResponse)` |   
  
### lookupEntryLinksCallable()
    
    
    public final UnaryCallable<LookupEntryLinksRequest,LookupEntryLinksResponse> lookupEntryLinksCallable()

Looks up Entry Links referencing the specified Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LookupEntryLinksRequest request =
           LookupEntryLinksRequest.newBuilder()
               .setName("name3373707")
               .setEntry(
                   EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]").toString())
               .addAllEntryLinkTypes(new ArrayList<String>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         LookupEntryLinksResponse response =
             catalogServiceClient.lookupEntryLinksCallable().call(request);
         for (EntryLink element : response.getEntryLinksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[LookupEntryLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupEntryLinksRequest),[LookupEntryLinksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupEntryLinksResponse)>` |   
  
### lookupEntryLinksPagedCallable()
    
    
    public final UnaryCallable<LookupEntryLinksRequest,CatalogServiceClient.LookupEntryLinksPagedResponse> lookupEntryLinksPagedCallable()

Looks up Entry Links referencing the specified Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LookupEntryLinksRequest request =
           LookupEntryLinksRequest.newBuilder()
               .setName("name3373707")
               .setEntry(
                   EntryName.of("[PROJECT]", "[LOCATION]", "[ENTRY_GROUP]", "[ENTRY]").toString())
               .addAllEntryLinkTypes(new ArrayList<String>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<EntryLink> future =
           catalogServiceClient.lookupEntryLinksPagedCallable().futureCall(request);
       // Do something.
       for (EntryLink element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[LookupEntryLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LookupEntryLinksRequest),[LookupEntryLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.LookupEntryLinksPagedResponse)>` |   
  
### modifyEntry(ModifyEntryRequest request)
    
    
    public final Entry modifyEntry(ModifyEntryRequest request)

Modifies an entry using the permission on the source system.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ModifyEntryRequest request =
           ModifyEntryRequest.newBuilder()
               .setName("name3373707")
               .setEntry(Entry.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDeleteMissingAspects(true)
               .addAllAspectKeys(new ArrayList<String>())
               .build();
       Entry response = catalogServiceClient.modifyEntry(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ModifyEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ModifyEntryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### modifyEntryCallable()
    
    
    public final UnaryCallable<ModifyEntryRequest,Entry> modifyEntryCallable()

Modifies an entry using the permission on the source system.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ModifyEntryRequest request =
           ModifyEntryRequest.newBuilder()
               .setName("name3373707")
               .setEntry(Entry.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDeleteMissingAspects(true)
               .addAllAspectKeys(new ArrayList<String>())
               .build();
       ApiFuture<Entry> future = catalogServiceClient.modifyEntryCallable().futureCall(request);
       // Do something.
       Entry response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ModifyEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ModifyEntryRequest),[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)>` |   
  
### searchEntries(@Nullable LocationName name, String query)
    
    
    public final CatalogServiceClient.SearchEntriesPagedResponse searchEntries(@Nullable LocationName name, String query)

Searches for Entries matching the given query and scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LocationName name = LocationName.of("[PROJECT]", "[LOCATION]");
       String query = "query107944136";
       for (SearchEntriesResult element :
           catalogServiceClient.searchEntries(name, query).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The project to which the request should be attributed in the following form: `projects/{project}/locations/global`.  
`query` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The query against which entries in scope should be matched. The query syntax is defined in [Search syntax for Dataplex Universal Catalog](https://cloud.google.com/dataplex/docs/search-syntax).  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.SearchEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.SearchEntriesPagedResponse)` |   
  
### searchEntries(SearchEntriesRequest request)
    
    
    public final CatalogServiceClient.SearchEntriesPagedResponse searchEntries(SearchEntriesRequest request)

Searches for Entries matching the given query and scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       SearchEntriesRequest request =
           SearchEntriesRequest.newBuilder()
               .setName(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery("query107944136")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setScope("scope109264468")
               .setSemanticSearch(true)
               .build();
       for (SearchEntriesResult element : catalogServiceClient.searchEntries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.SearchEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.SearchEntriesPagedResponse)` |   
  
### searchEntries(String name, String query)
    
    
    public final CatalogServiceClient.SearchEntriesPagedResponse searchEntries(String name, String query)

Searches for Entries matching the given query and scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String query = "query107944136";
       for (SearchEntriesResult element :
           catalogServiceClient.searchEntries(name, query).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project to which the request should be attributed in the following form: `projects/{project}/locations/global`.  
`query` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The query against which entries in scope should be matched. The query syntax is defined in [Search syntax for Dataplex Universal Catalog](https://cloud.google.com/dataplex/docs/search-syntax).  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.SearchEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.SearchEntriesPagedResponse)` |   
  
### searchEntriesCallable()
    
    
    public final UnaryCallable<SearchEntriesRequest,SearchEntriesResponse> searchEntriesCallable()

Searches for Entries matching the given query and scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       SearchEntriesRequest request =
           SearchEntriesRequest.newBuilder()
               .setName(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery("query107944136")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setScope("scope109264468")
               .setSemanticSearch(true)
               .build();
       while (true) {
         SearchEntriesResponse response = catalogServiceClient.searchEntriesCallable().call(request);
         for (SearchEntriesResult element : response.getResultsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest),[SearchEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesResponse)>` |   
  
### searchEntriesPagedCallable()
    
    
    public final UnaryCallable<SearchEntriesRequest,CatalogServiceClient.SearchEntriesPagedResponse> searchEntriesPagedCallable()

Searches for Entries matching the given query and scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       SearchEntriesRequest request =
           SearchEntriesRequest.newBuilder()
               .setName(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setQuery("query107944136")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setScope("scope109264468")
               .setSemanticSearch(true)
               .build();
       ApiFuture<SearchEntriesResult> future =
           catalogServiceClient.searchEntriesPagedCallable().futureCall(request);
       // Do something.
       for (SearchEntriesResult element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.SearchEntriesRequest),[SearchEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.SearchEntriesPagedResponse)>` |   
  
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
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = catalogServiceClient.setIamPolicy(request);
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
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = catalogServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = catalogServiceClient.testIamPermissions(request);
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
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           catalogServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateAspectTypeAsync(AspectType aspectType, FieldMask updateMask)
    
    
    public final OperationFuture<AspectType,OperationMetadata> updateAspectTypeAsync(AspectType aspectType, FieldMask updateMask)

Updates an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       AspectType aspectType = AspectType.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AspectType response =
           catalogServiceClient.updateAspectTypeAsync(aspectType, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`aspectType` | `[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType)`  
Required. AspectType Resource  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateAspectTypeAsync(UpdateAspectTypeRequest request)
    
    
    public final OperationFuture<AspectType,OperationMetadata> updateAspectTypeAsync(UpdateAspectTypeRequest request)

Updates an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateAspectTypeRequest request =
           UpdateAspectTypeRequest.newBuilder()
               .setAspectType(AspectType.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       AspectType response = catalogServiceClient.updateAspectTypeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateAspectTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateAspectTypeCallable()
    
    
    public final UnaryCallable<UpdateAspectTypeRequest,Operation> updateAspectTypeCallable()

Updates an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateAspectTypeRequest request =
           UpdateAspectTypeRequest.newBuilder()
               .setAspectType(AspectType.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.updateAspectTypeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateAspectTypeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAspectTypeOperationCallable()
    
    
    public final OperationCallable<UpdateAspectTypeRequest,AspectType,OperationMetadata> updateAspectTypeOperationCallable()

Updates an AspectType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateAspectTypeRequest request =
           UpdateAspectTypeRequest.newBuilder()
               .setAspectType(AspectType.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<AspectType, OperationMetadata> future =
           catalogServiceClient.updateAspectTypeOperationCallable().futureCall(request);
       // Do something.
       AspectType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAspectTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateAspectTypeRequest),[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateEntry(Entry entry, FieldMask updateMask)
    
    
    public final Entry updateEntry(Entry entry, FieldMask updateMask)

Updates an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       Entry entry = Entry.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Entry response = catalogServiceClient.updateEntry(entry, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`entry` | `[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)`  
Required. Entry resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Mask of fields to update. To update Aspects, the update_mask must contain the value "aspects". If the update_mask is empty, the service will update all modifiable fields present in the request.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### updateEntry(UpdateEntryRequest request)
    
    
    public final Entry updateEntry(UpdateEntryRequest request)

Updates an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateEntryRequest request =
           UpdateEntryRequest.newBuilder()
               .setEntry(Entry.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAllowMissing(true)
               .setDeleteMissingAspects(true)
               .addAllAspectKeys(new ArrayList<String>())
               .build();
       Entry response = catalogServiceClient.updateEntry(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)` |   
  
### updateEntryCallable()
    
    
    public final UnaryCallable<UpdateEntryRequest,Entry> updateEntryCallable()

Updates an Entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateEntryRequest request =
           UpdateEntryRequest.newBuilder()
               .setEntry(Entry.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAllowMissing(true)
               .setDeleteMissingAspects(true)
               .addAllAspectKeys(new ArrayList<String>())
               .build();
       ApiFuture<Entry> future = catalogServiceClient.updateEntryCallable().futureCall(request);
       // Do something.
       Entry response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryRequest),[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Entry)>` |   
  
### updateEntryGroupAsync(EntryGroup entryGroup, FieldMask updateMask)
    
    
    public final OperationFuture<EntryGroup,OperationMetadata> updateEntryGroupAsync(EntryGroup entryGroup, FieldMask updateMask)

Updates an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryGroup entryGroup = EntryGroup.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       EntryGroup response =
           catalogServiceClient.updateEntryGroupAsync(entryGroup, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`entryGroup` | `[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup)`  
Required. EntryGroup Resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateEntryGroupAsync(UpdateEntryGroupRequest request)
    
    
    public final OperationFuture<EntryGroup,OperationMetadata> updateEntryGroupAsync(UpdateEntryGroupRequest request)

Updates an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateEntryGroupRequest request =
           UpdateEntryGroupRequest.newBuilder()
               .setEntryGroup(EntryGroup.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       EntryGroup response = catalogServiceClient.updateEntryGroupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateEntryGroupCallable()
    
    
    public final UnaryCallable<UpdateEntryGroupRequest,Operation> updateEntryGroupCallable()

Updates an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateEntryGroupRequest request =
           UpdateEntryGroupRequest.newBuilder()
               .setEntryGroup(EntryGroup.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.updateEntryGroupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateEntryGroupOperationCallable()
    
    
    public final OperationCallable<UpdateEntryGroupRequest,EntryGroup,OperationMetadata> updateEntryGroupOperationCallable()

Updates an EntryGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateEntryGroupRequest request =
           UpdateEntryGroupRequest.newBuilder()
               .setEntryGroup(EntryGroup.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<EntryGroup, OperationMetadata> future =
           catalogServiceClient.updateEntryGroupOperationCallable().futureCall(request);
       // Do something.
       EntryGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryGroupRequest),[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateEntryLink(EntryLink entryLink)
    
    
    public final EntryLink updateEntryLink(EntryLink entryLink)

Updates an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryLink entryLink = EntryLink.newBuilder().build();
       EntryLink response = catalogServiceClient.updateEntryLink(entryLink);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`entryLink` | `[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)`  
Required. Entry Link resource.  
**Returns**  
---  
**Type** | **Description**  
`[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)` |   
  
### updateEntryLink(UpdateEntryLinkRequest request)
    
    
    public final EntryLink updateEntryLink(UpdateEntryLinkRequest request)

Updates an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateEntryLinkRequest request =
           UpdateEntryLinkRequest.newBuilder()
               .setEntryLink(EntryLink.newBuilder().build())
               .setAllowMissing(true)
               .addAllAspectKeys(new ArrayList<String>())
               .build();
       EntryLink response = catalogServiceClient.updateEntryLink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryLinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)` |   
  
### updateEntryLinkCallable()
    
    
    public final UnaryCallable<UpdateEntryLinkRequest,EntryLink> updateEntryLinkCallable()

Updates an Entry Link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateEntryLinkRequest request =
           UpdateEntryLinkRequest.newBuilder()
               .setEntryLink(EntryLink.newBuilder().build())
               .setAllowMissing(true)
               .addAllAspectKeys(new ArrayList<String>())
               .build();
       ApiFuture<EntryLink> future =
           catalogServiceClient.updateEntryLinkCallable().futureCall(request);
       // Do something.
       EntryLink response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEntryLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryLinkRequest),[EntryLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryLink)>` |   
  
### updateEntryTypeAsync(EntryType entryType, FieldMask updateMask)
    
    
    public final OperationFuture<EntryType,OperationMetadata> updateEntryTypeAsync(EntryType entryType, FieldMask updateMask)

Updates an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       EntryType entryType = EntryType.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       EntryType response = catalogServiceClient.updateEntryTypeAsync(entryType, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`entryType` | `[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType)`  
Required. EntryType Resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateEntryTypeAsync(UpdateEntryTypeRequest request)
    
    
    public final OperationFuture<EntryType,OperationMetadata> updateEntryTypeAsync(UpdateEntryTypeRequest request)

Updates an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateEntryTypeRequest request =
           UpdateEntryTypeRequest.newBuilder()
               .setEntryType(EntryType.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       EntryType response = catalogServiceClient.updateEntryTypeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEntryTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateEntryTypeCallable()
    
    
    public final UnaryCallable<UpdateEntryTypeRequest,Operation> updateEntryTypeCallable()

Updates an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateEntryTypeRequest request =
           UpdateEntryTypeRequest.newBuilder()
               .setEntryType(EntryType.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.updateEntryTypeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEntryTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryTypeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateEntryTypeOperationCallable()
    
    
    public final OperationCallable<UpdateEntryTypeRequest,EntryType,OperationMetadata> updateEntryTypeOperationCallable()

Updates an EntryType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateEntryTypeRequest request =
           UpdateEntryTypeRequest.newBuilder()
               .setEntryType(EntryType.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<EntryType, OperationMetadata> future =
           catalogServiceClient.updateEntryTypeOperationCallable().futureCall(request);
       // Do something.
       EntryType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateEntryTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEntryTypeRequest),[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EntryType),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateMetadataFeedAsync(MetadataFeed metadataFeed, FieldMask updateMask)
    
    
    public final OperationFuture<MetadataFeed,OperationMetadata> updateMetadataFeedAsync(MetadataFeed metadataFeed, FieldMask updateMask)

Updates a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       MetadataFeed metadataFeed = MetadataFeed.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       MetadataFeed response =
           catalogServiceClient.updateMetadataFeedAsync(metadataFeed, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`metadataFeed` | `[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed)`  
Required. Update description. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Mask of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateMetadataFeedAsync(UpdateMetadataFeedRequest request)
    
    
    public final OperationFuture<MetadataFeed,OperationMetadata> updateMetadataFeedAsync(UpdateMetadataFeedRequest request)

Updates a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateMetadataFeedRequest request =
           UpdateMetadataFeedRequest.newBuilder()
               .setMetadataFeed(MetadataFeed.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       MetadataFeed response = catalogServiceClient.updateMetadataFeedAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateMetadataFeedRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateMetadataFeedCallable()
    
    
    public final UnaryCallable<UpdateMetadataFeedRequest,Operation> updateMetadataFeedCallable()

Updates a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateMetadataFeedRequest request =
           UpdateMetadataFeedRequest.newBuilder()
               .setMetadataFeed(MetadataFeed.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           catalogServiceClient.updateMetadataFeedCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateMetadataFeedRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateMetadataFeedOperationCallable()
    
    
    public final OperationCallable<UpdateMetadataFeedRequest,MetadataFeed,OperationMetadata> updateMetadataFeedOperationCallable()

Updates a MetadataFeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateMetadataFeedRequest request =
           UpdateMetadataFeedRequest.newBuilder()
               .setMetadataFeed(MetadataFeed.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<MetadataFeed, OperationMetadata> future =
           catalogServiceClient.updateMetadataFeedOperationCallable().futureCall(request);
       // Do something.
       MetadataFeed response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateMetadataFeedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateMetadataFeedRequest),[MetadataFeed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataFeed),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
