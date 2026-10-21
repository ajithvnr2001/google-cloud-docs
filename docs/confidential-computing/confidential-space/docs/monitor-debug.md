---
url: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/monitor-debug/
title: Monitor and debug workloads \u00a0|\u00a0 Confidential Space \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:18:00.260134+00:00
---

# Monitor and debug workloads  |  Confidential Space  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/monitor-debug/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Confidential Space ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview)



Send feedback 

#  Monitor and debug workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Workload author ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview#roles) [ Workload operator ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview#roles)

When building, testing, and running a workload, it can be useful to monitor its progress to debug issues. The following tools are available to use for monitoring and debugging:

  * **Cloud Logging** : As the first step in troubleshooting a Confidential Space workload, you can [redirect `STDOUT` and `STDERR` to Cloud Logging](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/deploy-workloads#tee-container-log-redirect), and then check it for workload return codes to see where a failure occurred.

  * **The debug Confidential Space image** : The [debug Confidential Space image](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-images#types_of_images) keeps the Confidential VM running the workload operational after the workload has completed, and runs an SSH server. This lets you [remotely log into the VM](https://docs.cloud.google.com/compute/docs/instances/ssh) to diagnose issues. It's useful to use the debug image until you're confident that your code is behaving as it should. When it's time to start working on sensitive production data, switch to the production Confidential Space image.

  * **Memory usage monitoring** : You can view the memory usage of the workload in [Cloud Logging](https://docs.cloud.google.com/logging) or [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). The [workload author needs to allow it](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/reference/launch-policies#monitoring-memory-allow), and the [workload operator needs to enable it](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/reference/metadata-variables#tee-monitoring-memory-enable) before memory usage is tracked.

  * **Interactive shell** : After using SSH to connect to your workload Confidential VM, you can use the `sudo ctr task exec -t --exec-id shell tee-container bash` command to enter an interactive shell inside the container to diagnose workload issues.




## Logging

Like any command line program, the workload `STDOUT` and `STDERR` can be displayed in the console. It can also be redirected to Cloud Logging by the workload operator setting the [`tee-container-log-redirect`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/deploy-workloads#tee-container-log-redirect) metadata key to `true` or `cloud_logging` on the Confidential Space VM, and ensuring that the service account running the workload has the `logging.logWriter` role.

Redirection can be prevented by the workload author with the [`log_redirect` launch policy](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#log-redirect).

To reduce your risk profile, log the minimum amount of information, and don't log sensitive information.

### View Confidential Space logs

If the service account attached to your Confidential Space VM has been granted the `logging.logWriter` role and you've redirected logs to Cloud Logging, you can troubleshoot errors by viewing the VM's logs:

  1. Go to **Logging** in the workload operator's project in the Google Cloud console.

[Go to Logging](https://console.cloud.google.com/logs)

  2. Next to the **Query** tab, click the time range to set the logging period you want to view.

  3. Filter the logs by the following log fields if they're available:

     * **Resource type** : VM Instance

     * **Instance ID** : The instance ID of the Confidential VM

     * **Log name** : confidential-space-launcher

  4. Read the failure message to find out what the problem is. A resource might not have been set up properly, the attribute conditions in your data collaborators' WIP providers might not match the claims made by the Confidential Space workload, or the workload itself might have had an error.




## Return codes

Return codes are displayed in the console when running the [launcher](https://docs.cloud.google.com/docs/security/confidential-space#attestation-process) and workload, and can be redirected to Cloud Logging.

The return codes are described in the following table:

Code | Definition | VM stop behavior  
---|---|---  
0  | The workload completed successfully when using the production image. | The VM stops after the workload is complete.  
1  | The workload or launcher returned an error when using the production image. | The VM stops after it has returned an error.   
3  | The launcher has restarted after a failure due to its `tee-restart-policy`. | The VM is restarted.   
4  | The workload or launcher has finished running when using the debug image, and the VM is now idling. | The VM doesn't stop after the workload completes or returns an error. This is so you can debug the workload over SSH.  
  
If a workload fails, a workload operator only receives the message `workload finished with a non-zero return code`, without further context. For a production image, the launcher can be set to restart on failure with [`tee-restart-policy=OnFailure`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/deploy-workloads#tee-restart-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
