---
url: https://docs.cloud.google.com/migrate/kf/docs/2.11/how-to/autoscaling/
title: Manage autoscaling \u00a0|\u00a0 Kf 2.11 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:45.172678+00:00
---

# Manage autoscaling  |  Kf 2.11  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.11/how-to/autoscaling/

Version 2.11 - Latest version

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
  * [ 2.11 ](https://docs.cloud.google.com/migrate/kf/docs/2.11)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.11/getting-started)



Send feedback 

#  Manage autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

Kf Apps can be automatically scaled based on CPU usage. You can configure autoscaling limits for your Apps and the target CPU usage for each App instance. Kf automatically scales your Apps up and down in response to demand.

By default, autoscaling is disabled. Follow the steps below to enable autoscaling.

## View Apps

You can view the autoscaling status for an App using the `kf apps` command. If autoscaling is enabled for an App, `Instances` includes the autoscaling status.
    
    
    $ kf apps
    
    Name   Instances              Memory  Disk  CPU
    app1   4 (autoscaled 4 to 5)  256Mi   1Gi   100m
    app2   1                      256Mi   1Gi   100m
    

Autoscaling is enabled for `app1` with `min-instances` set to 4 and `max-instances` set to 5. Autoscaling is disabled for `app2`.

## Update autoscaling limits

You can update the instance limits using the `kf update-autoscaling-limits` command.
    
    
    kf update-autoscaling-limits app-name min-instances max-instances

## Create autoscaling rule

You can create autoscaling rules using the `kf create-autoscaling-rule` command.
    
    
    kf create-autoscaling-rule app-name CPU min-threshold max-threshold

## Delete autoscaling rules

You can delete all autoscaling rules with the `kf delete-autoscaling-rule` command. Kf only supports one autoscaling rule.
    
    
    kf delete-autoscaling-rules app-name

## Enable and disable autoscaling

Autoscaling can be enabled by using `enable-autoscaling` and disabled by using `disable-autoscaling`. When it is disabled, the configurations, including limits and rules, are preserved.
    
    
    kf enable-autoscaling app-name
    kf disable-autoscaling app-name

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
