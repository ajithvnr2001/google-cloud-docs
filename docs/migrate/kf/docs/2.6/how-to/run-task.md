---
url: https://docs.cloud.google.com/migrate/kf/docs/2.6/how-to/run-task/
title: Run Tasks \u00a0|\u00a0 Kf 2.6 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:27:17.867247+00:00
---

# Run Tasks  |  Kf 2.6  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.6/how-to/run-task/

Version 2.6

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.6 ](https://docs.cloud.google.com/migrate/kf/docs/2.6)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.6/getting-started)



Send feedback 

#  Run Tasks Stay organized with collections  Save and categorize content based on your preferences. 

You can execute short-lived workflows by running them as Tasks in Kf. Tasks are run under Apps, meaning that each Task must have an associated App. Each Task execution uses the build artifacts from the parent App. Because Tasks are short-lived, the App is not deployed as a long-running application, and no routes should be created for the App or the Task.

## Push an App for running Tasks

  1. Clone the [test-app repo](https://github.com/cloudfoundry-samples/test-app) repo:
         
         git clone https://github.com/cloudfoundry-samples/test-app test-app
         cd test-app

  2. Push the App.

Push the App with the `kf push APP_NAME --task` command. The `--task` flag indicates that the App is meant to be used for running Tasks, and thus no routes are created on the App, and it is not deployed as a long-running application:
         
         kf push test-app --task

  3. Confirm that no App instances or routes were created by listing the App:
         
         kf apps

Notice that the App is not started and has no URLs:
         
         Listing Apps in Space: test-space
         Name                     Instances  Memory  Disk  CPU   URLs
         test-app                 stopped    1Gi     1Gi   100m  <nil>
         




## Run a Task on the App

When you run a Task on the App, you can optionally specify a start command by using the `--command` flag. If no start command is specified, it uses the start command specified on the App. If the App doesn't have a start command specified, it looks up the CMD configuration of the container image. A start command must exist in order to run the Task successfully.
    
    
    kf run-task test-app --command "printenv"

You see something similar to this, confirming that the Task was submitted:
    
    
    Task test-app-gd8dv is submitted successfully for execution.
    

The Task name is automatically generated, prefixed with the App name, and suffixed with an arbitrary string. The Task name is a unique identifier for Tasks within the same cluster.

## Specify Task resource limits

Resource limits (such as CPU cores/Memory limit/Disk quota) can be specified in the App (during `kf push`) or during the `kf run-task` command. The limits specified in the `kf run-task` command take prededence over the limits specified on the App.

To specify resource limits in an App, you can use the `--cpu-cores`, `--memory-limit`, and `--disk-quota` flags in the `kf push` command:
    
    
    kf push test-app --command "printenv" --cpu-cores=0.5 --memory-limit=2G --disk-quota=5G --task

To override these limits in the App, you can use the `--cpu-cores`, `--memory-limit`, and `--disk-quota` flags in the `kf run-task` command:
    
    
    kf run-task test-app --command "printenv" --cpu-cores=0.5 --memory-limit=2G --disk-quota=5G

## Specify a custom display name for a Task

You can optionally use the `--name` flag to specify a custom display name for a Task for easier identification/grouping:
    
    
    $ kf run-task test-app --command "printenv" --name foo
    Task test-app-6swct is submitted successfully for execution.
    
    $ kf tasks test-app
    Listing Tasks in Space: test space
    Name              ID  DisplayName        Age    Duration  Succeeded  Reason
    test-app-6swct    3   foo                1m     21s       True       <nil>
    

## Manage Tasks

View all Tasks of an App with the `kf tasks APP_NAME` command:
    
    
    $ kf tasks test-app
    Listing Tasks in Space: test space
    Name              ID  DisplayName        Age    Duration  Succeeded  Reason
    test-app-gd8dv    1   test-app-gd8dv     1m     21s       True       <nil>
    

## Cancel a Task

Cancel an active Task by using the `kf terminate-task` command:

  * Cancel a Task by Task name:
        
        $ kf terminate-task test-app-6w6mz
        Task "test-app-6w6mz" is successfully submitted for termination
        

  * Or cancel a Task by `APP_NAME` \+ Task ID:
        
        $ kf terminate-task test-app 2
        Task "test-app-6w6mz" is successfully submitted for termination
        


**Note:** You can only cancel Tasks that are pending/running. Completed Tasks are not cancellable.

Cancelled Tasks have `PipelineRunCancelled` status.
    
    
    $ kf tasks test-app
    Listing Tasks in Space: test space
    Name              ID  DisplayName        Age    Duration  Succeeded  Reason
    test-app-gd8dv    1   test-app-gd8dv     1m     21s       True       <nil>
    test-app-6w6mz    2   test-app-6w6mz     38s    11s       False      PipelineRunCancelled
    

## View Task logs

View logs of a Task by using the `kf logs APP_NAME --task` command:
    
    
    $ kf logs test-app --task

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
