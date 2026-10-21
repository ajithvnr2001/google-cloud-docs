---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cronjobs/
title: CronJobs \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:33:15.441567+00:00
---

# CronJobs  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cronjobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  CronJobs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

CronJobs is generally available (GA) in Google Kubernetes Engine (GKE) version 1.21 and later. This document explains how to run CronJobs in GKE. CronJobs are a built-in feature of Kubernetes. For more details, see the [Kubernetes documentation about CronJobs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/).

## Overview

CronJobs create Kubernetes [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/) on a repeating schedule. CronJobs allow you to automate regular tasks like making backups, creating reports, sending emails, or cleanup tasks.

CronJobs are created, managed, scaled, and deleted in the same way as Jobs. The exact number of Job objects created depends on several factors. For more information, see [CronJob limitations](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#cron-job-limitations).

For more information about Jobs, see [Running a Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Creating a CronJob

You can create a CronJob using a manifest file. For example, the following YAML manifest prints the current time and a string once every minute, while retaining the default values for CronJob parameters:
    
    
    # cronjob.yaml
    apiVersion: batch/v1
    kind: CronJob
    metadata:
      name: hello
    spec:
      schedule: "*/1 * * * *"
      concurrencyPolicy: Allow
      startingDeadlineSeconds: 100
      suspend: false
      successfulJobsHistoryLimit: 3
      failedJobsHistoryLimit: 1
      jobTemplate:
        spec:
          template:
            spec:
              containers:
              - name: hello
                image: busybox
                **args :
                - /bin/sh
                - -c
                - date; echo "Hello, World!"**
              restartPolicy: OnFailure
    

**Note:** If your cluster runs GKE versions prior to 1.21, specify `batch/v1beta1` in the `apiVersion` field.

To create this CronJob, save the YAML manifest to a file and apply it to the cluster:
    
    
    kubectl apply -f PATH_TO_FILE
    

Replace `PATH_TO_FILE` with the path to the YAML manifest.

## Configuring a CronJob

You can specify the following parameters when you create a CronJob:

  * When the CronJob runs
  * What the CronJob does
  * The deadline for the CronJob to start
  * Whether concurrent Jobs are allowed for the CronJob
  * Whether new Jobs are suspended
  * How many executions the CronJob saves in its history



### Specifying when the CronJob runs

The `spec.schedule` field defines when, and how often, the CronJob runs, using Unix standard [`crontab`](https://en.wikipedia.org/wiki/Cron#Overview) format. All CronJob times are in UTC. There are five fields, separated by spaces. These fields represent the following:

  1. Minutes (between 0 and 59)
  2. Hours (between 0 and 23)
  3. Day of the month (between 1 and 31)
  4. Month (between 1 and 12)
  5. Day of the week (between 0 and 6 starting on Sunday)



You can use the following special characters in any of the `spec.schedule` fields:

  * `?` is a wildcard value that matches a single character.
  * `*` is a wildcard value that matches zero or more characters.
  * `/` allows you to specify an interval for a field. For example, if the first field (the minutes field) has a value of `*/5`, it means "every 5 minutes". If the fifth field (the day-of-week field) is set to `0/5`, it means "every fifth Sunday".



### Specifying what the CronJob runs

The `spec.jobTemplate` describes what the CronJob does, including its container images, the commands the containers execute, and the restart policy for the CronJob. For more details on what to include in the `spec.jobTemplate`, see the [Kubernetes CronJob documentation](https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/#job-template).

### Specifying a deadline

The optional `startingDeadlineSeconds` field indicates the maximum number of seconds the CronJob can take to start if it misses its scheduled time for any reason. Missed CronJobs are considered failures.

To specify a deadline, add the `startingDeadlineSeconds` value to the CronJob's `spec` field in the manifest file. For example, the following manifest specifies that the CronJob has 100 seconds to begin:
    
    
    apiVersion: batch/v1
    kind: CronJob
    metadata:
      name: hello
    spec:
      schedule: "*/1 * * * *"
      **startingDeadlineSeconds: 100**
      jobTemplate:
        spec:
        ...
    

**Note:** If you specify an empty value for the `startingDeadlineSeconds` field, the CronJob never times out. This could lead to the same CronJob running multiple times simultaneously. You can prevent this by specifying a concurrency policy.

### Specifying a concurrency policy

The optional `spec.concurrencyPolicy` field specifies how to treat concurrent executions of a Job created by the CronJob controller. If you do not set a value, multiple concurrent Jobs are allowed by default.

`concurrencyPolicy` accepts the following values:

Value | Meaning  
---|---  
`Allow` | Concurrent Jobs are allowed. This is the default.  
`Forbid` | Concurrent Jobs are forbidden, and new Jobs can't start until previous ones have completed or timed out.  
`Replace` | Concurrent Jobs are forbidden, and old Jobs are cancelled in favor of new ones.  
  
### Suspending subsequent executions

The optional `spec.suspend` field, when set to `true`, prevents new Jobs from being run, but allows current executions to finish.

### Specifying history limits

A CronJob creates a Pod each time it runs. Viewing the termination status of a CronJob's recent executions, as well as the logs of an individual Pod, are covered in Viewing CronJob history.

You can configure the number of successful and failed CronJob executions that are saved by specifying values for `spec.successfulJobsHistoryLimit` and `spec.failedJobsHistoryLimit`. By default, `successfulJobsHistoryLimit` is set to 3 and `failedJobsHistoryLimit` is set to 1.

For example, the following manifest instructs GKE to save a maximum of five successful CronJob executions and a maximum of 10 failed CronJob executions:
    
    
    apiVersion: batch/v1
    kind: CronJob
    metadata:
      name: hello
    spec:
      schedule: "*/1 * * * *"
      startingDeadlineSeconds: 100
      **successfulJobsHistoryLimit: 5
      failedJobsHistoryLimit: 10**
      jobTemplate:
        spec:
        ...
    

You can disable retention of successful or failed CronJob execution history by setting the respective value to `0`. Disabling history retention might make debugging failures more difficult. For example, the following manifest instructs GKE to only save failed CronJob executions:
    
    
    kind: CronJob
    metadata:
      name: hello
    spec:
      schedule: "*/1 * * * *"
      startingDeadlineSeconds: 100
      **successfulJobsHistoryLimit: 0**
      failedJobsHistoryLimit: 10
      jobTemplate:
        spec:
        ...
    

## Inspecting a CronJob

To check a CronJob's configuration, use `kubectl describe`:
    
    
    kubectl describe cronjob CRONJOB_NAME
    

Replace `CRONJOB_NAME` with the name of the CronJob to inspect.

## Viewing CronJob history

A CronJob runs within a Pod. By default, Kubernetes preserves the logs for terminated Pods representing the last three successful runs of a CronJob and the most recent failed Job. You can change or disable these defaults by changing the CronJob history limits.

To view a CronJob's history, first list all Pods. Completed CronJobs are shown with a status of `Completed`, and failed Jobs have a status of `RunContainerError`, `CrashLoopBackOff`, or another status indicating a failure.

**Note:** You may see more entries than you expect. CronJob history is subject to periodic garbage collection. For example, in the output below, four instances of the `hello` CronJob are shown.
    
    
    NAME                                READY   STATUS              RESTARTS   AGE
    hello-1556555640-9bc5r              0/1     Completed           0          3m6s
    hello-1556555700-cm6wk              0/1     Completed           0          2m6s
    hello-1556555760-62wf5              0/1     Completed           0          66s
    hello-1556555820-rl8kl              0/1     Completed           0          5s
    hello-failed-1556555820-wrvt2       0/1     RunContainerError   1          5s
    

You can cause a Job to fail on purpose by modifying the example manifest in Creating a CronJob. Change the `args` field in `spec.containers` to an invalid command or a path that doesn't exist, and change the `metadata.name` value to one that indicates that you are testing for failures. 

To view the logs for a specific CronJob, run the following command:
    
    
    kubectl logs POD_NAME
    

Replace `POD_NAME` with the name of the Pod you want to inspect.

The output is similar to the following:
    
    
    container_linux.go:247: starting container process caused
    "exec: \"/in/sh\": stat /in/sh: no such file or directory"
    

## Deleting a CronJob

To delete a CronJob, run the following command:
    
    
    kubectl delete cronjob CRONJOB_NAME
    

When you delete a CronJob, the Kubernetes garbage collector deletes the associated Jobs and prevents new Jobs from starting.

## What's next

  * Read the [Kubernetes documentation for CronJobs](https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/).
  * Learn how to [run a one-time Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
