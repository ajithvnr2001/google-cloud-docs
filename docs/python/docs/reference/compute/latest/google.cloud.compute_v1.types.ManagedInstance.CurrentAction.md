---
url: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ManagedInstance.CurrentAction
title: Class CurrentAction (1.56.0rc1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:47.047514+00:00
---

# Class CurrentAction (1.56.0rc1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ManagedInstance.CurrentAction

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CurrentAction (1.56.0rc1) Stay organized with collections  Save and categorize content based on your preferences. 

1.56.0-rc1  1.55.0 (latest)  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.2  1.18.0  1.17.0  1.16.1  1.15.0  1.14.1  1.13.0  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 
    
    
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
    

## Enums  
  
---  
**Name** | **Description**  
`UNDEFINED_CURRENT_ACTION` | A value indicating that the enum field is not set.  
`ABANDONING` | The managed instance group is abandoning this instance. The instance will be removed from the instance group and from any target pools that are associated with this group.  
`CREATING` | The managed instance group is creating this instance. If the group fails to create this instance, it will try again until it is successful.  
`CREATING_WITHOUT_RETRIES` | The managed instance group is attempting to create this instance only once. If the group fails to create this instance, it does not try again and the group's targetSize value is decreased.  
`DELETING` | The managed instance group is permanently deleting this instance.  
`NONE` | The managed instance group has not scheduled any actions for this instance.  
`RECREATING` | The managed instance group is recreating this instance.  
`REFRESHING` | The managed instance group is applying configuration changes to the instance without stopping it. For example, the group can update the target pool list for an instance without stopping that instance.  
`RESTARTING` | The managed instance group is restarting this instance.  
`RESUMING` | The managed instance group is resuming this instance.  
`STARTING` | The managed instance group is starting this instance.  
`VERIFYING` | The managed instance group is verifying this already created instance. Verification happens every time the instance is (re)created or restarted and consists of:  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
