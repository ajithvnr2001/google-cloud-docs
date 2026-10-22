---
url: https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/serving/
title: Troubleshoot serving issues in App Engine \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:32.781458+00:00
---

# Troubleshoot serving issues in App Engine  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/serving/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Troubleshoot serving issues in App Engine Stay organized with collections  Save and categorize content based on your preferences. 

This page describes common app initialization and serving errors in App Engine and methods to troubleshoot them.

### Permission error when creating an app with the default service account

When you create an app after enabling the App Engine API for the first time, it might fail with the following errors:

###  gcloud CLI 
    
    
    An internal error occurred while calling service consumer manager for service account.
    Creating  App Engine application in projectPROJECT and REGION....failed. DEBUG: (gcloud.app.create) Error Response: [13] an internal error has occurred
    

###  Request logs 
    
    
    Service account creation is not allowed on this project.
    

###  Console 
    
    
    Error while initialising App Engine.
    

This error might occur due to the enforcement of the organization policy constraint [`constraints/iam.disableServiceAccountCreation`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_creation) when creating your app. This policy prevents the provisioning of the [ App Engine default service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts) `PROJECT_ID@appspot.gserviceaccount.com`.

To resolve this issue, you must temporarily remove the organization policy constraint `constraints/iam.disableServiceAccountCreation` to allow for the creation and deployment of the App Engine default service account. The default service account is necessary for app creation and can't be skipped. This is also applicable when you use a per-version service account. The App Engine default service account can be deleted or replaced with a service account that you create after successful deployment.

If you are using a service account that you created, review the [Overview of role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview) to understand how to enforce restricting permissions, such as providing a token creator role on the service account you create for the service agent.

## Application isn't serving the latest code changes

If your application isn't serving the latest code changes after deployment, you can use the root file system of the container to check the contents. The following troubleshooting steps show how to fetch the container image, and export the root file system for further analysis:

  1. Use [Cloud Logging](https://docs.cloud.google.com/appengine/docs/flexible/writing-application-logs?tab=go#logs_explorer) to obtain the container image URL, with the filter `GAE_FULL_APP_CONTAINER`. After you apply the filter, Cloud Logging displays the container image URL, with your fully qualified domain name (FQDN). For example, `GAE_FULL_APP_CONTAINER: FQDN/PROJECT_ID/appengine/SERVICE_NAME.VERSION_ID@sha256:SHA256_DIGEST`.

  2. Run the following command to export the container image URL:
         
         export IMAGE_URL='FQDN/PROJECT_ID/appengine/SERVICE_NAME.VERSION_ID@sha256:SHA256_DIGEST'
         

Replace:

     * FQDN with the fully qualified domain name of the container image URL.
     * PROJECT_ID with the project ID of your Google Cloud project.
     * SERVICE_NAME with your service name.
     * VERSION_ID with the version ID of the service.
     * SHA256_DIGEST with the [SHA256](https://docs.cloud.google.com/iap/docs/reference/app-engine-apis#iap_properties) value.
  3. Create a new container with the container image URL:
         
         docker pull ${IMAGE_URL}
         export CONTAINER_ID=$(docker create ${IMAGE_URL})
         docker ps -a # the list should contain the newly created container with status `Created`
         

  4. Export the root file system (`rootfs`) of the container image:
         
         docker export ${CONTAINER_ID} -o gae_app.tar
          mkdir gae_app
          mv -v gae_app.tar gae_app/
          cd gae_app/
          tar -xf gae_app.tar
          ls -la # inspect the container FS
         

Alternatively, if you don't require the `TAR` file, run the following command:
         
         mkdir gae_app
           cd gae_app/
           docker export ${CONTAINER_ID} | tar -xC <dest>
           ls -la # inspect the container FS
         

Analyze the contents of the root file system to verify if the latest code changes are present.

  5. Run the following command to clean up the image:
         
         docker container rm ${CONTAINER_ID}
         docker image rm ${IMAGE_URL}
         unset IMAGE_URL CONTAINER_ID
         




### Nginx fails to connect or contact the app container

The following error only occurs in the App Engine flexible environment and typically returns with 502 errors immediately after the error:
    
    
    recv() failed (104: Connection reset by peer) while reading response header from upstream
    

This error indicates that nginx reverse proxy (nginx sidecar) is unable to reach the app container. In the logs, you can compare the close timing of the 502 error in the nginx log with the timing of the nginx.error log. A nginx.error followed immediately by a 502 nginx error is likely the cause of the nginx 502 error.

This error often occurs when the connection keepalive timeout of the application is smaller than the keepalive timeout of nginx. As nginx in the App Engine flexible environment has `keepalive_timeout` of 650 seconds, applications need to keep connections alive for at least this long. By default, Node.js applications have [`keepAliveTimeout`](https://nodejs.org/api/http.html#serverkeepalivetimeout) of 5000 milliseconds. In this case, you can set `server.keepAliveTimeout` to 700000 milliseconds.

To troubleshoot, check the logs written by the code running in your app container by [connecting to the VM instance](https://docs.cloud.google.com/appengine/docs/flexible/debugging-an-instance), and add more logging, if necessary, to find the root cause.

### Insufficient memory

The following out of memory error occurs in the App Engine flexible environment, and typically returns with 502 errors:
    
    
    kernel: [  133.706951] Out of memory: Kill process 4490 (java) score 878 or sacrifice child
    kernel: [  133.714468] Killed process 4306 (java) total-vm:5332376kB, anon-rss:2712108kB, file-rss:0kB
    

This error indicates that App Engine has terminated the application.

This error occurs when the instance has insufficient memory. By default App Engine flexible environment has 1GB of memory, with only 600MB available for the application container.

To troubleshoot, check the logs for an out of memory entry, and update the [`memory_gb`](https://docs.cloud.google.com/appengine/docs/flexible/go/reference/app-yaml#resource-settings) configuration in your `app.yaml` file, and redeploy.

### Insufficient open connections to handle incoming requests

Apps might encounter a 502 error if the maximum number of waiting connections is equal to or greater than 75% of the number of active connections.

To resolve the issue, check the [Cloud Monitoring metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-appengine) is less than or equal to 75% of the number of active connections.

### Nginx worker connection limit

In the App Engine flexible environment, the Nginx proxy has a limit of 4,096 worker connections per instance. If your application exceeds this limit, you might encounter 502 errors.

To resolve this issue, you can increase the number of instances or [configure your application](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#automatic_scaling) to target fewer concurrent requests per instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
