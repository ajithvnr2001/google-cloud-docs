---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient
title: Class ArtifactRegistryClient (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:20:17.782921+00:00
---

# Class ArtifactRegistryClient (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ArtifactRegistryClient (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  0.5.0  0.4.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-artifact-registry/google-cloud-artifact-registry/src/main/java/com/google/devtools/artifactregistry/v1beta2/ArtifactRegistryClient.java)| [Product Reference](https://cloud.google.com/artifact-registry)| [REST Documentation](https://cloud.google.com/artifact-registry/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/artifact-registry/docs/reference/rpc)  
---|---|---|---  
  
Service Description: The Artifact Registry API service.

Artifact Registry is an artifact management system for storing artifacts from different package management systems.

The resources managed by this API are:

  * Repositories, which group packages and their data. 
  * Packages, which group versions and their tags. 
  * Versions, which are specific forms of a package. 
  * Tags, which represent alternative names for versions. 
  * Files, which contain content and are optionally associated with a Package or Version. 



This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       RepositoryName name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       Repository response = artifactRegistryClient.getRepository(name);
     }
     

Note: close() needs to be called on the ArtifactRegistryClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ImportAptArtifacts |  Imports Apt artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importAptArtifactsAsync(ImportAptArtifactsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importAptArtifactsOperationCallable() 
  * importAptArtifactsCallable() 

  
ImportYumArtifacts |  Imports Yum (RPM) artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importYumArtifactsAsync(ImportYumArtifactsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importYumArtifactsOperationCallable() 
  * importYumArtifactsCallable() 

  
ListRepositories |  Lists repositories. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRepositories(ListRepositoriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRepositories(LocationName parent) 
  * listRepositories(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRepositoriesPagedCallable() 
  * listRepositoriesCallable() 

  
GetRepository |  Gets a repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRepository(GetRepositoryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRepository(RepositoryName name) 
  * getRepository(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRepositoryCallable() 

  
CreateRepository |  Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createRepositoryAsync(CreateRepositoryRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createRepositoryAsync(LocationName parent, Repository repository, String repositoryId) 
  * createRepositoryAsync(String parent, Repository repository, String repositoryId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createRepositoryOperationCallable() 
  * createRepositoryCallable() 

  
UpdateRepository |  Updates a repository. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRepository(UpdateRepositoryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateRepository(Repository repository, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRepositoryCallable() 

  
DeleteRepository |  Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRepositoryAsync(DeleteRepositoryRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteRepositoryAsync(RepositoryName name) 
  * deleteRepositoryAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRepositoryOperationCallable() 
  * deleteRepositoryCallable() 

  
ListPackages |  Lists packages. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPackages(ListPackagesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPackages(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPackagesPagedCallable() 
  * listPackagesCallable() 

  
GetPackage |  Gets a package. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPackage(GetPackageRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPackage(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPackageCallable() 

  
DeletePackage |  Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePackageAsync(DeletePackageRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePackageAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePackageOperationCallable() 
  * deletePackageCallable() 

  
ListVersions |  Lists versions. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listVersions(ListVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listVersionsPagedCallable() 
  * listVersionsCallable() 

  
GetVersion |  Gets a version |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getVersion(GetVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getVersion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getVersionCallable() 

  
DeleteVersion |  Deletes a version and all of its content. The returned operation will complete once the version has been deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteVersionAsync(DeleteVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteVersionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteVersionOperationCallable() 
  * deleteVersionCallable() 

  
ListFiles |  Lists files. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFiles(ListFilesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFiles(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFilesPagedCallable() 
  * listFilesCallable() 

  
GetFile |  Gets a file. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFile(GetFileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFile(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFileCallable() 

  
ListTags |  Lists tags. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTags(ListTagsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTags(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTagsPagedCallable() 
  * listTagsCallable() 

  
GetTag |  Gets a tag. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTag(GetTagRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTag(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTagCallable() 

  
CreateTag |  Creates a tag. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTag(CreateTagRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTag(String parent, Tag tag, String tagId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTagCallable() 

  
UpdateTag |  Updates a tag. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTag(UpdateTagRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTag(Tag tag, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTagCallable() 

  
DeleteTag |  Deletes a tag. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTag(DeleteTagRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteTag(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTagCallable() 

  
SetIamPolicy |  Updates the IAM policy for a given resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the IAM policy for a given resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Tests if the caller has a list of permissions on a resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
GetProjectSettings |  Retrieves the Settings for the Project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getProjectSettings(GetProjectSettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getProjectSettings(ProjectSettingsName name) 
  * getProjectSettings(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getProjectSettingsCallable() 

  
UpdateProjectSettings |  Updates the Settings for the Project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateProjectSettings(UpdateProjectSettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateProjectSettings(ProjectSettings projectSettings, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateProjectSettingsCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of ArtifactRegistrySettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ArtifactRegistrySettings artifactRegistrySettings =
         ArtifactRegistrySettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ArtifactRegistryClient artifactRegistryClient =
         ArtifactRegistryClient.create(artifactRegistrySettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ArtifactRegistrySettings artifactRegistrySettings =
         ArtifactRegistrySettings.newBuilder().setEndpoint(myEndpoint).build();
     ArtifactRegistryClient artifactRegistryClient =
         ArtifactRegistryClient.create(artifactRegistrySettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ArtifactRegistrySettings artifactRegistrySettings =
         ArtifactRegistrySettings.newHttpJsonBuilder().build();
     ArtifactRegistryClient artifactRegistryClient =
         ArtifactRegistryClient.create(artifactRegistrySettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ArtifactRegistryClient

## Static Methods 

### create()
    
    
    public static final ArtifactRegistryClient create()

Constructs an instance of ArtifactRegistryClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ArtifactRegistrySettings settings)
    
    
    public static final ArtifactRegistryClient create(ArtifactRegistrySettings settings)

Constructs an instance of ArtifactRegistryClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ArtifactRegistrySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistrySettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ArtifactRegistryStub stub)
    
    
    public static final ArtifactRegistryClient create(ArtifactRegistryStub stub)

Constructs an instance of ArtifactRegistryClient, using the given stub for making calls. This is for advanced usage - prefer using create(ArtifactRegistrySettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ArtifactRegistryStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.stub.ArtifactRegistryStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient)` |   
  
## Constructors 

### ArtifactRegistryClient(ArtifactRegistrySettings settings)
    
    
    protected ArtifactRegistryClient(ArtifactRegistrySettings settings)

Constructs an instance of ArtifactRegistryClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ArtifactRegistrySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistrySettings)`  
  
  
### ArtifactRegistryClient(ArtifactRegistryStub stub)
    
    
    protected ArtifactRegistryClient(ArtifactRegistryStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ArtifactRegistryStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.stub.ArtifactRegistryStub)`  
  
  
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

### createRepositoryAsync(@Nullable LocationName parent, Repository repository, String repositoryId)
    
    
    public final OperationFuture<Repository,OperationMetadata> createRepositoryAsync(@Nullable LocationName parent, Repository repository, String repositoryId)

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Repository repository = Repository.newBuilder().build();
       String repositoryId = "repositoryId2113747461";
       Repository response =
           artifactRegistryClient.createRepositoryAsync(parent, repository, repositoryId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.devtools.artifactregistry.v1beta2.LocationName`  
Required. The name of the parent resource where the repository will be created.  
`repository` | `[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository)`  
The repository to be created.  
`repositoryId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The repository id to use for this repository.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### createRepositoryAsync(CreateRepositoryRequest request)
    
    
    public final OperationFuture<Repository,OperationMetadata> createRepositoryAsync(CreateRepositoryRequest request)

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       CreateRepositoryRequest request =
           CreateRepositoryRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRepositoryId("repositoryId2113747461")
               .setRepository(Repository.newBuilder().build())
               .build();
       Repository response = artifactRegistryClient.createRepositoryAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.CreateRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### createRepositoryAsync(String parent, Repository repository, String repositoryId)
    
    
    public final OperationFuture<Repository,OperationMetadata> createRepositoryAsync(String parent, Repository repository, String repositoryId)

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Repository repository = Repository.newBuilder().build();
       String repositoryId = "repositoryId2113747461";
       Repository response =
           artifactRegistryClient.createRepositoryAsync(parent, repository, repositoryId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource where the repository will be created.  
`repository` | `[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository)`  
The repository to be created.  
`repositoryId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The repository id to use for this repository.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### createRepositoryCallable()
    
    
    public final UnaryCallable<CreateRepositoryRequest,Operation> createRepositoryCallable()

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       CreateRepositoryRequest request =
           CreateRepositoryRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRepositoryId("repositoryId2113747461")
               .setRepository(Repository.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           artifactRegistryClient.createRepositoryCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.CreateRepositoryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRepositoryOperationCallable()
    
    
    public final OperationCallable<CreateRepositoryRequest,Repository,OperationMetadata> createRepositoryOperationCallable()

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       CreateRepositoryRequest request =
           CreateRepositoryRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRepositoryId("repositoryId2113747461")
               .setRepository(Repository.newBuilder().build())
               .build();
       OperationFuture<Repository, OperationMetadata> future =
           artifactRegistryClient.createRepositoryOperationCallable().futureCall(request);
       // Do something.
       Repository response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.CreateRepositoryRequest),[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### createTag(CreateTagRequest request)
    
    
    public final Tag createTag(CreateTagRequest request)

Creates a tag.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       CreateTagRequest request =
           CreateTagRequest.newBuilder()
               .setParent("parent-995424086")
               .setTagId("tagId110119509")
               .setTag(Tag.newBuilder().build())
               .build();
       Tag response = artifactRegistryClient.createTag(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.CreateTagRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Tag)` |   
  
### createTag(String parent, Tag tag, String tagId)
    
    
    public final Tag createTag(String parent, Tag tag, String tagId)

Creates a tag.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String parent = "parent-995424086";
       Tag tag = Tag.newBuilder().build();
       String tagId = "tagId110119509";
       Tag response = artifactRegistryClient.createTag(parent, tag, tagId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the parent resource where the tag will be created.  
`tag` | `[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Tag)`  
The tag to be created.  
`tagId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The tag id to use for this repository.  
**Returns**  
---  
**Type** | **Description**  
`[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Tag)` |   
  
### createTagCallable()
    
    
    public final UnaryCallable<CreateTagRequest,Tag> createTagCallable()

Creates a tag.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       CreateTagRequest request =
           CreateTagRequest.newBuilder()
               .setParent("parent-995424086")
               .setTagId("tagId110119509")
               .setTag(Tag.newBuilder().build())
               .build();
       ApiFuture<Tag> future = artifactRegistryClient.createTagCallable().futureCall(request);
       // Do something.
       Tag response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.CreateTagRequest),[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Tag)>` |   
  
### deletePackageAsync(DeletePackageRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePackageAsync(DeletePackageRequest request)

Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       DeletePackageRequest request =
           DeletePackageRequest.newBuilder().setName("name3373707").build();
       artifactRegistryClient.deletePackageAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePackageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.DeletePackageRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### deletePackageAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePackageAsync(String name)

Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String name = "name3373707";
       artifactRegistryClient.deletePackageAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the package to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### deletePackageCallable()
    
    
    public final UnaryCallable<DeletePackageRequest,Operation> deletePackageCallable()

Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       DeletePackageRequest request =
           DeletePackageRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Operation> future =
           artifactRegistryClient.deletePackageCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePackageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.DeletePackageRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePackageOperationCallable()
    
    
    public final OperationCallable<DeletePackageRequest,Empty,OperationMetadata> deletePackageOperationCallable()

Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       DeletePackageRequest request =
           DeletePackageRequest.newBuilder().setName("name3373707").build();
       OperationFuture<Empty, OperationMetadata> future =
           artifactRegistryClient.deletePackageOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePackageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.DeletePackageRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### deleteRepositoryAsync(@Nullable RepositoryName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteRepositoryAsync(@Nullable RepositoryName name)

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       RepositoryName name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       artifactRegistryClient.deleteRepositoryAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.devtools.artifactregistry.v1beta2.RepositoryName`  
Required. The name of the repository to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### deleteRepositoryAsync(DeleteRepositoryRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteRepositoryAsync(DeleteRepositoryRequest request)

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       DeleteRepositoryRequest request =
           DeleteRepositoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .build();
       artifactRegistryClient.deleteRepositoryAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.DeleteRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### deleteRepositoryAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteRepositoryAsync(String name)

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       artifactRegistryClient.deleteRepositoryAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the repository to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### deleteRepositoryCallable()
    
    
    public final UnaryCallable<DeleteRepositoryRequest,Operation> deleteRepositoryCallable()

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       DeleteRepositoryRequest request =
           DeleteRepositoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .build();
       ApiFuture<Operation> future =
           artifactRegistryClient.deleteRepositoryCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.DeleteRepositoryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRepositoryOperationCallable()
    
    
    public final OperationCallable<DeleteRepositoryRequest,Empty,OperationMetadata> deleteRepositoryOperationCallable()

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       DeleteRepositoryRequest request =
           DeleteRepositoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           artifactRegistryClient.deleteRepositoryOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.DeleteRepositoryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### deleteTag(DeleteTagRequest request)
    
    
    public final void deleteTag(DeleteTagRequest request)

Deletes a tag.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       DeleteTagRequest request = DeleteTagRequest.newBuilder().setName("name3373707").build();
       artifactRegistryClient.deleteTag(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.DeleteTagRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteTag(String name)
    
    
    public final void deleteTag(String name)

Deletes a tag.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String name = "name3373707";
       artifactRegistryClient.deleteTag(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the tag to delete.  
  
### deleteTagCallable()
    
    
    public final UnaryCallable<DeleteTagRequest,Empty> deleteTagCallable()

Deletes a tag.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       DeleteTagRequest request = DeleteTagRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Empty> future = artifactRegistryClient.deleteTagCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.DeleteTagRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteVersionAsync(DeleteVersionRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteVersionAsync(DeleteVersionRequest request)

Deletes a version and all of its content. The returned operation will complete once the version has been deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       DeleteVersionRequest request =
           DeleteVersionRequest.newBuilder().setName("name3373707").setForce(true).build();
       artifactRegistryClient.deleteVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.DeleteVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### deleteVersionAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteVersionAsync(String name)

Deletes a version and all of its content. The returned operation will complete once the version has been deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String name = "name3373707";
       artifactRegistryClient.deleteVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the version to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### deleteVersionCallable()
    
    
    public final UnaryCallable<DeleteVersionRequest,Operation> deleteVersionCallable()

Deletes a version and all of its content. The returned operation will complete once the version has been deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       DeleteVersionRequest request =
           DeleteVersionRequest.newBuilder().setName("name3373707").setForce(true).build();
       ApiFuture<Operation> future =
           artifactRegistryClient.deleteVersionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.DeleteVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteVersionOperationCallable()
    
    
    public final OperationCallable<DeleteVersionRequest,Empty,OperationMetadata> deleteVersionOperationCallable()

Deletes a version and all of its content. The returned operation will complete once the version has been deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       DeleteVersionRequest request =
           DeleteVersionRequest.newBuilder().setName("name3373707").setForce(true).build();
       OperationFuture<Empty, OperationMetadata> future =
           artifactRegistryClient.deleteVersionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.DeleteVersionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.OperationMetadata)>` |   
  
### getFile(GetFileRequest request)
    
    
    public final File getFile(GetFileRequest request)

Gets a file.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetFileRequest request = GetFileRequest.newBuilder().setName("name3373707").build();
       File response = artifactRegistryClient.getFile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.GetFileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[File](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.File)` |   
  
### getFile(String name)
    
    
    public final File getFile(String name)

Gets a file.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String name = "name3373707";
       File response = artifactRegistryClient.getFile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the file to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[File](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.File)` |   
  
### getFileCallable()
    
    
    public final UnaryCallable<GetFileRequest,File> getFileCallable()

Gets a file.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetFileRequest request = GetFileRequest.newBuilder().setName("name3373707").build();
       ApiFuture<File> future = artifactRegistryClient.getFileCallable().futureCall(request);
       // Do something.
       File response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.GetFileRequest),[File](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.File)>` |   
  
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

Gets the IAM policy for a given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = artifactRegistryClient.getIamPolicy(request);
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

Gets the IAM policy for a given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = artifactRegistryClient.getIamPolicyCallable().futureCall(request);
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
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = artifactRegistryClient.getLocation(request);
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
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = artifactRegistryClient.getLocationCallable().futureCall(request);
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
  
### getPackage(GetPackageRequest request)
    
    
    public final Package getPackage(GetPackageRequest request)

Gets a package.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetPackageRequest request = GetPackageRequest.newBuilder().setName("name3373707").build();
       Package response = artifactRegistryClient.getPackage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPackageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.GetPackageRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Package](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Package)` |   
  
### getPackage(String name)
    
    
    public final Package getPackage(String name)

Gets a package.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String name = "name3373707";
       Package response = artifactRegistryClient.getPackage(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the package to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Package](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Package)` |   
  
### getPackageCallable()
    
    
    public final UnaryCallable<GetPackageRequest,Package> getPackageCallable()

Gets a package.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetPackageRequest request = GetPackageRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Package> future = artifactRegistryClient.getPackageCallable().futureCall(request);
       // Do something.
       Package response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPackageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.GetPackageRequest),[Package](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Package)>` |   
  
### getProjectSettings(@Nullable ProjectSettingsName name)
    
    
    public final ProjectSettings getProjectSettings(@Nullable ProjectSettingsName name)

Retrieves the Settings for the Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ProjectSettingsName name = ProjectSettingsName.of("[PROJECT]");
       ProjectSettings response = artifactRegistryClient.getProjectSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.devtools.artifactregistry.v1beta2.ProjectSettingsName`  
Required. The name of the projectSettings resource.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ProjectSettings)` |   
  
### getProjectSettings(GetProjectSettingsRequest request)
    
    
    public final ProjectSettings getProjectSettings(GetProjectSettingsRequest request)

Retrieves the Settings for the Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetProjectSettingsRequest request =
           GetProjectSettingsRequest.newBuilder()
               .setName(ProjectSettingsName.of("[PROJECT]").toString())
               .build();
       ProjectSettings response = artifactRegistryClient.getProjectSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetProjectSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.GetProjectSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ProjectSettings)` |   
  
### getProjectSettings(String name)
    
    
    public final ProjectSettings getProjectSettings(String name)

Retrieves the Settings for the Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String name = ProjectSettingsName.of("[PROJECT]").toString();
       ProjectSettings response = artifactRegistryClient.getProjectSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the projectSettings resource.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ProjectSettings)` |   
  
### getProjectSettingsCallable()
    
    
    public final UnaryCallable<GetProjectSettingsRequest,ProjectSettings> getProjectSettingsCallable()

Retrieves the Settings for the Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetProjectSettingsRequest request =
           GetProjectSettingsRequest.newBuilder()
               .setName(ProjectSettingsName.of("[PROJECT]").toString())
               .build();
       ApiFuture<ProjectSettings> future =
           artifactRegistryClient.getProjectSettingsCallable().futureCall(request);
       // Do something.
       ProjectSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetProjectSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.GetProjectSettingsRequest),[ProjectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ProjectSettings)>` |   
  
### getRepository(@Nullable RepositoryName name)
    
    
    public final Repository getRepository(@Nullable RepositoryName name)

Gets a repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       RepositoryName name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
       Repository response = artifactRegistryClient.getRepository(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.devtools.artifactregistry.v1beta2.RepositoryName`  
Required. The name of the repository to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository)` |   
  
### getRepository(GetRepositoryRequest request)
    
    
    public final Repository getRepository(GetRepositoryRequest request)

Gets a repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetRepositoryRequest request =
           GetRepositoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .build();
       Repository response = artifactRegistryClient.getRepository(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.GetRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository)` |   
  
### getRepository(String name)
    
    
    public final Repository getRepository(String name)

Gets a repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String name = RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString();
       Repository response = artifactRegistryClient.getRepository(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the repository to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository)` |   
  
### getRepositoryCallable()
    
    
    public final UnaryCallable<GetRepositoryRequest,Repository> getRepositoryCallable()

Gets a repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetRepositoryRequest request =
           GetRepositoryRequest.newBuilder()
               .setName(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .build();
       ApiFuture<Repository> future =
           artifactRegistryClient.getRepositoryCallable().futureCall(request);
       // Do something.
       Repository response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.GetRepositoryRequest),[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository)>` |   
  
### getSettings()
    
    
    public final @Nullable ArtifactRegistrySettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.devtools.artifactregistry.v1beta2.ArtifactRegistrySettings` |   
  
### getStub()
    
    
    public ArtifactRegistryStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.stub.ArtifactRegistryStub)` |   
  
### getTag(GetTagRequest request)
    
    
    public final Tag getTag(GetTagRequest request)

Gets a tag.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetTagRequest request = GetTagRequest.newBuilder().setName("name3373707").build();
       Tag response = artifactRegistryClient.getTag(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.GetTagRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Tag)` |   
  
### getTag(String name)
    
    
    public final Tag getTag(String name)

Gets a tag.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String name = "name3373707";
       Tag response = artifactRegistryClient.getTag(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the tag to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Tag)` |   
  
### getTagCallable()
    
    
    public final UnaryCallable<GetTagRequest,Tag> getTagCallable()

Gets a tag.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetTagRequest request = GetTagRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Tag> future = artifactRegistryClient.getTagCallable().futureCall(request);
       // Do something.
       Tag response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.GetTagRequest),[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Tag)>` |   
  
### getVersion(GetVersionRequest request)
    
    
    public final Version getVersion(GetVersionRequest request)

Gets a version

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetVersionRequest request =
           GetVersionRequest.newBuilder()
               .setName("name3373707")
               .setView(VersionView.forNumber(0))
               .build();
       Version response = artifactRegistryClient.getVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.GetVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Version)` |   
  
### getVersion(String name)
    
    
    public final Version getVersion(String name)

Gets a version

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String name = "name3373707";
       Version response = artifactRegistryClient.getVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the version to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Version)` |   
  
### getVersionCallable()
    
    
    public final UnaryCallable<GetVersionRequest,Version> getVersionCallable()

Gets a version

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       GetVersionRequest request =
           GetVersionRequest.newBuilder()
               .setName("name3373707")
               .setView(VersionView.forNumber(0))
               .build();
       ApiFuture<Version> future = artifactRegistryClient.getVersionCallable().futureCall(request);
       // Do something.
       Version response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.GetVersionRequest),[Version](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Version)>` |   
  
### importAptArtifactsAsync(ImportAptArtifactsRequest request)
    
    
    public final OperationFuture<ImportAptArtifactsResponse,ImportAptArtifactsMetadata> importAptArtifactsAsync(ImportAptArtifactsRequest request)

Imports Apt artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ImportAptArtifactsRequest request =
           ImportAptArtifactsRequest.newBuilder().setParent("parent-995424086").build();
       ImportAptArtifactsResponse response =
           artifactRegistryClient.importAptArtifactsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportAptArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportAptArtifactsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportAptArtifactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportAptArtifactsResponse),[ImportAptArtifactsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportAptArtifactsMetadata)>` |   
  
### importAptArtifactsCallable()
    
    
    public final UnaryCallable<ImportAptArtifactsRequest,Operation> importAptArtifactsCallable()

Imports Apt artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ImportAptArtifactsRequest request =
           ImportAptArtifactsRequest.newBuilder().setParent("parent-995424086").build();
       ApiFuture<Operation> future =
           artifactRegistryClient.importAptArtifactsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportAptArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportAptArtifactsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importAptArtifactsOperationCallable()
    
    
    public final OperationCallable<ImportAptArtifactsRequest,ImportAptArtifactsResponse,ImportAptArtifactsMetadata> importAptArtifactsOperationCallable()

Imports Apt artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ImportAptArtifactsRequest request =
           ImportAptArtifactsRequest.newBuilder().setParent("parent-995424086").build();
       OperationFuture<ImportAptArtifactsResponse, ImportAptArtifactsMetadata> future =
           artifactRegistryClient.importAptArtifactsOperationCallable().futureCall(request);
       // Do something.
       ImportAptArtifactsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportAptArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportAptArtifactsRequest),[ImportAptArtifactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportAptArtifactsResponse),[ImportAptArtifactsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportAptArtifactsMetadata)>` |   
  
### importYumArtifactsAsync(ImportYumArtifactsRequest request)
    
    
    public final OperationFuture<ImportYumArtifactsResponse,ImportYumArtifactsMetadata> importYumArtifactsAsync(ImportYumArtifactsRequest request)

Imports Yum (RPM) artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ImportYumArtifactsRequest request =
           ImportYumArtifactsRequest.newBuilder().setParent("parent-995424086").build();
       ImportYumArtifactsResponse response =
           artifactRegistryClient.importYumArtifactsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportYumArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportYumArtifactsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportYumArtifactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportYumArtifactsResponse),[ImportYumArtifactsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportYumArtifactsMetadata)>` |   
  
### importYumArtifactsCallable()
    
    
    public final UnaryCallable<ImportYumArtifactsRequest,Operation> importYumArtifactsCallable()

Imports Yum (RPM) artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ImportYumArtifactsRequest request =
           ImportYumArtifactsRequest.newBuilder().setParent("parent-995424086").build();
       ApiFuture<Operation> future =
           artifactRegistryClient.importYumArtifactsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportYumArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportYumArtifactsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importYumArtifactsOperationCallable()
    
    
    public final OperationCallable<ImportYumArtifactsRequest,ImportYumArtifactsResponse,ImportYumArtifactsMetadata> importYumArtifactsOperationCallable()

Imports Yum (RPM) artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ImportYumArtifactsRequest request =
           ImportYumArtifactsRequest.newBuilder().setParent("parent-995424086").build();
       OperationFuture<ImportYumArtifactsResponse, ImportYumArtifactsMetadata> future =
           artifactRegistryClient.importYumArtifactsOperationCallable().futureCall(request);
       // Do something.
       ImportYumArtifactsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportYumArtifactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportYumArtifactsRequest),[ImportYumArtifactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportYumArtifactsResponse),[ImportYumArtifactsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ImportYumArtifactsMetadata)>` |   
  
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
  
### listFiles(ListFilesRequest request)
    
    
    public final ArtifactRegistryClient.ListFilesPagedResponse listFiles(ListFilesRequest request)

Lists files.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListFilesRequest request =
           ListFilesRequest.newBuilder()
               .setParent("parent-995424086")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (File element : artifactRegistryClient.listFiles(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListFilesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient.ListFilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListFilesPagedResponse)` |   
  
### listFiles(String parent)
    
    
    public final ArtifactRegistryClient.ListFilesPagedResponse listFiles(String parent)

Lists files.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String parent = "parent-995424086";
       for (File element : artifactRegistryClient.listFiles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the repository whose files will be listed. For example: "projects/p1/locations/us-central1/repositories/repo1  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient.ListFilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListFilesPagedResponse)` |   
  
### listFilesCallable()
    
    
    public final UnaryCallable<ListFilesRequest,ListFilesResponse> listFilesCallable()

Lists files.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListFilesRequest request =
           ListFilesRequest.newBuilder()
               .setParent("parent-995424086")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListFilesResponse response = artifactRegistryClient.listFilesCallable().call(request);
         for (File element : response.getFilesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListFilesRequest),[ListFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListFilesResponse)>` |   
  
### listFilesPagedCallable()
    
    
    public final UnaryCallable<ListFilesRequest,ArtifactRegistryClient.ListFilesPagedResponse> listFilesPagedCallable()

Lists files.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListFilesRequest request =
           ListFilesRequest.newBuilder()
               .setParent("parent-995424086")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<File> future = artifactRegistryClient.listFilesPagedCallable().futureCall(request);
       // Do something.
       for (File element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListFilesRequest),[ListFilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListFilesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final ArtifactRegistryClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : artifactRegistryClient.listLocations(request).iterateAll()) {
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
`[ArtifactRegistryClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             artifactRegistryClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ArtifactRegistryClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           artifactRegistryClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListLocationsPagedResponse)>` |   
  
### listPackages(ListPackagesRequest request)
    
    
    public final ArtifactRegistryClient.ListPackagesPagedResponse listPackages(ListPackagesRequest request)

Lists packages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListPackagesRequest request =
           ListPackagesRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Package element : artifactRegistryClient.listPackages(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPackagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListPackagesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient.ListPackagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListPackagesPagedResponse)` |   
  
### listPackages(String parent)
    
    
    public final ArtifactRegistryClient.ListPackagesPagedResponse listPackages(String parent)

Lists packages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String parent = "parent-995424086";
       for (Package element : artifactRegistryClient.listPackages(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the parent resource whose packages will be listed.  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient.ListPackagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListPackagesPagedResponse)` |   
  
### listPackagesCallable()
    
    
    public final UnaryCallable<ListPackagesRequest,ListPackagesResponse> listPackagesCallable()

Lists packages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListPackagesRequest request =
           ListPackagesRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListPackagesResponse response = artifactRegistryClient.listPackagesCallable().call(request);
         for (Package element : response.getPackagesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPackagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListPackagesRequest),[ListPackagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListPackagesResponse)>` |   
  
### listPackagesPagedCallable()
    
    
    public final UnaryCallable<ListPackagesRequest,ArtifactRegistryClient.ListPackagesPagedResponse> listPackagesPagedCallable()

Lists packages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListPackagesRequest request =
           ListPackagesRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Package> future =
           artifactRegistryClient.listPackagesPagedCallable().futureCall(request);
       // Do something.
       for (Package element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPackagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListPackagesRequest),[ListPackagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListPackagesPagedResponse)>` |   
  
### listRepositories(@Nullable LocationName parent)
    
    
    public final ArtifactRegistryClient.ListRepositoriesPagedResponse listRepositories(@Nullable LocationName parent)

Lists repositories.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Repository element : artifactRegistryClient.listRepositories(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.devtools.artifactregistry.v1beta2.LocationName`  
Required. The name of the parent resource whose repositories will be listed.  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient.ListRepositoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListRepositoriesPagedResponse)` |   
  
### listRepositories(ListRepositoriesRequest request)
    
    
    public final ArtifactRegistryClient.ListRepositoriesPagedResponse listRepositories(ListRepositoriesRequest request)

Lists repositories.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListRepositoriesRequest request =
           ListRepositoriesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Repository element : artifactRegistryClient.listRepositories(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListRepositoriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient.ListRepositoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListRepositoriesPagedResponse)` |   
  
### listRepositories(String parent)
    
    
    public final ArtifactRegistryClient.ListRepositoriesPagedResponse listRepositories(String parent)

Lists repositories.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Repository element : artifactRegistryClient.listRepositories(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource whose repositories will be listed.  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient.ListRepositoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListRepositoriesPagedResponse)` |   
  
### listRepositoriesCallable()
    
    
    public final UnaryCallable<ListRepositoriesRequest,ListRepositoriesResponse> listRepositoriesCallable()

Lists repositories.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListRepositoriesRequest request =
           ListRepositoriesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListRepositoriesResponse response =
             artifactRegistryClient.listRepositoriesCallable().call(request);
         for (Repository element : response.getRepositoriesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListRepositoriesRequest),[ListRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListRepositoriesResponse)>` |   
  
### listRepositoriesPagedCallable()
    
    
    public final UnaryCallable<ListRepositoriesRequest,ArtifactRegistryClient.ListRepositoriesPagedResponse> listRepositoriesPagedCallable()

Lists repositories.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListRepositoriesRequest request =
           ListRepositoriesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Repository> future =
           artifactRegistryClient.listRepositoriesPagedCallable().futureCall(request);
       // Do something.
       for (Repository element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListRepositoriesRequest),[ListRepositoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListRepositoriesPagedResponse)>` |   
  
### listTags(ListTagsRequest request)
    
    
    public final ArtifactRegistryClient.ListTagsPagedResponse listTags(ListTagsRequest request)

Lists tags.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListTagsRequest request =
           ListTagsRequest.newBuilder()
               .setParent("parent-995424086")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Tag element : artifactRegistryClient.listTags(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTagsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListTagsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient.ListTagsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListTagsPagedResponse)` |   
  
### listTags(String parent)
    
    
    public final ArtifactRegistryClient.ListTagsPagedResponse listTags(String parent)

Lists tags.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String parent = "parent-995424086";
       for (Tag element : artifactRegistryClient.listTags(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the parent resource whose tags will be listed.  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient.ListTagsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListTagsPagedResponse)` |   
  
### listTagsCallable()
    
    
    public final UnaryCallable<ListTagsRequest,ListTagsResponse> listTagsCallable()

Lists tags.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListTagsRequest request =
           ListTagsRequest.newBuilder()
               .setParent("parent-995424086")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListTagsResponse response = artifactRegistryClient.listTagsCallable().call(request);
         for (Tag element : response.getTagsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTagsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListTagsRequest),[ListTagsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListTagsResponse)>` |   
  
### listTagsPagedCallable()
    
    
    public final UnaryCallable<ListTagsRequest,ArtifactRegistryClient.ListTagsPagedResponse> listTagsPagedCallable()

Lists tags.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListTagsRequest request =
           ListTagsRequest.newBuilder()
               .setParent("parent-995424086")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Tag> future = artifactRegistryClient.listTagsPagedCallable().futureCall(request);
       // Do something.
       for (Tag element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTagsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListTagsRequest),[ListTagsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListTagsPagedResponse)>` |   
  
### listVersions(ListVersionsRequest request)
    
    
    public final ArtifactRegistryClient.ListVersionsPagedResponse listVersions(ListVersionsRequest request)

Lists versions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListVersionsRequest request =
           ListVersionsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(VersionView.forNumber(0))
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Version element : artifactRegistryClient.listVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient.ListVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListVersionsPagedResponse)` |   
  
### listVersions(String parent)
    
    
    public final ArtifactRegistryClient.ListVersionsPagedResponse listVersions(String parent)

Lists versions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       String parent = "parent-995424086";
       for (Version element : artifactRegistryClient.listVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the parent resource whose versions will be listed.  
**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient.ListVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListVersionsPagedResponse)` |   
  
### listVersionsCallable()
    
    
    public final UnaryCallable<ListVersionsRequest,ListVersionsResponse> listVersionsCallable()

Lists versions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListVersionsRequest request =
           ListVersionsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(VersionView.forNumber(0))
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListVersionsResponse response = artifactRegistryClient.listVersionsCallable().call(request);
         for (Version element : response.getVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListVersionsRequest),[ListVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListVersionsResponse)>` |   
  
### listVersionsPagedCallable()
    
    
    public final UnaryCallable<ListVersionsRequest,ArtifactRegistryClient.ListVersionsPagedResponse> listVersionsPagedCallable()

Lists versions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ListVersionsRequest request =
           ListVersionsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(VersionView.forNumber(0))
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Version> future =
           artifactRegistryClient.listVersionsPagedCallable().futureCall(request);
       // Do something.
       for (Version element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ListVersionsRequest),[ListVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ArtifactRegistryClient.ListVersionsPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Updates the IAM policy for a given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = artifactRegistryClient.setIamPolicy(request);
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

Updates the IAM policy for a given resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = artifactRegistryClient.setIamPolicyCallable().futureCall(request);
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

Tests if the caller has a list of permissions on a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = artifactRegistryClient.testIamPermissions(request);
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

Tests if the caller has a list of permissions on a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(RepositoryName.of("[PROJECT]", "[LOCATION]", "[REPOSITORY]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           artifactRegistryClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateProjectSettings(ProjectSettings projectSettings, FieldMask updateMask)
    
    
    public final ProjectSettings updateProjectSettings(ProjectSettings projectSettings, FieldMask updateMask)

Updates the Settings for the Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       ProjectSettings projectSettings = ProjectSettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ProjectSettings response =
           artifactRegistryClient.updateProjectSettings(projectSettings, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectSettings` | `[ProjectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ProjectSettings)`  
The project settings.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask to support partial updates.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ProjectSettings)` |   
  
### updateProjectSettings(UpdateProjectSettingsRequest request)
    
    
    public final ProjectSettings updateProjectSettings(UpdateProjectSettingsRequest request)

Updates the Settings for the Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       UpdateProjectSettingsRequest request =
           UpdateProjectSettingsRequest.newBuilder()
               .setProjectSettings(ProjectSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ProjectSettings response = artifactRegistryClient.updateProjectSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateProjectSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.UpdateProjectSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ProjectSettings)` |   
  
### updateProjectSettingsCallable()
    
    
    public final UnaryCallable<UpdateProjectSettingsRequest,ProjectSettings> updateProjectSettingsCallable()

Updates the Settings for the Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       UpdateProjectSettingsRequest request =
           UpdateProjectSettingsRequest.newBuilder()
               .setProjectSettings(ProjectSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ProjectSettings> future =
           artifactRegistryClient.updateProjectSettingsCallable().futureCall(request);
       // Do something.
       ProjectSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateProjectSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.UpdateProjectSettingsRequest),[ProjectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.ProjectSettings)>` |   
  
### updateRepository(Repository repository, FieldMask updateMask)
    
    
    public final Repository updateRepository(Repository repository, FieldMask updateMask)

Updates a repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       Repository repository = Repository.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Repository response = artifactRegistryClient.updateRepository(repository, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`repository` | `[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository)`  
The repository that replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository)` |   
  
### updateRepository(UpdateRepositoryRequest request)
    
    
    public final Repository updateRepository(UpdateRepositoryRequest request)

Updates a repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       UpdateRepositoryRequest request =
           UpdateRepositoryRequest.newBuilder()
               .setRepository(Repository.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Repository response = artifactRegistryClient.updateRepository(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.UpdateRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository)` |   
  
### updateRepositoryCallable()
    
    
    public final UnaryCallable<UpdateRepositoryRequest,Repository> updateRepositoryCallable()

Updates a repository.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       UpdateRepositoryRequest request =
           UpdateRepositoryRequest.newBuilder()
               .setRepository(Repository.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Repository> future =
           artifactRegistryClient.updateRepositoryCallable().futureCall(request);
       // Do something.
       Repository response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.UpdateRepositoryRequest),[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Repository)>` |   
  
### updateTag(Tag tag, FieldMask updateMask)
    
    
    public final Tag updateTag(Tag tag, FieldMask updateMask)

Updates a tag.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       Tag tag = Tag.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Tag response = artifactRegistryClient.updateTag(tag, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tag` | `[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Tag)`  
The tag that replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
**Returns**  
---  
**Type** | **Description**  
`[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Tag)` |   
  
### updateTag(UpdateTagRequest request)
    
    
    public final Tag updateTag(UpdateTagRequest request)

Updates a tag.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       UpdateTagRequest request =
           UpdateTagRequest.newBuilder()
               .setTag(Tag.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Tag response = artifactRegistryClient.updateTag(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.UpdateTagRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Tag)` |   
  
### updateTagCallable()
    
    
    public final UnaryCallable<UpdateTagRequest,Tag> updateTagCallable()

Updates a tag.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ArtifactRegistryClient artifactRegistryClient = ArtifactRegistryClient.create()) {
       UpdateTagRequest request =
           UpdateTagRequest.newBuilder()
               .setTag(Tag.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Tag> future = artifactRegistryClient.updateTagCallable().futureCall(request);
       // Do something.
       Tag response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.UpdateTagRequest),[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-artifact-registry/latest/com.google.devtools.artifactregistry.v1beta2.Tag)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
