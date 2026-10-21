---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/diagnostic-collector/
title: Using the Diagnostic collector \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:20:30.936148+00:00
---

# Using the Diagnostic collector  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/diagnostic-collector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using the Diagnostic collector Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/diagnostic-collector.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/diagnostic-collector.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/diagnostic-collector.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/diagnostic-collector.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/diagnostic-collector.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/diagnostic-collector.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/diagnostic-collector.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/diagnostic-collector.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/diagnostic-collector.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/diagnostic-collector.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/diagnostic-collector.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/diagnostic-collector.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/diagnostic-collector.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/diagnostic-collector.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/diagnostic-collector.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/diagnostic-collector.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/diagnostic-collector.html)



The Diagnostic collector is a tool that captures diagnostic data on the Kubernetes components of an Apigee hybrid instance on demand, and stores them in Google Cloud storage buckets. You invoke the Diagnostic collector with the `apigeectl diagnostic` command. 

##  What System data is captured? 

Diagnostics collector captures following types of data: 

  * Changing Log levels.
  * Jstack.
  * POD configuration yaml.
  * PS -ef output.
  * TCP dump.
  * TOP output.



##  What happens to the data?

When the Diagnostic collector captures the data, it is uploaded to a storage bucket in your Google Cloud project. You can view the stored data in the [Google Cloud Platform: Cloud Storage browser](https://console.cloud.google.com/storage/browser/).

You can optionally choose to share this data with Google Apigee Support when you create a support ticket.

**Note:** No user runtime data or sensitive information is captured in the data collected by the Diagnostic collector.

##  Prerequisites for running Diagnostic collector 

Before using the Diagnostic collector, you must complete the following prerequisites: 

###  Google Cloud Storage bucket 

Create a Google Cloud Storage bucket with a unique name in your Google Cloud project. You can create and manage buckets with `gcloud storage` commands or in the [Google Cloud Platform: Cloud Storage browser](https://console.cloud.google.com/storage/browser/). 

For example: 
    
    
    gcloud storage buckets create gs://apigee_diagnostic_data
    
    
    Creating gs://apigee_diagnostic_data/...

Bucket names must be globally unique across all Google Cloud projects, including those outside of your organization.

See [Creating storage buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) for instructions.

###  Service account 

Create a service account with the **Storage Admin** role (`roles/storage.admin`) in your project, and download the service account `.json` key file. 

The service account can have any unique name. This guide uses "`apigee-diagnostic`" for the service account name. 

For example: 
    
    
    gcloud config set project ${PROJECT_ID}
    
    
    gcloud iam service-accounts create apigee-diagnostic
    
    
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="serviceAccount:apigee-diagnostic@${PROJECT_ID}.iam.gserviceaccount.com" \
        --role="roles/storage.admin"
    
    
    gcloud iam service-accounts keys create ${PROJECT_ID}-apigee-diagnostic.json \
        --iam-account=apigee-diagnostic@${PROJECT_ID}.iam.gserviceaccount.com

See:

  * [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).
  * [Creating and managing service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).
  * [Understanding roles: Cloud Storage roles](https://docs.cloud.google.com/iam/docs/roles-permissions/storage).



##  Using Diagnostic collector 

The sequence to use the Diagnostic collector is: 

  1. Configure the Diagnostic stanza in your `overrides.yaml` file to select the type of information, the Apigee container, and the individual pods you want diagnostic data from. See Configuring `overrides.yaml` for Diagnostic collector.
  2. Run Diagnostic collector with the following `apigeectl` command. 
         
         apigeectl diagnostic -f OVERRIDES_FILE

Where OVERRIDES_FILE is the path to your `overrides.yaml` file. 

  3. Check the logs: 
     1. Get the pods in the `apigee-diagnostic` namespace. 
            
            kubectl get pods -n apigee-diagnostic

     2. Make note of the pod with the name containing `diagnostic-collector`
     3. Check the logs with the following command: 
            
            kubectl -n apigee-diagnostic logs -f POD_NAME

Where POD_NAME is the name of the Diagnostic collector pod. 

You can also view the collected logs in the [Google Cloud Platform: Cloud Storage browser](https://console.cloud.google.com/storage/browser/). 

  4. After you have collected the data, delete the Diagnostic collector. You cannot run it again until you have deleted it. 
         
         apigeectl diagnostic delete -f OVERRIDES_FILE




##  Configuring `overrides.yaml` for Diagnostic collector 

Before you can run the Diagnostic collector, you need to configure it in your `overrides.yaml` file. 

For a complete reference of `diagnostic` configuration properties, see the [Configuration property reference: `diagnostic`.](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#diagnostic)

###  Required properties 

The following properties are required for the Diagnostic collector to run. 

  * `diagnostic.serviceAccountPath`: The path to a service account key file for the service account with the Storage Admin role in Prerequisites.
  * `diagnostic.operation`: Specifies whether to collect all statistics or just logs. 

Values are: `"ALL"` or `"LOGGING"`

If you set `diagnostic.operation` to `"LOGGING"`, the following properties are required:

    * `diagnostic.loggingDetails.logDuration`
    * `diagnostic.loggingDetails.loggerNames`
    * `diagnostic.loggingDetails.logLevel`
  * `diagnostic.bucket`: The name of the Google Cloud storage bucket where your diagnostic data will be deposited. This is the bucket you created in Prerequisites.
  * `diagnostic.container`: This specifies which type of pod you are capturing data from. The values can be one of: `container` value| Apigee component| Kubernetes namespace| Example pod name in this container  
---|---|---|---  
`apigee-cassandra` | Cassandra | `apigee` | `apigee-cassandra-default-0`  
`istio-proxy` | Istio ingress | `istio-system` | `istio-ingressgateway-696879cdf8-9zzzf`  
`apigee-mart-server` | MART | `apigee` | `apigee-mart-hybrid-example-d89fed1-151-jj2ux-l7nlb`  
`apigee-runtime` | Message Processor | `apigee` | `apigee-runtime-hybrid-example-3b2ebf3-151-s64bh-g9qmv`  
`apigee-synchronizer` | Synchronizer | `apigee` | `apigee-synchronizer-hybrid-example-3b2ebf3-151-xx4z6cg78`  
`apigee-udca` | UDCA | `apigee` | `apigee-udca-hybrid-example-3b2ebf3-151-q4g2c-vnzg9`  
`apigee-watcher` | Watcher | `apigee` | `apigee-watcher-hybrid-example-d89fed1-151-cpu3s-sxxdf`  
  * `diagnostic.namespace`: The Kubernetes namespace in which the pods you are collecting data on reside. The namespace must be the correct one for the container you specify with `diagnostic.container`.
  * `diagnostic.podNames`: The names of the individual pods on which you want to collect diagnostic data. For example: 
        
        diagnostic:
         …
         podNames:
         - apigee-runtime-hybrid-example-3b2ebf3-150-8vfoj-2wcjn
         - apigee-runtime-hybrid-example-3b2ebf3-150-8vfoj-6xzn2




###  Properties required only when the operation is set to `LOGGING`

The following properties are required only when running Diagnostic collector with `diagnostic.operation` is `LOGGING`. 

  * `diagnostic.loggerNames`: Specifies by name which loggers to collect data from. For Apigee hybrid version 1.6.0, the only value supported is `ALL`, meaning all loggers. For example: 
        
        diagnostic:
         …
         loggingDetails:
           loggerNames:
           - ALL

  * `diagnostic.logLevel`: Specifies the granularity of the logging data to collect. In Apigee hybrid 1.6, Only `FINE` is supported.
  * `diagnostic.logDuration`: The duration in milliseconds of the log data collected. A typical value is `30000`.



###  Optional properties 

The following properties are optional. 

  * `diagnostic.tcpDumpDetails.maxMsgs`: Sets the maximum number of `tcpDump` messages to collect. Apigee recommends a maximum value no greater than `1000`.
  * `diagnostic.tcpDumpDetails.timeoutInSeconds`: Sets the amount of time in seconds to wait for `tcpDump` to return messages.
  * `diagnostic.threadDumpDetails.delayInSeconds`: The delay in seconds between collecting each thread dump. Must be used with `diagnostic.threadDumpDetails.iterations`.
  * `diagnostic.threadDumpDetails.iterations`: The number of jstack thread dump iterations to collect. Must be used with `diagnostic.threadDumpDetails.delayInSeconds`.



###  General example 

The following is an example `diagnostic` stanza showing all possible entries: 
    
    
    diagnostic:
      # required properties:
      serviceAccountPath: "service-accounts/apigee-diagnostics.json"
      operation: "ALL"
      bucket: "diagnostics_data"
      container: "apigee-runtime"
      namespace: "apigee"
      podNames:
      - apigee-runtime-hybrid-example-3b2ebf3-150-8vfoj-2wcjn
      - apigee-runtime-hybrid-example-3b2ebf3-150-8vfoj-6xzn2
    
      # required if operation is Logging
      loggingDetails:
        loggerNames:
        - ALL
        logLevel: FINE
        logDuration: 30000
    
      # optional properties:
      tcpDumpDetails:
        maxMsgs: 10
        timeoutInSeconds: 100
    
      threadDumpDetails:
        iterations: 5
        delayInSeconds: 2

##  Common use cases 

The following examples show how to configure and use Diagnostic collector in some common situations. 

###  High Proxy Latency 

In this case Apigee-runtime is taking a long time to process requests, causing customers to see high proxy latencies. You need to collect Jstack and TOP output. 

  1. Select any 2 runtime pods.
  2. Create your `diagnostic` stanza with the following structure: 
         
         diagnostic:
           serviceAccountPath: "service-accounts/apigee-diagnostics.json"
           operation: "ALL"
           bucket: "diagnostics_data"
           container: "apigee-runtime"
           namespace: "apigee"
           podNames:
           - apigee-runtime-hybrid-example-3b2ebf3-150-8vfoj-2wcjn
           - apigee-runtime-hybrid-example-3b2ebf3-150-8vfoj-6xzn2
         
           tcpDumpDetails:
             maxMsgs: 10
         
           threadDumpDetails:
             iterations: 15
             delayInSeconds: 1

  3. After configuring the `diagnostic` stanza, run the Diagnostic collector. 
         
         apigeectl diagnostic -f OVERRIDES_FILE

  4. Collect the logs and delete the Diagnostic collector. 
         
         apigeectl diagnostic delete -f OVERRIDES_FILE




###  Network / connectivity problems 

You need to run diagnostics on apigee-runtime as well as ingress gateway pods. 

  1. Select any 2 runtime pods.
  2. Create your `diagnostic` stanza with the following structure: 
         
         diagnostic:
           serviceAccountPath: "service-accounts/apigee-diagnostics.json"
           operation: "ALL"
           bucket: "diagnostics_data"
           container: "apigee-runtime"
           namespace: "apigee"
           podNames:
           - apigee-runtime-hybrid-example-3b2ebf3-150-8vfoj-2wcjn
           - apigee-runtime-hybrid-example-3b2ebf3-150-8vfoj-6xzn2
         
           tcpDumpDetails:
             maxMsgs: 1000

  3. After configuring the `diagnostic` stanza, run the Diagnostic collector. 
         
         apigeectl diagnostic -f OVERRIDES_FILE

  4. Collect the logs and delete the Diagnostic collector. 
         
         apigeectl diagnostic delete -f OVERRIDES_FILE

  5. Select two pods from the Istio ingress gateway.
  6. Reconfigure your `diagnostic` stanza with the Istio ingress pods: 
         
         diagnostic:
           serviceAccountPath: "service-accounts/apigee-diagnostics.json"
           operation: "ALL"
           bucket: "diagnostics_data"
           container: "istio-proxy"
           namespace: "istio-system"
           podNames:
           - istio-ingressgateway-696879cdf8-9zzzf
           - istio-ingressgateway-696879cdf8-6abc7
         
           tcpDumpDetails:
             maxMsgs: 1000

  7. After configuring the `diagnostic` stanza, run the Diagnostic collector. 
         
         apigeectl diagnostic -f OVERRIDES_FILE

  8. Collect the logs and delete the Diagnostic collector. 
         
         apigeectl diagnostic delete -f OVERRIDES_FILE




###  Proxies are throwing unexpected errors or new contracts are not getting applied 

In this case you need to change log levels to debug for at least 5 minutes, or even 10 minutes as in this example. This will increase the amount of logs but helpful information will be logged. You will run Diagnostic collector twice, once on Apigee runtime then on Apigee synchronizer. 

  1. Select any 2 runtime pods.
  2. Create your `diagnostic` stanza with the following structure: 
         
         diagnostic:
           serviceAccountPath: "service-accounts/apigee-diagnostics.json"
           operation: "LOGGING"
           bucket: "diagnostics_data"
           namespace: "apigee"
           container: "apigee-runtime"
           podNames:
           - apigee-runtime-hybrid-example-3b2ebf3-150-8vfoj-2wcjn
           - apigee-runtime-hybrid-example-3b2ebf3-150-8vfoj-6xzn2
         
           loggingDetails:
             loggerNames:
             - ALL
             logLevel: FINE
             logDuration: 60000

  3. After configuring the `diagnostic` stanza, run the Diagnostic collector. 
         
         apigeectl diagnostic -f OVERRIDES_FILE

  4. Collect the logs and delete the Diagnostic collector. 
         
         apigeectl diagnostic delete -f OVERRIDES_FILE

  5. Select any 2 synchronizer pods.
  6. Create your `diagnostic` stanza with the following structure: 
         
         diagnostic:
           serviceAccountPath: "service-accounts/apigee-diagnostics.json"
           operation: "LOGGING"
           bucket: "diagnostics_data"
           namespace: "apigee"
           container: "apigee-synchronizer"
           podNames:
           - apigee-synchronizer-hybrid-example-3b2ebf3-150-xx4z-6cg78
           - apigee-synchronizer-hybrid-example-3b2ebf3-150-xx4z-1a2b3
         
           loggingDetails:
             loggerNames:
             - ALL
             logLevel: FINE
             logDuration: 60000

  7. After configuring the `diagnostic` stanza, run the Diagnostic collector. 
         
         apigeectl diagnostic -f OVERRIDES_FILE

  8. Collect the logs and delete the Diagnostic collector. 
         
         apigeectl diagnostic delete -f OVERRIDES_FILE




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
