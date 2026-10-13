---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient
title: Class RegionInstanceGroupManagersClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:41.341054+00:00
---

# Class RegionInstanceGroupManagersClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionInstanceGroupManagersClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionInstanceGroupManagersClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionInstanceGroupManagers API.

This client uses RegionInstanceGroupManagers version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManager response =
           regionInstanceGroupManagersClient.get(project, region, instanceGroupManager);
     }
     

Note: close() needs to be called on the RegionInstanceGroupManagersClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AbandonInstances |  Flags the specified instances to be immediately removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces thetargetSize of the managed instance group by the number of instances that you abandon. This operation is marked asDONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with thelistmanagedinstances method.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * abandonInstancesAsync(AbandonInstancesRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * abandonInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersAbandonInstancesRequest regionInstanceGroupManagersAbandonInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * abandonInstancesOperationCallable() 
  * abandonInstancesCallable() 

  
ApplyUpdatesToInstances |  Apply updates to selected instances the managed instance group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * applyUpdatesToInstancesAsync(ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * applyUpdatesToInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersApplyUpdatesRequest regionInstanceGroupManagersApplyUpdatesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * applyUpdatesToInstancesOperationCallable() 
  * applyUpdatesToInstancesCallable() 

  
CreateInstances |  Creates instances with per-instance configurations in this regional managed instance group. Instances are created using the current instance template. The create instances operation is marked DONE if the createInstances request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or actions with the listmanagedinstances method. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createInstancesAsync(CreateInstancesRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersCreateInstancesRequest regionInstanceGroupManagersCreateInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createInstancesOperationCallable() 
  * createInstancesCallable() 

  
Delete |  Deletes the specified managed instance group and all of the instances in that group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String instanceGroupManager) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
DeleteInstances |  Flags the specified instances in the managed instance group to be immediately deleted. The instances are also removed from any target pools of which they were a member. This method reduces thetargetSize of the managed instance group by the number of instances that you delete. The deleteInstances operation is marked DONE if the deleteInstances request is successful. The underlying actions take additional time. You must separately verify the status of thedeleting action with thelistmanagedinstances method.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteInstancesAsync(DeleteInstancesRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersDeleteInstancesRequest regionInstanceGroupManagersDeleteInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteInstancesOperationCallable() 
  * deleteInstancesCallable() 

  
DeletePerInstanceConfigs |  Deletes selected per-instance configurations for the managed instance group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePerInstanceConfigsAsync(DeletePerInstanceConfigsRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePerInstanceConfigsAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagerDeleteInstanceConfigReq regionInstanceGroupManagerDeleteInstanceConfigReqResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePerInstanceConfigsOperationCallable() 
  * deletePerInstanceConfigsCallable() 

  
Get |  Returns all of the details about the specified managed instance group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionInstanceGroupManagerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String instanceGroupManager) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with thelistmanagedinstances method.  A regional managed instance group can contain up to 2000 instances. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, InstanceGroupManager instanceGroupManagerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of managed instance groups that are contained within the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionInstanceGroupManagersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListErrors |  Lists all errors thrown by actions on instances for a given regional managed instance group. The filter andorderBy query parameters are not supported. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listErrors(ListErrorsRegionInstanceGroupManagersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listErrors(String project, String region, String instanceGroupManager) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listErrorsPagedCallable() 
  * listErrorsCallable() 

  
ListManagedInstances |  Lists the instances in the managed instance group and instances that are scheduled to be created. The list includes any current actions that the group has scheduled for its instances. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listManagedInstances(ListManagedInstancesRegionInstanceGroupManagersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listManagedInstances(String project, String region, String instanceGroupManager) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listManagedInstancesPagedCallable() 
  * listManagedInstancesCallable() 

  
ListPerInstanceConfigs |  Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPerInstanceConfigs(ListPerInstanceConfigsRegionInstanceGroupManagersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPerInstanceConfigs(String project, String region, String instanceGroupManager) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPerInstanceConfigsPagedCallable() 
  * listPerInstanceConfigsCallable() 

  
Patch |  Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with the listmanagedinstances method. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.  If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String instanceGroupManager, InstanceGroupManager instanceGroupManagerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
PatchPerInstanceConfigs |  Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchPerInstanceConfigsAsync(PatchPerInstanceConfigsRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchPerInstanceConfigsAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagerPatchInstanceConfigReq regionInstanceGroupManagerPatchInstanceConfigReqResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchPerInstanceConfigsOperationCallable() 
  * patchPerInstanceConfigsCallable() 

  
RecreateInstances |  Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking itscurrentAction field; for more information, see Checking the status of managed instances.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * recreateInstancesAsync(RecreateInstancesRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * recreateInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersRecreateRequest regionInstanceGroupManagersRecreateRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * recreateInstancesOperationCallable() 
  * recreateInstancesCallable() 

  
Resize |  Changes the intended size of the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes one or more instances.  The resize operation is marked DONE if theresize request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or deleting actions with thelistmanagedinstances method.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resizeAsync(ResizeRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * resizeAsync(String project, String region, String instanceGroupManager, int size) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resizeOperationCallable() 
  * resizeCallable() 

  
ResumeInstances |  Flags the specified instances in the managed instance group to be resumed. This method increases thetargetSize and decreases the targetSuspendedSize of the managed instance group by the number of instances that you resume. The resumeInstances operation is marked DONE if the resumeInstances request is successful. The underlying actions take additional time. You must separately verify the status of theRESUMING action with thelistmanagedinstances method.  In this request, you can only specify instances that are suspended. For example, if an instance was previously suspended using the suspendInstances method, it can be resumed using the resumeInstances method.  If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are resumed.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resumeInstancesAsync(ResumeInstancesRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * resumeInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersResumeInstancesRequest regionInstanceGroupManagersResumeInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resumeInstancesOperationCallable() 
  * resumeInstancesCallable() 

  
SetInstanceTemplate |  Sets the instance template to use when creating new instances or recreating instances in this group. Existing instances are not affected. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setInstanceTemplateAsync(SetInstanceTemplateRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setInstanceTemplateAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersSetTemplateRequest regionInstanceGroupManagersSetTemplateRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setInstanceTemplateOperationCallable() 
  * setInstanceTemplateCallable() 

  
SetTargetPools |  Modifies the target pools to which all new instances in this group are assigned. Existing instances in the group are not affected. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setTargetPoolsAsync(SetTargetPoolsRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setTargetPoolsAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersSetTargetPoolsRequest regionInstanceGroupManagersSetTargetPoolsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setTargetPoolsOperationCallable() 
  * setTargetPoolsCallable() 

  
StartInstances |  Flags the specified instances in the managed instance group to be started. This method increases thetargetSize and decreases the targetStoppedSize of the managed instance group by the number of instances that you start. The startInstances operation is marked DONE if the startInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTARTING action with thelistmanagedinstances method.  In this request, you can only specify instances that are stopped. For example, if an instance was previously stopped using the stopInstances method, it can be started using the startInstances method.  If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are started.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startInstancesAsync(StartInstancesRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * startInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersStartInstancesRequest regionInstanceGroupManagersStartInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startInstancesOperationCallable() 
  * startInstancesCallable() 

  
StopInstances |  Flags the specified instances in the managed instance group to be immediately stopped. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetStoppedSize of the managed instance group by the number of instances that you stop. The stopInstances operation is marked DONE if the stopInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTOPPING action with thelistmanagedinstances method.  If the standbyPolicy.initialDelaySec field is set, the group delays stopping the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is stopped.  Stopped instances can be started using the startInstances method.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopInstancesAsync(StopInstancesRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * stopInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersStopInstancesRequest regionInstanceGroupManagersStopInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopInstancesOperationCallable() 
  * stopInstancesCallable() 

  
SuspendInstances |  Flags the specified instances in the managed instance group to be immediately suspended. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetSuspendedSize of the managed instance group by the number of instances that you suspend. The suspendInstances operation is marked DONE if the suspendInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSUSPENDING action with thelistmanagedinstances method.  If the standbyPolicy.initialDelaySec field is set, the group delays suspension of the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is suspended.  Suspended instances can be resumed using the resumeInstances method.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * suspendInstancesAsync(SuspendInstancesRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * suspendInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersSuspendInstancesRequest regionInstanceGroupManagersSuspendInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * suspendInstancesOperationCallable() 
  * suspendInstancesCallable() 

  
UpdatePerInstanceConfigs |  Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePerInstanceConfigsAsync(UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updatePerInstanceConfigsAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagerUpdateInstanceConfigReq regionInstanceGroupManagerUpdateInstanceConfigReqResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePerInstanceConfigsOperationCallable() 
  * updatePerInstanceConfigsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionInstanceGroupManagersSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionInstanceGroupManagersSettings regionInstanceGroupManagersSettings =
         RegionInstanceGroupManagersSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create(regionInstanceGroupManagersSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionInstanceGroupManagersSettings regionInstanceGroupManagersSettings =
         RegionInstanceGroupManagersSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create(regionInstanceGroupManagersSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionInstanceGroupManagersClient

## Static Methods 

### create()
    
    
    public static final RegionInstanceGroupManagersClient create()

Constructs an instance of RegionInstanceGroupManagersClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionInstanceGroupManagersSettings settings)
    
    
    public static final RegionInstanceGroupManagersClient create(RegionInstanceGroupManagersSettings settings)

Constructs an instance of RegionInstanceGroupManagersClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionInstanceGroupManagersSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionInstanceGroupManagersStub stub)
    
    
    public static final RegionInstanceGroupManagersClient create(RegionInstanceGroupManagersStub stub)

Constructs an instance of RegionInstanceGroupManagersClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionInstanceGroupManagersSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionInstanceGroupManagersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstanceGroupManagersStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient)` |   
  
## Constructors 

### RegionInstanceGroupManagersClient(RegionInstanceGroupManagersSettings settings)
    
    
    protected RegionInstanceGroupManagersClient(RegionInstanceGroupManagersSettings settings)

Constructs an instance of RegionInstanceGroupManagersClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionInstanceGroupManagersSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersSettings)`  
  
  
### RegionInstanceGroupManagersClient(RegionInstanceGroupManagersStub stub)
    
    
    protected RegionInstanceGroupManagersClient(RegionInstanceGroupManagersStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionInstanceGroupManagersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstanceGroupManagersStub)`  
  
  
## Methods 

### abandonInstancesAsync(AbandonInstancesRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> abandonInstancesAsync(AbandonInstancesRegionInstanceGroupManagerRequest request)

Flags the specified instances to be immediately removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces thetargetSize of the managed instance group by the number of instances that you abandon. This operation is marked asDONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       AbandonInstancesRegionInstanceGroupManagerRequest request =
           AbandonInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersAbandonInstancesRequestResource(
                   RegionInstanceGroupManagersAbandonInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupManagersClient.abandonInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AbandonInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AbandonInstancesRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### abandonInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersAbandonInstancesRequest regionInstanceGroupManagersAbandonInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> abandonInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersAbandonInstancesRequest regionInstanceGroupManagersAbandonInstancesRequestResource)

Flags the specified instances to be immediately removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces thetargetSize of the managed instance group by the number of instances that you abandon. This operation is marked asDONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagersAbandonInstancesRequest
           regionInstanceGroupManagersAbandonInstancesRequestResource =
               RegionInstanceGroupManagersAbandonInstancesRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .abandonInstancesAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagersAbandonInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the managed instance group.  
`regionInstanceGroupManagersAbandonInstancesRequestResource` | `[RegionInstanceGroupManagersAbandonInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersAbandonInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### abandonInstancesCallable()
    
    
    public final UnaryCallable<AbandonInstancesRegionInstanceGroupManagerRequest,Operation> abandonInstancesCallable()

Flags the specified instances to be immediately removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces thetargetSize of the managed instance group by the number of instances that you abandon. This operation is marked asDONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       AbandonInstancesRegionInstanceGroupManagerRequest request =
           AbandonInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersAbandonInstancesRequestResource(
                   RegionInstanceGroupManagersAbandonInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.abandonInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AbandonInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AbandonInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### abandonInstancesOperationCallable()
    
    
    public final OperationCallable<AbandonInstancesRegionInstanceGroupManagerRequest,Operation,Operation> abandonInstancesOperationCallable()

Flags the specified instances to be immediately removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces thetargetSize of the managed instance group by the number of instances that you abandon. This operation is marked asDONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       AbandonInstancesRegionInstanceGroupManagerRequest request =
           AbandonInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersAbandonInstancesRequestResource(
                   RegionInstanceGroupManagersAbandonInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient.abandonInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AbandonInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AbandonInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### applyUpdatesToInstancesAsync(ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> applyUpdatesToInstancesAsync(ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest request)

Apply updates to selected instances the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest request =
           ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersApplyUpdatesRequestResource(
                   RegionInstanceGroupManagersApplyUpdatesRequest.newBuilder().build())
               .build();
       Operation response =
           regionInstanceGroupManagersClient.applyUpdatesToInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### applyUpdatesToInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersApplyUpdatesRequest regionInstanceGroupManagersApplyUpdatesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> applyUpdatesToInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersApplyUpdatesRequest regionInstanceGroupManagersApplyUpdatesRequestResource)

Apply updates to selected instances the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagersApplyUpdatesRequest
           regionInstanceGroupManagersApplyUpdatesRequestResource =
               RegionInstanceGroupManagersApplyUpdatesRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .applyUpdatesToInstancesAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagersApplyUpdatesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request, should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group, should conform to RFC1035.  
`regionInstanceGroupManagersApplyUpdatesRequestResource` | `[RegionInstanceGroupManagersApplyUpdatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersApplyUpdatesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### applyUpdatesToInstancesCallable()
    
    
    public final UnaryCallable<ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest,Operation> applyUpdatesToInstancesCallable()

Apply updates to selected instances the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest request =
           ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersApplyUpdatesRequestResource(
                   RegionInstanceGroupManagersApplyUpdatesRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.applyUpdatesToInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### applyUpdatesToInstancesOperationCallable()
    
    
    public final OperationCallable<ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest,Operation,Operation> applyUpdatesToInstancesOperationCallable()

Apply updates to selected instances the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest request =
           ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersApplyUpdatesRequestResource(
                   RegionInstanceGroupManagersApplyUpdatesRequest.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient
               .applyUpdatesToInstancesOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ApplyUpdatesToInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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

### createInstancesAsync(CreateInstancesRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> createInstancesAsync(CreateInstancesRegionInstanceGroupManagerRequest request)

Creates instances with per-instance configurations in this regional managed instance group. Instances are created using the current instance template. The create instances operation is marked DONE if the createInstances request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or actions with the listmanagedinstances method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       CreateInstancesRegionInstanceGroupManagerRequest request =
           CreateInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersCreateInstancesRequestResource(
                   RegionInstanceGroupManagersCreateInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupManagersClient.createInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CreateInstancesRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### createInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersCreateInstancesRequest regionInstanceGroupManagersCreateInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> createInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersCreateInstancesRequest regionInstanceGroupManagersCreateInstancesRequestResource)

Creates instances with per-instance configurations in this regional managed instance group. Instances are created using the current instance template. The create instances operation is marked DONE if the createInstances request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or actions with the listmanagedinstances method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagersCreateInstancesRequest
           regionInstanceGroupManagersCreateInstancesRequestResource =
               RegionInstanceGroupManagersCreateInstancesRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .createInstancesAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagersCreateInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of theregion where the managed instance group is located. It should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. It should conform to RFC1035.  
`regionInstanceGroupManagersCreateInstancesRequestResource` | `[RegionInstanceGroupManagersCreateInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersCreateInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### createInstancesCallable()
    
    
    public final UnaryCallable<CreateInstancesRegionInstanceGroupManagerRequest,Operation> createInstancesCallable()

Creates instances with per-instance configurations in this regional managed instance group. Instances are created using the current instance template. The create instances operation is marked DONE if the createInstances request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or actions with the listmanagedinstances method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       CreateInstancesRegionInstanceGroupManagerRequest request =
           CreateInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersCreateInstancesRequestResource(
                   RegionInstanceGroupManagersCreateInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.createInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CreateInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### createInstancesOperationCallable()
    
    
    public final OperationCallable<CreateInstancesRegionInstanceGroupManagerRequest,Operation,Operation> createInstancesOperationCallable()

Creates instances with per-instance configurations in this regional managed instance group. Instances are created using the current instance template. The create instances operation is marked DONE if the createInstances request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or actions with the listmanagedinstances method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       CreateInstancesRegionInstanceGroupManagerRequest request =
           CreateInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersCreateInstancesRequestResource(
                   RegionInstanceGroupManagersCreateInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient.createInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CreateInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(DeleteRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionInstanceGroupManagerRequest request)

Deletes the specified managed instance group and all of the instances in that group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       DeleteRegionInstanceGroupManagerRequest request =
           DeleteRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupManagersClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String instanceGroupManager)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String instanceGroupManager)

Deletes the specified managed instance group and all of the instances in that group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       Operation response =
           regionInstanceGroupManagersClient
               .deleteAsync(project, region, instanceGroupManager)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the managed instance group to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionInstanceGroupManagerRequest,Operation> deleteCallable()

Deletes the specified managed instance group and all of the instances in that group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       DeleteRegionInstanceGroupManagerRequest request =
           DeleteRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteInstancesAsync(DeleteInstancesRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteInstancesAsync(DeleteInstancesRegionInstanceGroupManagerRequest request)

Flags the specified instances in the managed instance group to be immediately deleted. The instances are also removed from any target pools of which they were a member. This method reduces thetargetSize of the managed instance group by the number of instances that you delete. The deleteInstances operation is marked DONE if the deleteInstances request is successful. The underlying actions take additional time. You must separately verify the status of thedeleting action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       DeleteInstancesRegionInstanceGroupManagerRequest request =
           DeleteInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersDeleteInstancesRequestResource(
                   RegionInstanceGroupManagersDeleteInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupManagersClient.deleteInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstancesRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersDeleteInstancesRequest regionInstanceGroupManagersDeleteInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> deleteInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersDeleteInstancesRequest regionInstanceGroupManagersDeleteInstancesRequestResource)

Flags the specified instances in the managed instance group to be immediately deleted. The instances are also removed from any target pools of which they were a member. This method reduces thetargetSize of the managed instance group by the number of instances that you delete. The deleteInstances operation is marked DONE if the deleteInstances request is successful. The underlying actions take additional time. You must separately verify the status of thedeleting action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagersDeleteInstancesRequest
           regionInstanceGroupManagersDeleteInstancesRequestResource =
               RegionInstanceGroupManagersDeleteInstancesRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .deleteInstancesAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagersDeleteInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the managed instance group.  
`regionInstanceGroupManagersDeleteInstancesRequestResource` | `[RegionInstanceGroupManagersDeleteInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersDeleteInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteInstancesCallable()
    
    
    public final UnaryCallable<DeleteInstancesRegionInstanceGroupManagerRequest,Operation> deleteInstancesCallable()

Flags the specified instances in the managed instance group to be immediately deleted. The instances are also removed from any target pools of which they were a member. This method reduces thetargetSize of the managed instance group by the number of instances that you delete. The deleteInstances operation is marked DONE if the deleteInstances request is successful. The underlying actions take additional time. You must separately verify the status of thedeleting action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       DeleteInstancesRegionInstanceGroupManagerRequest request =
           DeleteInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersDeleteInstancesRequestResource(
                   RegionInstanceGroupManagersDeleteInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.deleteInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteInstancesOperationCallable()
    
    
    public final OperationCallable<DeleteInstancesRegionInstanceGroupManagerRequest,Operation,Operation> deleteInstancesOperationCallable()

Flags the specified instances in the managed instance group to be immediately deleted. The instances are also removed from any target pools of which they were a member. This method reduces thetargetSize of the managed instance group by the number of instances that you delete. The deleteInstances operation is marked DONE if the deleteInstances request is successful. The underlying actions take additional time. You must separately verify the status of thedeleting action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       DeleteInstancesRegionInstanceGroupManagerRequest request =
           DeleteInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersDeleteInstancesRequestResource(
                   RegionInstanceGroupManagersDeleteInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient.deleteInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionInstanceGroupManagerRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified managed instance group and all of the instances in that group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       DeleteRegionInstanceGroupManagerRequest request =
           DeleteRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deletePerInstanceConfigsAsync(DeletePerInstanceConfigsRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> deletePerInstanceConfigsAsync(DeletePerInstanceConfigsRegionInstanceGroupManagerRequest request)

Deletes selected per-instance configurations for the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       DeletePerInstanceConfigsRegionInstanceGroupManagerRequest request =
           DeletePerInstanceConfigsRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagerDeleteInstanceConfigReqResource(
                   RegionInstanceGroupManagerDeleteInstanceConfigReq.newBuilder().build())
               .build();
       Operation response =
           regionInstanceGroupManagersClient.deletePerInstanceConfigsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePerInstanceConfigsRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeletePerInstanceConfigsRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deletePerInstanceConfigsAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagerDeleteInstanceConfigReq regionInstanceGroupManagerDeleteInstanceConfigReqResource)
    
    
    public final OperationFuture<Operation,Operation> deletePerInstanceConfigsAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagerDeleteInstanceConfigReq regionInstanceGroupManagerDeleteInstanceConfigReqResource)

Deletes selected per-instance configurations for the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagerDeleteInstanceConfigReq
           regionInstanceGroupManagerDeleteInstanceConfigReqResource =
               RegionInstanceGroupManagerDeleteInstanceConfigReq.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .deletePerInstanceConfigsAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagerDeleteInstanceConfigReqResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request, should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. It should conform to RFC1035.  
`regionInstanceGroupManagerDeleteInstanceConfigReqResource` | `[RegionInstanceGroupManagerDeleteInstanceConfigReq](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerDeleteInstanceConfigReq)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deletePerInstanceConfigsCallable()
    
    
    public final UnaryCallable<DeletePerInstanceConfigsRegionInstanceGroupManagerRequest,Operation> deletePerInstanceConfigsCallable()

Deletes selected per-instance configurations for the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       DeletePerInstanceConfigsRegionInstanceGroupManagerRequest request =
           DeletePerInstanceConfigsRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagerDeleteInstanceConfigReqResource(
                   RegionInstanceGroupManagerDeleteInstanceConfigReq.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.deletePerInstanceConfigsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePerInstanceConfigsRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeletePerInstanceConfigsRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deletePerInstanceConfigsOperationCallable()
    
    
    public final OperationCallable<DeletePerInstanceConfigsRegionInstanceGroupManagerRequest,Operation,Operation> deletePerInstanceConfigsOperationCallable()

Deletes selected per-instance configurations for the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       DeletePerInstanceConfigsRegionInstanceGroupManagerRequest request =
           DeletePerInstanceConfigsRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagerDeleteInstanceConfigReqResource(
                   RegionInstanceGroupManagerDeleteInstanceConfigReq.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient
               .deletePerInstanceConfigsOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePerInstanceConfigsRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeletePerInstanceConfigsRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionInstanceGroupManagerRequest request)
    
    
    public final InstanceGroupManager get(GetRegionInstanceGroupManagerRequest request)

Returns all of the details about the specified managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       GetRegionInstanceGroupManagerRequest request =
           GetRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       InstanceGroupManager response = regionInstanceGroupManagersClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManager)` |   
  
### get(String project, String region, String instanceGroupManager)
    
    
    public final InstanceGroupManager get(String project, String region, String instanceGroupManager)

Returns all of the details about the specified managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManager response =
           regionInstanceGroupManagersClient.get(project, region, instanceGroupManager);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the managed instance group to return.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManager)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionInstanceGroupManagerRequest,InstanceGroupManager> getCallable()

Returns all of the details about the specified managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       GetRegionInstanceGroupManagerRequest request =
           GetRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<InstanceGroupManager> future =
           regionInstanceGroupManagersClient.getCallable().futureCall(request);
       // Do something.
       InstanceGroupManager response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionInstanceGroupManagerRequest),[InstanceGroupManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManager)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionInstanceGroupManagersSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionInstanceGroupManagersSettings` |   
  
### getStub()
    
    
    public RegionInstanceGroupManagersStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstanceGroupManagersStub)` |   
  
### insertAsync(InsertRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionInstanceGroupManagerRequest request)

Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with thelistmanagedinstances method.

A regional managed instance group can contain up to 2000 instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       InsertRegionInstanceGroupManagerRequest request =
           InsertRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManagerResource(InstanceGroupManager.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupManagersClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, InstanceGroupManager instanceGroupManagerResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, InstanceGroupManager instanceGroupManagerResource)

Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with thelistmanagedinstances method.

A regional managed instance group can contain up to 2000 instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       InstanceGroupManager instanceGroupManagerResource = InstanceGroupManager.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .insertAsync(project, region, instanceGroupManagerResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManagerResource` | `[InstanceGroupManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManager)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionInstanceGroupManagerRequest,Operation> insertCallable()

Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with thelistmanagedinstances method.

A regional managed instance group can contain up to 2000 instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       InsertRegionInstanceGroupManagerRequest request =
           InsertRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManagerResource(InstanceGroupManager.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionInstanceGroupManagerRequest,Operation,Operation> insertOperationCallable()

Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with thelistmanagedinstances method.

A regional managed instance group can contain up to 2000 instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       InsertRegionInstanceGroupManagerRequest request =
           InsertRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManagerResource(InstanceGroupManager.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionInstanceGroupManagersRequest request)
    
    
    public final RegionInstanceGroupManagersClient.ListPagedResponse list(ListRegionInstanceGroupManagersRequest request)

Retrieves the list of managed instance groups that are contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ListRegionInstanceGroupManagersRequest request =
           ListRegionInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (InstanceGroupManager element :
           regionInstanceGroupManagersClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstanceGroupManagersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagersClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionInstanceGroupManagersClient.ListPagedResponse list(String project, String region)

Retrieves the list of managed instance groups that are contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (InstanceGroupManager element :
           regionInstanceGroupManagersClient.list(project, region).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagersClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionInstanceGroupManagersRequest,RegionInstanceGroupManagerList> listCallable()

Retrieves the list of managed instance groups that are contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ListRegionInstanceGroupManagersRequest request =
           ListRegionInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         RegionInstanceGroupManagerList response =
             regionInstanceGroupManagersClient.listCallable().call(request);
         for (InstanceGroupManager element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstanceGroupManagersRequest),[RegionInstanceGroupManagerList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerList)>` |   
  
### listErrors(ListErrorsRegionInstanceGroupManagersRequest request)
    
    
    public final RegionInstanceGroupManagersClient.ListErrorsPagedResponse listErrors(ListErrorsRegionInstanceGroupManagersRequest request)

Lists all errors thrown by actions on instances for a given regional managed instance group. The filter andorderBy query parameters are not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ListErrorsRegionInstanceGroupManagersRequest request =
           ListErrorsRegionInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (InstanceManagedByIgmError element :
           regionInstanceGroupManagersClient.listErrors(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListErrorsRegionInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListErrorsRegionInstanceGroupManagersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagersClient.ListErrorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient.ListErrorsPagedResponse)` |   
  
### listErrors(String project, String region, String instanceGroupManager)
    
    
    public final RegionInstanceGroupManagersClient.ListErrorsPagedResponse listErrors(String project, String region, String instanceGroupManager)

Lists all errors thrown by actions on instances for a given regional managed instance group. The filter andorderBy query parameters are not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       for (InstanceManagedByIgmError element :
           regionInstanceGroupManagersClient
               .listErrors(project, region, instanceGroupManager)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request. This should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. It must be a string that meets the requirements in RFC1035, or an unsigned long integer: must match regexp pattern: (?:[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?)|1-9{0,19}.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagersClient.ListErrorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient.ListErrorsPagedResponse)` |   
  
### listErrorsCallable()
    
    
    public final UnaryCallable<ListErrorsRegionInstanceGroupManagersRequest,RegionInstanceGroupManagersListErrorsResponse> listErrorsCallable()

Lists all errors thrown by actions on instances for a given regional managed instance group. The filter andorderBy query parameters are not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ListErrorsRegionInstanceGroupManagersRequest request =
           ListErrorsRegionInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         RegionInstanceGroupManagersListErrorsResponse response =
             regionInstanceGroupManagersClient.listErrorsCallable().call(request);
         for (InstanceManagedByIgmError element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListErrorsRegionInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListErrorsRegionInstanceGroupManagersRequest),[RegionInstanceGroupManagersListErrorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersListErrorsResponse)>` |   
  
### listErrorsPagedCallable()
    
    
    public final UnaryCallable<ListErrorsRegionInstanceGroupManagersRequest,RegionInstanceGroupManagersClient.ListErrorsPagedResponse> listErrorsPagedCallable()

Lists all errors thrown by actions on instances for a given regional managed instance group. The filter andorderBy query parameters are not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ListErrorsRegionInstanceGroupManagersRequest request =
           ListErrorsRegionInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<InstanceManagedByIgmError> future =
           regionInstanceGroupManagersClient.listErrorsPagedCallable().futureCall(request);
       // Do something.
       for (InstanceManagedByIgmError element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListErrorsRegionInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListErrorsRegionInstanceGroupManagersRequest),[ListErrorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient.ListErrorsPagedResponse)>` |   
  
### listManagedInstances(ListManagedInstancesRegionInstanceGroupManagersRequest request)
    
    
    public final RegionInstanceGroupManagersClient.ListManagedInstancesPagedResponse listManagedInstances(ListManagedInstancesRegionInstanceGroupManagersRequest request)

Lists the instances in the managed instance group and instances that are scheduled to be created. The list includes any current actions that the group has scheduled for its instances. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ListManagedInstancesRegionInstanceGroupManagersRequest request =
           ListManagedInstancesRegionInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (ManagedInstance element :
           regionInstanceGroupManagersClient.listManagedInstances(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListManagedInstancesRegionInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListManagedInstancesRegionInstanceGroupManagersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagersClient.ListManagedInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient.ListManagedInstancesPagedResponse)` |   
  
### listManagedInstances(String project, String region, String instanceGroupManager)
    
    
    public final RegionInstanceGroupManagersClient.ListManagedInstancesPagedResponse listManagedInstances(String project, String region, String instanceGroupManager)

Lists the instances in the managed instance group and instances that are scheduled to be created. The list includes any current actions that the group has scheduled for its instances. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       for (ManagedInstance element :
           regionInstanceGroupManagersClient
               .listManagedInstances(project, region, instanceGroupManager)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagersClient.ListManagedInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient.ListManagedInstancesPagedResponse)` |   
  
### listManagedInstancesCallable()
    
    
    public final UnaryCallable<ListManagedInstancesRegionInstanceGroupManagersRequest,RegionInstanceGroupManagersListInstancesResponse> listManagedInstancesCallable()

Lists the instances in the managed instance group and instances that are scheduled to be created. The list includes any current actions that the group has scheduled for its instances. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ListManagedInstancesRegionInstanceGroupManagersRequest request =
           ListManagedInstancesRegionInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         RegionInstanceGroupManagersListInstancesResponse response =
             regionInstanceGroupManagersClient.listManagedInstancesCallable().call(request);
         for (ManagedInstance element : response.getManagedInstancesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListManagedInstancesRegionInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListManagedInstancesRegionInstanceGroupManagersRequest),[RegionInstanceGroupManagersListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersListInstancesResponse)>` |   
  
### listManagedInstancesPagedCallable()
    
    
    public final UnaryCallable<ListManagedInstancesRegionInstanceGroupManagersRequest,RegionInstanceGroupManagersClient.ListManagedInstancesPagedResponse> listManagedInstancesPagedCallable()

Lists the instances in the managed instance group and instances that are scheduled to be created. The list includes any current actions that the group has scheduled for its instances. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ListManagedInstancesRegionInstanceGroupManagersRequest request =
           ListManagedInstancesRegionInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<ManagedInstance> future =
           regionInstanceGroupManagersClient.listManagedInstancesPagedCallable().futureCall(request);
       // Do something.
       for (ManagedInstance element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListManagedInstancesRegionInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListManagedInstancesRegionInstanceGroupManagersRequest),[ListManagedInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient.ListManagedInstancesPagedResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionInstanceGroupManagersRequest,RegionInstanceGroupManagersClient.ListPagedResponse> listPagedCallable()

Retrieves the list of managed instance groups that are contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ListRegionInstanceGroupManagersRequest request =
           ListRegionInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<InstanceGroupManager> future =
           regionInstanceGroupManagersClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InstanceGroupManager element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstanceGroupManagersRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient.ListPagedResponse)>` |   
  
### listPerInstanceConfigs(ListPerInstanceConfigsRegionInstanceGroupManagersRequest request)
    
    
    public final RegionInstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse listPerInstanceConfigs(ListPerInstanceConfigsRegionInstanceGroupManagersRequest request)

Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ListPerInstanceConfigsRegionInstanceGroupManagersRequest request =
           ListPerInstanceConfigsRegionInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (PerInstanceConfig element :
           regionInstanceGroupManagersClient.listPerInstanceConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPerInstanceConfigsRegionInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPerInstanceConfigsRegionInstanceGroupManagersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse)` |   
  
### listPerInstanceConfigs(String project, String region, String instanceGroupManager)
    
    
    public final RegionInstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse listPerInstanceConfigs(String project, String region, String instanceGroupManager)

Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       for (PerInstanceConfig element :
           regionInstanceGroupManagersClient
               .listPerInstanceConfigs(project, region, instanceGroupManager)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request, should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. It should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse)` |   
  
### listPerInstanceConfigsCallable()
    
    
    public final UnaryCallable<ListPerInstanceConfigsRegionInstanceGroupManagersRequest,RegionInstanceGroupManagersListInstanceConfigsResp> listPerInstanceConfigsCallable()

Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ListPerInstanceConfigsRegionInstanceGroupManagersRequest request =
           ListPerInstanceConfigsRegionInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         RegionInstanceGroupManagersListInstanceConfigsResp response =
             regionInstanceGroupManagersClient.listPerInstanceConfigsCallable().call(request);
         for (PerInstanceConfig element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPerInstanceConfigsRegionInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPerInstanceConfigsRegionInstanceGroupManagersRequest),[RegionInstanceGroupManagersListInstanceConfigsResp](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersListInstanceConfigsResp)>` |   
  
### listPerInstanceConfigsPagedCallable()
    
    
    public final UnaryCallable<ListPerInstanceConfigsRegionInstanceGroupManagersRequest,RegionInstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse> listPerInstanceConfigsPagedCallable()

Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ListPerInstanceConfigsRegionInstanceGroupManagersRequest request =
           ListPerInstanceConfigsRegionInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<PerInstanceConfig> future =
           regionInstanceGroupManagersClient
               .listPerInstanceConfigsPagedCallable()
               .futureCall(request);
       // Do something.
       for (PerInstanceConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPerInstanceConfigsRegionInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPerInstanceConfigsRegionInstanceGroupManagersRequest),[ListPerInstanceConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse)>` |   
  
### patchAsync(PatchRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchRegionInstanceGroupManagerRequest request)

Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with the listmanagedinstances method. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       PatchRegionInstanceGroupManagerRequest request =
           PatchRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagerResource(InstanceGroupManager.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupManagersClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String instanceGroupManager, InstanceGroupManager instanceGroupManagerResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String instanceGroupManager, InstanceGroupManager instanceGroupManagerResource)

Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with the listmanagedinstances method. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManager instanceGroupManagerResource = InstanceGroupManager.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .patchAsync(project, region, instanceGroupManager, instanceGroupManagerResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the instance group manager.  
`instanceGroupManagerResource` | `[InstanceGroupManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManager)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchRegionInstanceGroupManagerRequest,Operation> patchCallable()

Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with the listmanagedinstances method. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       PatchRegionInstanceGroupManagerRequest request =
           PatchRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagerResource(InstanceGroupManager.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchRegionInstanceGroupManagerRequest,Operation,Operation> patchOperationCallable()

Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with the listmanagedinstances method. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       PatchRegionInstanceGroupManagerRequest request =
           PatchRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagerResource(InstanceGroupManager.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchPerInstanceConfigsAsync(PatchPerInstanceConfigsRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchPerInstanceConfigsAsync(PatchPerInstanceConfigsRegionInstanceGroupManagerRequest request)

Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       PatchPerInstanceConfigsRegionInstanceGroupManagerRequest request =
           PatchPerInstanceConfigsRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagerPatchInstanceConfigReqResource(
                   RegionInstanceGroupManagerPatchInstanceConfigReq.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response =
           regionInstanceGroupManagersClient.patchPerInstanceConfigsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchPerInstanceConfigsRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPerInstanceConfigsRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchPerInstanceConfigsAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagerPatchInstanceConfigReq regionInstanceGroupManagerPatchInstanceConfigReqResource)
    
    
    public final OperationFuture<Operation,Operation> patchPerInstanceConfigsAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagerPatchInstanceConfigReq regionInstanceGroupManagerPatchInstanceConfigReqResource)

Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagerPatchInstanceConfigReq
           regionInstanceGroupManagerPatchInstanceConfigReqResource =
               RegionInstanceGroupManagerPatchInstanceConfigReq.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .patchPerInstanceConfigsAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagerPatchInstanceConfigReqResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request, should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. It should conform to RFC1035.  
`regionInstanceGroupManagerPatchInstanceConfigReqResource` | `[RegionInstanceGroupManagerPatchInstanceConfigReq](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerPatchInstanceConfigReq)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchPerInstanceConfigsCallable()
    
    
    public final UnaryCallable<PatchPerInstanceConfigsRegionInstanceGroupManagerRequest,Operation> patchPerInstanceConfigsCallable()

Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       PatchPerInstanceConfigsRegionInstanceGroupManagerRequest request =
           PatchPerInstanceConfigsRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagerPatchInstanceConfigReqResource(
                   RegionInstanceGroupManagerPatchInstanceConfigReq.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.patchPerInstanceConfigsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchPerInstanceConfigsRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPerInstanceConfigsRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchPerInstanceConfigsOperationCallable()
    
    
    public final OperationCallable<PatchPerInstanceConfigsRegionInstanceGroupManagerRequest,Operation,Operation> patchPerInstanceConfigsOperationCallable()

Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       PatchPerInstanceConfigsRegionInstanceGroupManagerRequest request =
           PatchPerInstanceConfigsRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagerPatchInstanceConfigReqResource(
                   RegionInstanceGroupManagerPatchInstanceConfigReq.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient
               .patchPerInstanceConfigsOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchPerInstanceConfigsRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPerInstanceConfigsRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### recreateInstancesAsync(RecreateInstancesRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> recreateInstancesAsync(RecreateInstancesRegionInstanceGroupManagerRequest request)

Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking itscurrentAction field; for more information, see Checking the status of managed instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       RecreateInstancesRegionInstanceGroupManagerRequest request =
           RecreateInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersRecreateRequestResource(
                   RegionInstanceGroupManagersRecreateRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupManagersClient.recreateInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RecreateInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RecreateInstancesRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### recreateInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersRecreateRequest regionInstanceGroupManagersRecreateRequestResource)
    
    
    public final OperationFuture<Operation,Operation> recreateInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersRecreateRequest regionInstanceGroupManagersRecreateRequestResource)

Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking itscurrentAction field; for more information, see Checking the status of managed instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagersRecreateRequest
           regionInstanceGroupManagersRecreateRequestResource =
               RegionInstanceGroupManagersRecreateRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .recreateInstancesAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagersRecreateRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the managed instance group.  
`regionInstanceGroupManagersRecreateRequestResource` | `[RegionInstanceGroupManagersRecreateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersRecreateRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### recreateInstancesCallable()
    
    
    public final UnaryCallable<RecreateInstancesRegionInstanceGroupManagerRequest,Operation> recreateInstancesCallable()

Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking itscurrentAction field; for more information, see Checking the status of managed instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       RecreateInstancesRegionInstanceGroupManagerRequest request =
           RecreateInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersRecreateRequestResource(
                   RegionInstanceGroupManagersRecreateRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.recreateInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RecreateInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RecreateInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### recreateInstancesOperationCallable()
    
    
    public final OperationCallable<RecreateInstancesRegionInstanceGroupManagerRequest,Operation,Operation> recreateInstancesOperationCallable()

Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking itscurrentAction field; for more information, see Checking the status of managed instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       RecreateInstancesRegionInstanceGroupManagerRequest request =
           RecreateInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersRecreateRequestResource(
                   RegionInstanceGroupManagersRecreateRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient
               .recreateInstancesOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RecreateInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RecreateInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeAsync(ResizeRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> resizeAsync(ResizeRegionInstanceGroupManagerRequest request)

Changes the intended size of the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes one or more instances.

The resize operation is marked DONE if theresize request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or deleting actions with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ResizeRegionInstanceGroupManagerRequest request =
           ResizeRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSize(3530753)
               .build();
       Operation response = regionInstanceGroupManagersClient.resizeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResizeRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeAsync(String project, String region, String instanceGroupManager, int size)
    
    
    public final OperationFuture<Operation,Operation> resizeAsync(String project, String region, String instanceGroupManager, int size)

Changes the intended size of the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes one or more instances.

The resize operation is marked DONE if theresize request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or deleting actions with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       int size = 3530753;
       Operation response =
           regionInstanceGroupManagersClient
               .resizeAsync(project, region, instanceGroupManager, size)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the managed instance group.  
`size` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Number of instances that should exist in this instance group manager.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeCallable()
    
    
    public final UnaryCallable<ResizeRegionInstanceGroupManagerRequest,Operation> resizeCallable()

Changes the intended size of the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes one or more instances.

The resize operation is marked DONE if theresize request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or deleting actions with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ResizeRegionInstanceGroupManagerRequest request =
           ResizeRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSize(3530753)
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.resizeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResizeRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeOperationCallable()
    
    
    public final OperationCallable<ResizeRegionInstanceGroupManagerRequest,Operation,Operation> resizeOperationCallable()

Changes the intended size of the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes one or more instances.

The resize operation is marked DONE if theresize request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or deleting actions with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ResizeRegionInstanceGroupManagerRequest request =
           ResizeRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSize(3530753)
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient.resizeOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ResizeRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeInstancesAsync(ResumeInstancesRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> resumeInstancesAsync(ResumeInstancesRegionInstanceGroupManagerRequest request)

Flags the specified instances in the managed instance group to be resumed. This method increases thetargetSize and decreases the targetSuspendedSize of the managed instance group by the number of instances that you resume. The resumeInstances operation is marked DONE if the resumeInstances request is successful. The underlying actions take additional time. You must separately verify the status of theRESUMING action with thelistmanagedinstances method.

In this request, you can only specify instances that are suspended. For example, if an instance was previously suspended using the suspendInstances method, it can be resumed using the resumeInstances method.

If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are resumed.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ResumeInstancesRegionInstanceGroupManagerRequest request =
           ResumeInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersResumeInstancesRequestResource(
                   RegionInstanceGroupManagersResumeInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupManagersClient.resumeInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResumeInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeInstancesRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersResumeInstancesRequest regionInstanceGroupManagersResumeInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> resumeInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersResumeInstancesRequest regionInstanceGroupManagersResumeInstancesRequestResource)

Flags the specified instances in the managed instance group to be resumed. This method increases thetargetSize and decreases the targetSuspendedSize of the managed instance group by the number of instances that you resume. The resumeInstances operation is marked DONE if the resumeInstances request is successful. The underlying actions take additional time. You must separately verify the status of theRESUMING action with thelistmanagedinstances method.

In this request, you can only specify instances that are suspended. For example, if an instance was previously suspended using the suspendInstances method, it can be resumed using the resumeInstances method.

If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are resumed.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagersResumeInstancesRequest
           regionInstanceGroupManagersResumeInstancesRequestResource =
               RegionInstanceGroupManagersResumeInstancesRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .resumeInstancesAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagersResumeInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the managed instance group.  
`regionInstanceGroupManagersResumeInstancesRequestResource` | `[RegionInstanceGroupManagersResumeInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersResumeInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeInstancesCallable()
    
    
    public final UnaryCallable<ResumeInstancesRegionInstanceGroupManagerRequest,Operation> resumeInstancesCallable()

Flags the specified instances in the managed instance group to be resumed. This method increases thetargetSize and decreases the targetSuspendedSize of the managed instance group by the number of instances that you resume. The resumeInstances operation is marked DONE if the resumeInstances request is successful. The underlying actions take additional time. You must separately verify the status of theRESUMING action with thelistmanagedinstances method.

In this request, you can only specify instances that are suspended. For example, if an instance was previously suspended using the suspendInstances method, it can be resumed using the resumeInstances method.

If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are resumed.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ResumeInstancesRegionInstanceGroupManagerRequest request =
           ResumeInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersResumeInstancesRequestResource(
                   RegionInstanceGroupManagersResumeInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.resumeInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResumeInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeInstancesOperationCallable()
    
    
    public final OperationCallable<ResumeInstancesRegionInstanceGroupManagerRequest,Operation,Operation> resumeInstancesOperationCallable()

Flags the specified instances in the managed instance group to be resumed. This method increases thetargetSize and decreases the targetSuspendedSize of the managed instance group by the number of instances that you resume. The resumeInstances operation is marked DONE if the resumeInstances request is successful. The underlying actions take additional time. You must separately verify the status of theRESUMING action with thelistmanagedinstances method.

In this request, you can only specify instances that are suspended. For example, if an instance was previously suspended using the suspendInstances method, it can be resumed using the resumeInstances method.

If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are resumed.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       ResumeInstancesRegionInstanceGroupManagerRequest request =
           ResumeInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersResumeInstancesRequestResource(
                   RegionInstanceGroupManagersResumeInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient.resumeInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ResumeInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setInstanceTemplateAsync(SetInstanceTemplateRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> setInstanceTemplateAsync(SetInstanceTemplateRegionInstanceGroupManagerRequest request)

Sets the instance template to use when creating new instances or recreating instances in this group. Existing instances are not affected.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       SetInstanceTemplateRegionInstanceGroupManagerRequest request =
           SetInstanceTemplateRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersSetTemplateRequestResource(
                   RegionInstanceGroupManagersSetTemplateRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response =
           regionInstanceGroupManagersClient.setInstanceTemplateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetInstanceTemplateRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetInstanceTemplateRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setInstanceTemplateAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersSetTemplateRequest regionInstanceGroupManagersSetTemplateRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setInstanceTemplateAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersSetTemplateRequest regionInstanceGroupManagersSetTemplateRequestResource)

Sets the instance template to use when creating new instances or recreating instances in this group. Existing instances are not affected.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagersSetTemplateRequest
           regionInstanceGroupManagersSetTemplateRequestResource =
               RegionInstanceGroupManagersSetTemplateRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .setInstanceTemplateAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagersSetTemplateRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
`regionInstanceGroupManagersSetTemplateRequestResource` | `[RegionInstanceGroupManagersSetTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersSetTemplateRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setInstanceTemplateCallable()
    
    
    public final UnaryCallable<SetInstanceTemplateRegionInstanceGroupManagerRequest,Operation> setInstanceTemplateCallable()

Sets the instance template to use when creating new instances or recreating instances in this group. Existing instances are not affected.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       SetInstanceTemplateRegionInstanceGroupManagerRequest request =
           SetInstanceTemplateRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersSetTemplateRequestResource(
                   RegionInstanceGroupManagersSetTemplateRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.setInstanceTemplateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetInstanceTemplateRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetInstanceTemplateRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setInstanceTemplateOperationCallable()
    
    
    public final OperationCallable<SetInstanceTemplateRegionInstanceGroupManagerRequest,Operation,Operation> setInstanceTemplateOperationCallable()

Sets the instance template to use when creating new instances or recreating instances in this group. Existing instances are not affected.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       SetInstanceTemplateRegionInstanceGroupManagerRequest request =
           SetInstanceTemplateRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersSetTemplateRequestResource(
                   RegionInstanceGroupManagersSetTemplateRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient
               .setInstanceTemplateOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetInstanceTemplateRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetInstanceTemplateRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetPoolsAsync(SetTargetPoolsRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> setTargetPoolsAsync(SetTargetPoolsRegionInstanceGroupManagerRequest request)

Modifies the target pools to which all new instances in this group are assigned. Existing instances in the group are not affected.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       SetTargetPoolsRegionInstanceGroupManagerRequest request =
           SetTargetPoolsRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersSetTargetPoolsRequestResource(
                   RegionInstanceGroupManagersSetTargetPoolsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupManagersClient.setTargetPoolsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetTargetPoolsRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTargetPoolsRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetPoolsAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersSetTargetPoolsRequest regionInstanceGroupManagersSetTargetPoolsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setTargetPoolsAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersSetTargetPoolsRequest regionInstanceGroupManagersSetTargetPoolsRequestResource)

Modifies the target pools to which all new instances in this group are assigned. Existing instances in the group are not affected.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagersSetTargetPoolsRequest
           regionInstanceGroupManagersSetTargetPoolsRequestResource =
               RegionInstanceGroupManagersSetTargetPoolsRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .setTargetPoolsAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagersSetTargetPoolsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the managed instance group.  
`regionInstanceGroupManagersSetTargetPoolsRequestResource` | `[RegionInstanceGroupManagersSetTargetPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersSetTargetPoolsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetPoolsCallable()
    
    
    public final UnaryCallable<SetTargetPoolsRegionInstanceGroupManagerRequest,Operation> setTargetPoolsCallable()

Modifies the target pools to which all new instances in this group are assigned. Existing instances in the group are not affected.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       SetTargetPoolsRegionInstanceGroupManagerRequest request =
           SetTargetPoolsRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersSetTargetPoolsRequestResource(
                   RegionInstanceGroupManagersSetTargetPoolsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.setTargetPoolsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetTargetPoolsRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTargetPoolsRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetPoolsOperationCallable()
    
    
    public final OperationCallable<SetTargetPoolsRegionInstanceGroupManagerRequest,Operation,Operation> setTargetPoolsOperationCallable()

Modifies the target pools to which all new instances in this group are assigned. Existing instances in the group are not affected.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       SetTargetPoolsRegionInstanceGroupManagerRequest request =
           SetTargetPoolsRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersSetTargetPoolsRequestResource(
                   RegionInstanceGroupManagersSetTargetPoolsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient.setTargetPoolsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetTargetPoolsRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTargetPoolsRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### startInstancesAsync(StartInstancesRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> startInstancesAsync(StartInstancesRegionInstanceGroupManagerRequest request)

Flags the specified instances in the managed instance group to be started. This method increases thetargetSize and decreases the targetStoppedSize of the managed instance group by the number of instances that you start. The startInstances operation is marked DONE if the startInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTARTING action with thelistmanagedinstances method.

In this request, you can only specify instances that are stopped. For example, if an instance was previously stopped using the stopInstances method, it can be started using the startInstances method.

If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are started.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       StartInstancesRegionInstanceGroupManagerRequest request =
           StartInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersStartInstancesRequestResource(
                   RegionInstanceGroupManagersStartInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupManagersClient.startInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstancesRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersStartInstancesRequest regionInstanceGroupManagersStartInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> startInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersStartInstancesRequest regionInstanceGroupManagersStartInstancesRequestResource)

Flags the specified instances in the managed instance group to be started. This method increases thetargetSize and decreases the targetStoppedSize of the managed instance group by the number of instances that you start. The startInstances operation is marked DONE if the startInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTARTING action with thelistmanagedinstances method.

In this request, you can only specify instances that are stopped. For example, if an instance was previously stopped using the stopInstances method, it can be started using the startInstances method.

If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are started.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagersStartInstancesRequest
           regionInstanceGroupManagersStartInstancesRequestResource =
               RegionInstanceGroupManagersStartInstancesRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .startInstancesAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagersStartInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the managed instance group.  
`regionInstanceGroupManagersStartInstancesRequestResource` | `[RegionInstanceGroupManagersStartInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersStartInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startInstancesCallable()
    
    
    public final UnaryCallable<StartInstancesRegionInstanceGroupManagerRequest,Operation> startInstancesCallable()

Flags the specified instances in the managed instance group to be started. This method increases thetargetSize and decreases the targetStoppedSize of the managed instance group by the number of instances that you start. The startInstances operation is marked DONE if the startInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTARTING action with thelistmanagedinstances method.

In this request, you can only specify instances that are stopped. For example, if an instance was previously stopped using the stopInstances method, it can be started using the startInstances method.

If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are started.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       StartInstancesRegionInstanceGroupManagerRequest request =
           StartInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersStartInstancesRequestResource(
                   RegionInstanceGroupManagersStartInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.startInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startInstancesOperationCallable()
    
    
    public final OperationCallable<StartInstancesRegionInstanceGroupManagerRequest,Operation,Operation> startInstancesOperationCallable()

Flags the specified instances in the managed instance group to be started. This method increases thetargetSize and decreases the targetStoppedSize of the managed instance group by the number of instances that you start. The startInstances operation is marked DONE if the startInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTARTING action with thelistmanagedinstances method.

In this request, you can only specify instances that are stopped. For example, if an instance was previously stopped using the stopInstances method, it can be started using the startInstances method.

If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are started.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       StartInstancesRegionInstanceGroupManagerRequest request =
           StartInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersStartInstancesRequestResource(
                   RegionInstanceGroupManagersStartInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient.startInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StartInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopInstancesAsync(StopInstancesRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> stopInstancesAsync(StopInstancesRegionInstanceGroupManagerRequest request)

Flags the specified instances in the managed instance group to be immediately stopped. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetStoppedSize of the managed instance group by the number of instances that you stop. The stopInstances operation is marked DONE if the stopInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTOPPING action with thelistmanagedinstances method.

If the standbyPolicy.initialDelaySec field is set, the group delays stopping the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is stopped.

Stopped instances can be started using the startInstances method.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       StopInstancesRegionInstanceGroupManagerRequest request =
           StopInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersStopInstancesRequestResource(
                   RegionInstanceGroupManagersStopInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupManagersClient.stopInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstancesRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersStopInstancesRequest regionInstanceGroupManagersStopInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> stopInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersStopInstancesRequest regionInstanceGroupManagersStopInstancesRequestResource)

Flags the specified instances in the managed instance group to be immediately stopped. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetStoppedSize of the managed instance group by the number of instances that you stop. The stopInstances operation is marked DONE if the stopInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTOPPING action with thelistmanagedinstances method.

If the standbyPolicy.initialDelaySec field is set, the group delays stopping the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is stopped.

Stopped instances can be started using the startInstances method.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagersStopInstancesRequest
           regionInstanceGroupManagersStopInstancesRequestResource =
               RegionInstanceGroupManagersStopInstancesRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .stopInstancesAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagersStopInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
`regionInstanceGroupManagersStopInstancesRequestResource` | `[RegionInstanceGroupManagersStopInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersStopInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopInstancesCallable()
    
    
    public final UnaryCallable<StopInstancesRegionInstanceGroupManagerRequest,Operation> stopInstancesCallable()

Flags the specified instances in the managed instance group to be immediately stopped. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetStoppedSize of the managed instance group by the number of instances that you stop. The stopInstances operation is marked DONE if the stopInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTOPPING action with thelistmanagedinstances method.

If the standbyPolicy.initialDelaySec field is set, the group delays stopping the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is stopped.

Stopped instances can be started using the startInstances method.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       StopInstancesRegionInstanceGroupManagerRequest request =
           StopInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersStopInstancesRequestResource(
                   RegionInstanceGroupManagersStopInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.stopInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StopInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopInstancesOperationCallable()
    
    
    public final OperationCallable<StopInstancesRegionInstanceGroupManagerRequest,Operation,Operation> stopInstancesOperationCallable()

Flags the specified instances in the managed instance group to be immediately stopped. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetStoppedSize of the managed instance group by the number of instances that you stop. The stopInstances operation is marked DONE if the stopInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTOPPING action with thelistmanagedinstances method.

If the standbyPolicy.initialDelaySec field is set, the group delays stopping the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is stopped.

Stopped instances can be started using the startInstances method.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       StopInstancesRegionInstanceGroupManagerRequest request =
           StopInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersStopInstancesRequestResource(
                   RegionInstanceGroupManagersStopInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient.stopInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StopInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendInstancesAsync(SuspendInstancesRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> suspendInstancesAsync(SuspendInstancesRegionInstanceGroupManagerRequest request)

Flags the specified instances in the managed instance group to be immediately suspended. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetSuspendedSize of the managed instance group by the number of instances that you suspend. The suspendInstances operation is marked DONE if the suspendInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSUSPENDING action with thelistmanagedinstances method.

If the standbyPolicy.initialDelaySec field is set, the group delays suspension of the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is suspended.

Suspended instances can be resumed using the resumeInstances method.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       SuspendInstancesRegionInstanceGroupManagerRequest request =
           SuspendInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersSuspendInstancesRequestResource(
                   RegionInstanceGroupManagersSuspendInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupManagersClient.suspendInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SuspendInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SuspendInstancesRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersSuspendInstancesRequest regionInstanceGroupManagersSuspendInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> suspendInstancesAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagersSuspendInstancesRequest regionInstanceGroupManagersSuspendInstancesRequestResource)

Flags the specified instances in the managed instance group to be immediately suspended. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetSuspendedSize of the managed instance group by the number of instances that you suspend. The suspendInstances operation is marked DONE if the suspendInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSUSPENDING action with thelistmanagedinstances method.

If the standbyPolicy.initialDelaySec field is set, the group delays suspension of the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is suspended.

Suspended instances can be resumed using the resumeInstances method.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagersSuspendInstancesRequest
           regionInstanceGroupManagersSuspendInstancesRequestResource =
               RegionInstanceGroupManagersSuspendInstancesRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .suspendInstancesAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagersSuspendInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the managed instance group.  
`regionInstanceGroupManagersSuspendInstancesRequestResource` | `[RegionInstanceGroupManagersSuspendInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagersSuspendInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendInstancesCallable()
    
    
    public final UnaryCallable<SuspendInstancesRegionInstanceGroupManagerRequest,Operation> suspendInstancesCallable()

Flags the specified instances in the managed instance group to be immediately suspended. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetSuspendedSize of the managed instance group by the number of instances that you suspend. The suspendInstances operation is marked DONE if the suspendInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSUSPENDING action with thelistmanagedinstances method.

If the standbyPolicy.initialDelaySec field is set, the group delays suspension of the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is suspended.

Suspended instances can be resumed using the resumeInstances method.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       SuspendInstancesRegionInstanceGroupManagerRequest request =
           SuspendInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersSuspendInstancesRequestResource(
                   RegionInstanceGroupManagersSuspendInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.suspendInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SuspendInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SuspendInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendInstancesOperationCallable()
    
    
    public final OperationCallable<SuspendInstancesRegionInstanceGroupManagerRequest,Operation,Operation> suspendInstancesOperationCallable()

Flags the specified instances in the managed instance group to be immediately suspended. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetSuspendedSize of the managed instance group by the number of instances that you suspend. The suspendInstances operation is marked DONE if the suspendInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSUSPENDING action with thelistmanagedinstances method.

If the standbyPolicy.initialDelaySec field is set, the group delays suspension of the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is suspended.

Suspended instances can be resumed using the resumeInstances method.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       SuspendInstancesRegionInstanceGroupManagerRequest request =
           SuspendInstancesRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagersSuspendInstancesRequestResource(
                   RegionInstanceGroupManagersSuspendInstancesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient.suspendInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SuspendInstancesRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SuspendInstancesRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updatePerInstanceConfigsAsync(UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> updatePerInstanceConfigsAsync(UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest request)

Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest request =
           UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagerUpdateInstanceConfigReqResource(
                   RegionInstanceGroupManagerUpdateInstanceConfigReq.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response =
           regionInstanceGroupManagersClient.updatePerInstanceConfigsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updatePerInstanceConfigsAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagerUpdateInstanceConfigReq regionInstanceGroupManagerUpdateInstanceConfigReqResource)
    
    
    public final OperationFuture<Operation,Operation> updatePerInstanceConfigsAsync(String project, String region, String instanceGroupManager, RegionInstanceGroupManagerUpdateInstanceConfigReq regionInstanceGroupManagerUpdateInstanceConfigReqResource)

Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       RegionInstanceGroupManagerUpdateInstanceConfigReq
           regionInstanceGroupManagerUpdateInstanceConfigReqResource =
               RegionInstanceGroupManagerUpdateInstanceConfigReq.newBuilder().build();
       Operation response =
           regionInstanceGroupManagersClient
               .updatePerInstanceConfigsAsync(
                   project,
                   region,
                   instanceGroupManager,
                   regionInstanceGroupManagerUpdateInstanceConfigReqResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request, should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. It should conform to RFC1035.  
`regionInstanceGroupManagerUpdateInstanceConfigReqResource` | `[RegionInstanceGroupManagerUpdateInstanceConfigReq](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerUpdateInstanceConfigReq)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updatePerInstanceConfigsCallable()
    
    
    public final UnaryCallable<UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest,Operation> updatePerInstanceConfigsCallable()

Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest request =
           UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagerUpdateInstanceConfigReqResource(
                   RegionInstanceGroupManagerUpdateInstanceConfigReq.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagersClient.updatePerInstanceConfigsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updatePerInstanceConfigsOperationCallable()
    
    
    public final OperationCallable<UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest,Operation,Operation> updatePerInstanceConfigsOperationCallable()

Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagersClient regionInstanceGroupManagersClient =
         RegionInstanceGroupManagersClient.create()) {
       UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest request =
           UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupManagerUpdateInstanceConfigReqResource(
                   RegionInstanceGroupManagerUpdateInstanceConfigReq.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagersClient
               .updatePerInstanceConfigsOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdatePerInstanceConfigsRegionInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
