---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsSettings
title: Class ProjectsSettings (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:32.551545+00:00
---

# Class ProjectsSettings (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ProjectsSettings (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.97.0  1.96.0  1.95.0  1.93.0  1.90.0  1.89.0  1.87.0  1.85.0  1.84.0  1.82.0  1.80.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.72.0  1.70.0  1.69.0  1.66.0  1.65.0  1.64.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.6  1.4.0  1.3.2  1.2.12 
    
    
    public class ProjectsSettings extends ClientSettings<ProjectsSettings>

Settings class to configure an instance of [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient).

The default instance has everything set to sensible defaults:

  * The default service address (cloudresourcemanager.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getProject:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProjectsSettings.Builder projectsSettingsBuilder = ProjectsSettings.newBuilder();
     projectsSettingsBuilder
         .getProjectSettings()
         .setRetrySettings(
             projectsSettingsBuilder
                 .getProjectSettings()
                 .getRetrySettings()
                 .toBuilder()
                 .setInitialRetryDelayDuration(Duration.ofSeconds(1))
                 .setInitialRpcTimeoutDuration(Duration.ofSeconds(5))
                 .setMaxAttempts(5)
                 .setMaxRetryDelayDuration(Duration.ofSeconds(30))
                 .setMaxRpcTimeoutDuration(Duration.ofSeconds(60))
                 .setRetryDelayMultiplier(1.3)
                 .setRpcTimeoutMultiplier(1.5)
                 .setTotalTimeoutDuration(Duration.ofSeconds(300))
                 .build());
     ProjectsSettings projectsSettings = projectsSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createProject:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProjectsSettings.Builder projectsSettingsBuilder = ProjectsSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     projectsSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > ProjectsSettings

## Inherited Members

[ClientSettings.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

[ClientSettings.getApiKey()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getApiKey__)

[ClientSettings.getBackgroundExecutorProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getBackgroundExecutorProvider__)

[ClientSettings.getClock()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getClock__)

[ClientSettings.getCredentialsProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getCredentialsProvider__)

[ClientSettings.getEndpoint()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getEndpoint__)

[ClientSettings.getExecutorProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getExecutorProvider__)

[ClientSettings.getGdchApiAudience()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getGdchApiAudience__)

[ClientSettings.getHeaderProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getHeaderProvider__)

[ClientSettings.getInternalHeaderProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getInternalHeaderProvider__)

[ClientSettings.getQuotaProjectId()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getQuotaProjectId__)

[ClientSettings.getStubSettings()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getStubSettings__)

[ClientSettings.getTransportChannelProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getTransportChannelProvider__)

[ClientSettings.getUniverseDomain()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getUniverseDomain__)

[ClientSettings.getWatchdogCheckInterval()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getWatchdogCheckInterval__)

[ClientSettings.getWatchdogCheckIntervalDuration()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getWatchdogCheckIntervalDuration__)

[ClientSettings.getWatchdogProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getWatchdogProvider__)

[ClientSettings.toString()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### create(ProjectsStubSettings stub)
    
    
    public static final ProjectsSettings create(ProjectsStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ProjectsStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.stub.ProjectsStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProjectsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### defaultApiClientHeaderProviderBuilder()
    
    
    public static ApiClientHeaderProvider.Builder defaultApiClientHeaderProviderBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider.Builder.html)` |   
  
### defaultCredentialsProviderBuilder()
    
    
    public static GoogleCredentialsProvider.Builder defaultCredentialsProviderBuilder()

Returns a builder for the default credentials for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.GoogleCredentialsProvider.Builder.html)` |   
  
### defaultExecutorProviderBuilder()
    
    
    public static InstantiatingExecutorProvider.Builder defaultExecutorProviderBuilder()

Returns a builder for the default ExecutorProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.Builder.html)` |   
  
### defaultGrpcTransportProviderBuilder()
    
    
    public static InstantiatingGrpcChannelProvider.Builder defaultGrpcTransportProviderBuilder()

Returns a builder for the default gRPC ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder.html)` |   
  
### defaultHttpJsonTransportProviderBuilder()
    
    
    public static InstantiatingHttpJsonChannelProvider.Builder defaultHttpJsonTransportProviderBuilder()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns a builder for the default REST ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.InstantiatingHttpJsonChannelProvider.Builder.html)` |   
  
### defaultTransportChannelProvider()
    
    
    public static TransportChannelProvider defaultTransportChannelProvider()

**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider.html)` |   
  
### getDefaultEndpoint()
    
    
    public static String getDefaultEndpoint()

Returns the default service endpoint.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDefaultServiceScopes()
    
    
    public static List<String> getDefaultServiceScopes()

Returns the default service scopes.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### newBuilder()
    
    
    public static ProjectsSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[ProjectsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static ProjectsSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProjectsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static ProjectsSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[ProjectsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsSettings.Builder)` |   
  
## Constructors 

### ProjectsSettings(ProjectsSettings.Builder settingsBuilder)
    
    
    protected ProjectsSettings(ProjectsSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[ProjectsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsSettings.Builder)`  
  
  
## Methods 

### createProjectOperationSettings()
    
    
    public OperationCallSettings<CreateProjectRequest,Project,CreateProjectMetadata> createProjectOperationSettings()

Returns the object with the settings used for calls to createProject.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.CreateProjectRequest),[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project),[CreateProjectMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.CreateProjectMetadata)>` |   
  
### createProjectSettings()
    
    
    public UnaryCallSettings<CreateProjectRequest,Operation> createProjectSettings()

Returns the object with the settings used for calls to createProject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.CreateProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteProjectOperationSettings()
    
    
    public OperationCallSettings<DeleteProjectRequest,Project,DeleteProjectMetadata> deleteProjectOperationSettings()

Returns the object with the settings used for calls to deleteProject.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.DeleteProjectRequest),[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project),[DeleteProjectMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.DeleteProjectMetadata)>` |   
  
### deleteProjectSettings()
    
    
    public UnaryCallSettings<DeleteProjectRequest,Operation> deleteProjectSettings()

Returns the object with the settings used for calls to deleteProject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.DeleteProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getIamPolicySettings()
    
    
    public UnaryCallSettings<GetIamPolicyRequest,Policy> getIamPolicySettings()

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getProjectSettings()
    
    
    public UnaryCallSettings<GetProjectRequest,Project> getProjectSettings()

Returns the object with the settings used for calls to getProject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.GetProjectRequest),[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project)>` |   
  
### listProjectsSettings()
    
    
    public PagedCallSettings<ListProjectsRequest,ListProjectsResponse,ProjectsClient.ListProjectsPagedResponse> listProjectsSettings()

Returns the object with the settings used for calls to listProjects.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListProjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ListProjectsRequest),[ListProjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ListProjectsResponse),[ListProjectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.ListProjectsPagedResponse)>` |   
  
### moveProjectOperationSettings()
    
    
    public OperationCallSettings<MoveProjectRequest,Project,MoveProjectMetadata> moveProjectOperationSettings()

Returns the object with the settings used for calls to moveProject.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[MoveProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.MoveProjectRequest),[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project),[MoveProjectMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.MoveProjectMetadata)>` |   
  
### moveProjectSettings()
    
    
    public UnaryCallSettings<MoveProjectRequest,Operation> moveProjectSettings()

Returns the object with the settings used for calls to moveProject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MoveProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.MoveProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### searchProjectsSettings()
    
    
    public PagedCallSettings<SearchProjectsRequest,SearchProjectsResponse,ProjectsClient.SearchProjectsPagedResponse> searchProjectsSettings()

Returns the object with the settings used for calls to searchProjects.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SearchProjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.SearchProjectsRequest),[SearchProjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.SearchProjectsResponse),[SearchProjectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.SearchProjectsPagedResponse)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder()
    
    
    public ProjectsSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[ProjectsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### undeleteProjectOperationSettings()
    
    
    public OperationCallSettings<UndeleteProjectRequest,Project,UndeleteProjectMetadata> undeleteProjectOperationSettings()

Returns the object with the settings used for calls to undeleteProject.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UndeleteProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.UndeleteProjectRequest),[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project),[UndeleteProjectMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.UndeleteProjectMetadata)>` |   
  
### undeleteProjectSettings()
    
    
    public UnaryCallSettings<UndeleteProjectRequest,Operation> undeleteProjectSettings()

Returns the object with the settings used for calls to undeleteProject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UndeleteProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.UndeleteProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateProjectOperationSettings()
    
    
    public OperationCallSettings<UpdateProjectRequest,Project,UpdateProjectMetadata> updateProjectOperationSettings()

Returns the object with the settings used for calls to updateProject.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.UpdateProjectRequest),[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project),[UpdateProjectMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.UpdateProjectMetadata)>` |   
  
### updateProjectSettings()
    
    
    public UnaryCallSettings<UpdateProjectRequest,Operation> updateProjectSettings()

Returns the object with the settings used for calls to updateProject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.UpdateProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
