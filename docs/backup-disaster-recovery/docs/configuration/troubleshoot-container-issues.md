---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/troubleshoot-container-issues/
title: Troubleshoot container issues \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:35.247092+00:00
---

# Troubleshoot container issues  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/troubleshoot-container-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Troubleshoot container issues Stay organized with collections  Save and categorize content based on your preferences. 

**Issue** : The pod fails to start the application and it is not able to consume data mounted from the backup/recovery appliance. This is happening due to the differences in the `user ID` with which all the application processes ran on the source machine—from where the data was captured—and the one with which they are run on the Pod.

**Solution** : Explicitly set the security context for a pod and specify the appropriate user ID value for **runAsUser** field in the pod's YAML file. For example, if the MySQL application on the source host ran all the processes with the user ID of 997, then it is recommended to set the security context for the pod to use the same user ID 997. This could be done by specifying the following steps in the "spec" section of the Pod's YAML file.

See [Configure a Security Context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod) for more information. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
