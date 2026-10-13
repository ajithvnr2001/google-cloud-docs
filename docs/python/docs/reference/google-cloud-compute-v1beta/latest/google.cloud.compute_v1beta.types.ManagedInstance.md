---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ManagedInstance
title: Class ManagedInstance (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:12.929809+00:00
---

# Class ManagedInstance (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ManagedInstance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ManagedInstance (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    ManagedInstance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A Managed Instance resource.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`all_instances_config` |  `[google.cloud.compute_v1beta.types.ManagedInstanceAllInstancesConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ManagedInstanceAllInstancesConfig)`   
Output only. [Output Only] Current all-instances configuration revision applied to this instance. This field is a member of `oneof`_ `_all_instances_config`.   
`current_action` |  `str`   
Output only. [Output Only] The current action that the managed instance group has scheduled for the instance. Possible values: :: \- NONE The instance is running, and the managed instance group does not have any scheduled actions for this instance. \- CREATING The managed instance group is creating this instance. If the group fails to create this instance, it will try again until it is successful. \- CREATING_WITHOUT_RETRIES The managed instance group is attempting to create this instance only once. If the group fails to create this instance, it does not try again and the group'stargetSize value is decreased instead. \- RECREATING The managed instance group is recreating this instance. \- DELETING The managed instance group is permanently deleting this instance. \- ABANDONING The managed instance group is abandoning this instance. The instance will be removed from the instance group and from any target pools that are associated with this group. \- RESTARTING The managed instance group is restarting the instance. \- REFRESHING The managed instance group is applying configuration changes to the instance without stopping it. For example, the group can update the target pool list for an instance without stopping that instance. \- VERIFYING The managed instance group has created the instance and it is in the process of being verified. Check the CurrentAction enum for the list of possible values. This field is a member of `oneof`_ `_current_action`.   
`id` |  `int`   
Output only. [Output only] The unique identifier for this resource. This field is empty when instance does not exist. This field is a member of `oneof`_ `_id`.   
`instance` |  `str`   
Output only. [Output Only] The URL of the instance. The URL can exist even if the instance has not yet been created. This field is a member of `oneof`_ `_instance`.   
`instance_health` |  `MutableSequence[[google.cloud.compute_v1beta.types.ManagedInstanceInstanceHealth](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ManagedInstanceInstanceHealth)]`   
Output only. [Output Only] Health state of the instance per health-check.   
`instance_status` |  `str`   
Output only. [Output Only] The status of the instance. This field is empty when the instance does not exist. Check the InstanceStatus enum for the list of possible values. This field is a member of `oneof`_ `_instance_status`.   
`last_attempt` |  `[google.cloud.compute_v1beta.types.ManagedInstanceLastAttempt](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ManagedInstanceLastAttempt)`   
Output only. [Output Only] Information about the last attempt to create or delete the instance. This field is a member of `oneof`_ `_last_attempt`.   
`name` |  `str`   
Output only. [Output Only] The name of the instance. The name always exists even if the instance has not yet been created. This field is a member of `oneof`_ `_name`.   
`preserved_state_from_config` |  `[google.cloud.compute_v1beta.types.PreservedState](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PreservedState)`   
Output only. [Output Only] Preserved state applied from per-instance config for this instance. This field is a member of `oneof`_ `_preserved_state_from_config`.   
`preserved_state_from_policy` |  `[google.cloud.compute_v1beta.types.PreservedState](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PreservedState)`   
Output only. [Output Only] Preserved state generated based on stateful policy for this instance. This field is a member of `oneof`_ `_preserved_state_from_policy`.   
`properties_from_flexibility_policy` |  `[google.cloud.compute_v1beta.types.ManagedInstancePropertiesFromFlexibilityPolicy](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ManagedInstancePropertiesFromFlexibilityPolicy)`   
Output only. [Output Only] Instance properties selected for this instance resulting from InstanceFlexibilityPolicy. This field is a member of `oneof`_ `_properties_from_flexibility_policy`.   
`scheduling` |  `[google.cloud.compute_v1beta.types.ManagedInstanceScheduling](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ManagedInstanceScheduling)`   
Output only. Information about the termination timestamp of the instance, if applicable. This field is a member of `oneof`_ `_scheduling`.   
`shutdown_details` |  `[google.cloud.compute_v1beta.types.ManagedInstanceShutdownDetails](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ManagedInstanceShutdownDetails)`   
Output only. Specifies the graceful shutdown details if the instance is in `PENDING_STOP` state or there is a programmed stop scheduled. This field is a member of `oneof`_ `_shutdown_details`.   
`target_status` |  `str`   
Output only. The eventual status of the instance. The instance group manager will not be identified as stable till each managed instance reaches its targetStatus. Check the TargetStatus enum for the list of possible values. This field is a member of `oneof`_ `_target_status`.   
`version` |  `[google.cloud.compute_v1beta.types.ManagedInstanceVersion](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ManagedInstanceVersion)`   
Output only. [Output Only] Intended version of this instance. This field is a member of `oneof`_ `_version`.   
  
## Classes 

### CurrentAction
    
    
    CurrentAction(value)

Output only. [Output Only] The current action that the managed instance group has scheduled for the instance. Possible values:

::

  * NONE The instance is running, and the managed instance group does not have any scheduled actions for this instance.
  * CREATING The managed instance group is creating this instance. If the group fails to create this instance, it will try again until it is successful.
  * CREATING_WITHOUT_RETRIES The managed instance group is attempting to create this instance only once. If the group fails to create this instance, it does not try again and the group'stargetSize value is decreased instead.
  * RECREATING The managed instance group is recreating this instance.
  * DELETING The managed instance group is permanently deleting this instance.
  * ABANDONING The managed instance group is abandoning this instance. The instance will be removed from the instance group and from any target pools that are associated with this group.
  * RESTARTING The managed instance group is restarting the instance.
  * REFRESHING The managed instance group is applying configuration changes to the instance without stopping it. For example, the group can update the target pool list for an instance without stopping that instance.
  * VERIFYING The managed instance group has created the instance and it is in the process of being verified.



Additional supported values which may be not listed in the enum directly due to technical reasons: STOPPING SUSPENDING
    
    
         1. Waiting until health check specified as part
            of this managed instance     group's
            autohealing policy reports HEALTHY.
            Note: Applies only if autohealing policy has
            a health check specified
         2. Waiting for addition verification steps
            performed as post-instance     creation
            (subject to future extensions).
    

### InstanceStatus
    
    
    InstanceStatus(value)

Output only. [Output Only] The status of the instance. This field is empty when the instance does not exist. Additional supported values which may be not listed in the enum directly due to technical reasons: RUNNING STOPPED SUSPENDED

### TargetStatus
    
    
    TargetStatus(value)

Output only. The eventual status of the instance. The instance group manager will not be identified as stable till each managed instance reaches its targetStatus. Additional supported values which may be not listed in the enum directly due to technical reasons:

RUNNING STOPPED SUSPENDED

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
