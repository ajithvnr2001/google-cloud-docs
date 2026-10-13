---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient
title: Class InstancesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:46.561222+00:00
---

# Class InstancesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InstancesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/InstancesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The Instances API.

This client uses Instances version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Instance response = instancesClient.get(project, zone, instance);
     }
     

Note: close() needs to be called on the InstancesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddAccessConfig |  Adds an access config to an instance's network interface. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addAccessConfigAsync(AddAccessConfigInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addAccessConfigAsync(String project, String zone, String instance, String networkInterface, AccessConfig accessConfigResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addAccessConfigOperationCallable() 
  * addAccessConfigCallable() 

  
AddNetworkInterface |  Adds one dynamic network interface to an active instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addNetworkInterfaceAsync(AddNetworkInterfaceInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addNetworkInterfaceAsync(String project, String zone, String instance, NetworkInterface networkInterfaceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addNetworkInterfaceOperationCallable() 
  * addNetworkInterfaceCallable() 

  
AddResourcePolicies |  Adds existing resource policies to an instance. You can only add one policy right now which will be applied to this instance for scheduling live migrations. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addResourcePoliciesAsync(AddResourcePoliciesInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addResourcePoliciesAsync(String project, String zone, String instance, InstancesAddResourcePoliciesRequest instancesAddResourcePoliciesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addResourcePoliciesOperationCallable() 
  * addResourcePoliciesCallable() 

  
AggregatedList |  Retrieves an aggregated list of all of the instances in your project across all regions and zones.  The performance of this method degrades when a filter is specified on a project that has a very large number of instances.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListInstancesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
AttachDisk |  Attaches an existing Disk resource to an instance. You must first create the disk before you can attach it. It is not possible to create and attach a disk at the same time. For more information, readAdding a persistent disk to your instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * attachDiskAsync(AttachDiskInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * attachDiskAsync(String project, String zone, String instance, AttachedDisk attachedDiskResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * attachDiskOperationCallable() 
  * attachDiskCallable() 

  
BulkInsert |  Creates multiple instances. Count specifies the number of instances to create. For more information, seeAbout bulk creation of VMs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * bulkInsertAsync(BulkInsertInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * bulkInsertAsync(String project, String zone, BulkInsertInstanceResource bulkInsertInstanceResourceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * bulkInsertOperationCallable() 
  * bulkInsertCallable() 

  
Delete |  Deletes the specified Instance resource. For more information, seeDeleting an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
DeleteAccessConfig |  Deletes an access config from an instance's network interface. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAccessConfigAsync(DeleteAccessConfigInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAccessConfigAsync(String project, String zone, String instance, String accessConfig, String networkInterface) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAccessConfigOperationCallable() 
  * deleteAccessConfigCallable() 

  
DeleteNetworkInterface |  Deletes one dynamic network interface from an active instance. InstancesDeleteNetworkInterfaceRequest indicates: - instance from which to delete, using project+zone+resource_id fields; - dynamic network interface to be deleted, using network_interface_name field; |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNetworkInterfaceAsync(DeleteNetworkInterfaceInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteNetworkInterfaceAsync(String project, String zone, String instance, String networkInterfaceName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNetworkInterfaceOperationCallable() 
  * deleteNetworkInterfaceCallable() 

  
DetachDisk |  Detaches a disk from an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * detachDiskAsync(DetachDiskInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * detachDiskAsync(String project, String zone, String instance, String deviceName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * detachDiskOperationCallable() 
  * detachDiskCallable() 

  
Get |  Returns the specified Instance resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetEffectiveFirewalls |  Returns effective firewalls applied to an interface of the instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEffectiveFirewalls(GetEffectiveFirewallsInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEffectiveFirewalls(String project, String zone, String instance, String networkInterface) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEffectiveFirewallsCallable() 

  
GetGuestAttributes |  Returns the specified guest attributes entry. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGuestAttributes(GetGuestAttributesInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGuestAttributes(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGuestAttributesCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String zone, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
GetScreenshot |  Returns the screenshot from the specified instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getScreenshot(GetScreenshotInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getScreenshot(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getScreenshotCallable() 

  
GetSerialPortOutput |  Returns the last 1 MB of serial port output from the specified instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSerialPortOutput(GetSerialPortOutputInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSerialPortOutput(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSerialPortOutputCallable() 

  
GetShieldedInstanceIdentity |  Returns the Shielded Instance Identity of an instance |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getShieldedInstanceIdentity(GetShieldedInstanceIdentityInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getShieldedInstanceIdentity(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getShieldedInstanceIdentityCallable() 

  
Insert |  Creates an instance resource in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String zone, Instance instanceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of instances contained within the specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListInstancesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListReferrers |  Retrieves a list of resources that refer to the VM instance specified in the request. For example, if the VM instance is part of a managed or unmanaged instance group, the referrers list includes the instance group. For more information, readViewing referrers to VM instances. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listReferrers(ListReferrersInstancesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listReferrers(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listReferrersPagedCallable() 
  * listReferrersCallable() 

  
PerformMaintenance |  Perform a manual maintenance on the instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * performMaintenanceAsync(PerformMaintenanceInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * performMaintenanceAsync(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * performMaintenanceOperationCallable() 
  * performMaintenanceCallable() 

  
RemoveResourcePolicies |  Removes resource policies from an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeResourcePoliciesAsync(RemoveResourcePoliciesInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeResourcePoliciesAsync(String project, String zone, String instance, InstancesRemoveResourcePoliciesRequest instancesRemoveResourcePoliciesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeResourcePoliciesOperationCallable() 
  * removeResourcePoliciesCallable() 

  
ReportHostAsFaulty |  Mark the host as faulty and try to restart the instance on a new host. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * reportHostAsFaultyAsync(ReportHostAsFaultyInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * reportHostAsFaultyAsync(String project, String zone, String instance, InstancesReportHostAsFaultyRequest instancesReportHostAsFaultyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * reportHostAsFaultyOperationCallable() 
  * reportHostAsFaultyCallable() 

  
Reset |  Performs a reset on the instance. This is a hard reset. The VM does not do a graceful shutdown. For more information, seeResetting an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resetAsync(ResetInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * resetAsync(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resetOperationCallable() 
  * resetCallable() 

  
Resume |  Resumes an instance that was suspended using theinstances().suspend method. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resumeAsync(ResumeInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * resumeAsync(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resumeOperationCallable() 
  * resumeCallable() 

  
SendDiagnosticInterrupt |  Sends diagnostic interrupt to the instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * sendDiagnosticInterrupt(SendDiagnosticInterruptInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * sendDiagnosticInterrupt(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * sendDiagnosticInterruptCallable() 

  
SetDeletionProtection |  Sets deletion protection on the instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setDeletionProtectionAsync(SetDeletionProtectionInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setDeletionProtectionAsync(String project, String zone, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setDeletionProtectionOperationCallable() 
  * setDeletionProtectionCallable() 

  
SetDiskAutoDelete |  Sets the auto-delete flag for a disk attached to an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setDiskAutoDeleteAsync(SetDiskAutoDeleteInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setDiskAutoDeleteAsync(String project, String zone, String instance, boolean autoDelete, String deviceName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setDiskAutoDeleteOperationCallable() 
  * setDiskAutoDeleteCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String zone, String resource, ZoneSetPolicyRequest zoneSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
SetLabels |  Sets labels on an instance. To learn more about labels, read theLabeling Resources documentation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLabelsAsync(SetLabelsInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setLabelsAsync(String project, String zone, String instance, InstancesSetLabelsRequest instancesSetLabelsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLabelsOperationCallable() 
  * setLabelsCallable() 

  
SetMachineResources |  Changes the number and/or type of accelerator for a stopped instance to the values specified in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setMachineResourcesAsync(SetMachineResourcesInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setMachineResourcesAsync(String project, String zone, String instance, InstancesSetMachineResourcesRequest instancesSetMachineResourcesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setMachineResourcesOperationCallable() 
  * setMachineResourcesCallable() 

  
SetMachineType |  Changes the machine type for a stopped instance to the machine type specified in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setMachineTypeAsync(SetMachineTypeInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setMachineTypeAsync(String project, String zone, String instance, InstancesSetMachineTypeRequest instancesSetMachineTypeRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setMachineTypeOperationCallable() 
  * setMachineTypeCallable() 

  
SetMetadata |  Sets metadata for the specified instance to the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setMetadataAsync(SetMetadataInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setMetadataAsync(String project, String zone, String instance, Metadata metadataResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setMetadataOperationCallable() 
  * setMetadataCallable() 

  
SetMinCpuPlatform |  Changes the minimum CPU platform that this instance should use. This method can only be called on a stopped instance. For more information, readSpecifying a Minimum CPU Platform. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setMinCpuPlatformAsync(SetMinCpuPlatformInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setMinCpuPlatformAsync(String project, String zone, String instance, InstancesSetMinCpuPlatformRequest instancesSetMinCpuPlatformRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setMinCpuPlatformOperationCallable() 
  * setMinCpuPlatformCallable() 

  
SetName |  Sets name of an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setNameAsync(SetNameInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setNameAsync(String project, String zone, String instance, InstancesSetNameRequest instancesSetNameRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setNameOperationCallable() 
  * setNameCallable() 

  
SetScheduling |  Sets an instance's scheduling options. You can only call this method on astopped instance, that is, a VM instance that is in a `TERMINATED` state. SeeInstance Life Cycle for more information on the possible instance states. For more information about setting scheduling options for a VM, seeSet VM host maintenance policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setSchedulingAsync(SetSchedulingInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setSchedulingAsync(String project, String zone, String instance, Scheduling schedulingResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setSchedulingOperationCallable() 
  * setSchedulingCallable() 

  
SetSecurityPolicy |  Sets the Google Cloud Armor security policy for the specified instance. For more information, seeGoogle Cloud Armor Overview |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setSecurityPolicyAsync(SetSecurityPolicyInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setSecurityPolicyAsync(String project, String zone, String instance, InstancesSetSecurityPolicyRequest instancesSetSecurityPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setSecurityPolicyOperationCallable() 
  * setSecurityPolicyCallable() 

  
SetServiceAccount |  Sets the service account on the instance. For more information, readChanging the service account and access scopes for an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setServiceAccountAsync(SetServiceAccountInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setServiceAccountAsync(String project, String zone, String instance, InstancesSetServiceAccountRequest instancesSetServiceAccountRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setServiceAccountOperationCallable() 
  * setServiceAccountCallable() 

  
SetShieldedInstanceIntegrityPolicy |  Sets the Shielded Instance integrity policy for an instance. You can only use this method on a running instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setShieldedInstanceIntegrityPolicyAsync(SetShieldedInstanceIntegrityPolicyInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setShieldedInstanceIntegrityPolicyAsync(String project, String zone, String instance, ShieldedInstanceIntegrityPolicy shieldedInstanceIntegrityPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setShieldedInstanceIntegrityPolicyOperationCallable() 
  * setShieldedInstanceIntegrityPolicyCallable() 

  
SetTags |  Sets network tags for the specified instance to the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setTagsAsync(SetTagsInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setTagsAsync(String project, String zone, String instance, Tags tagsResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setTagsOperationCallable() 
  * setTagsCallable() 

  
SimulateMaintenanceEvent |  Simulates a host maintenance event on a VM. For more information, see Simulate a host maintenance event. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * simulateMaintenanceEventAsync(SimulateMaintenanceEventInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * simulateMaintenanceEventAsync(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * simulateMaintenanceEventOperationCallable() 
  * simulateMaintenanceEventCallable() 

  
Start |  Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startAsync(StartInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * startAsync(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startOperationCallable() 
  * startCallable() 

  
StartWithEncryptionKey |  Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startWithEncryptionKeyAsync(StartWithEncryptionKeyInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * startWithEncryptionKeyAsync(String project, String zone, String instance, InstancesStartWithEncryptionKeyRequest instancesStartWithEncryptionKeyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startWithEncryptionKeyOperationCallable() 
  * startWithEncryptionKeyCallable() 

  
Stop |  Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time. Stopped instances do not incur VM usage charges while they are stopped. However, resources that the VM is using, such as persistent disks and static IP addresses, will continue to be charged until they are deleted. For more information, seeStopping an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopAsync(StopInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * stopAsync(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopOperationCallable() 
  * stopCallable() 

  
Suspend |  This method suspends a running instance, saving its state to persistent storage, and allows you to resume the instance at a later time. Suspended instances have no compute costs (cores or RAM), and incur only storage charges for the saved VM memory and localSSD data. Any charged resources the virtual machine was using, such as persistent disks and static IP addresses, will continue to be charged while the instance is suspended. For more information, see Suspending and resuming an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * suspendAsync(SuspendInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * suspendAsync(String project, String zone, String instance) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * suspendOperationCallable() 
  * suspendCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
Update |  Updates an instance only if the necessary resources are available. This method can update only a specific set of instance properties. See Updating a running instance for a list of updatable instance properties. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String zone, String instance, Instance instanceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
UpdateAccessConfig |  Updates the specified access config from an instance's network interface with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAccessConfigAsync(UpdateAccessConfigInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAccessConfigAsync(String project, String zone, String instance, String networkInterface, AccessConfig accessConfigResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAccessConfigOperationCallable() 
  * updateAccessConfigCallable() 

  
UpdateDisplayDevice |  Updates the Display config for a VM instance. You can only use this method on a stopped VM instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDisplayDeviceAsync(UpdateDisplayDeviceInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDisplayDeviceAsync(String project, String zone, String instance, DisplayDevice displayDeviceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDisplayDeviceOperationCallable() 
  * updateDisplayDeviceCallable() 

  
UpdateNetworkInterface |  Updates an instance's network interface. This method can only update an interface's alias IP range and attached network. See Modifying alias IP ranges for an existing instance for instructions on changing alias IP ranges. See Migrating a VM between networks for instructions on migrating an interface. This method follows PATCH semantics. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateNetworkInterfaceAsync(UpdateNetworkInterfaceInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateNetworkInterfaceAsync(String project, String zone, String instance, String networkInterface, NetworkInterface networkInterfaceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateNetworkInterfaceOperationCallable() 
  * updateNetworkInterfaceCallable() 

  
UpdateShieldedInstanceConfig |  Updates the Shielded Instance config for an instance. You can only use this method on a stopped instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateShieldedInstanceConfigAsync(UpdateShieldedInstanceConfigInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateShieldedInstanceConfigAsync(String project, String zone, String instance, ShieldedInstanceConfig shieldedInstanceConfigResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateShieldedInstanceConfigOperationCallable() 
  * updateShieldedInstanceConfigCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of InstancesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InstancesSettings instancesSettings =
         InstancesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     InstancesClient instancesClient = InstancesClient.create(instancesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InstancesSettings instancesSettings =
         InstancesSettings.newBuilder().setEndpoint(myEndpoint).build();
     InstancesClient instancesClient = InstancesClient.create(instancesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InstancesClient

## Static Methods 

### create()
    
    
    public static final InstancesClient create()

Constructs an instance of InstancesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InstancesSettings settings)
    
    
    public static final InstancesClient create(InstancesSettings settings)

Constructs an instance of InstancesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InstancesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InstancesStub stub)
    
    
    public static final InstancesClient create(InstancesStub stub)

Constructs an instance of InstancesClient, using the given stub for making calls. This is for advanced usage - prefer using create(InstancesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InstancesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstancesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient)` |   
  
## Constructors 

### InstancesClient(InstancesSettings settings)
    
    
    protected InstancesClient(InstancesSettings settings)

Constructs an instance of InstancesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InstancesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSettings)`  
  
  
### InstancesClient(InstancesStub stub)
    
    
    protected InstancesClient(InstancesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InstancesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstancesStub)`  
  
  
## Methods 

### addAccessConfigAsync(AddAccessConfigInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> addAccessConfigAsync(AddAccessConfigInstanceRequest request)

Adds an access config to an instance's network interface.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AddAccessConfigInstanceRequest request =
           AddAccessConfigInstanceRequest.newBuilder()
               .setAccessConfigResource(AccessConfig.newBuilder().build())
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.addAccessConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAccessConfigInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAccessConfigAsync(String project, String zone, String instance, String networkInterface, AccessConfig accessConfigResource)
    
    
    public final OperationFuture<Operation,Operation> addAccessConfigAsync(String project, String zone, String instance, String networkInterface, AccessConfig accessConfigResource)

Adds an access config to an instance's network interface.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       String networkInterface = "networkInterface-341981525";
       AccessConfig accessConfigResource = AccessConfig.newBuilder().build();
       Operation response =
           instancesClient
               .addAccessConfigAsync(project, zone, instance, networkInterface, accessConfigResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instance name for this request.  
`networkInterface` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network interface to add to this instance.  
`accessConfigResource` | `[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAccessConfigCallable()
    
    
    public final UnaryCallable<AddAccessConfigInstanceRequest,Operation> addAccessConfigCallable()

Adds an access config to an instance's network interface.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AddAccessConfigInstanceRequest request =
           AddAccessConfigInstanceRequest.newBuilder()
               .setAccessConfigResource(AccessConfig.newBuilder().build())
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.addAccessConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAccessConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAccessConfigOperationCallable()
    
    
    public final OperationCallable<AddAccessConfigInstanceRequest,Operation,Operation> addAccessConfigOperationCallable()

Adds an access config to an instance's network interface.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AddAccessConfigInstanceRequest request =
           AddAccessConfigInstanceRequest.newBuilder()
               .setAccessConfigResource(AccessConfig.newBuilder().build())
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.addAccessConfigOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAccessConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addNetworkInterfaceAsync(AddNetworkInterfaceInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> addNetworkInterfaceAsync(AddNetworkInterfaceInstanceRequest request)

Adds one dynamic network interface to an active instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AddNetworkInterfaceInstanceRequest request =
           AddNetworkInterfaceInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNetworkInterfaceResource(NetworkInterface.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.addNetworkInterfaceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddNetworkInterfaceInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addNetworkInterfaceAsync(String project, String zone, String instance, NetworkInterface networkInterfaceResource)
    
    
    public final OperationFuture<Operation,Operation> addNetworkInterfaceAsync(String project, String zone, String instance, NetworkInterface networkInterfaceResource)

Adds one dynamic network interface to an active instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       NetworkInterface networkInterfaceResource = NetworkInterface.newBuilder().build();
       Operation response =
           instancesClient
               .addNetworkInterfaceAsync(project, zone, instance, networkInterfaceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instance name for this request stored as resource_id. Name should conform to RFC1035 or be an unsigned long integer.  
`networkInterfaceResource` | `[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addNetworkInterfaceCallable()
    
    
    public final UnaryCallable<AddNetworkInterfaceInstanceRequest,Operation> addNetworkInterfaceCallable()

Adds one dynamic network interface to an active instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AddNetworkInterfaceInstanceRequest request =
           AddNetworkInterfaceInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNetworkInterfaceResource(NetworkInterface.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.addNetworkInterfaceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddNetworkInterfaceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addNetworkInterfaceOperationCallable()
    
    
    public final OperationCallable<AddNetworkInterfaceInstanceRequest,Operation,Operation> addNetworkInterfaceOperationCallable()

Adds one dynamic network interface to an active instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AddNetworkInterfaceInstanceRequest request =
           AddNetworkInterfaceInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNetworkInterfaceResource(NetworkInterface.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.addNetworkInterfaceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddNetworkInterfaceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addResourcePoliciesAsync(AddResourcePoliciesInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> addResourcePoliciesAsync(AddResourcePoliciesInstanceRequest request)

Adds existing resource policies to an instance. You can only add one policy right now which will be applied to this instance for scheduling live migrations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AddResourcePoliciesInstanceRequest request =
           AddResourcePoliciesInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesAddResourcePoliciesRequestResource(
                   InstancesAddResourcePoliciesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.addResourcePoliciesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddResourcePoliciesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddResourcePoliciesInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addResourcePoliciesAsync(String project, String zone, String instance, InstancesAddResourcePoliciesRequest instancesAddResourcePoliciesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> addResourcePoliciesAsync(String project, String zone, String instance, InstancesAddResourcePoliciesRequest instancesAddResourcePoliciesRequestResource)

Adds existing resource policies to an instance. You can only add one policy right now which will be applied to this instance for scheduling live migrations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       InstancesAddResourcePoliciesRequest instancesAddResourcePoliciesRequestResource =
           InstancesAddResourcePoliciesRequest.newBuilder().build();
       Operation response =
           instancesClient
               .addResourcePoliciesAsync(
                   project, zone, instance, instancesAddResourcePoliciesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instance name for this request.  
`instancesAddResourcePoliciesRequestResource` | `[InstancesAddResourcePoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesAddResourcePoliciesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addResourcePoliciesCallable()
    
    
    public final UnaryCallable<AddResourcePoliciesInstanceRequest,Operation> addResourcePoliciesCallable()

Adds existing resource policies to an instance. You can only add one policy right now which will be applied to this instance for scheduling live migrations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AddResourcePoliciesInstanceRequest request =
           AddResourcePoliciesInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesAddResourcePoliciesRequestResource(
                   InstancesAddResourcePoliciesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.addResourcePoliciesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddResourcePoliciesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddResourcePoliciesInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addResourcePoliciesOperationCallable()
    
    
    public final OperationCallable<AddResourcePoliciesInstanceRequest,Operation,Operation> addResourcePoliciesOperationCallable()

Adds existing resource policies to an instance. You can only add one policy right now which will be applied to this instance for scheduling live migrations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AddResourcePoliciesInstanceRequest request =
           AddResourcePoliciesInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesAddResourcePoliciesRequestResource(
                   InstancesAddResourcePoliciesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.addResourcePoliciesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddResourcePoliciesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddResourcePoliciesInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### aggregatedList(AggregatedListInstancesRequest request)
    
    
    public final InstancesClient.AggregatedListPagedResponse aggregatedList(AggregatedListInstancesRequest request)

Retrieves an aggregated list of all of the instances in your project across all regions and zones.

The performance of this method degrades when a filter is specified on a project that has a very large number of instances.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AggregatedListInstancesRequest request =
           AggregatedListInstancesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, InstancesScopedList> element :
           instancesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstancesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final InstancesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of all of the instances in your project across all regions and zones.

The performance of this method degrades when a filter is specified on a project that has a very large number of instances.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, InstancesScopedList> element :
           instancesClient.aggregatedList(project).iterateAll()) {
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
`[InstancesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListInstancesRequest,InstanceAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of all of the instances in your project across all regions and zones.

The performance of this method degrades when a filter is specified on a project that has a very large number of instances.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AggregatedListInstancesRequest request =
           AggregatedListInstancesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         InstanceAggregatedList response = instancesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, InstancesScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstancesRequest),[InstanceAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListInstancesRequest,InstancesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of all of the instances in your project across all regions and zones.

The performance of this method degrades when a filter is specified on a project that has a very large number of instances.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AggregatedListInstancesRequest request =
           AggregatedListInstancesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, InstancesScopedList>> future =
           instancesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, InstancesScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstancesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.AggregatedListPagedResponse)>` |   
  
### attachDiskAsync(AttachDiskInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> attachDiskAsync(AttachDiskInstanceRequest request)

Attaches an existing Disk resource to an instance. You must first create the disk before you can attach it. It is not possible to create and attach a disk at the same time. For more information, readAdding a persistent disk to your instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AttachDiskInstanceRequest request =
           AttachDiskInstanceRequest.newBuilder()
               .setAttachedDiskResource(AttachedDisk.newBuilder().build())
               .setForceAttach(true)
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.attachDiskAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AttachDiskInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachDiskInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachDiskAsync(String project, String zone, String instance, AttachedDisk attachedDiskResource)
    
    
    public final OperationFuture<Operation,Operation> attachDiskAsync(String project, String zone, String instance, AttachedDisk attachedDiskResource)

Attaches an existing Disk resource to an instance. You must first create the disk before you can attach it. It is not possible to create and attach a disk at the same time. For more information, readAdding a persistent disk to your instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       AttachedDisk attachedDiskResource = AttachedDisk.newBuilder().build();
       Operation response =
           instancesClient.attachDiskAsync(project, zone, instance, attachedDiskResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instance name for this request.  
`attachedDiskResource` | `[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachDiskCallable()
    
    
    public final UnaryCallable<AttachDiskInstanceRequest,Operation> attachDiskCallable()

Attaches an existing Disk resource to an instance. You must first create the disk before you can attach it. It is not possible to create and attach a disk at the same time. For more information, readAdding a persistent disk to your instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AttachDiskInstanceRequest request =
           AttachDiskInstanceRequest.newBuilder()
               .setAttachedDiskResource(AttachedDisk.newBuilder().build())
               .setForceAttach(true)
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.attachDiskCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AttachDiskInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachDiskInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachDiskOperationCallable()
    
    
    public final OperationCallable<AttachDiskInstanceRequest,Operation,Operation> attachDiskOperationCallable()

Attaches an existing Disk resource to an instance. You must first create the disk before you can attach it. It is not possible to create and attach a disk at the same time. For more information, readAdding a persistent disk to your instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       AttachDiskInstanceRequest request =
           AttachDiskInstanceRequest.newBuilder()
               .setAttachedDiskResource(AttachedDisk.newBuilder().build())
               .setForceAttach(true)
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.attachDiskOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AttachDiskInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachDiskInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### bulkInsertAsync(BulkInsertInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> bulkInsertAsync(BulkInsertInstanceRequest request)

Creates multiple instances. Count specifies the number of instances to create. For more information, seeAbout bulk creation of VMs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       BulkInsertInstanceRequest request =
           BulkInsertInstanceRequest.newBuilder()
               .setBulkInsertInstanceResourceResource(
                   BulkInsertInstanceResource.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.bulkInsertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BulkInsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BulkInsertInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### bulkInsertAsync(String project, String zone, BulkInsertInstanceResource bulkInsertInstanceResourceResource)
    
    
    public final OperationFuture<Operation,Operation> bulkInsertAsync(String project, String zone, BulkInsertInstanceResource bulkInsertInstanceResourceResource)

Creates multiple instances. Count specifies the number of instances to create. For more information, seeAbout bulk creation of VMs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       BulkInsertInstanceResource bulkInsertInstanceResourceResource =
           BulkInsertInstanceResource.newBuilder().build();
       Operation response =
           instancesClient.bulkInsertAsync(project, zone, bulkInsertInstanceResourceResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`bulkInsertInstanceResourceResource` | `[BulkInsertInstanceResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BulkInsertInstanceResource)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### bulkInsertCallable()
    
    
    public final UnaryCallable<BulkInsertInstanceRequest,Operation> bulkInsertCallable()

Creates multiple instances. Count specifies the number of instances to create. For more information, seeAbout bulk creation of VMs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       BulkInsertInstanceRequest request =
           BulkInsertInstanceRequest.newBuilder()
               .setBulkInsertInstanceResourceResource(
                   BulkInsertInstanceResource.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.bulkInsertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BulkInsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BulkInsertInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### bulkInsertOperationCallable()
    
    
    public final OperationCallable<BulkInsertInstanceRequest,Operation,Operation> bulkInsertOperationCallable()

Creates multiple instances. Count specifies the number of instances to create. For more information, seeAbout bulk creation of VMs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       BulkInsertInstanceRequest request =
           BulkInsertInstanceRequest.newBuilder()
               .setBulkInsertInstanceResourceResource(
                   BulkInsertInstanceResource.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.bulkInsertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BulkInsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BulkInsertInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### close()
    
    
    public final void close()

### deleteAccessConfigAsync(DeleteAccessConfigInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAccessConfigAsync(DeleteAccessConfigInstanceRequest request)

Deletes an access config from an instance's network interface.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       DeleteAccessConfigInstanceRequest request =
           DeleteAccessConfigInstanceRequest.newBuilder()
               .setAccessConfig("accessConfig1549765062")
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.deleteAccessConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteAccessConfigInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAccessConfigAsync(String project, String zone, String instance, String accessConfig, String networkInterface)
    
    
    public final OperationFuture<Operation,Operation> deleteAccessConfigAsync(String project, String zone, String instance, String accessConfig, String networkInterface)

Deletes an access config from an instance's network interface.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       String accessConfig = "accessConfig1549765062";
       String networkInterface = "networkInterface-341981525";
       Operation response =
           instancesClient
               .deleteAccessConfigAsync(project, zone, instance, accessConfig, networkInterface)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instance name for this request.  
`accessConfig` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the access config to delete.  
`networkInterface` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network interface.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAccessConfigCallable()
    
    
    public final UnaryCallable<DeleteAccessConfigInstanceRequest,Operation> deleteAccessConfigCallable()

Deletes an access config from an instance's network interface.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       DeleteAccessConfigInstanceRequest request =
           DeleteAccessConfigInstanceRequest.newBuilder()
               .setAccessConfig("accessConfig1549765062")
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.deleteAccessConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteAccessConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAccessConfigOperationCallable()
    
    
    public final OperationCallable<DeleteAccessConfigInstanceRequest,Operation,Operation> deleteAccessConfigOperationCallable()

Deletes an access config from an instance's network interface.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       DeleteAccessConfigInstanceRequest request =
           DeleteAccessConfigInstanceRequest.newBuilder()
               .setAccessConfig("accessConfig1549765062")
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.deleteAccessConfigOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteAccessConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(DeleteInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteInstanceRequest request)

Deletes the specified Instance resource. For more information, seeDeleting an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String zone, String instance)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String zone, String instance)

Deletes the specified Instance resource. For more information, seeDeleting an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Operation response = instancesClient.deleteAsync(project, zone, instance).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteInstanceRequest,Operation> deleteCallable()

Deletes the specified Instance resource. For more information, seeDeleting an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNetworkInterfaceAsync(DeleteNetworkInterfaceInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteNetworkInterfaceAsync(DeleteNetworkInterfaceInstanceRequest request)

Deletes one dynamic network interface from an active instance. InstancesDeleteNetworkInterfaceRequest indicates: - instance from which to delete, using project+zone+resource_id fields; - dynamic network interface to be deleted, using network_interface_name field;

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       DeleteNetworkInterfaceInstanceRequest request =
           DeleteNetworkInterfaceInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNetworkInterfaceName("networkInterfaceName-992385066")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.deleteNetworkInterfaceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkInterfaceInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNetworkInterfaceAsync(String project, String zone, String instance, String networkInterfaceName)
    
    
    public final OperationFuture<Operation,Operation> deleteNetworkInterfaceAsync(String project, String zone, String instance, String networkInterfaceName)

Deletes one dynamic network interface from an active instance. InstancesDeleteNetworkInterfaceRequest indicates: - instance from which to delete, using project+zone+resource_id fields; - dynamic network interface to be deleted, using network_interface_name field;

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       String networkInterfaceName = "networkInterfaceName-992385066";
       Operation response =
           instancesClient
               .deleteNetworkInterfaceAsync(project, zone, instance, networkInterfaceName)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instance name for this request stored as resource_id. Name should conform to RFC1035 or be an unsigned long integer.  
`networkInterfaceName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the dynamic network interface to be deleted from the instance.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNetworkInterfaceCallable()
    
    
    public final UnaryCallable<DeleteNetworkInterfaceInstanceRequest,Operation> deleteNetworkInterfaceCallable()

Deletes one dynamic network interface from an active instance. InstancesDeleteNetworkInterfaceRequest indicates: - instance from which to delete, using project+zone+resource_id fields; - dynamic network interface to be deleted, using network_interface_name field;

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       DeleteNetworkInterfaceInstanceRequest request =
           DeleteNetworkInterfaceInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNetworkInterfaceName("networkInterfaceName-992385066")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.deleteNetworkInterfaceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkInterfaceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNetworkInterfaceOperationCallable()
    
    
    public final OperationCallable<DeleteNetworkInterfaceInstanceRequest,Operation,Operation> deleteNetworkInterfaceOperationCallable()

Deletes one dynamic network interface from an active instance. InstancesDeleteNetworkInterfaceRequest indicates: - instance from which to delete, using project+zone+resource_id fields; - dynamic network interface to be deleted, using network_interface_name field;

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       DeleteNetworkInterfaceInstanceRequest request =
           DeleteNetworkInterfaceInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNetworkInterfaceName("networkInterfaceName-992385066")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.deleteNetworkInterfaceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkInterfaceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteInstanceRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified Instance resource. For more information, seeDeleting an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachDiskAsync(DetachDiskInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> detachDiskAsync(DetachDiskInstanceRequest request)

Detaches a disk from an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       DetachDiskInstanceRequest request =
           DetachDiskInstanceRequest.newBuilder()
               .setDeviceName("deviceName780988929")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.detachDiskAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DetachDiskInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachDiskInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachDiskAsync(String project, String zone, String instance, String deviceName)
    
    
    public final OperationFuture<Operation,Operation> detachDiskAsync(String project, String zone, String instance, String deviceName)

Detaches a disk from an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       String deviceName = "deviceName780988929";
       Operation response =
           instancesClient.detachDiskAsync(project, zone, instance, deviceName).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Instance name for this request.  
`deviceName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The device name of the disk to detach. Make a get() request on the instance to view currently attached disks and device names.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachDiskCallable()
    
    
    public final UnaryCallable<DetachDiskInstanceRequest,Operation> detachDiskCallable()

Detaches a disk from an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       DetachDiskInstanceRequest request =
           DetachDiskInstanceRequest.newBuilder()
               .setDeviceName("deviceName780988929")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.detachDiskCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DetachDiskInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachDiskInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachDiskOperationCallable()
    
    
    public final OperationCallable<DetachDiskInstanceRequest,Operation,Operation> detachDiskOperationCallable()

Detaches a disk from an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       DetachDiskInstanceRequest request =
           DetachDiskInstanceRequest.newBuilder()
               .setDeviceName("deviceName780988929")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.detachDiskOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DetachDiskInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachDiskInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetInstanceRequest request)
    
    
    public final Instance get(GetInstanceRequest request)

Returns the specified Instance resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetInstanceRequest request =
           GetInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       Instance response = instancesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance)` |   
  
### get(String project, String zone, String instance)
    
    
    public final Instance get(String project, String zone, String instance)

Returns the specified Instance resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Instance response = instancesClient.get(project, zone, instance);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetInstanceRequest,Instance> getCallable()

Returns the specified Instance resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetInstanceRequest request =
           GetInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Instance> future = instancesClient.getCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance)>` |   
  
### getEffectiveFirewalls(GetEffectiveFirewallsInstanceRequest request)
    
    
    public final InstancesGetEffectiveFirewallsResponse getEffectiveFirewalls(GetEffectiveFirewallsInstanceRequest request)

Returns effective firewalls applied to an interface of the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetEffectiveFirewallsInstanceRequest request =
           GetEffectiveFirewallsInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       InstancesGetEffectiveFirewallsResponse response =
           instancesClient.getEffectiveFirewalls(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveFirewallsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetEffectiveFirewallsInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstancesGetEffectiveFirewallsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesGetEffectiveFirewallsResponse)` |   
  
### getEffectiveFirewalls(String project, String zone, String instance, String networkInterface)
    
    
    public final InstancesGetEffectiveFirewallsResponse getEffectiveFirewalls(String project, String zone, String instance, String networkInterface)

Returns effective firewalls applied to an interface of the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       String networkInterface = "networkInterface-341981525";
       InstancesGetEffectiveFirewallsResponse response =
           instancesClient.getEffectiveFirewalls(project, zone, instance, networkInterface);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
`networkInterface` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network interface to get the effective firewalls.  
**Returns**  
---  
**Type** | **Description**  
`[InstancesGetEffectiveFirewallsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesGetEffectiveFirewallsResponse)` |   
  
### getEffectiveFirewallsCallable()
    
    
    public final UnaryCallable<GetEffectiveFirewallsInstanceRequest,InstancesGetEffectiveFirewallsResponse> getEffectiveFirewallsCallable()

Returns effective firewalls applied to an interface of the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetEffectiveFirewallsInstanceRequest request =
           GetEffectiveFirewallsInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<InstancesGetEffectiveFirewallsResponse> future =
           instancesClient.getEffectiveFirewallsCallable().futureCall(request);
       // Do something.
       InstancesGetEffectiveFirewallsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEffectiveFirewallsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetEffectiveFirewallsInstanceRequest),[InstancesGetEffectiveFirewallsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesGetEffectiveFirewallsResponse)>` |   
  
### getGuestAttributes(GetGuestAttributesInstanceRequest request)
    
    
    public final GuestAttributes getGuestAttributes(GetGuestAttributesInstanceRequest request)

Returns the specified guest attributes entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetGuestAttributesInstanceRequest request =
           GetGuestAttributesInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setQueryPath("queryPath-1807004403")
               .setVariableKey("variableKey-1951698365")
               .setZone("zone3744684")
               .build();
       GuestAttributes response = instancesClient.getGuestAttributes(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGuestAttributesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGuestAttributesInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GuestAttributes](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GuestAttributes)` |   
  
### getGuestAttributes(String project, String zone, String instance)
    
    
    public final GuestAttributes getGuestAttributes(String project, String zone, String instance)

Returns the specified guest attributes entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       GuestAttributes response = instancesClient.getGuestAttributes(project, zone, instance);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[GuestAttributes](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GuestAttributes)` |   
  
### getGuestAttributesCallable()
    
    
    public final UnaryCallable<GetGuestAttributesInstanceRequest,GuestAttributes> getGuestAttributesCallable()

Returns the specified guest attributes entry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetGuestAttributesInstanceRequest request =
           GetGuestAttributesInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setQueryPath("queryPath-1807004403")
               .setVariableKey("variableKey-1951698365")
               .setZone("zone3744684")
               .build();
       ApiFuture<GuestAttributes> future =
           instancesClient.getGuestAttributesCallable().futureCall(request);
       // Do something.
       GuestAttributes response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGuestAttributesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGuestAttributesInstanceRequest),[GuestAttributes](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GuestAttributes)>` |   
  
### getIamPolicy(GetIamPolicyInstanceRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyInstanceRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetIamPolicyInstanceRequest request =
           GetIamPolicyInstanceRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       Policy response = instancesClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String zone, String resource)
    
    
    public final Policy getIamPolicy(String project, String zone, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       Policy response = instancesClient.getIamPolicy(project, zone, resource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyInstanceRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetIamPolicyInstanceRequest request =
           GetIamPolicyInstanceRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       ApiFuture<Policy> future = instancesClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyInstanceRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getScreenshot(GetScreenshotInstanceRequest request)
    
    
    public final Screenshot getScreenshot(GetScreenshotInstanceRequest request)

Returns the screenshot from the specified instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetScreenshotInstanceRequest request =
           GetScreenshotInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       Screenshot response = instancesClient.getScreenshot(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetScreenshotInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetScreenshotInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Screenshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Screenshot)` |   
  
### getScreenshot(String project, String zone, String instance)
    
    
    public final Screenshot getScreenshot(String project, String zone, String instance)

Returns the screenshot from the specified instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Screenshot response = instancesClient.getScreenshot(project, zone, instance);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[Screenshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Screenshot)` |   
  
### getScreenshotCallable()
    
    
    public final UnaryCallable<GetScreenshotInstanceRequest,Screenshot> getScreenshotCallable()

Returns the screenshot from the specified instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetScreenshotInstanceRequest request =
           GetScreenshotInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Screenshot> future = instancesClient.getScreenshotCallable().futureCall(request);
       // Do something.
       Screenshot response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetScreenshotInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetScreenshotInstanceRequest),[Screenshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Screenshot)>` |   
  
### getSerialPortOutput(GetSerialPortOutputInstanceRequest request)
    
    
    public final SerialPortOutput getSerialPortOutput(GetSerialPortOutputInstanceRequest request)

Returns the last 1 MB of serial port output from the specified instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetSerialPortOutputInstanceRequest request =
           GetSerialPortOutputInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setPort(3446913)
               .setProject("project-309310695")
               .setStart(109757538)
               .setZone("zone3744684")
               .build();
       SerialPortOutput response = instancesClient.getSerialPortOutput(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSerialPortOutputInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetSerialPortOutputInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SerialPortOutput](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SerialPortOutput)` |   
  
### getSerialPortOutput(String project, String zone, String instance)
    
    
    public final SerialPortOutput getSerialPortOutput(String project, String zone, String instance)

Returns the last 1 MB of serial port output from the specified instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       SerialPortOutput response = instancesClient.getSerialPortOutput(project, zone, instance);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance for this request.  
**Returns**  
---  
**Type** | **Description**  
`[SerialPortOutput](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SerialPortOutput)` |   
  
### getSerialPortOutputCallable()
    
    
    public final UnaryCallable<GetSerialPortOutputInstanceRequest,SerialPortOutput> getSerialPortOutputCallable()

Returns the last 1 MB of serial port output from the specified instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetSerialPortOutputInstanceRequest request =
           GetSerialPortOutputInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setPort(3446913)
               .setProject("project-309310695")
               .setStart(109757538)
               .setZone("zone3744684")
               .build();
       ApiFuture<SerialPortOutput> future =
           instancesClient.getSerialPortOutputCallable().futureCall(request);
       // Do something.
       SerialPortOutput response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSerialPortOutputInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetSerialPortOutputInstanceRequest),[SerialPortOutput](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SerialPortOutput)>` |   
  
### getSettings()
    
    
    public final @Nullable InstancesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.InstancesSettings` |   
  
### getShieldedInstanceIdentity(GetShieldedInstanceIdentityInstanceRequest request)
    
    
    public final ShieldedInstanceIdentity getShieldedInstanceIdentity(GetShieldedInstanceIdentityInstanceRequest request)

Returns the Shielded Instance Identity of an instance

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetShieldedInstanceIdentityInstanceRequest request =
           GetShieldedInstanceIdentityInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ShieldedInstanceIdentity response = instancesClient.getShieldedInstanceIdentity(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetShieldedInstanceIdentityInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetShieldedInstanceIdentityInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ShieldedInstanceIdentity](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShieldedInstanceIdentity)` |   
  
### getShieldedInstanceIdentity(String project, String zone, String instance)
    
    
    public final ShieldedInstanceIdentity getShieldedInstanceIdentity(String project, String zone, String instance)

Returns the Shielded Instance Identity of an instance

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       ShieldedInstanceIdentity response =
           instancesClient.getShieldedInstanceIdentity(project, zone, instance);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the instance scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[ShieldedInstanceIdentity](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShieldedInstanceIdentity)` |   
  
### getShieldedInstanceIdentityCallable()
    
    
    public final UnaryCallable<GetShieldedInstanceIdentityInstanceRequest,ShieldedInstanceIdentity> getShieldedInstanceIdentityCallable()

Returns the Shielded Instance Identity of an instance

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       GetShieldedInstanceIdentityInstanceRequest request =
           GetShieldedInstanceIdentityInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<ShieldedInstanceIdentity> future =
           instancesClient.getShieldedInstanceIdentityCallable().futureCall(request);
       // Do something.
       ShieldedInstanceIdentity response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetShieldedInstanceIdentityInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetShieldedInstanceIdentityInstanceRequest),[ShieldedInstanceIdentity](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShieldedInstanceIdentity)>` |   
  
### getStub()
    
    
    public InstancesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[InstancesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstancesStub)` |   
  
### insertAsync(InsertInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertInstanceRequest request)

Creates an instance resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       InsertInstanceRequest request =
           InsertInstanceRequest.newBuilder()
               .setInstanceResource(Instance.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSourceInstanceTemplate("sourceInstanceTemplate949712490")
               .setSourceMachineImage("sourceMachineImage1261073679")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String zone, Instance instanceResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String zone, Instance instanceResource)

Creates an instance resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       Instance instanceResource = Instance.newBuilder().build();
       Operation response = instancesClient.insertAsync(project, zone, instanceResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instanceResource` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertInstanceRequest,Operation> insertCallable()

Creates an instance resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       InsertInstanceRequest request =
           InsertInstanceRequest.newBuilder()
               .setInstanceResource(Instance.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSourceInstanceTemplate("sourceInstanceTemplate949712490")
               .setSourceMachineImage("sourceMachineImage1261073679")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertInstanceRequest,Operation,Operation> insertOperationCallable()

Creates an instance resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       InsertInstanceRequest request =
           InsertInstanceRequest.newBuilder()
               .setInstanceResource(Instance.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSourceInstanceTemplate("sourceInstanceTemplate949712490")
               .setSourceMachineImage("sourceMachineImage1261073679")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListInstancesRequest request)
    
    
    public final InstancesClient.ListPagedResponse list(ListInstancesRequest request)

Retrieves the list of instances contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (Instance element : instancesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstancesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final InstancesClient.ListPagedResponse list(String project, String zone)

Retrieves the list of instances contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (Instance element : instancesClient.list(project, zone).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
**Returns**  
---  
**Type** | **Description**  
`[InstancesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListInstancesRequest,InstanceList> listCallable()

Retrieves the list of instances contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         InstanceList response = instancesClient.listCallable().call(request);
         for (Instance element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstancesRequest),[InstanceList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListInstancesRequest,InstancesClient.ListPagedResponse> listPagedCallable()

Retrieves the list of instances contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Instance> future = instancesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Instance element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstancesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.ListPagedResponse)>` |   
  
### listReferrers(ListReferrersInstancesRequest request)
    
    
    public final InstancesClient.ListReferrersPagedResponse listReferrers(ListReferrersInstancesRequest request)

Retrieves a list of resources that refer to the VM instance specified in the request. For example, if the VM instance is part of a managed or unmanaged instance group, the referrers list includes the instance group. For more information, readViewing referrers to VM instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ListReferrersInstancesRequest request =
           ListReferrersInstancesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstance("instance555127957")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (Reference element : instancesClient.listReferrers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReferrersInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReferrersInstancesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstancesClient.ListReferrersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.ListReferrersPagedResponse)` |   
  
### listReferrers(String project, String zone, String instance)
    
    
    public final InstancesClient.ListReferrersPagedResponse listReferrers(String project, String zone, String instance)

Retrieves a list of resources that refer to the VM instance specified in the request. For example, if the VM instance is part of a managed or unmanaged instance group, the referrers list includes the instance group. For more information, readViewing referrers to VM instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       for (Reference element :
           instancesClient.listReferrers(project, zone, instance).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the target instance scoping this request, or '-' if the request should span over all instances in the container.  
**Returns**  
---  
**Type** | **Description**  
`[InstancesClient.ListReferrersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.ListReferrersPagedResponse)` |   
  
### listReferrersCallable()
    
    
    public final UnaryCallable<ListReferrersInstancesRequest,InstanceListReferrers> listReferrersCallable()

Retrieves a list of resources that refer to the VM instance specified in the request. For example, if the VM instance is part of a managed or unmanaged instance group, the referrers list includes the instance group. For more information, readViewing referrers to VM instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ListReferrersInstancesRequest request =
           ListReferrersInstancesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstance("instance555127957")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         InstanceListReferrers response = instancesClient.listReferrersCallable().call(request);
         for (Reference element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReferrersInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReferrersInstancesRequest),[InstanceListReferrers](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceListReferrers)>` |   
  
### listReferrersPagedCallable()
    
    
    public final UnaryCallable<ListReferrersInstancesRequest,InstancesClient.ListReferrersPagedResponse> listReferrersPagedCallable()

Retrieves a list of resources that refer to the VM instance specified in the request. For example, if the VM instance is part of a managed or unmanaged instance group, the referrers list includes the instance group. For more information, readViewing referrers to VM instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ListReferrersInstancesRequest request =
           ListReferrersInstancesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstance("instance555127957")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Reference> future =
           instancesClient.listReferrersPagedCallable().futureCall(request);
       // Do something.
       for (Reference element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReferrersInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReferrersInstancesRequest),[ListReferrersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.ListReferrersPagedResponse)>` |   
  
### performMaintenanceAsync(PerformMaintenanceInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> performMaintenanceAsync(PerformMaintenanceInstanceRequest request)

Perform a manual maintenance on the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       PerformMaintenanceInstanceRequest request =
           PerformMaintenanceInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.performMaintenanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PerformMaintenanceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceAsync(String project, String zone, String instance)
    
    
    public final OperationFuture<Operation,Operation> performMaintenanceAsync(String project, String zone, String instance)

Perform a manual maintenance on the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Operation response = instancesClient.performMaintenanceAsync(project, zone, instance).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceCallable()
    
    
    public final UnaryCallable<PerformMaintenanceInstanceRequest,Operation> performMaintenanceCallable()

Perform a manual maintenance on the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       PerformMaintenanceInstanceRequest request =
           PerformMaintenanceInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.performMaintenanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PerformMaintenanceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceOperationCallable()
    
    
    public final OperationCallable<PerformMaintenanceInstanceRequest,Operation,Operation> performMaintenanceOperationCallable()

Perform a manual maintenance on the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       PerformMaintenanceInstanceRequest request =
           PerformMaintenanceInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.performMaintenanceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PerformMaintenanceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeResourcePoliciesAsync(RemoveResourcePoliciesInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeResourcePoliciesAsync(RemoveResourcePoliciesInstanceRequest request)

Removes resource policies from an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       RemoveResourcePoliciesInstanceRequest request =
           RemoveResourcePoliciesInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesRemoveResourcePoliciesRequestResource(
                   InstancesRemoveResourcePoliciesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.removeResourcePoliciesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveResourcePoliciesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveResourcePoliciesInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeResourcePoliciesAsync(String project, String zone, String instance, InstancesRemoveResourcePoliciesRequest instancesRemoveResourcePoliciesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> removeResourcePoliciesAsync(String project, String zone, String instance, InstancesRemoveResourcePoliciesRequest instancesRemoveResourcePoliciesRequestResource)

Removes resource policies from an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       InstancesRemoveResourcePoliciesRequest instancesRemoveResourcePoliciesRequestResource =
           InstancesRemoveResourcePoliciesRequest.newBuilder().build();
       Operation response =
           instancesClient
               .removeResourcePoliciesAsync(
                   project, zone, instance, instancesRemoveResourcePoliciesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instance name for this request.  
`instancesRemoveResourcePoliciesRequestResource` | `[InstancesRemoveResourcePoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesRemoveResourcePoliciesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeResourcePoliciesCallable()
    
    
    public final UnaryCallable<RemoveResourcePoliciesInstanceRequest,Operation> removeResourcePoliciesCallable()

Removes resource policies from an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       RemoveResourcePoliciesInstanceRequest request =
           RemoveResourcePoliciesInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesRemoveResourcePoliciesRequestResource(
                   InstancesRemoveResourcePoliciesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.removeResourcePoliciesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveResourcePoliciesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveResourcePoliciesInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeResourcePoliciesOperationCallable()
    
    
    public final OperationCallable<RemoveResourcePoliciesInstanceRequest,Operation,Operation> removeResourcePoliciesOperationCallable()

Removes resource policies from an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       RemoveResourcePoliciesInstanceRequest request =
           RemoveResourcePoliciesInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesRemoveResourcePoliciesRequestResource(
                   InstancesRemoveResourcePoliciesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.removeResourcePoliciesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveResourcePoliciesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveResourcePoliciesInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### reportHostAsFaultyAsync(ReportHostAsFaultyInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> reportHostAsFaultyAsync(ReportHostAsFaultyInstanceRequest request)

Mark the host as faulty and try to restart the instance on a new host.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ReportHostAsFaultyInstanceRequest request =
           ReportHostAsFaultyInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesReportHostAsFaultyRequestResource(
                   InstancesReportHostAsFaultyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.reportHostAsFaultyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReportHostAsFaultyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReportHostAsFaultyInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### reportHostAsFaultyAsync(String project, String zone, String instance, InstancesReportHostAsFaultyRequest instancesReportHostAsFaultyRequestResource)
    
    
    public final OperationFuture<Operation,Operation> reportHostAsFaultyAsync(String project, String zone, String instance, InstancesReportHostAsFaultyRequest instancesReportHostAsFaultyRequestResource)

Mark the host as faulty and try to restart the instance on a new host.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       InstancesReportHostAsFaultyRequest instancesReportHostAsFaultyRequestResource =
           InstancesReportHostAsFaultyRequest.newBuilder().build();
       Operation response =
           instancesClient
               .reportHostAsFaultyAsync(
                   project, zone, instance, instancesReportHostAsFaultyRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
`instancesReportHostAsFaultyRequestResource` | `[InstancesReportHostAsFaultyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesReportHostAsFaultyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### reportHostAsFaultyCallable()
    
    
    public final UnaryCallable<ReportHostAsFaultyInstanceRequest,Operation> reportHostAsFaultyCallable()

Mark the host as faulty and try to restart the instance on a new host.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ReportHostAsFaultyInstanceRequest request =
           ReportHostAsFaultyInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesReportHostAsFaultyRequestResource(
                   InstancesReportHostAsFaultyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.reportHostAsFaultyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReportHostAsFaultyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReportHostAsFaultyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### reportHostAsFaultyOperationCallable()
    
    
    public final OperationCallable<ReportHostAsFaultyInstanceRequest,Operation,Operation> reportHostAsFaultyOperationCallable()

Mark the host as faulty and try to restart the instance on a new host.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ReportHostAsFaultyInstanceRequest request =
           ReportHostAsFaultyInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesReportHostAsFaultyRequestResource(
                   InstancesReportHostAsFaultyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.reportHostAsFaultyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ReportHostAsFaultyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReportHostAsFaultyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resetAsync(ResetInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> resetAsync(ResetInstanceRequest request)

Performs a reset on the instance. This is a hard reset. The VM does not do a graceful shutdown. For more information, seeResetting an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ResetInstanceRequest request =
           ResetInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.resetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resetAsync(String project, String zone, String instance)
    
    
    public final OperationFuture<Operation,Operation> resetAsync(String project, String zone, String instance)

Performs a reset on the instance. This is a hard reset. The VM does not do a graceful shutdown. For more information, seeResetting an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Operation response = instancesClient.resetAsync(project, zone, instance).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resetCallable()
    
    
    public final UnaryCallable<ResetInstanceRequest,Operation> resetCallable()

Performs a reset on the instance. This is a hard reset. The VM does not do a graceful shutdown. For more information, seeResetting an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ResetInstanceRequest request =
           ResetInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.resetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResetInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resetOperationCallable()
    
    
    public final OperationCallable<ResetInstanceRequest,Operation,Operation> resetOperationCallable()

Performs a reset on the instance. This is a hard reset. The VM does not do a graceful shutdown. For more information, seeResetting an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ResetInstanceRequest request =
           ResetInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.resetOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ResetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResetInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeAsync(ResumeInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> resumeAsync(ResumeInstanceRequest request)

Resumes an instance that was suspended using theinstances().suspend method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ResumeInstanceRequest request =
           ResumeInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.resumeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResumeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeAsync(String project, String zone, String instance)
    
    
    public final OperationFuture<Operation,Operation> resumeAsync(String project, String zone, String instance)

Resumes an instance that was suspended using theinstances().suspend method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Operation response = instancesClient.resumeAsync(project, zone, instance).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance resource to resume.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeCallable()
    
    
    public final UnaryCallable<ResumeInstanceRequest,Operation> resumeCallable()

Resumes an instance that was suspended using theinstances().suspend method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ResumeInstanceRequest request =
           ResumeInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.resumeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResumeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeOperationCallable()
    
    
    public final OperationCallable<ResumeInstanceRequest,Operation,Operation> resumeOperationCallable()

Resumes an instance that was suspended using theinstances().suspend method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       ResumeInstanceRequest request =
           ResumeInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.resumeOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ResumeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### sendDiagnosticInterrupt(SendDiagnosticInterruptInstanceRequest request)
    
    
    public final SendDiagnosticInterruptInstanceResponse sendDiagnosticInterrupt(SendDiagnosticInterruptInstanceRequest request)

Sends diagnostic interrupt to the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SendDiagnosticInterruptInstanceRequest request =
           SendDiagnosticInterruptInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       SendDiagnosticInterruptInstanceResponse response =
           instancesClient.sendDiagnosticInterrupt(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SendDiagnosticInterruptInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SendDiagnosticInterruptInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SendDiagnosticInterruptInstanceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SendDiagnosticInterruptInstanceResponse)` |   
  
### sendDiagnosticInterrupt(String project, String zone, String instance)
    
    
    public final SendDiagnosticInterruptInstanceResponse sendDiagnosticInterrupt(String project, String zone, String instance)

Sends diagnostic interrupt to the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       SendDiagnosticInterruptInstanceResponse response =
           instancesClient.sendDiagnosticInterrupt(project, zone, instance);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[SendDiagnosticInterruptInstanceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SendDiagnosticInterruptInstanceResponse)` |   
  
### sendDiagnosticInterruptCallable()
    
    
    public final UnaryCallable<SendDiagnosticInterruptInstanceRequest,SendDiagnosticInterruptInstanceResponse> sendDiagnosticInterruptCallable()

Sends diagnostic interrupt to the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SendDiagnosticInterruptInstanceRequest request =
           SendDiagnosticInterruptInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<SendDiagnosticInterruptInstanceResponse> future =
           instancesClient.sendDiagnosticInterruptCallable().futureCall(request);
       // Do something.
       SendDiagnosticInterruptInstanceResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SendDiagnosticInterruptInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SendDiagnosticInterruptInstanceRequest),[SendDiagnosticInterruptInstanceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SendDiagnosticInterruptInstanceResponse)>` |   
  
### setDeletionProtectionAsync(SetDeletionProtectionInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setDeletionProtectionAsync(SetDeletionProtectionInstanceRequest request)

Sets deletion protection on the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetDeletionProtectionInstanceRequest request =
           SetDeletionProtectionInstanceRequest.newBuilder()
               .setDeletionProtection(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setDeletionProtectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDeletionProtectionInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDeletionProtectionAsync(String project, String zone, String resource)
    
    
    public final OperationFuture<Operation,Operation> setDeletionProtectionAsync(String project, String zone, String resource)

Sets deletion protection on the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       Operation response =
           instancesClient.setDeletionProtectionAsync(project, zone, resource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDeletionProtectionCallable()
    
    
    public final UnaryCallable<SetDeletionProtectionInstanceRequest,Operation> setDeletionProtectionCallable()

Sets deletion protection on the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetDeletionProtectionInstanceRequest request =
           SetDeletionProtectionInstanceRequest.newBuilder()
               .setDeletionProtection(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.setDeletionProtectionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDeletionProtectionInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDeletionProtectionOperationCallable()
    
    
    public final OperationCallable<SetDeletionProtectionInstanceRequest,Operation,Operation> setDeletionProtectionOperationCallable()

Sets deletion protection on the instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetDeletionProtectionInstanceRequest request =
           SetDeletionProtectionInstanceRequest.newBuilder()
               .setDeletionProtection(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setDeletionProtectionOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDeletionProtectionInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDiskAutoDeleteAsync(SetDiskAutoDeleteInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setDiskAutoDeleteAsync(SetDiskAutoDeleteInstanceRequest request)

Sets the auto-delete flag for a disk attached to an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetDiskAutoDeleteInstanceRequest request =
           SetDiskAutoDeleteInstanceRequest.newBuilder()
               .setAutoDelete(true)
               .setDeviceName("deviceName780988929")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setDiskAutoDeleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDiskAutoDeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDiskAutoDeleteAsync(String project, String zone, String instance, boolean autoDelete, String deviceName)
    
    
    public final OperationFuture<Operation,Operation> setDiskAutoDeleteAsync(String project, String zone, String instance, boolean autoDelete, String deviceName)

Sets the auto-delete flag for a disk attached to an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       boolean autoDelete = true;
       String deviceName = "deviceName780988929";
       Operation response =
           instancesClient
               .setDiskAutoDeleteAsync(project, zone, instance, autoDelete, deviceName)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instance name for this request.  
`autoDelete` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Whether to auto-delete the disk when the instance is deleted.  
`deviceName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The device name of the disk to modify. Make a get() request on the instance to view currently attached disks and device names.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDiskAutoDeleteCallable()
    
    
    public final UnaryCallable<SetDiskAutoDeleteInstanceRequest,Operation> setDiskAutoDeleteCallable()

Sets the auto-delete flag for a disk attached to an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetDiskAutoDeleteInstanceRequest request =
           SetDiskAutoDeleteInstanceRequest.newBuilder()
               .setAutoDelete(true)
               .setDeviceName("deviceName780988929")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.setDiskAutoDeleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDiskAutoDeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDiskAutoDeleteOperationCallable()
    
    
    public final OperationCallable<SetDiskAutoDeleteInstanceRequest,Operation,Operation> setDiskAutoDeleteOperationCallable()

Sets the auto-delete flag for a disk attached to an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetDiskAutoDeleteInstanceRequest request =
           SetDiskAutoDeleteInstanceRequest.newBuilder()
               .setAutoDelete(true)
               .setDeviceName("deviceName780988929")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setDiskAutoDeleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDiskAutoDeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyInstanceRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyInstanceRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetIamPolicyInstanceRequest request =
           SetIamPolicyInstanceRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetPolicyRequestResource(ZoneSetPolicyRequest.newBuilder().build())
               .build();
       Policy response = instancesClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String zone, String resource, ZoneSetPolicyRequest zoneSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String zone, String resource, ZoneSetPolicyRequest zoneSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       ZoneSetPolicyRequest zoneSetPolicyRequestResource = ZoneSetPolicyRequest.newBuilder().build();
       Policy response =
           instancesClient.setIamPolicy(project, zone, resource, zoneSetPolicyRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`zoneSetPolicyRequestResource` | `[ZoneSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyInstanceRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetIamPolicyInstanceRequest request =
           SetIamPolicyInstanceRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetPolicyRequestResource(ZoneSetPolicyRequest.newBuilder().build())
               .build();
       ApiFuture<Policy> future = instancesClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyInstanceRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### setLabelsAsync(SetLabelsInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(SetLabelsInstanceRequest request)

Sets labels on an instance. To learn more about labels, read theLabeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetLabelsInstanceRequest request =
           SetLabelsInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetLabelsRequestResource(InstancesSetLabelsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setLabelsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLabelsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsAsync(String project, String zone, String instance, InstancesSetLabelsRequest instancesSetLabelsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(String project, String zone, String instance, InstancesSetLabelsRequest instancesSetLabelsRequestResource)

Sets labels on an instance. To learn more about labels, read theLabeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       InstancesSetLabelsRequest instancesSetLabelsRequestResource =
           InstancesSetLabelsRequest.newBuilder().build();
       Operation response =
           instancesClient
               .setLabelsAsync(project, zone, instance, instancesSetLabelsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
`instancesSetLabelsRequestResource` | `[InstancesSetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSetLabelsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsCallable()
    
    
    public final UnaryCallable<SetLabelsInstanceRequest,Operation> setLabelsCallable()

Sets labels on an instance. To learn more about labels, read theLabeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetLabelsInstanceRequest request =
           SetLabelsInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetLabelsRequestResource(InstancesSetLabelsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.setLabelsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLabelsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsOperationCallable()
    
    
    public final OperationCallable<SetLabelsInstanceRequest,Operation,Operation> setLabelsOperationCallable()

Sets labels on an instance. To learn more about labels, read theLabeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetLabelsInstanceRequest request =
           SetLabelsInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetLabelsRequestResource(InstancesSetLabelsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setLabelsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetLabelsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMachineResourcesAsync(SetMachineResourcesInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setMachineResourcesAsync(SetMachineResourcesInstanceRequest request)

Changes the number and/or type of accelerator for a stopped instance to the values specified in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetMachineResourcesInstanceRequest request =
           SetMachineResourcesInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetMachineResourcesRequestResource(
                   InstancesSetMachineResourcesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setMachineResourcesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetMachineResourcesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineResourcesInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMachineResourcesAsync(String project, String zone, String instance, InstancesSetMachineResourcesRequest instancesSetMachineResourcesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setMachineResourcesAsync(String project, String zone, String instance, InstancesSetMachineResourcesRequest instancesSetMachineResourcesRequestResource)

Changes the number and/or type of accelerator for a stopped instance to the values specified in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       InstancesSetMachineResourcesRequest instancesSetMachineResourcesRequestResource =
           InstancesSetMachineResourcesRequest.newBuilder().build();
       Operation response =
           instancesClient
               .setMachineResourcesAsync(
                   project, zone, instance, instancesSetMachineResourcesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
`instancesSetMachineResourcesRequestResource` | `[InstancesSetMachineResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSetMachineResourcesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMachineResourcesCallable()
    
    
    public final UnaryCallable<SetMachineResourcesInstanceRequest,Operation> setMachineResourcesCallable()

Changes the number and/or type of accelerator for a stopped instance to the values specified in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetMachineResourcesInstanceRequest request =
           SetMachineResourcesInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetMachineResourcesRequestResource(
                   InstancesSetMachineResourcesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.setMachineResourcesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetMachineResourcesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineResourcesInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMachineResourcesOperationCallable()
    
    
    public final OperationCallable<SetMachineResourcesInstanceRequest,Operation,Operation> setMachineResourcesOperationCallable()

Changes the number and/or type of accelerator for a stopped instance to the values specified in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetMachineResourcesInstanceRequest request =
           SetMachineResourcesInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetMachineResourcesRequestResource(
                   InstancesSetMachineResourcesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setMachineResourcesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetMachineResourcesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineResourcesInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMachineTypeAsync(SetMachineTypeInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setMachineTypeAsync(SetMachineTypeInstanceRequest request)

Changes the machine type for a stopped instance to the machine type specified in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetMachineTypeInstanceRequest request =
           SetMachineTypeInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetMachineTypeRequestResource(
                   InstancesSetMachineTypeRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setMachineTypeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetMachineTypeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineTypeInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMachineTypeAsync(String project, String zone, String instance, InstancesSetMachineTypeRequest instancesSetMachineTypeRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setMachineTypeAsync(String project, String zone, String instance, InstancesSetMachineTypeRequest instancesSetMachineTypeRequestResource)

Changes the machine type for a stopped instance to the machine type specified in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       InstancesSetMachineTypeRequest instancesSetMachineTypeRequestResource =
           InstancesSetMachineTypeRequest.newBuilder().build();
       Operation response =
           instancesClient
               .setMachineTypeAsync(project, zone, instance, instancesSetMachineTypeRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
`instancesSetMachineTypeRequestResource` | `[InstancesSetMachineTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSetMachineTypeRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMachineTypeCallable()
    
    
    public final UnaryCallable<SetMachineTypeInstanceRequest,Operation> setMachineTypeCallable()

Changes the machine type for a stopped instance to the machine type specified in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetMachineTypeInstanceRequest request =
           SetMachineTypeInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetMachineTypeRequestResource(
                   InstancesSetMachineTypeRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.setMachineTypeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetMachineTypeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineTypeInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMachineTypeOperationCallable()
    
    
    public final OperationCallable<SetMachineTypeInstanceRequest,Operation,Operation> setMachineTypeOperationCallable()

Changes the machine type for a stopped instance to the machine type specified in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetMachineTypeInstanceRequest request =
           SetMachineTypeInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetMachineTypeRequestResource(
                   InstancesSetMachineTypeRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setMachineTypeOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetMachineTypeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineTypeInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMetadataAsync(SetMetadataInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setMetadataAsync(SetMetadataInstanceRequest request)

Sets metadata for the specified instance to the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetMetadataInstanceRequest request =
           SetMetadataInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setMetadataResource(Metadata.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setMetadataAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetMetadataInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMetadataInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMetadataAsync(String project, String zone, String instance, Metadata metadataResource)
    
    
    public final OperationFuture<Operation,Operation> setMetadataAsync(String project, String zone, String instance, Metadata metadataResource)

Sets metadata for the specified instance to the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Metadata metadataResource = Metadata.newBuilder().build();
       Operation response =
           instancesClient.setMetadataAsync(project, zone, instance, metadataResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
`metadataResource` | `[Metadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Metadata)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMetadataCallable()
    
    
    public final UnaryCallable<SetMetadataInstanceRequest,Operation> setMetadataCallable()

Sets metadata for the specified instance to the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetMetadataInstanceRequest request =
           SetMetadataInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setMetadataResource(Metadata.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.setMetadataCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetMetadataInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMetadataInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMetadataOperationCallable()
    
    
    public final OperationCallable<SetMetadataInstanceRequest,Operation,Operation> setMetadataOperationCallable()

Sets metadata for the specified instance to the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetMetadataInstanceRequest request =
           SetMetadataInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setMetadataResource(Metadata.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setMetadataOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetMetadataInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMetadataInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMinCpuPlatformAsync(SetMinCpuPlatformInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setMinCpuPlatformAsync(SetMinCpuPlatformInstanceRequest request)

Changes the minimum CPU platform that this instance should use. This method can only be called on a stopped instance. For more information, readSpecifying a Minimum CPU Platform.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetMinCpuPlatformInstanceRequest request =
           SetMinCpuPlatformInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetMinCpuPlatformRequestResource(
                   InstancesSetMinCpuPlatformRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setMinCpuPlatformAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetMinCpuPlatformInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMinCpuPlatformInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMinCpuPlatformAsync(String project, String zone, String instance, InstancesSetMinCpuPlatformRequest instancesSetMinCpuPlatformRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setMinCpuPlatformAsync(String project, String zone, String instance, InstancesSetMinCpuPlatformRequest instancesSetMinCpuPlatformRequestResource)

Changes the minimum CPU platform that this instance should use. This method can only be called on a stopped instance. For more information, readSpecifying a Minimum CPU Platform.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       InstancesSetMinCpuPlatformRequest instancesSetMinCpuPlatformRequestResource =
           InstancesSetMinCpuPlatformRequest.newBuilder().build();
       Operation response =
           instancesClient
               .setMinCpuPlatformAsync(
                   project, zone, instance, instancesSetMinCpuPlatformRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
`instancesSetMinCpuPlatformRequestResource` | `[InstancesSetMinCpuPlatformRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSetMinCpuPlatformRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMinCpuPlatformCallable()
    
    
    public final UnaryCallable<SetMinCpuPlatformInstanceRequest,Operation> setMinCpuPlatformCallable()

Changes the minimum CPU platform that this instance should use. This method can only be called on a stopped instance. For more information, readSpecifying a Minimum CPU Platform.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetMinCpuPlatformInstanceRequest request =
           SetMinCpuPlatformInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetMinCpuPlatformRequestResource(
                   InstancesSetMinCpuPlatformRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.setMinCpuPlatformCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetMinCpuPlatformInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMinCpuPlatformInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMinCpuPlatformOperationCallable()
    
    
    public final OperationCallable<SetMinCpuPlatformInstanceRequest,Operation,Operation> setMinCpuPlatformOperationCallable()

Changes the minimum CPU platform that this instance should use. This method can only be called on a stopped instance. For more information, readSpecifying a Minimum CPU Platform.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetMinCpuPlatformInstanceRequest request =
           SetMinCpuPlatformInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetMinCpuPlatformRequestResource(
                   InstancesSetMinCpuPlatformRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setMinCpuPlatformOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetMinCpuPlatformInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMinCpuPlatformInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNameAsync(SetNameInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setNameAsync(SetNameInstanceRequest request)

Sets name of an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetNameInstanceRequest request =
           SetNameInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetNameRequestResource(InstancesSetNameRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setNameAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetNameInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNameInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNameAsync(String project, String zone, String instance, InstancesSetNameRequest instancesSetNameRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setNameAsync(String project, String zone, String instance, InstancesSetNameRequest instancesSetNameRequestResource)

Sets name of an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       InstancesSetNameRequest instancesSetNameRequestResource =
           InstancesSetNameRequest.newBuilder().build();
       Operation response =
           instancesClient
               .setNameAsync(project, zone, instance, instancesSetNameRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instance name for this request.  
`instancesSetNameRequestResource` | `[InstancesSetNameRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSetNameRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNameCallable()
    
    
    public final UnaryCallable<SetNameInstanceRequest,Operation> setNameCallable()

Sets name of an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetNameInstanceRequest request =
           SetNameInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetNameRequestResource(InstancesSetNameRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.setNameCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetNameInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNameInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNameOperationCallable()
    
    
    public final OperationCallable<SetNameInstanceRequest,Operation,Operation> setNameOperationCallable()

Sets name of an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetNameInstanceRequest request =
           SetNameInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetNameRequestResource(InstancesSetNameRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setNameOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetNameInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNameInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSchedulingAsync(SetSchedulingInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setSchedulingAsync(SetSchedulingInstanceRequest request)

Sets an instance's scheduling options. You can only call this method on astopped instance, that is, a VM instance that is in a `TERMINATED` state. SeeInstance Life Cycle for more information on the possible instance states. For more information about setting scheduling options for a VM, seeSet VM host maintenance policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetSchedulingInstanceRequest request =
           SetSchedulingInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSchedulingResource(Scheduling.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setSchedulingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetSchedulingInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSchedulingInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSchedulingAsync(String project, String zone, String instance, Scheduling schedulingResource)
    
    
    public final OperationFuture<Operation,Operation> setSchedulingAsync(String project, String zone, String instance, Scheduling schedulingResource)

Sets an instance's scheduling options. You can only call this method on astopped instance, that is, a VM instance that is in a `TERMINATED` state. SeeInstance Life Cycle for more information on the possible instance states. For more information about setting scheduling options for a VM, seeSet VM host maintenance policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Scheduling schedulingResource = Scheduling.newBuilder().build();
       Operation response =
           instancesClient.setSchedulingAsync(project, zone, instance, schedulingResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Instance name for this request.  
`schedulingResource` | `[Scheduling](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Scheduling)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSchedulingCallable()
    
    
    public final UnaryCallable<SetSchedulingInstanceRequest,Operation> setSchedulingCallable()

Sets an instance's scheduling options. You can only call this method on astopped instance, that is, a VM instance that is in a `TERMINATED` state. SeeInstance Life Cycle for more information on the possible instance states. For more information about setting scheduling options for a VM, seeSet VM host maintenance policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetSchedulingInstanceRequest request =
           SetSchedulingInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSchedulingResource(Scheduling.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.setSchedulingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetSchedulingInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSchedulingInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSchedulingOperationCallable()
    
    
    public final OperationCallable<SetSchedulingInstanceRequest,Operation,Operation> setSchedulingOperationCallable()

Sets an instance's scheduling options. You can only call this method on astopped instance, that is, a VM instance that is in a `TERMINATED` state. SeeInstance Life Cycle for more information on the possible instance states. For more information about setting scheduling options for a VM, seeSet VM host maintenance policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetSchedulingInstanceRequest request =
           SetSchedulingInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSchedulingResource(Scheduling.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setSchedulingOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetSchedulingInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSchedulingInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicyAsync(SetSecurityPolicyInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setSecurityPolicyAsync(SetSecurityPolicyInstanceRequest request)

Sets the Google Cloud Armor security policy for the specified instance. For more information, seeGoogle Cloud Armor Overview

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetSecurityPolicyInstanceRequest request =
           SetSecurityPolicyInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetSecurityPolicyRequestResource(
                   InstancesSetSecurityPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setSecurityPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetSecurityPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSecurityPolicyInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicyAsync(String project, String zone, String instance, InstancesSetSecurityPolicyRequest instancesSetSecurityPolicyRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setSecurityPolicyAsync(String project, String zone, String instance, InstancesSetSecurityPolicyRequest instancesSetSecurityPolicyRequestResource)

Sets the Google Cloud Armor security policy for the specified instance. For more information, seeGoogle Cloud Armor Overview

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       InstancesSetSecurityPolicyRequest instancesSetSecurityPolicyRequestResource =
           InstancesSetSecurityPolicyRequest.newBuilder().build();
       Operation response =
           instancesClient
               .setSecurityPolicyAsync(
                   project, zone, instance, instancesSetSecurityPolicyRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone scoping this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Instance resource to which the security policy should be set. The name should conform to RFC1035.  
`instancesSetSecurityPolicyRequestResource` | `[InstancesSetSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSetSecurityPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicyCallable()
    
    
    public final UnaryCallable<SetSecurityPolicyInstanceRequest,Operation> setSecurityPolicyCallable()

Sets the Google Cloud Armor security policy for the specified instance. For more information, seeGoogle Cloud Armor Overview

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetSecurityPolicyInstanceRequest request =
           SetSecurityPolicyInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetSecurityPolicyRequestResource(
                   InstancesSetSecurityPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.setSecurityPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetSecurityPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSecurityPolicyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicyOperationCallable()
    
    
    public final OperationCallable<SetSecurityPolicyInstanceRequest,Operation,Operation> setSecurityPolicyOperationCallable()

Sets the Google Cloud Armor security policy for the specified instance. For more information, seeGoogle Cloud Armor Overview

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetSecurityPolicyInstanceRequest request =
           SetSecurityPolicyInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetSecurityPolicyRequestResource(
                   InstancesSetSecurityPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setSecurityPolicyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetSecurityPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSecurityPolicyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setServiceAccountAsync(SetServiceAccountInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setServiceAccountAsync(SetServiceAccountInstanceRequest request)

Sets the service account on the instance. For more information, readChanging the service account and access scopes for an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetServiceAccountInstanceRequest request =
           SetServiceAccountInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetServiceAccountRequestResource(
                   InstancesSetServiceAccountRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setServiceAccountAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetServiceAccountInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetServiceAccountInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setServiceAccountAsync(String project, String zone, String instance, InstancesSetServiceAccountRequest instancesSetServiceAccountRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setServiceAccountAsync(String project, String zone, String instance, InstancesSetServiceAccountRequest instancesSetServiceAccountRequestResource)

Sets the service account on the instance. For more information, readChanging the service account and access scopes for an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       InstancesSetServiceAccountRequest instancesSetServiceAccountRequestResource =
           InstancesSetServiceAccountRequest.newBuilder().build();
       Operation response =
           instancesClient
               .setServiceAccountAsync(
                   project, zone, instance, instancesSetServiceAccountRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance resource to start.  
`instancesSetServiceAccountRequestResource` | `[InstancesSetServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSetServiceAccountRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setServiceAccountCallable()
    
    
    public final UnaryCallable<SetServiceAccountInstanceRequest,Operation> setServiceAccountCallable()

Sets the service account on the instance. For more information, readChanging the service account and access scopes for an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetServiceAccountInstanceRequest request =
           SetServiceAccountInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetServiceAccountRequestResource(
                   InstancesSetServiceAccountRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.setServiceAccountCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetServiceAccountInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetServiceAccountInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setServiceAccountOperationCallable()
    
    
    public final OperationCallable<SetServiceAccountInstanceRequest,Operation,Operation> setServiceAccountOperationCallable()

Sets the service account on the instance. For more information, readChanging the service account and access scopes for an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetServiceAccountInstanceRequest request =
           SetServiceAccountInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesSetServiceAccountRequestResource(
                   InstancesSetServiceAccountRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setServiceAccountOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetServiceAccountInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetServiceAccountInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setShieldedInstanceIntegrityPolicyAsync(SetShieldedInstanceIntegrityPolicyInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setShieldedInstanceIntegrityPolicyAsync(SetShieldedInstanceIntegrityPolicyInstanceRequest request)

Sets the Shielded Instance integrity policy for an instance. You can only use this method on a running instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetShieldedInstanceIntegrityPolicyInstanceRequest request =
           SetShieldedInstanceIntegrityPolicyInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setShieldedInstanceIntegrityPolicyResource(
                   ShieldedInstanceIntegrityPolicy.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setShieldedInstanceIntegrityPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetShieldedInstanceIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetShieldedInstanceIntegrityPolicyInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setShieldedInstanceIntegrityPolicyAsync(String project, String zone, String instance, ShieldedInstanceIntegrityPolicy shieldedInstanceIntegrityPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> setShieldedInstanceIntegrityPolicyAsync(String project, String zone, String instance, ShieldedInstanceIntegrityPolicy shieldedInstanceIntegrityPolicyResource)

Sets the Shielded Instance integrity policy for an instance. You can only use this method on a running instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       ShieldedInstanceIntegrityPolicy shieldedInstanceIntegrityPolicyResource =
           ShieldedInstanceIntegrityPolicy.newBuilder().build();
       Operation response =
           instancesClient
               .setShieldedInstanceIntegrityPolicyAsync(
                   project, zone, instance, shieldedInstanceIntegrityPolicyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the instance scoping this request.  
`shieldedInstanceIntegrityPolicyResource` | `[ShieldedInstanceIntegrityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShieldedInstanceIntegrityPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setShieldedInstanceIntegrityPolicyCallable()
    
    
    public final UnaryCallable<SetShieldedInstanceIntegrityPolicyInstanceRequest,Operation> setShieldedInstanceIntegrityPolicyCallable()

Sets the Shielded Instance integrity policy for an instance. You can only use this method on a running instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetShieldedInstanceIntegrityPolicyInstanceRequest request =
           SetShieldedInstanceIntegrityPolicyInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setShieldedInstanceIntegrityPolicyResource(
                   ShieldedInstanceIntegrityPolicy.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.setShieldedInstanceIntegrityPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetShieldedInstanceIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetShieldedInstanceIntegrityPolicyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setShieldedInstanceIntegrityPolicyOperationCallable()
    
    
    public final OperationCallable<SetShieldedInstanceIntegrityPolicyInstanceRequest,Operation,Operation> setShieldedInstanceIntegrityPolicyOperationCallable()

Sets the Shielded Instance integrity policy for an instance. You can only use this method on a running instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetShieldedInstanceIntegrityPolicyInstanceRequest request =
           SetShieldedInstanceIntegrityPolicyInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setShieldedInstanceIntegrityPolicyResource(
                   ShieldedInstanceIntegrityPolicy.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setShieldedInstanceIntegrityPolicyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetShieldedInstanceIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetShieldedInstanceIntegrityPolicyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTagsAsync(SetTagsInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setTagsAsync(SetTagsInstanceRequest request)

Sets network tags for the specified instance to the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetTagsInstanceRequest request =
           SetTagsInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTagsResource(Tags.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.setTagsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetTagsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTagsInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTagsAsync(String project, String zone, String instance, Tags tagsResource)
    
    
    public final OperationFuture<Operation,Operation> setTagsAsync(String project, String zone, String instance, Tags tagsResource)

Sets network tags for the specified instance to the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Tags tagsResource = Tags.newBuilder().build();
       Operation response =
           instancesClient.setTagsAsync(project, zone, instance, tagsResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
`tagsResource` | `[Tags](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Tags)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTagsCallable()
    
    
    public final UnaryCallable<SetTagsInstanceRequest,Operation> setTagsCallable()

Sets network tags for the specified instance to the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetTagsInstanceRequest request =
           SetTagsInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTagsResource(Tags.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.setTagsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetTagsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTagsInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTagsOperationCallable()
    
    
    public final OperationCallable<SetTagsInstanceRequest,Operation,Operation> setTagsOperationCallable()

Sets network tags for the specified instance to the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SetTagsInstanceRequest request =
           SetTagsInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTagsResource(Tags.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.setTagsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetTagsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTagsInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### simulateMaintenanceEventAsync(SimulateMaintenanceEventInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> simulateMaintenanceEventAsync(SimulateMaintenanceEventInstanceRequest request)

Simulates a host maintenance event on a VM. For more information, see Simulate a host maintenance event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SimulateMaintenanceEventInstanceRequest request =
           SimulateMaintenanceEventInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setWithExtendedNotifications(true)
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.simulateMaintenanceEventAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SimulateMaintenanceEventInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SimulateMaintenanceEventInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### simulateMaintenanceEventAsync(String project, String zone, String instance)
    
    
    public final OperationFuture<Operation,Operation> simulateMaintenanceEventAsync(String project, String zone, String instance)

Simulates a host maintenance event on a VM. For more information, see Simulate a host maintenance event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Operation response =
           instancesClient.simulateMaintenanceEventAsync(project, zone, instance).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### simulateMaintenanceEventCallable()
    
    
    public final UnaryCallable<SimulateMaintenanceEventInstanceRequest,Operation> simulateMaintenanceEventCallable()

Simulates a host maintenance event on a VM. For more information, see Simulate a host maintenance event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SimulateMaintenanceEventInstanceRequest request =
           SimulateMaintenanceEventInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setWithExtendedNotifications(true)
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.simulateMaintenanceEventCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SimulateMaintenanceEventInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SimulateMaintenanceEventInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### simulateMaintenanceEventOperationCallable()
    
    
    public final OperationCallable<SimulateMaintenanceEventInstanceRequest,Operation,Operation> simulateMaintenanceEventOperationCallable()

Simulates a host maintenance event on a VM. For more information, see Simulate a host maintenance event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SimulateMaintenanceEventInstanceRequest request =
           SimulateMaintenanceEventInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setWithExtendedNotifications(true)
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.simulateMaintenanceEventOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SimulateMaintenanceEventInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SimulateMaintenanceEventInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startAsync(StartInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> startAsync(StartInstanceRequest request)

Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       StartInstanceRequest request =
           StartInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.startAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startAsync(String project, String zone, String instance)
    
    
    public final OperationFuture<Operation,Operation> startAsync(String project, String zone, String instance)

Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Operation response = instancesClient.startAsync(project, zone, instance).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance resource to start.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startCallable()
    
    
    public final UnaryCallable<StartInstanceRequest,Operation> startCallable()

Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       StartInstanceRequest request =
           StartInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.startCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startOperationCallable()
    
    
    public final OperationCallable<StartInstanceRequest,Operation,Operation> startOperationCallable()

Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       StartInstanceRequest request =
           StartInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.startOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startWithEncryptionKeyAsync(StartWithEncryptionKeyInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> startWithEncryptionKeyAsync(StartWithEncryptionKeyInstanceRequest request)

Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       StartWithEncryptionKeyInstanceRequest request =
           StartWithEncryptionKeyInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesStartWithEncryptionKeyRequestResource(
                   InstancesStartWithEncryptionKeyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.startWithEncryptionKeyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartWithEncryptionKeyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartWithEncryptionKeyInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startWithEncryptionKeyAsync(String project, String zone, String instance, InstancesStartWithEncryptionKeyRequest instancesStartWithEncryptionKeyRequestResource)
    
    
    public final OperationFuture<Operation,Operation> startWithEncryptionKeyAsync(String project, String zone, String instance, InstancesStartWithEncryptionKeyRequest instancesStartWithEncryptionKeyRequestResource)

Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       InstancesStartWithEncryptionKeyRequest instancesStartWithEncryptionKeyRequestResource =
           InstancesStartWithEncryptionKeyRequest.newBuilder().build();
       Operation response =
           instancesClient
               .startWithEncryptionKeyAsync(
                   project, zone, instance, instancesStartWithEncryptionKeyRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance resource to start.  
`instancesStartWithEncryptionKeyRequestResource` | `[InstancesStartWithEncryptionKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesStartWithEncryptionKeyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startWithEncryptionKeyCallable()
    
    
    public final UnaryCallable<StartWithEncryptionKeyInstanceRequest,Operation> startWithEncryptionKeyCallable()

Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       StartWithEncryptionKeyInstanceRequest request =
           StartWithEncryptionKeyInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesStartWithEncryptionKeyRequestResource(
                   InstancesStartWithEncryptionKeyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.startWithEncryptionKeyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartWithEncryptionKeyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartWithEncryptionKeyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startWithEncryptionKeyOperationCallable()
    
    
    public final OperationCallable<StartWithEncryptionKeyInstanceRequest,Operation,Operation> startWithEncryptionKeyOperationCallable()

Starts an instance that was stopped using theinstances().stop method. For more information, seeRestart an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       StartWithEncryptionKeyInstanceRequest request =
           StartWithEncryptionKeyInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setInstancesStartWithEncryptionKeyRequestResource(
                   InstancesStartWithEncryptionKeyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.startWithEncryptionKeyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StartWithEncryptionKeyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartWithEncryptionKeyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopAsync(StopInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> stopAsync(StopInstanceRequest request)

Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time. Stopped instances do not incur VM usage charges while they are stopped. However, resources that the VM is using, such as persistent disks and static IP addresses, will continue to be charged until they are deleted. For more information, seeStopping an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       StopInstanceRequest request =
           StopInstanceRequest.newBuilder()
               .setDiscardLocalSsd(true)
               .setInstance("instance555127957")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.stopAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopAsync(String project, String zone, String instance)
    
    
    public final OperationFuture<Operation,Operation> stopAsync(String project, String zone, String instance)

Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time. Stopped instances do not incur VM usage charges while they are stopped. However, resources that the VM is using, such as persistent disks and static IP addresses, will continue to be charged until they are deleted. For more information, seeStopping an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Operation response = instancesClient.stopAsync(project, zone, instance).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance resource to stop.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopCallable()
    
    
    public final UnaryCallable<StopInstanceRequest,Operation> stopCallable()

Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time. Stopped instances do not incur VM usage charges while they are stopped. However, resources that the VM is using, such as persistent disks and static IP addresses, will continue to be charged until they are deleted. For more information, seeStopping an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       StopInstanceRequest request =
           StopInstanceRequest.newBuilder()
               .setDiscardLocalSsd(true)
               .setInstance("instance555127957")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.stopCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopOperationCallable()
    
    
    public final OperationCallable<StopInstanceRequest,Operation,Operation> stopOperationCallable()

Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time. Stopped instances do not incur VM usage charges while they are stopped. However, resources that the VM is using, such as persistent disks and static IP addresses, will continue to be charged until they are deleted. For more information, seeStopping an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       StopInstanceRequest request =
           StopInstanceRequest.newBuilder()
               .setDiscardLocalSsd(true)
               .setInstance("instance555127957")
               .setNoGracefulShutdown(true)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.stopOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendAsync(SuspendInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> suspendAsync(SuspendInstanceRequest request)

This method suspends a running instance, saving its state to persistent storage, and allows you to resume the instance at a later time. Suspended instances have no compute costs (cores or RAM), and incur only storage charges for the saved VM memory and localSSD data. Any charged resources the virtual machine was using, such as persistent disks and static IP addresses, will continue to be charged while the instance is suspended. For more information, see Suspending and resuming an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SuspendInstanceRequest request =
           SuspendInstanceRequest.newBuilder()
               .setDiscardLocalSsd(true)
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.suspendAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SuspendInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SuspendInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendAsync(String project, String zone, String instance)
    
    
    public final OperationFuture<Operation,Operation> suspendAsync(String project, String zone, String instance)

This method suspends a running instance, saving its state to persistent storage, and allows you to resume the instance at a later time. Suspended instances have no compute costs (cores or RAM), and incur only storage charges for the saved VM memory and localSSD data. Any charged resources the virtual machine was using, such as persistent disks and static IP addresses, will continue to be charged while the instance is suspended. For more information, see Suspending and resuming an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Operation response = instancesClient.suspendAsync(project, zone, instance).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance resource to suspend.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendCallable()
    
    
    public final UnaryCallable<SuspendInstanceRequest,Operation> suspendCallable()

This method suspends a running instance, saving its state to persistent storage, and allows you to resume the instance at a later time. Suspended instances have no compute costs (cores or RAM), and incur only storage charges for the saved VM memory and localSSD data. Any charged resources the virtual machine was using, such as persistent disks and static IP addresses, will continue to be charged while the instance is suspended. For more information, see Suspending and resuming an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SuspendInstanceRequest request =
           SuspendInstanceRequest.newBuilder()
               .setDiscardLocalSsd(true)
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.suspendCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SuspendInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SuspendInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendOperationCallable()
    
    
    public final OperationCallable<SuspendInstanceRequest,Operation,Operation> suspendOperationCallable()

This method suspends a running instance, saving its state to persistent storage, and allows you to resume the instance at a later time. Suspended instances have no compute costs (cores or RAM), and incur only storage charges for the saved VM memory and localSSD data. Any charged resources the virtual machine was using, such as persistent disks and static IP addresses, will continue to be charged while the instance is suspended. For more information, see Suspending and resuming an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       SuspendInstanceRequest request =
           SuspendInstanceRequest.newBuilder()
               .setDiscardLocalSsd(true)
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.suspendOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SuspendInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SuspendInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### testIamPermissions(TestIamPermissionsInstanceRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsInstanceRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       TestIamPermissionsInstanceRequest request =
           TestIamPermissionsInstanceRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       TestPermissionsResponse response = instancesClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           instancesClient.testIamPermissions(
               project, zone, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsInstanceRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       TestIamPermissionsInstanceRequest request =
           TestIamPermissionsInstanceRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<TestPermissionsResponse> future =
           instancesClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInstanceRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### updateAccessConfigAsync(UpdateAccessConfigInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAccessConfigAsync(UpdateAccessConfigInstanceRequest request)

Updates the specified access config from an instance's network interface with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateAccessConfigInstanceRequest request =
           UpdateAccessConfigInstanceRequest.newBuilder()
               .setAccessConfigResource(AccessConfig.newBuilder().build())
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.updateAccessConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateAccessConfigInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAccessConfigAsync(String project, String zone, String instance, String networkInterface, AccessConfig accessConfigResource)
    
    
    public final OperationFuture<Operation,Operation> updateAccessConfigAsync(String project, String zone, String instance, String networkInterface, AccessConfig accessConfigResource)

Updates the specified access config from an instance's network interface with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       String networkInterface = "networkInterface-341981525";
       AccessConfig accessConfigResource = AccessConfig.newBuilder().build();
       Operation response =
           instancesClient
               .updateAccessConfigAsync(
                   project, zone, instance, networkInterface, accessConfigResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instance name for this request.  
`networkInterface` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network interface where the access config is attached.  
`accessConfigResource` | `[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAccessConfigCallable()
    
    
    public final UnaryCallable<UpdateAccessConfigInstanceRequest,Operation> updateAccessConfigCallable()

Updates the specified access config from an instance's network interface with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateAccessConfigInstanceRequest request =
           UpdateAccessConfigInstanceRequest.newBuilder()
               .setAccessConfigResource(AccessConfig.newBuilder().build())
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.updateAccessConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateAccessConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAccessConfigOperationCallable()
    
    
    public final OperationCallable<UpdateAccessConfigInstanceRequest,Operation,Operation> updateAccessConfigOperationCallable()

Updates the specified access config from an instance's network interface with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateAccessConfigInstanceRequest request =
           UpdateAccessConfigInstanceRequest.newBuilder()
               .setAccessConfigResource(AccessConfig.newBuilder().build())
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.updateAccessConfigOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateAccessConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(UpdateInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateInstanceRequest request)

Updates an instance only if the necessary resources are available. This method can update only a specific set of instance properties. See Updating a running instance for a list of updatable instance properties.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setDiscardLocalSsd(true)
               .setInstance("instance555127957")
               .setInstanceResource(Instance.newBuilder().build())
               .setMinimalAction("minimalAction624261943")
               .setMostDisruptiveAllowedAction("mostDisruptiveAllowedAction-1597376488")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String zone, String instance, Instance instanceResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String zone, String instance, Instance instanceResource)

Updates an instance only if the necessary resources are available. This method can update only a specific set of instance properties. See Updating a running instance for a list of updatable instance properties.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       Instance instanceResource = Instance.newBuilder().build();
       Operation response =
           instancesClient.updateAsync(project, zone, instance, instanceResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance resource to update.  
`instanceResource` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateInstanceRequest,Operation> updateCallable()

Updates an instance only if the necessary resources are available. This method can update only a specific set of instance properties. See Updating a running instance for a list of updatable instance properties.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setDiscardLocalSsd(true)
               .setInstance("instance555127957")
               .setInstanceResource(Instance.newBuilder().build())
               .setMinimalAction("minimalAction624261943")
               .setMostDisruptiveAllowedAction("mostDisruptiveAllowedAction-1597376488")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instancesClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateDisplayDeviceAsync(UpdateDisplayDeviceInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateDisplayDeviceAsync(UpdateDisplayDeviceInstanceRequest request)

Updates the Display config for a VM instance. You can only use this method on a stopped VM instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateDisplayDeviceInstanceRequest request =
           UpdateDisplayDeviceInstanceRequest.newBuilder()
               .setDisplayDeviceResource(DisplayDevice.newBuilder().build())
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.updateDisplayDeviceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDisplayDeviceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateDisplayDeviceInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateDisplayDeviceAsync(String project, String zone, String instance, DisplayDevice displayDeviceResource)
    
    
    public final OperationFuture<Operation,Operation> updateDisplayDeviceAsync(String project, String zone, String instance, DisplayDevice displayDeviceResource)

Updates the Display config for a VM instance. You can only use this method on a stopped VM instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       DisplayDevice displayDeviceResource = DisplayDevice.newBuilder().build();
       Operation response =
           instancesClient
               .updateDisplayDeviceAsync(project, zone, instance, displayDeviceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance scoping this request.  
`displayDeviceResource` | `[DisplayDevice](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisplayDevice)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateDisplayDeviceCallable()
    
    
    public final UnaryCallable<UpdateDisplayDeviceInstanceRequest,Operation> updateDisplayDeviceCallable()

Updates the Display config for a VM instance. You can only use this method on a stopped VM instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateDisplayDeviceInstanceRequest request =
           UpdateDisplayDeviceInstanceRequest.newBuilder()
               .setDisplayDeviceResource(DisplayDevice.newBuilder().build())
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.updateDisplayDeviceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDisplayDeviceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateDisplayDeviceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateDisplayDeviceOperationCallable()
    
    
    public final OperationCallable<UpdateDisplayDeviceInstanceRequest,Operation,Operation> updateDisplayDeviceOperationCallable()

Updates the Display config for a VM instance. You can only use this method on a stopped VM instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateDisplayDeviceInstanceRequest request =
           UpdateDisplayDeviceInstanceRequest.newBuilder()
               .setDisplayDeviceResource(DisplayDevice.newBuilder().build())
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.updateDisplayDeviceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDisplayDeviceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateDisplayDeviceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateNetworkInterfaceAsync(UpdateNetworkInterfaceInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateNetworkInterfaceAsync(UpdateNetworkInterfaceInstanceRequest request)

Updates an instance's network interface. This method can only update an interface's alias IP range and attached network. See Modifying alias IP ranges for an existing instance for instructions on changing alias IP ranges. See Migrating a VM between networks for instructions on migrating an interface. This method follows PATCH semantics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateNetworkInterfaceInstanceRequest request =
           UpdateNetworkInterfaceInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setNetworkInterfaceResource(NetworkInterface.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.updateNetworkInterfaceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateNetworkInterfaceInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateNetworkInterfaceAsync(String project, String zone, String instance, String networkInterface, NetworkInterface networkInterfaceResource)
    
    
    public final OperationFuture<Operation,Operation> updateNetworkInterfaceAsync(String project, String zone, String instance, String networkInterface, NetworkInterface networkInterfaceResource)

Updates an instance's network interface. This method can only update an interface's alias IP range and attached network. See Modifying alias IP ranges for an existing instance for instructions on changing alias IP ranges. See Migrating a VM between networks for instructions on migrating an interface. This method follows PATCH semantics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       String networkInterface = "networkInterface-341981525";
       NetworkInterface networkInterfaceResource = NetworkInterface.newBuilder().build();
       Operation response =
           instancesClient
               .updateNetworkInterfaceAsync(
                   project, zone, instance, networkInterface, networkInterfaceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instance name for this request.  
`networkInterface` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network interface to update.  
`networkInterfaceResource` | `[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateNetworkInterfaceCallable()
    
    
    public final UnaryCallable<UpdateNetworkInterfaceInstanceRequest,Operation> updateNetworkInterfaceCallable()

Updates an instance's network interface. This method can only update an interface's alias IP range and attached network. See Modifying alias IP ranges for an existing instance for instructions on changing alias IP ranges. See Migrating a VM between networks for instructions on migrating an interface. This method follows PATCH semantics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateNetworkInterfaceInstanceRequest request =
           UpdateNetworkInterfaceInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setNetworkInterfaceResource(NetworkInterface.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.updateNetworkInterfaceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateNetworkInterfaceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateNetworkInterfaceOperationCallable()
    
    
    public final OperationCallable<UpdateNetworkInterfaceInstanceRequest,Operation,Operation> updateNetworkInterfaceOperationCallable()

Updates an instance's network interface. This method can only update an interface's alias IP range and attached network. See Modifying alias IP ranges for an existing instance for instructions on changing alias IP ranges. See Migrating a VM between networks for instructions on migrating an interface. This method follows PATCH semantics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateNetworkInterfaceInstanceRequest request =
           UpdateNetworkInterfaceInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setNetworkInterface("networkInterface-341981525")
               .setNetworkInterfaceResource(NetworkInterface.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.updateNetworkInterfaceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateNetworkInterfaceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateInstanceRequest,Operation,Operation> updateOperationCallable()

Updates an instance only if the necessary resources are available. This method can update only a specific set of instance properties. See Updating a running instance for a list of updatable instance properties.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setDiscardLocalSsd(true)
               .setInstance("instance555127957")
               .setInstanceResource(Instance.newBuilder().build())
               .setMinimalAction("minimalAction624261943")
               .setMostDisruptiveAllowedAction("mostDisruptiveAllowedAction-1597376488")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateShieldedInstanceConfigAsync(UpdateShieldedInstanceConfigInstanceRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateShieldedInstanceConfigAsync(UpdateShieldedInstanceConfigInstanceRequest request)

Updates the Shielded Instance config for an instance. You can only use this method on a stopped instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateShieldedInstanceConfigInstanceRequest request =
           UpdateShieldedInstanceConfigInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setShieldedInstanceConfigResource(ShieldedInstanceConfig.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = instancesClient.updateShieldedInstanceConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateShieldedInstanceConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateShieldedInstanceConfigInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateShieldedInstanceConfigAsync(String project, String zone, String instance, ShieldedInstanceConfig shieldedInstanceConfigResource)
    
    
    public final OperationFuture<Operation,Operation> updateShieldedInstanceConfigAsync(String project, String zone, String instance, ShieldedInstanceConfig shieldedInstanceConfigResource)

Updates the Shielded Instance config for an instance. You can only use this method on a stopped instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instance = "instance555127957";
       ShieldedInstanceConfig shieldedInstanceConfigResource =
           ShieldedInstanceConfig.newBuilder().build();
       Operation response =
           instancesClient
               .updateShieldedInstanceConfigAsync(
                   project, zone, instance, shieldedInstanceConfigResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the instance scoping this request.  
`shieldedInstanceConfigResource` | `[ShieldedInstanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShieldedInstanceConfig)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateShieldedInstanceConfigCallable()
    
    
    public final UnaryCallable<UpdateShieldedInstanceConfigInstanceRequest,Operation> updateShieldedInstanceConfigCallable()

Updates the Shielded Instance config for an instance. You can only use this method on a stopped instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateShieldedInstanceConfigInstanceRequest request =
           UpdateShieldedInstanceConfigInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setShieldedInstanceConfigResource(ShieldedInstanceConfig.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instancesClient.updateShieldedInstanceConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateShieldedInstanceConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateShieldedInstanceConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateShieldedInstanceConfigOperationCallable()
    
    
    public final OperationCallable<UpdateShieldedInstanceConfigInstanceRequest,Operation,Operation> updateShieldedInstanceConfigOperationCallable()

Updates the Shielded Instance config for an instance. You can only use this method on a stopped instance. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstancesClient instancesClient = InstancesClient.create()) {
       UpdateShieldedInstanceConfigInstanceRequest request =
           UpdateShieldedInstanceConfigInstanceRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setShieldedInstanceConfigResource(ShieldedInstanceConfig.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instancesClient.updateShieldedInstanceConfigOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateShieldedInstanceConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateShieldedInstanceConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
