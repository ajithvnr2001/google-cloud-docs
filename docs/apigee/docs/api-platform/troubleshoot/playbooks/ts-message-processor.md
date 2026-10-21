---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ts-message-processor/
title: Message processor troubleshooting guide \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:24.047738+00:00
---

# Message processor troubleshooting guide  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ts-message-processor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Message processor troubleshooting guide Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document is applicable for Apigee hybrid users only. 

This topic discusses steps you can take to troubleshoot and fix problems with the [message processor](https://docs.cloud.google.com/apigee/docs/hybrid/latest/what-is-hybrid#message-processor). The message processor is part of the [ `apigee-runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/latest/what-is-hybrid#about-the-runtime-plane) component. See also [Runtime service configuration overview](https://docs.cloud.google.com/apigee/docs/hybrid/latest/service-config). 

## Readiness probe fails with HTTP status code 500

### Symptom

One or more `apigee-runtime` pods are not in the Ready state. 

### Error message

When you use `kubectl` to describe a failed `apigee-runtime` pod, you see the error:

`Readiness probe failed: HTTP probe failed with statuscode: 500`

For example:
    
    
    kubectl describe pod -n hybrid \
    apigee-runtime-apigee-gcp-prod1-test-blue-67db4f457b-9c7c7
    
    ...
    apigee-runtime-apigee-gcp-prod1-test-blue-67db4f457b-9c7c7  **Readiness probe failed: HTTP probe
    failed with statuscode: 500**
    ...

### Possible causes

The error means that no active [contract](https://docs.cloud.google.com/apigee/docs/hybrid/latest/what-is-hybrid#synchronizer) is available for the message processor to serve the traffic. In this state, the message processor cannot call itself "ready". 

Cause  | Description   
---|---  
Synchronizer to management plane connection problem | The synchronizer is unable to connect to the management plane. This problem is usually caused in cases where you override the `contractProvider` URL and associate the wrong service account with it. For example, if you configure a service account for a staging deployment with a `contractProvider` URL that points to the production server.   
Message processor to synchronizer connection problem | If the new MP comes up as part of an autoscale or pod restart, you might see this error. Generally, this problem occurs when the synchronizer is down and the MP was unable to load its [contract](https://docs.cloud.google.com/apigee/docs/hybrid/latest/what-is-hybrid#synchronizer).   
  
### Diagnosis: Synchronizer to management plane connection problem

To diagnose a **synchronizer to management plane connection problem** , do the following: 

  1. List the pods in the cluster: 
         
         kubectl get pods -n namespace

  2. Open a shell in an `apigee-synchronizer` pod: 
         
         kubectl exec -it -n namespace synchronizer-pod-name -- bash

For example:
         
         kubectl exec -it -n apigee apigee-synchronizer-apigee-gcp-prod1-test-blue-cnj5x -- bash

  3. Go to the following directory (this is the standard path for Apigee hybrid versions):
    
    cd /application/opt/apigee/var/log/apigee-synchronizer
    ls -l
    
      total 12
      drwxr-xr-x 2 apigee apigee 4096 2026-02-17 03:16 29
      drwxr-xr-x 3 apigee apigee 4096 2026-02-17 01:45 api-security-contract
      -rw-r--r-- 1 apigee apigee   75 2026-02-17 03:16 versions.properties

  4. Check the active version in `version.properties`. For example:
    
    cat versions.properties
    
      #active repository version
      #Sat Dec 14 19:45:00 GMT 2019
      active.version=28

  5. Be sure the value of `active.version` matches the name of the contract folder number. In the above example (also shown below), the folder name is `29`; therefore, they do not match: 
         
         dr-xr-sr-x 4 apigee apigee  4096 Sep 12 16:52 **29**

  6. Exit the pod shell.



### Resolution

If `version.properties` is missing, or if there is a version mis-match as explained above, check the [synchronizer logs](https://docs.cloud.google.com/apigee/docs/hybrid/latest/sync-logs) to try to determine why the most current contracts are not being downloaded. For example:
    
    
    kubectl logs -f -n namespace synchronizer-pod-name

For information on interpreting the synchronizer logs, see [Synchronizer logs](https://docs.cloud.google.com/apigee/docs/hybrid/latest/sync-logs). If the synchronizer is down, try restarting it using [Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference): 
    
    
    helm upgrade ENV_NAME apigee-env/ \
    --namespace APIGEE_NAMESPACE \
    --set env=ENV_NAME \
    --atomic \
    -f OVERRIDES_FILE

Make sure to include all of the settings shown, including `--atomic` so that the action rolls back on failure.

### Diagnosis: Message processor to synchronizer connection problem

To diagnose a **message processor to synchronizer connection problem** , do the following: 

  1. List the pods in the cluster: 
         
         kubectl get pods -n namespace

  2. Check the [runtime logs](https://docs.cloud.google.com/apigee/docs/hybrid/latest/runtime-logs) to try to figure out why the contracts are not being downloaded: 
         
         kubectl logs -f -n namespace pod-name

For example:
         
         kubectl logs -f -n apigee apigee-runtime-apigee-gcp-prod1-test-blue-67db4f457b-9c7c7

It is possible if the new MP comes up as part of an autoscale or pod restart, that the MP might not load the contracts. Generally, the problem occurs when the synchronizer is down, preventing the MP from loading the contracts. For example: 
         
         2019-09-13 16:59:24,331 podName:N/A ipAddress:N/A dpColor:N/A
         HttpClient@331886186-301 DEBUG o.e.j.c.AbstractConnectionPool - AbstractConnectionPool$1.failed() :
         Connection 1/64 creation failed
         java.net.UnknownHostException: apigee-synchronizer-apigee-gcp-prod1-test.hybrid.svc.cluster.local
         at java.net.InetAddress.getAllByName0(InetAddress.java:1281)
         at java.net.InetAddress.getAllByName(InetAddress.java:1193)
         at java.net.InetAddress.getAllByName(InetAddress.java:1127)
         at org.eclipse.jetty.util.SocketAddressResolver$Async.lambda$resolve$1(SocketAddressResolver.java:167)
         at org.eclipse.jetty.util.thread.QueuedThreadPool.runJob(QueuedThreadPool.java:672)
         at org.eclipse.jetty.util.thread.QueuedThreadPool$2.run(QueuedThreadPool.java:590)
         at java.lang.Thread.run(Thread.java:748)
           at org.eclipse.jetty.util.thread.QueuedThreadPool$2.run(QueuedThreadPool.java:590)
           at java.lang.Thread.run(Thread.java:748)




### Resolution

Try restarting the synchronizer. For example: 
    
    
    helm upgrade ENV_NAME apigee-env/ \
      --namespace APIGEE_NAMESPACE \
      --set env=ENV_NAME \
      --atomic \
      -f OVERRIDES_FILE

## Readiness probe fails for an invalid encryption key

### Symptom

The `apigee-runtime` pods are not in the Ready state.

### Diagnosis

When you use `kubectl` to describe a failed `apigee-runtime` pod, you see this error: `Readiness probe failed: Probe hybrid-encryption-key-validation-probe failed`. For example: 
    
    
    kubectl describe pod -n namespace apigee-runtime-pod-name
    
    ...
    Readiness probe failed: **Probe hybrid-encryption-key-validation-probe failed** due to
    com.apigee.probe.model.ProbeFailedException{ code = hybrid.encryption.key.InvalidEncryptionKey,
    message = Invalid encryption key. Please check the length of the encryption key, associated
    contexts = []}
    ...

### Resolution

Supported encryption key lengths are 16 or 24 or 32 bytes and the key's value has to be base64 encoded. For more information on creating a properly formatted key, see [Data encryption](https://docs.cloud.google.com/apigee/docs/hybrid/latest/key-encryption).

## Viewing message processor logs

For details about viewing and interpreting message processor logs, see [Runtime logs](https://docs.cloud.google.com/apigee/docs/hybrid/latest/runtime-logs). 

## Call an API proxy from the runtime pod

In some situations to help isolate a problem, you might want to check if you can make an API proxy call directly from inside the `apigee-runtime` pod, and thereby bypassing the ingress gateway.

  1. Execute the following command to forward to port 8443. This allows you to call the API in the pod:
    
    kubectl port-forward -n namespace apigee-runtime-pod-name 8443:8443

  2. Call a deployed API proxy. For example, where the proxy basepath is `ilove-apis`: 
         
         curl -k -v https://0:8443//ilove-apis
         
             < HTTP/1.1 200 OK
             < X-Powered-By: Apigee
             < Access-Control-Allow-Origin: *
             < X-Frame-Options: ALLOW-FROM RESOURCE-URL
             < X-XSS-Protection: 1
             < X-Content-Type-Options: nosniff
             < Content-Type: text/html; charset=utf-8
             < Content-Length: 18
             < ETag: W/"12-Jb9QP1bUxNSmZkxQGt5KLQ"
             < Date: Fri, 13 Sep 2019 18:33:46 GMT
             < Via: 1.1 google
             < X-Apigee.Message-ID: 016f5f7f-c59e-404c-86e8-7b0737833f982
             < X-Apigee.dp.color: blue
             < X-Apigee.proxy: /organizations/my-org/environments/test/apiproxies/i-loveapis/revisions/1
             < X-Apigee.proxy.basepath: /ilove-apis
             < X-Apigee.target-latency: 9
             <
             * Connection #0 to host 0 left intact
             <H2>I <3 APIs




##  Check the management API 

You can use the API described below to check if the management API is working properly. 

  1. Get the names of the pods in your cluster: 
         
         kubectl get pods -n namespace

  2. Use [port-forwarding](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) to gain access to the `apigee-runtime` pod. The syntax for port forwarding is as follows: 
         
         kubectl port-forward -n namespace podname 8843:8843

For example:
         
         kubectl port-forward -n apigee \
             apigee-runtime-my-organization-test-blue-57965b7789-6j4bp 8843:8843

  3. Then, in another terminal window, use a utility such as `curl` to send a request to the `classification/tree` API, as the following example shows: 
         
         curl -k https://0:8843/v1/classification/tree

Here is an example response, which lists information about the deployed proxies in the "test" environment:
         
         [ {
           "condition" : "(always matches)",
           "virtualHost" : {
             "env" : "test",
             "name" : "default",
             "org" : "my-organization",
             "tree" : {
               "elements" : [ {
                 "application" : "myproxy",
                 "basePath" : "/myproxy",
                 "name" : "default",
                 "revision" : "1"
               } ],
               "name" : "IdentificationTree"
             }
           }
         } ]




## Using DEBUG mode

To help with troubleshooting, you can enable DEBUG mode to include more detailed information in the `apigee-runtime` pod logs. 

  1. List the pods in your namespace:
    
    kubectl get pods -n namespace

  2. Pick any one of the listed `apigee-runtime` pods to debug.
  3. Execute the port forwarding command for that pod. For example: 
         
         kubectl port-forward -n hybrid apigee-runtime-hybrid-prod-blue-fcpdd 8843

  4. Open another terminal and call the following API to enable debugging: 
         
         curl "https://0:8843/v1/logsessions?sessions=debug" -X POST -v -k

  5. Run the `kubectl logs` command to check the log that is in DEBUG Mode. For example: 
         
         kubectl logs -f -n hybrid apigee-runtime-hybrid-prod-blue-fcpdd

  6. When you are finished examining the DEBUG log, reset the log level to INFO (the default). For example: 
         
         curl "https://0:8843/v1/logsessions?sessions=info" -X POST -v -k

  7. Run the `kubectl logs` command to make sure the log is back in INFO mode.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
