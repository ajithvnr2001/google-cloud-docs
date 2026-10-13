---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient
title: Class InstanceGroupManagersClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:35.412400+00:00
---

# Class InstanceGroupManagersClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InstanceGroupManagersClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/InstanceGroupManagersClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The InstanceGroupManagers API.

This client uses InstanceGroupManagers version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManager response =
           instanceGroupManagersClient.get(project, zone, instanceGroupManager);
     }
     

Note: close() needs to be called on the InstanceGroupManagersClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AbandonInstances |  Flags the specified instances to be removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces thetargetSize of the managed instance group by the number of instances that you abandon. This operation is marked asDONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with thelistmanagedinstances method.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * abandonInstancesAsync(AbandonInstancesInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * abandonInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersAbandonInstancesRequest instanceGroupManagersAbandonInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * abandonInstancesOperationCallable() 
  * abandonInstancesCallable() 

  
AggregatedList |  Retrieves the list of managed instance groups and groups them by zone.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListInstanceGroupManagersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
ApplyUpdatesToInstances |  Applies changes to selected instances on the managed instance group. This method can be used to apply new overrides and/or new versions. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * applyUpdatesToInstancesAsync(ApplyUpdatesToInstancesInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * applyUpdatesToInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersApplyUpdatesRequest instanceGroupManagersApplyUpdatesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * applyUpdatesToInstancesOperationCallable() 
  * applyUpdatesToInstancesCallable() 

  
CreateInstances |  Creates instances with per-instance configurations in this managed instance group. Instances are created using the current instance template. Thecreate instances operation is marked DONE if thecreateInstances request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or actions with the listmanagedinstances method. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createInstancesAsync(CreateInstancesInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersCreateInstancesRequest instanceGroupManagersCreateInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createInstancesOperationCallable() 
  * createInstancesCallable() 

  
Delete |  Deletes the specified managed instance group and all of the instances in that group. Note that the instance group must not belong to a backend service. Read Deleting an instance group for more information. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String zone, String instanceGroupManager) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
DeleteInstances |  Flags the specified instances in the managed instance group for immediate deletion. The instances are also removed from any target pools of which they were a member. This method reduces thetargetSize of the managed instance group by the number of instances that you delete. This operation is marked as DONE when the action is scheduled even if the instances are still being deleted. You must separately verify the status of the deleting action with thelistmanagedinstances method.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteInstancesAsync(DeleteInstancesInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersDeleteInstancesRequest instanceGroupManagersDeleteInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteInstancesOperationCallable() 
  * deleteInstancesCallable() 

  
DeletePerInstanceConfigs |  Deletes selected per-instance configurations for the managed instance group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePerInstanceConfigsAsync(DeletePerInstanceConfigsInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePerInstanceConfigsAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersDeletePerInstanceConfigsReq instanceGroupManagersDeletePerInstanceConfigsReqResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePerInstanceConfigsOperationCallable() 
  * deletePerInstanceConfigsCallable() 

  
Get |  Returns all of the details about the specified managed instance group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetInstanceGroupManagerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String instanceGroupManager) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with thelistmanagedinstances method.  A managed instance group can have up to 1000 VM instances per group. Please contact Cloud Support if you need an increase in this limit. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String zone, InstanceGroupManager instanceGroupManagerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of managed instance groups that are contained within the specified project and zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListInstanceGroupManagersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListErrors |  Lists all errors thrown by actions on instances for a given managed instance group. The filter and orderBy query parameters are not supported. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listErrors(ListErrorsInstanceGroupManagersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listErrors(String project, String zone, String instanceGroupManager) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listErrorsPagedCallable() 
  * listErrorsCallable() 

  
ListManagedInstances |  Lists all of the instances in the managed instance group. Each instance in the list has a currentAction, which indicates the action that the managed instance group is performing on the instance. For example, if the group is still creating an instance, the currentAction is CREATING. If a previous action failed, the list displays the errors for that failed action. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listManagedInstances(ListManagedInstancesInstanceGroupManagersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listManagedInstances(String project, String zone, String instanceGroupManager) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listManagedInstancesPagedCallable() 
  * listManagedInstancesCallable() 

  
ListPerInstanceConfigs |  Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPerInstanceConfigs(ListPerInstanceConfigsInstanceGroupManagersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPerInstanceConfigs(String project, String zone, String instanceGroupManager) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPerInstanceConfigsPagedCallable() 
  * listPerInstanceConfigsCallable() 

  
Patch |  Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with thelistManagedInstances method. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.  If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String zone, String instanceGroupManager, InstanceGroupManager instanceGroupManagerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
PatchPerInstanceConfigs |  Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchPerInstanceConfigsAsync(PatchPerInstanceConfigsInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchPerInstanceConfigsAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersPatchPerInstanceConfigsReq instanceGroupManagersPatchPerInstanceConfigsReqResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchPerInstanceConfigsOperationCallable() 
  * patchPerInstanceConfigsCallable() 

  
RecreateInstances |  Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking itscurrentAction field; for more information, see Checking the status of managed instances.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * recreateInstancesAsync(RecreateInstancesInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * recreateInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersRecreateInstancesRequest instanceGroupManagersRecreateInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * recreateInstancesOperationCallable() 
  * recreateInstancesCallable() 

  
Resize |  Resizes the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes instances. The resize operation is markedDONE when the resize actions are scheduled even if the group has not yet added or deleted any instances. You must separately verify the status of the creating or deleting actions with thelistmanagedinstances method.  When resizing down, the instance group arbitrarily chooses the order in which VMs are deleted. The group takes into account some VM attributes when making the selection including:  \+ The status of the VM instance. + The health of the VM instance. + The instance template version the VM is based on. + For regional managed instance groups, the location of the VM instance.  This list is subject to change.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resizeAsync(ResizeInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * resizeAsync(String project, String zone, String instanceGroupManager, int size) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resizeOperationCallable() 
  * resizeCallable() 

  
ResumeInstances |  Flags the specified instances in the managed instance group to be resumed. This method increases thetargetSize and decreases the targetSuspendedSize of the managed instance group by the number of instances that you resume. The resumeInstances operation is marked DONE if the resumeInstances request is successful. The underlying actions take additional time. You must separately verify the status of theRESUMING action with thelistmanagedinstances method.  In this request, you can only specify instances that are suspended. For example, if an instance was previously suspended using the suspendInstances method, it can be resumed using the resumeInstances method.  If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are resumed.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resumeInstancesAsync(ResumeInstancesInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * resumeInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersResumeInstancesRequest instanceGroupManagersResumeInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resumeInstancesOperationCallable() 
  * resumeInstancesCallable() 

  
SetInstanceTemplate |  Specifies the instance template to use when creating new instances in this group. The templates for existing instances in the group do not change unless you run recreateInstances, runapplyUpdatesToInstances, or set the group'supdatePolicy.type to PROACTIVE. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setInstanceTemplateAsync(SetInstanceTemplateInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setInstanceTemplateAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersSetInstanceTemplateRequest instanceGroupManagersSetInstanceTemplateRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setInstanceTemplateOperationCallable() 
  * setInstanceTemplateCallable() 

  
SetTargetPools |  Modifies the target pools to which all instances in this managed instance group are assigned. The target pools automatically apply to all of the instances in the managed instance group. This operation is markedDONE when you make the request even if the instances have not yet been added to their target pools. The change might take some time to apply to all of the instances in the group depending on the size of the group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setTargetPoolsAsync(SetTargetPoolsInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setTargetPoolsAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersSetTargetPoolsRequest instanceGroupManagersSetTargetPoolsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setTargetPoolsOperationCallable() 
  * setTargetPoolsCallable() 

  
StartInstances |  Flags the specified instances in the managed instance group to be started. This method increases thetargetSize and decreases the targetStoppedSize of the managed instance group by the number of instances that you start. The startInstances operation is marked DONE if the startInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTARTING action with thelistmanagedinstances method.  In this request, you can only specify instances that are stopped. For example, if an instance was previously stopped using the stopInstances method, it can be started using the startInstances method.  If a health check is attached to the managed instance group, the specified instances will be verified as healthy after they are started.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startInstancesAsync(StartInstancesInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * startInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersStartInstancesRequest instanceGroupManagersStartInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startInstancesOperationCallable() 
  * startInstancesCallable() 

  
StopInstances |  Flags the specified instances in the managed instance group to be immediately stopped. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetStoppedSize of the managed instance group by the number of instances that you stop. The stopInstances operation is marked DONE if the stopInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSTOPPING action with thelistmanagedinstances method.  If the standbyPolicy.initialDelaySec field is set, the group delays stopping the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is stopped.  Stopped instances can be started using the startInstances method.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopInstancesAsync(StopInstancesInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * stopInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersStopInstancesRequest instanceGroupManagersStopInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopInstancesOperationCallable() 
  * stopInstancesCallable() 

  
SuspendInstances |  Flags the specified instances in the managed instance group to be immediately suspended. You can only specify instances that are running in this request. This method reduces thetargetSize and increases the targetSuspendedSize of the managed instance group by the number of instances that you suspend. The suspendInstances operation is marked DONE if the suspendInstances request is successful. The underlying actions take additional time. You must separately verify the status of theSUSPENDING action with thelistmanagedinstances method.  If the standbyPolicy.initialDelaySec field is set, the group delays suspension of the instances until initialDelaySec have passed from instance.creationTimestamp (that is, when the instance was created). This delay gives your application time to set itself up and initialize on the instance. If more thaninitialDelaySec seconds have passed sinceinstance.creationTimestamp when this method is called, there will be zero delay.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is suspended.  Suspended instances can be resumed using the resumeInstances method.  You can specify a maximum of 1000 instances with this method per request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * suspendInstancesAsync(SuspendInstancesInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * suspendInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersSuspendInstancesRequest instanceGroupManagersSuspendInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * suspendInstancesOperationCallable() 
  * suspendInstancesCallable() 

  
UpdatePerInstanceConfigs |  Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePerInstanceConfigsAsync(UpdatePerInstanceConfigsInstanceGroupManagerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updatePerInstanceConfigsAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersUpdatePerInstanceConfigsReq instanceGroupManagersUpdatePerInstanceConfigsReqResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePerInstanceConfigsOperationCallable() 
  * updatePerInstanceConfigsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of InstanceGroupManagersSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InstanceGroupManagersSettings instanceGroupManagersSettings =
         InstanceGroupManagersSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create(instanceGroupManagersSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InstanceGroupManagersSettings instanceGroupManagersSettings =
         InstanceGroupManagersSettings.newBuilder().setEndpoint(myEndpoint).build();
     InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create(instanceGroupManagersSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InstanceGroupManagersClient

## Static Methods 

### create()
    
    
    public static final InstanceGroupManagersClient create()

Constructs an instance of InstanceGroupManagersClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InstanceGroupManagersSettings settings)
    
    
    public static final InstanceGroupManagersClient create(InstanceGroupManagersSettings settings)

Constructs an instance of InstanceGroupManagersClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InstanceGroupManagersSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InstanceGroupManagersStub stub)
    
    
    public static final InstanceGroupManagersClient create(InstanceGroupManagersStub stub)

Constructs an instance of InstanceGroupManagersClient, using the given stub for making calls. This is for advanced usage - prefer using create(InstanceGroupManagersSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InstanceGroupManagersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstanceGroupManagersStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient)` |   
  
## Constructors 

### InstanceGroupManagersClient(InstanceGroupManagersSettings settings)
    
    
    protected InstanceGroupManagersClient(InstanceGroupManagersSettings settings)

Constructs an instance of InstanceGroupManagersClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InstanceGroupManagersSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersSettings)`  
  
  
### InstanceGroupManagersClient(InstanceGroupManagersStub stub)
    
    
    protected InstanceGroupManagersClient(InstanceGroupManagersStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InstanceGroupManagersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstanceGroupManagersStub)`  
  
  
## Methods 

### abandonInstancesAsync(AbandonInstancesInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> abandonInstancesAsync(AbandonInstancesInstanceGroupManagerRequest request)

Flags the specified instances to be removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces thetargetSize of the managed instance group by the number of instances that you abandon. This operation is marked asDONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       AbandonInstancesInstanceGroupManagerRequest request =
           AbandonInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersAbandonInstancesRequestResource(
                   InstanceGroupManagersAbandonInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.abandonInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AbandonInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AbandonInstancesInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### abandonInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersAbandonInstancesRequest instanceGroupManagersAbandonInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> abandonInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersAbandonInstancesRequest instanceGroupManagersAbandonInstancesRequestResource)

Flags the specified instances to be removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces thetargetSize of the managed instance group by the number of instances that you abandon. This operation is marked asDONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersAbandonInstancesRequest
           instanceGroupManagersAbandonInstancesRequestResource =
               InstanceGroupManagersAbandonInstancesRequest.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .abandonInstancesAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersAbandonInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
`instanceGroupManagersAbandonInstancesRequestResource` | `[InstanceGroupManagersAbandonInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersAbandonInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### abandonInstancesCallable()
    
    
    public final UnaryCallable<AbandonInstancesInstanceGroupManagerRequest,Operation> abandonInstancesCallable()

Flags the specified instances to be removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces thetargetSize of the managed instance group by the number of instances that you abandon. This operation is marked asDONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       AbandonInstancesInstanceGroupManagerRequest request =
           AbandonInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersAbandonInstancesRequestResource(
                   InstanceGroupManagersAbandonInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.abandonInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AbandonInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AbandonInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### abandonInstancesOperationCallable()
    
    
    public final OperationCallable<AbandonInstancesInstanceGroupManagerRequest,Operation,Operation> abandonInstancesOperationCallable()

Flags the specified instances to be removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces thetargetSize of the managed instance group by the number of instances that you abandon. This operation is marked asDONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       AbandonInstancesInstanceGroupManagerRequest request =
           AbandonInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersAbandonInstancesRequestResource(
                   InstanceGroupManagersAbandonInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.abandonInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AbandonInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AbandonInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### aggregatedList(AggregatedListInstanceGroupManagersRequest request)
    
    
    public final InstanceGroupManagersClient.AggregatedListPagedResponse aggregatedList(AggregatedListInstanceGroupManagersRequest request)

Retrieves the list of managed instance groups and groups them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       AggregatedListInstanceGroupManagersRequest request =
           AggregatedListInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, InstanceGroupManagersScopedList> element :
           instanceGroupManagersClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstanceGroupManagersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final InstanceGroupManagersClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of managed instance groups and groups them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, InstanceGroupManagersScopedList> element :
           instanceGroupManagersClient.aggregatedList(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListInstanceGroupManagersRequest,InstanceGroupManagerAggregatedList> aggregatedListCallable()

Retrieves the list of managed instance groups and groups them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       AggregatedListInstanceGroupManagersRequest request =
           AggregatedListInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         InstanceGroupManagerAggregatedList response =
             instanceGroupManagersClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, InstanceGroupManagersScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstanceGroupManagersRequest),[InstanceGroupManagerAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagerAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListInstanceGroupManagersRequest,InstanceGroupManagersClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of managed instance groups and groups them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       AggregatedListInstanceGroupManagersRequest request =
           AggregatedListInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, InstanceGroupManagersScopedList>> future =
           instanceGroupManagersClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, InstanceGroupManagersScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstanceGroupManagersRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.AggregatedListPagedResponse)>` |   
  
### applyUpdatesToInstancesAsync(ApplyUpdatesToInstancesInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> applyUpdatesToInstancesAsync(ApplyUpdatesToInstancesInstanceGroupManagerRequest request)

Applies changes to selected instances on the managed instance group. This method can be used to apply new overrides and/or new versions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ApplyUpdatesToInstancesInstanceGroupManagerRequest request =
           ApplyUpdatesToInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersApplyUpdatesRequestResource(
                   InstanceGroupManagersApplyUpdatesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.applyUpdatesToInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ApplyUpdatesToInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ApplyUpdatesToInstancesInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### applyUpdatesToInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersApplyUpdatesRequest instanceGroupManagersApplyUpdatesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> applyUpdatesToInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersApplyUpdatesRequest instanceGroupManagersApplyUpdatesRequestResource)

Applies changes to selected instances on the managed instance group. This method can be used to apply new overrides and/or new versions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersApplyUpdatesRequest instanceGroupManagersApplyUpdatesRequestResource =
           InstanceGroupManagersApplyUpdatesRequest.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .applyUpdatesToInstancesAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersApplyUpdatesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located. Should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group, should conform to RFC1035.  
`instanceGroupManagersApplyUpdatesRequestResource` | `[InstanceGroupManagersApplyUpdatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersApplyUpdatesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### applyUpdatesToInstancesCallable()
    
    
    public final UnaryCallable<ApplyUpdatesToInstancesInstanceGroupManagerRequest,Operation> applyUpdatesToInstancesCallable()

Applies changes to selected instances on the managed instance group. This method can be used to apply new overrides and/or new versions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ApplyUpdatesToInstancesInstanceGroupManagerRequest request =
           ApplyUpdatesToInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersApplyUpdatesRequestResource(
                   InstanceGroupManagersApplyUpdatesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.applyUpdatesToInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ApplyUpdatesToInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ApplyUpdatesToInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### applyUpdatesToInstancesOperationCallable()
    
    
    public final OperationCallable<ApplyUpdatesToInstancesInstanceGroupManagerRequest,Operation,Operation> applyUpdatesToInstancesOperationCallable()

Applies changes to selected instances on the managed instance group. This method can be used to apply new overrides and/or new versions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ApplyUpdatesToInstancesInstanceGroupManagerRequest request =
           ApplyUpdatesToInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersApplyUpdatesRequestResource(
                   InstanceGroupManagersApplyUpdatesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient
               .applyUpdatesToInstancesOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ApplyUpdatesToInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ApplyUpdatesToInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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

### createInstancesAsync(CreateInstancesInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> createInstancesAsync(CreateInstancesInstanceGroupManagerRequest request)

Creates instances with per-instance configurations in this managed instance group. Instances are created using the current instance template. Thecreate instances operation is marked DONE if thecreateInstances request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or actions with the listmanagedinstances method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       CreateInstancesInstanceGroupManagerRequest request =
           CreateInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersCreateInstancesRequestResource(
                   InstanceGroupManagersCreateInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.createInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CreateInstancesInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### createInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersCreateInstancesRequest instanceGroupManagersCreateInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> createInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersCreateInstancesRequest instanceGroupManagersCreateInstancesRequestResource)

Creates instances with per-instance configurations in this managed instance group. Instances are created using the current instance template. Thecreate instances operation is marked DONE if thecreateInstances request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or actions with the listmanagedinstances method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersCreateInstancesRequest
           instanceGroupManagersCreateInstancesRequestResource =
               InstanceGroupManagersCreateInstancesRequest.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .createInstancesAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersCreateInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located. It should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. It should conform to RFC1035.  
`instanceGroupManagersCreateInstancesRequestResource` | `[InstanceGroupManagersCreateInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersCreateInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### createInstancesCallable()
    
    
    public final UnaryCallable<CreateInstancesInstanceGroupManagerRequest,Operation> createInstancesCallable()

Creates instances with per-instance configurations in this managed instance group. Instances are created using the current instance template. Thecreate instances operation is marked DONE if thecreateInstances request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or actions with the listmanagedinstances method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       CreateInstancesInstanceGroupManagerRequest request =
           CreateInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersCreateInstancesRequestResource(
                   InstanceGroupManagersCreateInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.createInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CreateInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### createInstancesOperationCallable()
    
    
    public final OperationCallable<CreateInstancesInstanceGroupManagerRequest,Operation,Operation> createInstancesOperationCallable()

Creates instances with per-instance configurations in this managed instance group. Instances are created using the current instance template. Thecreate instances operation is marked DONE if thecreateInstances request is successful. The underlying actions take additional time. You must separately verify the status of thecreating or actions with the listmanagedinstances method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       CreateInstancesInstanceGroupManagerRequest request =
           CreateInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersCreateInstancesRequestResource(
                   InstanceGroupManagersCreateInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.createInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CreateInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(DeleteInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteInstanceGroupManagerRequest request)

Deletes the specified managed instance group and all of the instances in that group. Note that the instance group must not belong to a backend service. Read Deleting an instance group for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       DeleteInstanceGroupManagerRequest request =
           DeleteInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String zone, String instanceGroupManager)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String zone, String instanceGroupManager)

Deletes the specified managed instance group and all of the instances in that group. Note that the instance group must not belong to a backend service. Read Deleting an instance group for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       Operation response =
           instanceGroupManagersClient.deleteAsync(project, zone, instanceGroupManager).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteInstanceGroupManagerRequest,Operation> deleteCallable()

Deletes the specified managed instance group and all of the instances in that group. Note that the instance group must not belong to a backend service. Read Deleting an instance group for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       DeleteInstanceGroupManagerRequest request =
           DeleteInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteInstancesAsync(DeleteInstancesInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteInstancesAsync(DeleteInstancesInstanceGroupManagerRequest request)

Flags the specified instances in the managed instance group for immediate deletion. The instances are also removed from any target pools of which they were a member. This method reduces thetargetSize of the managed instance group by the number of instances that you delete. This operation is marked as DONE when the action is scheduled even if the instances are still being deleted. You must separately verify the status of the deleting action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       DeleteInstancesInstanceGroupManagerRequest request =
           DeleteInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersDeleteInstancesRequestResource(
                   InstanceGroupManagersDeleteInstancesRequest.newBuilder().build())
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.deleteInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstancesInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersDeleteInstancesRequest instanceGroupManagersDeleteInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> deleteInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersDeleteInstancesRequest instanceGroupManagersDeleteInstancesRequestResource)

Flags the specified instances in the managed instance group for immediate deletion. The instances are also removed from any target pools of which they were a member. This method reduces thetargetSize of the managed instance group by the number of instances that you delete. This operation is marked as DONE when the action is scheduled even if the instances are still being deleted. You must separately verify the status of the deleting action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersDeleteInstancesRequest
           instanceGroupManagersDeleteInstancesRequestResource =
               InstanceGroupManagersDeleteInstancesRequest.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .deleteInstancesAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersDeleteInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
`instanceGroupManagersDeleteInstancesRequestResource` | `[InstanceGroupManagersDeleteInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersDeleteInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteInstancesCallable()
    
    
    public final UnaryCallable<DeleteInstancesInstanceGroupManagerRequest,Operation> deleteInstancesCallable()

Flags the specified instances in the managed instance group for immediate deletion. The instances are also removed from any target pools of which they were a member. This method reduces thetargetSize of the managed instance group by the number of instances that you delete. This operation is marked as DONE when the action is scheduled even if the instances are still being deleted. You must separately verify the status of the deleting action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       DeleteInstancesInstanceGroupManagerRequest request =
           DeleteInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersDeleteInstancesRequestResource(
                   InstanceGroupManagersDeleteInstancesRequest.newBuilder().build())
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.deleteInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteInstancesOperationCallable()
    
    
    public final OperationCallable<DeleteInstancesInstanceGroupManagerRequest,Operation,Operation> deleteInstancesOperationCallable()

Flags the specified instances in the managed instance group for immediate deletion. The instances are also removed from any target pools of which they were a member. This method reduces thetargetSize of the managed instance group by the number of instances that you delete. This operation is marked as DONE when the action is scheduled even if the instances are still being deleted. You must separately verify the status of the deleting action with thelistmanagedinstances method.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       DeleteInstancesInstanceGroupManagerRequest request =
           DeleteInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersDeleteInstancesRequestResource(
                   InstanceGroupManagersDeleteInstancesRequest.newBuilder().build())
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.deleteInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteInstanceGroupManagerRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified managed instance group and all of the instances in that group. Note that the instance group must not belong to a backend service. Read Deleting an instance group for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       DeleteInstanceGroupManagerRequest request =
           DeleteInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deletePerInstanceConfigsAsync(DeletePerInstanceConfigsInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> deletePerInstanceConfigsAsync(DeletePerInstanceConfigsInstanceGroupManagerRequest request)

Deletes selected per-instance configurations for the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       DeletePerInstanceConfigsInstanceGroupManagerRequest request =
           DeletePerInstanceConfigsInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersDeletePerInstanceConfigsReqResource(
                   InstanceGroupManagersDeletePerInstanceConfigsReq.newBuilder().build())
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.deletePerInstanceConfigsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeletePerInstanceConfigsInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deletePerInstanceConfigsAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersDeletePerInstanceConfigsReq instanceGroupManagersDeletePerInstanceConfigsReqResource)
    
    
    public final OperationFuture<Operation,Operation> deletePerInstanceConfigsAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersDeletePerInstanceConfigsReq instanceGroupManagersDeletePerInstanceConfigsReqResource)

Deletes selected per-instance configurations for the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersDeletePerInstanceConfigsReq
           instanceGroupManagersDeletePerInstanceConfigsReqResource =
               InstanceGroupManagersDeletePerInstanceConfigsReq.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .deletePerInstanceConfigsAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersDeletePerInstanceConfigsReqResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located. It should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. It should conform to RFC1035.  
`instanceGroupManagersDeletePerInstanceConfigsReqResource` | `[InstanceGroupManagersDeletePerInstanceConfigsReq](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersDeletePerInstanceConfigsReq)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deletePerInstanceConfigsCallable()
    
    
    public final UnaryCallable<DeletePerInstanceConfigsInstanceGroupManagerRequest,Operation> deletePerInstanceConfigsCallable()

Deletes selected per-instance configurations for the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       DeletePerInstanceConfigsInstanceGroupManagerRequest request =
           DeletePerInstanceConfigsInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersDeletePerInstanceConfigsReqResource(
                   InstanceGroupManagersDeletePerInstanceConfigsReq.newBuilder().build())
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.deletePerInstanceConfigsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeletePerInstanceConfigsInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deletePerInstanceConfigsOperationCallable()
    
    
    public final OperationCallable<DeletePerInstanceConfigsInstanceGroupManagerRequest,Operation,Operation> deletePerInstanceConfigsOperationCallable()

Deletes selected per-instance configurations for the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       DeletePerInstanceConfigsInstanceGroupManagerRequest request =
           DeletePerInstanceConfigsInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersDeletePerInstanceConfigsReqResource(
                   InstanceGroupManagersDeletePerInstanceConfigsReq.newBuilder().build())
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient
               .deletePerInstanceConfigsOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeletePerInstanceConfigsInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetInstanceGroupManagerRequest request)
    
    
    public final InstanceGroupManager get(GetInstanceGroupManagerRequest request)

Returns all of the details about the specified managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       GetInstanceGroupManagerRequest request =
           GetInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       InstanceGroupManager response = instanceGroupManagersClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManager)` |   
  
### get(String project, String zone, String instanceGroupManager)
    
    
    public final InstanceGroupManager get(String project, String zone, String instanceGroupManager)

Returns all of the details about the specified managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManager response =
           instanceGroupManagersClient.get(project, zone, instanceGroupManager);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManager)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetInstanceGroupManagerRequest,InstanceGroupManager> getCallable()

Returns all of the details about the specified managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       GetInstanceGroupManagerRequest request =
           GetInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<InstanceGroupManager> future =
           instanceGroupManagersClient.getCallable().futureCall(request);
       // Do something.
       InstanceGroupManager response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceGroupManagerRequest),[InstanceGroupManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManager)>` |   
  
### getSettings()
    
    
    public final @Nullable InstanceGroupManagersSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.InstanceGroupManagersSettings` |   
  
### getStub()
    
    
    public InstanceGroupManagersStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstanceGroupManagersStub)` |   
  
### insertAsync(InsertInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertInstanceGroupManagerRequest request)

Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with thelistmanagedinstances method.

A managed instance group can have up to 1000 VM instances per group. Please contact Cloud Support if you need an increase in this limit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       InsertInstanceGroupManagerRequest request =
           InsertInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManagerResource(InstanceGroupManager.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String zone, InstanceGroupManager instanceGroupManagerResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String zone, InstanceGroupManager instanceGroupManagerResource)

Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with thelistmanagedinstances method.

A managed instance group can have up to 1000 VM instances per group. Please contact Cloud Support if you need an increase in this limit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       InstanceGroupManager instanceGroupManagerResource = InstanceGroupManager.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .insertAsync(project, zone, instanceGroupManagerResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where you want to create the managed instance group.  
`instanceGroupManagerResource` | `[InstanceGroupManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManager)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertInstanceGroupManagerRequest,Operation> insertCallable()

Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with thelistmanagedinstances method.

A managed instance group can have up to 1000 VM instances per group. Please contact Cloud Support if you need an increase in this limit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       InsertInstanceGroupManagerRequest request =
           InsertInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManagerResource(InstanceGroupManager.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertInstanceGroupManagerRequest,Operation,Operation> insertOperationCallable()

Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with thelistmanagedinstances method.

A managed instance group can have up to 1000 VM instances per group. Please contact Cloud Support if you need an increase in this limit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       InsertInstanceGroupManagerRequest request =
           InsertInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManagerResource(InstanceGroupManager.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListInstanceGroupManagersRequest request)
    
    
    public final InstanceGroupManagersClient.ListPagedResponse list(ListInstanceGroupManagersRequest request)

Retrieves a list of managed instance groups that are contained within the specified project and zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ListInstanceGroupManagersRequest request =
           ListInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (InstanceGroupManager element : instanceGroupManagersClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstanceGroupManagersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final InstanceGroupManagersClient.ListPagedResponse list(String project, String zone)

Retrieves a list of managed instance groups that are contained within the specified project and zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (InstanceGroupManager element :
           instanceGroupManagersClient.list(project, zone).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListInstanceGroupManagersRequest,InstanceGroupManagerList> listCallable()

Retrieves a list of managed instance groups that are contained within the specified project and zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ListInstanceGroupManagersRequest request =
           ListInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         InstanceGroupManagerList response =
             instanceGroupManagersClient.listCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstanceGroupManagersRequest),[InstanceGroupManagerList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagerList)>` |   
  
### listErrors(ListErrorsInstanceGroupManagersRequest request)
    
    
    public final InstanceGroupManagersClient.ListErrorsPagedResponse listErrors(ListErrorsInstanceGroupManagersRequest request)

Lists all errors thrown by actions on instances for a given managed instance group. The filter and orderBy query parameters are not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ListErrorsInstanceGroupManagersRequest request =
           ListErrorsInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (InstanceManagedByIgmError element :
           instanceGroupManagersClient.listErrors(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListErrorsInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListErrorsInstanceGroupManagersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient.ListErrorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.ListErrorsPagedResponse)` |   
  
### listErrors(String project, String zone, String instanceGroupManager)
    
    
    public final InstanceGroupManagersClient.ListErrorsPagedResponse listErrors(String project, String zone, String instanceGroupManager)

Lists all errors thrown by actions on instances for a given managed instance group. The filter and orderBy query parameters are not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       for (InstanceManagedByIgmError element :
           instanceGroupManagersClient
               .listErrors(project, zone, instanceGroupManager)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located. It should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. It must be a string that meets the requirements in RFC1035, or an unsigned long integer: must match regexp pattern: (?:[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?)|1-9{0,19}.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient.ListErrorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.ListErrorsPagedResponse)` |   
  
### listErrorsCallable()
    
    
    public final UnaryCallable<ListErrorsInstanceGroupManagersRequest,InstanceGroupManagersListErrorsResponse> listErrorsCallable()

Lists all errors thrown by actions on instances for a given managed instance group. The filter and orderBy query parameters are not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ListErrorsInstanceGroupManagersRequest request =
           ListErrorsInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         InstanceGroupManagersListErrorsResponse response =
             instanceGroupManagersClient.listErrorsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListErrorsInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListErrorsInstanceGroupManagersRequest),[InstanceGroupManagersListErrorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersListErrorsResponse)>` |   
  
### listErrorsPagedCallable()
    
    
    public final UnaryCallable<ListErrorsInstanceGroupManagersRequest,InstanceGroupManagersClient.ListErrorsPagedResponse> listErrorsPagedCallable()

Lists all errors thrown by actions on instances for a given managed instance group. The filter and orderBy query parameters are not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ListErrorsInstanceGroupManagersRequest request =
           ListErrorsInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<InstanceManagedByIgmError> future =
           instanceGroupManagersClient.listErrorsPagedCallable().futureCall(request);
       // Do something.
       for (InstanceManagedByIgmError element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListErrorsInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListErrorsInstanceGroupManagersRequest),[ListErrorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.ListErrorsPagedResponse)>` |   
  
### listManagedInstances(ListManagedInstancesInstanceGroupManagersRequest request)
    
    
    public final InstanceGroupManagersClient.ListManagedInstancesPagedResponse listManagedInstances(ListManagedInstancesInstanceGroupManagersRequest request)

Lists all of the instances in the managed instance group. Each instance in the list has a currentAction, which indicates the action that the managed instance group is performing on the instance. For example, if the group is still creating an instance, the currentAction is CREATING. If a previous action failed, the list displays the errors for that failed action. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ListManagedInstancesInstanceGroupManagersRequest request =
           ListManagedInstancesInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (ManagedInstance element :
           instanceGroupManagersClient.listManagedInstances(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListManagedInstancesInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListManagedInstancesInstanceGroupManagersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient.ListManagedInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.ListManagedInstancesPagedResponse)` |   
  
### listManagedInstances(String project, String zone, String instanceGroupManager)
    
    
    public final InstanceGroupManagersClient.ListManagedInstancesPagedResponse listManagedInstances(String project, String zone, String instanceGroupManager)

Lists all of the instances in the managed instance group. Each instance in the list has a currentAction, which indicates the action that the managed instance group is performing on the instance. For example, if the group is still creating an instance, the currentAction is CREATING. If a previous action failed, the list displays the errors for that failed action. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       for (ManagedInstance element :
           instanceGroupManagersClient
               .listManagedInstances(project, zone, instanceGroupManager)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient.ListManagedInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.ListManagedInstancesPagedResponse)` |   
  
### listManagedInstancesCallable()
    
    
    public final UnaryCallable<ListManagedInstancesInstanceGroupManagersRequest,InstanceGroupManagersListManagedInstancesResponse> listManagedInstancesCallable()

Lists all of the instances in the managed instance group. Each instance in the list has a currentAction, which indicates the action that the managed instance group is performing on the instance. For example, if the group is still creating an instance, the currentAction is CREATING. If a previous action failed, the list displays the errors for that failed action. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ListManagedInstancesInstanceGroupManagersRequest request =
           ListManagedInstancesInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         InstanceGroupManagersListManagedInstancesResponse response =
             instanceGroupManagersClient.listManagedInstancesCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListManagedInstancesInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListManagedInstancesInstanceGroupManagersRequest),[InstanceGroupManagersListManagedInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersListManagedInstancesResponse)>` |   
  
### listManagedInstancesPagedCallable()
    
    
    public final UnaryCallable<ListManagedInstancesInstanceGroupManagersRequest,InstanceGroupManagersClient.ListManagedInstancesPagedResponse> listManagedInstancesPagedCallable()

Lists all of the instances in the managed instance group. Each instance in the list has a currentAction, which indicates the action that the managed instance group is performing on the instance. For example, if the group is still creating an instance, the currentAction is CREATING. If a previous action failed, the list displays the errors for that failed action. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ListManagedInstancesInstanceGroupManagersRequest request =
           ListManagedInstancesInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<ManagedInstance> future =
           instanceGroupManagersClient.listManagedInstancesPagedCallable().futureCall(request);
       // Do something.
       for (ManagedInstance element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListManagedInstancesInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListManagedInstancesInstanceGroupManagersRequest),[ListManagedInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.ListManagedInstancesPagedResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListInstanceGroupManagersRequest,InstanceGroupManagersClient.ListPagedResponse> listPagedCallable()

Retrieves a list of managed instance groups that are contained within the specified project and zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ListInstanceGroupManagersRequest request =
           ListInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<InstanceGroupManager> future =
           instanceGroupManagersClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InstanceGroupManager element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstanceGroupManagersRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.ListPagedResponse)>` |   
  
### listPerInstanceConfigs(ListPerInstanceConfigsInstanceGroupManagersRequest request)
    
    
    public final InstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse listPerInstanceConfigs(ListPerInstanceConfigsInstanceGroupManagersRequest request)

Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ListPerInstanceConfigsInstanceGroupManagersRequest request =
           ListPerInstanceConfigsInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (PerInstanceConfig element :
           instanceGroupManagersClient.listPerInstanceConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPerInstanceConfigsInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPerInstanceConfigsInstanceGroupManagersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse)` |   
  
### listPerInstanceConfigs(String project, String zone, String instanceGroupManager)
    
    
    public final InstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse listPerInstanceConfigs(String project, String zone, String instanceGroupManager)

Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       for (PerInstanceConfig element :
           instanceGroupManagersClient
               .listPerInstanceConfigs(project, zone, instanceGroupManager)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located. It should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. It should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse)` |   
  
### listPerInstanceConfigsCallable()
    
    
    public final UnaryCallable<ListPerInstanceConfigsInstanceGroupManagersRequest,InstanceGroupManagersListPerInstanceConfigsResp> listPerInstanceConfigsCallable()

Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ListPerInstanceConfigsInstanceGroupManagersRequest request =
           ListPerInstanceConfigsInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         InstanceGroupManagersListPerInstanceConfigsResp response =
             instanceGroupManagersClient.listPerInstanceConfigsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPerInstanceConfigsInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPerInstanceConfigsInstanceGroupManagersRequest),[InstanceGroupManagersListPerInstanceConfigsResp](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersListPerInstanceConfigsResp)>` |   
  
### listPerInstanceConfigsPagedCallable()
    
    
    public final UnaryCallable<ListPerInstanceConfigsInstanceGroupManagersRequest,InstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse> listPerInstanceConfigsPagedCallable()

Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ListPerInstanceConfigsInstanceGroupManagersRequest request =
           ListPerInstanceConfigsInstanceGroupManagersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<PerInstanceConfig> future =
           instanceGroupManagersClient.listPerInstanceConfigsPagedCallable().futureCall(request);
       // Do something.
       for (PerInstanceConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPerInstanceConfigsInstanceGroupManagersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPerInstanceConfigsInstanceGroupManagersRequest),[ListPerInstanceConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersClient.ListPerInstanceConfigsPagedResponse)>` |   
  
### patchAsync(PatchInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchInstanceGroupManagerRequest request)

Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with thelistManagedInstances method. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       PatchInstanceGroupManagerRequest request =
           PatchInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagerResource(InstanceGroupManager.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String zone, String instanceGroupManager, InstanceGroupManager instanceGroupManagerResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String zone, String instanceGroupManager, InstanceGroupManager instanceGroupManagerResource)

Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with thelistManagedInstances method. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManager instanceGroupManagerResource = InstanceGroupManager.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .patchAsync(project, zone, instanceGroupManager, instanceGroupManagerResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where you want to create the managed instance group.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the instance group manager.  
`instanceGroupManagerResource` | `[InstanceGroupManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManager)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchInstanceGroupManagerRequest,Operation> patchCallable()

Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with thelistManagedInstances method. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       PatchInstanceGroupManagerRequest request =
           PatchInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagerResource(InstanceGroupManager.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instanceGroupManagersClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchInstanceGroupManagerRequest,Operation,Operation> patchOperationCallable()

Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with thelistManagedInstances method. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, seeUpdating instances in a MIG.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       PatchInstanceGroupManagerRequest request =
           PatchInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagerResource(InstanceGroupManager.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchPerInstanceConfigsAsync(PatchPerInstanceConfigsInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchPerInstanceConfigsAsync(PatchPerInstanceConfigsInstanceGroupManagerRequest request)

Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       PatchPerInstanceConfigsInstanceGroupManagerRequest request =
           PatchPerInstanceConfigsInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersPatchPerInstanceConfigsReqResource(
                   InstanceGroupManagersPatchPerInstanceConfigsReq.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.patchPerInstanceConfigsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchPerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPerInstanceConfigsInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchPerInstanceConfigsAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersPatchPerInstanceConfigsReq instanceGroupManagersPatchPerInstanceConfigsReqResource)
    
    
    public final OperationFuture<Operation,Operation> patchPerInstanceConfigsAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersPatchPerInstanceConfigsReq instanceGroupManagersPatchPerInstanceConfigsReqResource)

Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersPatchPerInstanceConfigsReq
           instanceGroupManagersPatchPerInstanceConfigsReqResource =
               InstanceGroupManagersPatchPerInstanceConfigsReq.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .patchPerInstanceConfigsAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersPatchPerInstanceConfigsReqResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located. It should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. It should conform to RFC1035.  
`instanceGroupManagersPatchPerInstanceConfigsReqResource` | `[InstanceGroupManagersPatchPerInstanceConfigsReq](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersPatchPerInstanceConfigsReq)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchPerInstanceConfigsCallable()
    
    
    public final UnaryCallable<PatchPerInstanceConfigsInstanceGroupManagerRequest,Operation> patchPerInstanceConfigsCallable()

Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       PatchPerInstanceConfigsInstanceGroupManagerRequest request =
           PatchPerInstanceConfigsInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersPatchPerInstanceConfigsReqResource(
                   InstanceGroupManagersPatchPerInstanceConfigsReq.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.patchPerInstanceConfigsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchPerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPerInstanceConfigsInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchPerInstanceConfigsOperationCallable()
    
    
    public final OperationCallable<PatchPerInstanceConfigsInstanceGroupManagerRequest,Operation,Operation> patchPerInstanceConfigsOperationCallable()

Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       PatchPerInstanceConfigsInstanceGroupManagerRequest request =
           PatchPerInstanceConfigsInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersPatchPerInstanceConfigsReqResource(
                   InstanceGroupManagersPatchPerInstanceConfigsReq.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient
               .patchPerInstanceConfigsOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchPerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPerInstanceConfigsInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### recreateInstancesAsync(RecreateInstancesInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> recreateInstancesAsync(RecreateInstancesInstanceGroupManagerRequest request)

Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking itscurrentAction field; for more information, see Checking the status of managed instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       RecreateInstancesInstanceGroupManagerRequest request =
           RecreateInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersRecreateInstancesRequestResource(
                   InstanceGroupManagersRecreateInstancesRequest.newBuilder().build())
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.recreateInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RecreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RecreateInstancesInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### recreateInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersRecreateInstancesRequest instanceGroupManagersRecreateInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> recreateInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersRecreateInstancesRequest instanceGroupManagersRecreateInstancesRequestResource)

Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking itscurrentAction field; for more information, see Checking the status of managed instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersRecreateInstancesRequest
           instanceGroupManagersRecreateInstancesRequestResource =
               InstanceGroupManagersRecreateInstancesRequest.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .recreateInstancesAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersRecreateInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
`instanceGroupManagersRecreateInstancesRequestResource` | `[InstanceGroupManagersRecreateInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersRecreateInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### recreateInstancesCallable()
    
    
    public final UnaryCallable<RecreateInstancesInstanceGroupManagerRequest,Operation> recreateInstancesCallable()

Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking itscurrentAction field; for more information, see Checking the status of managed instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       RecreateInstancesInstanceGroupManagerRequest request =
           RecreateInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersRecreateInstancesRequestResource(
                   InstanceGroupManagersRecreateInstancesRequest.newBuilder().build())
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.recreateInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RecreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RecreateInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### recreateInstancesOperationCallable()
    
    
    public final OperationCallable<RecreateInstancesInstanceGroupManagerRequest,Operation,Operation> recreateInstancesOperationCallable()

Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking itscurrentAction field; for more information, see Checking the status of managed instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

You can specify a maximum of 1000 instances with this method per request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       RecreateInstancesInstanceGroupManagerRequest request =
           RecreateInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersRecreateInstancesRequestResource(
                   InstanceGroupManagersRecreateInstancesRequest.newBuilder().build())
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.recreateInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RecreateInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RecreateInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeAsync(ResizeInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> resizeAsync(ResizeInstanceGroupManagerRequest request)

Resizes the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes instances. The resize operation is markedDONE when the resize actions are scheduled even if the group has not yet added or deleted any instances. You must separately verify the status of the creating or deleting actions with thelistmanagedinstances method.

When resizing down, the instance group arbitrarily chooses the order in which VMs are deleted. The group takes into account some VM attributes when making the selection including:

\+ The status of the VM instance. + The health of the VM instance. + The instance template version the VM is based on. + For regional managed instance groups, the location of the VM instance.

This list is subject to change.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ResizeInstanceGroupManagerRequest request =
           ResizeInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSize(3530753)
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.resizeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResizeInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeAsync(String project, String zone, String instanceGroupManager, int size)
    
    
    public final OperationFuture<Operation,Operation> resizeAsync(String project, String zone, String instanceGroupManager, int size)

Resizes the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes instances. The resize operation is markedDONE when the resize actions are scheduled even if the group has not yet added or deleted any instances. You must separately verify the status of the creating or deleting actions with thelistmanagedinstances method.

When resizing down, the instance group arbitrarily chooses the order in which VMs are deleted. The group takes into account some VM attributes when making the selection including:

\+ The status of the VM instance. + The health of the VM instance. + The instance template version the VM is based on. + For regional managed instance groups, the location of the VM instance.

This list is subject to change.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       int size = 3530753;
       Operation response =
           instanceGroupManagersClient.resizeAsync(project, zone, instanceGroupManager, size).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
`size` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The number of running instances that the managed instance group should maintain at any given time. The group automatically adds or removes instances to maintain the number of instances specified by this parameter.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeCallable()
    
    
    public final UnaryCallable<ResizeInstanceGroupManagerRequest,Operation> resizeCallable()

Resizes the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes instances. The resize operation is markedDONE when the resize actions are scheduled even if the group has not yet added or deleted any instances. You must separately verify the status of the creating or deleting actions with thelistmanagedinstances method.

When resizing down, the instance group arbitrarily chooses the order in which VMs are deleted. The group takes into account some VM attributes when making the selection including:

\+ The status of the VM instance. + The health of the VM instance. + The instance template version the VM is based on. + For regional managed instance groups, the location of the VM instance.

This list is subject to change.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ResizeInstanceGroupManagerRequest request =
           ResizeInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSize(3530753)
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.resizeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResizeInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeOperationCallable()
    
    
    public final OperationCallable<ResizeInstanceGroupManagerRequest,Operation,Operation> resizeOperationCallable()

Resizes the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes instances. The resize operation is markedDONE when the resize actions are scheduled even if the group has not yet added or deleted any instances. You must separately verify the status of the creating or deleting actions with thelistmanagedinstances method.

When resizing down, the instance group arbitrarily chooses the order in which VMs are deleted. The group takes into account some VM attributes when making the selection including:

\+ The status of the VM instance. + The health of the VM instance. + The instance template version the VM is based on. + For regional managed instance groups, the location of the VM instance.

This list is subject to change.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ResizeInstanceGroupManagerRequest request =
           ResizeInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSize(3530753)
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.resizeOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ResizeInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeInstancesAsync(ResumeInstancesInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> resumeInstancesAsync(ResumeInstancesInstanceGroupManagerRequest request)

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ResumeInstancesInstanceGroupManagerRequest request =
           ResumeInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersResumeInstancesRequestResource(
                   InstanceGroupManagersResumeInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.resumeInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResumeInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeInstancesInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersResumeInstancesRequest instanceGroupManagersResumeInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> resumeInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersResumeInstancesRequest instanceGroupManagersResumeInstancesRequestResource)

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersResumeInstancesRequest
           instanceGroupManagersResumeInstancesRequestResource =
               InstanceGroupManagersResumeInstancesRequest.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .resumeInstancesAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersResumeInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
`instanceGroupManagersResumeInstancesRequestResource` | `[InstanceGroupManagersResumeInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersResumeInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeInstancesCallable()
    
    
    public final UnaryCallable<ResumeInstancesInstanceGroupManagerRequest,Operation> resumeInstancesCallable()

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ResumeInstancesInstanceGroupManagerRequest request =
           ResumeInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersResumeInstancesRequestResource(
                   InstanceGroupManagersResumeInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.resumeInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResumeInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeInstancesOperationCallable()
    
    
    public final OperationCallable<ResumeInstancesInstanceGroupManagerRequest,Operation,Operation> resumeInstancesOperationCallable()

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       ResumeInstancesInstanceGroupManagerRequest request =
           ResumeInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersResumeInstancesRequestResource(
                   InstanceGroupManagersResumeInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.resumeInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ResumeInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setInstanceTemplateAsync(SetInstanceTemplateInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> setInstanceTemplateAsync(SetInstanceTemplateInstanceGroupManagerRequest request)

Specifies the instance template to use when creating new instances in this group. The templates for existing instances in the group do not change unless you run recreateInstances, runapplyUpdatesToInstances, or set the group'supdatePolicy.type to PROACTIVE.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       SetInstanceTemplateInstanceGroupManagerRequest request =
           SetInstanceTemplateInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersSetInstanceTemplateRequestResource(
                   InstanceGroupManagersSetInstanceTemplateRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.setInstanceTemplateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetInstanceTemplateInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetInstanceTemplateInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setInstanceTemplateAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersSetInstanceTemplateRequest instanceGroupManagersSetInstanceTemplateRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setInstanceTemplateAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersSetInstanceTemplateRequest instanceGroupManagersSetInstanceTemplateRequestResource)

Specifies the instance template to use when creating new instances in this group. The templates for existing instances in the group do not change unless you run recreateInstances, runapplyUpdatesToInstances, or set the group'supdatePolicy.type to PROACTIVE.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersSetInstanceTemplateRequest
           instanceGroupManagersSetInstanceTemplateRequestResource =
               InstanceGroupManagersSetInstanceTemplateRequest.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .setInstanceTemplateAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersSetInstanceTemplateRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
`instanceGroupManagersSetInstanceTemplateRequestResource` | `[InstanceGroupManagersSetInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersSetInstanceTemplateRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setInstanceTemplateCallable()
    
    
    public final UnaryCallable<SetInstanceTemplateInstanceGroupManagerRequest,Operation> setInstanceTemplateCallable()

Specifies the instance template to use when creating new instances in this group. The templates for existing instances in the group do not change unless you run recreateInstances, runapplyUpdatesToInstances, or set the group'supdatePolicy.type to PROACTIVE.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       SetInstanceTemplateInstanceGroupManagerRequest request =
           SetInstanceTemplateInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersSetInstanceTemplateRequestResource(
                   InstanceGroupManagersSetInstanceTemplateRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.setInstanceTemplateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetInstanceTemplateInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetInstanceTemplateInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setInstanceTemplateOperationCallable()
    
    
    public final OperationCallable<SetInstanceTemplateInstanceGroupManagerRequest,Operation,Operation> setInstanceTemplateOperationCallable()

Specifies the instance template to use when creating new instances in this group. The templates for existing instances in the group do not change unless you run recreateInstances, runapplyUpdatesToInstances, or set the group'supdatePolicy.type to PROACTIVE.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       SetInstanceTemplateInstanceGroupManagerRequest request =
           SetInstanceTemplateInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersSetInstanceTemplateRequestResource(
                   InstanceGroupManagersSetInstanceTemplateRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.setInstanceTemplateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetInstanceTemplateInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetInstanceTemplateInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetPoolsAsync(SetTargetPoolsInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> setTargetPoolsAsync(SetTargetPoolsInstanceGroupManagerRequest request)

Modifies the target pools to which all instances in this managed instance group are assigned. The target pools automatically apply to all of the instances in the managed instance group. This operation is markedDONE when you make the request even if the instances have not yet been added to their target pools. The change might take some time to apply to all of the instances in the group depending on the size of the group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       SetTargetPoolsInstanceGroupManagerRequest request =
           SetTargetPoolsInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersSetTargetPoolsRequestResource(
                   InstanceGroupManagersSetTargetPoolsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.setTargetPoolsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetTargetPoolsInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTargetPoolsInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetPoolsAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersSetTargetPoolsRequest instanceGroupManagersSetTargetPoolsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setTargetPoolsAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersSetTargetPoolsRequest instanceGroupManagersSetTargetPoolsRequestResource)

Modifies the target pools to which all instances in this managed instance group are assigned. The target pools automatically apply to all of the instances in the managed instance group. This operation is markedDONE when you make the request even if the instances have not yet been added to their target pools. The change might take some time to apply to all of the instances in the group depending on the size of the group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersSetTargetPoolsRequest
           instanceGroupManagersSetTargetPoolsRequestResource =
               InstanceGroupManagersSetTargetPoolsRequest.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .setTargetPoolsAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersSetTargetPoolsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
`instanceGroupManagersSetTargetPoolsRequestResource` | `[InstanceGroupManagersSetTargetPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersSetTargetPoolsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetPoolsCallable()
    
    
    public final UnaryCallable<SetTargetPoolsInstanceGroupManagerRequest,Operation> setTargetPoolsCallable()

Modifies the target pools to which all instances in this managed instance group are assigned. The target pools automatically apply to all of the instances in the managed instance group. This operation is markedDONE when you make the request even if the instances have not yet been added to their target pools. The change might take some time to apply to all of the instances in the group depending on the size of the group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       SetTargetPoolsInstanceGroupManagerRequest request =
           SetTargetPoolsInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersSetTargetPoolsRequestResource(
                   InstanceGroupManagersSetTargetPoolsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.setTargetPoolsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetTargetPoolsInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTargetPoolsInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTargetPoolsOperationCallable()
    
    
    public final OperationCallable<SetTargetPoolsInstanceGroupManagerRequest,Operation,Operation> setTargetPoolsOperationCallable()

Modifies the target pools to which all instances in this managed instance group are assigned. The target pools automatically apply to all of the instances in the managed instance group. This operation is markedDONE when you make the request even if the instances have not yet been added to their target pools. The change might take some time to apply to all of the instances in the group depending on the size of the group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       SetTargetPoolsInstanceGroupManagerRequest request =
           SetTargetPoolsInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersSetTargetPoolsRequestResource(
                   InstanceGroupManagersSetTargetPoolsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.setTargetPoolsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetTargetPoolsInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTargetPoolsInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### startInstancesAsync(StartInstancesInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> startInstancesAsync(StartInstancesInstanceGroupManagerRequest request)

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       StartInstancesInstanceGroupManagerRequest request =
           StartInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersStartInstancesRequestResource(
                   InstanceGroupManagersStartInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.startInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstancesInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersStartInstancesRequest instanceGroupManagersStartInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> startInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersStartInstancesRequest instanceGroupManagersStartInstancesRequestResource)

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersStartInstancesRequest
           instanceGroupManagersStartInstancesRequestResource =
               InstanceGroupManagersStartInstancesRequest.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .startInstancesAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersStartInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
`instanceGroupManagersStartInstancesRequestResource` | `[InstanceGroupManagersStartInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersStartInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startInstancesCallable()
    
    
    public final UnaryCallable<StartInstancesInstanceGroupManagerRequest,Operation> startInstancesCallable()

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       StartInstancesInstanceGroupManagerRequest request =
           StartInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersStartInstancesRequestResource(
                   InstanceGroupManagersStartInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.startInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startInstancesOperationCallable()
    
    
    public final OperationCallable<StartInstancesInstanceGroupManagerRequest,Operation,Operation> startInstancesOperationCallable()

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       StartInstancesInstanceGroupManagerRequest request =
           StartInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersStartInstancesRequestResource(
                   InstanceGroupManagersStartInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.startInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StartInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopInstancesAsync(StopInstancesInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> stopInstancesAsync(StopInstancesInstanceGroupManagerRequest request)

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       StopInstancesInstanceGroupManagerRequest request =
           StopInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersStopInstancesRequestResource(
                   InstanceGroupManagersStopInstancesRequest.newBuilder().build())
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.stopInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstancesInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersStopInstancesRequest instanceGroupManagersStopInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> stopInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersStopInstancesRequest instanceGroupManagersStopInstancesRequestResource)

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersStopInstancesRequest instanceGroupManagersStopInstancesRequestResource =
           InstanceGroupManagersStopInstancesRequest.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .stopInstancesAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersStopInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
`instanceGroupManagersStopInstancesRequestResource` | `[InstanceGroupManagersStopInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersStopInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopInstancesCallable()
    
    
    public final UnaryCallable<StopInstancesInstanceGroupManagerRequest,Operation> stopInstancesCallable()

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       StopInstancesInstanceGroupManagerRequest request =
           StopInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersStopInstancesRequestResource(
                   InstanceGroupManagersStopInstancesRequest.newBuilder().build())
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.stopInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StopInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopInstancesOperationCallable()
    
    
    public final OperationCallable<StopInstancesInstanceGroupManagerRequest,Operation,Operation> stopInstancesOperationCallable()

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       StopInstancesInstanceGroupManagerRequest request =
           StopInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersStopInstancesRequestResource(
                   InstanceGroupManagersStopInstancesRequest.newBuilder().build())
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.stopInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StopInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendInstancesAsync(SuspendInstancesInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> suspendInstancesAsync(SuspendInstancesInstanceGroupManagerRequest request)

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       SuspendInstancesInstanceGroupManagerRequest request =
           SuspendInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersSuspendInstancesRequestResource(
                   InstanceGroupManagersSuspendInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.suspendInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SuspendInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SuspendInstancesInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersSuspendInstancesRequest instanceGroupManagersSuspendInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> suspendInstancesAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersSuspendInstancesRequest instanceGroupManagersSuspendInstancesRequestResource)

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersSuspendInstancesRequest
           instanceGroupManagersSuspendInstancesRequestResource =
               InstanceGroupManagersSuspendInstancesRequest.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .suspendInstancesAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersSuspendInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group.  
`instanceGroupManagersSuspendInstancesRequestResource` | `[InstanceGroupManagersSuspendInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersSuspendInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendInstancesCallable()
    
    
    public final UnaryCallable<SuspendInstancesInstanceGroupManagerRequest,Operation> suspendInstancesCallable()

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       SuspendInstancesInstanceGroupManagerRequest request =
           SuspendInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersSuspendInstancesRequestResource(
                   InstanceGroupManagersSuspendInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.suspendInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SuspendInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SuspendInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendInstancesOperationCallable()
    
    
    public final OperationCallable<SuspendInstancesInstanceGroupManagerRequest,Operation,Operation> suspendInstancesOperationCallable()

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
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       SuspendInstancesInstanceGroupManagerRequest request =
           SuspendInstancesInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersSuspendInstancesRequestResource(
                   InstanceGroupManagersSuspendInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient.suspendInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SuspendInstancesInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SuspendInstancesInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updatePerInstanceConfigsAsync(UpdatePerInstanceConfigsInstanceGroupManagerRequest request)
    
    
    public final OperationFuture<Operation,Operation> updatePerInstanceConfigsAsync(UpdatePerInstanceConfigsInstanceGroupManagerRequest request)

Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       UpdatePerInstanceConfigsInstanceGroupManagerRequest request =
           UpdatePerInstanceConfigsInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersUpdatePerInstanceConfigsReqResource(
                   InstanceGroupManagersUpdatePerInstanceConfigsReq.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupManagersClient.updatePerInstanceConfigsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdatePerInstanceConfigsInstanceGroupManagerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updatePerInstanceConfigsAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersUpdatePerInstanceConfigsReq instanceGroupManagersUpdatePerInstanceConfigsReqResource)
    
    
    public final OperationFuture<Operation,Operation> updatePerInstanceConfigsAsync(String project, String zone, String instanceGroupManager, InstanceGroupManagersUpdatePerInstanceConfigsReq instanceGroupManagersUpdatePerInstanceConfigsReqResource)

Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagersUpdatePerInstanceConfigsReq
           instanceGroupManagersUpdatePerInstanceConfigsReqResource =
               InstanceGroupManagersUpdatePerInstanceConfigsReq.newBuilder().build();
       Operation response =
           instanceGroupManagersClient
               .updatePerInstanceConfigsAsync(
                   project,
                   zone,
                   instanceGroupManager,
                   instanceGroupManagersUpdatePerInstanceConfigsReqResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the managed instance group is located. It should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. It should conform to RFC1035.  
`instanceGroupManagersUpdatePerInstanceConfigsReqResource` | `[InstanceGroupManagersUpdatePerInstanceConfigsReq](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagersUpdatePerInstanceConfigsReq)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updatePerInstanceConfigsCallable()
    
    
    public final UnaryCallable<UpdatePerInstanceConfigsInstanceGroupManagerRequest,Operation> updatePerInstanceConfigsCallable()

Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       UpdatePerInstanceConfigsInstanceGroupManagerRequest request =
           UpdatePerInstanceConfigsInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersUpdatePerInstanceConfigsReqResource(
                   InstanceGroupManagersUpdatePerInstanceConfigsReq.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupManagersClient.updatePerInstanceConfigsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdatePerInstanceConfigsInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updatePerInstanceConfigsOperationCallable()
    
    
    public final OperationCallable<UpdatePerInstanceConfigsInstanceGroupManagerRequest,Operation,Operation> updatePerInstanceConfigsOperationCallable()

Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupManagersClient instanceGroupManagersClient =
         InstanceGroupManagersClient.create()) {
       UpdatePerInstanceConfigsInstanceGroupManagerRequest request =
           UpdatePerInstanceConfigsInstanceGroupManagerRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagersUpdatePerInstanceConfigsReqResource(
                   InstanceGroupManagersUpdatePerInstanceConfigsReq.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupManagersClient
               .updatePerInstanceConfigsOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePerInstanceConfigsInstanceGroupManagerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdatePerInstanceConfigsInstanceGroupManagerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
