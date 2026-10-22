---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/troubleshoot-response-errors/
title: Troubleshooting response errors \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:35.139789+00:00
---

# Troubleshooting response errors  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/troubleshoot-response-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Troubleshooting response errors Stay organized with collections  Save and categorize content based on your preferences. 

If you don't get a successful response from a request to your Cloud Endpoints Frameworks API, you can use Cloud Logging in the Google Cloud console to help troubleshoot.

## Viewing logs

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer** page.

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

  2. From the project drop-down list at the top of the page, select the Google Cloud project in which you created your API.

  3. Select **GAE Application** and **All logs**.

  4. Adjust the time range until you see a row that shows an error.

  5. Click **Expand All** to see the entire log for the error.




The following section provides troubleshooting information for specific error messages. If you are unable to fix the issue, copy one of the log entries that shows the error and paste it in a text file. Include the log in any communication that you have with Google.

### `503 Service Unavailable`

App Engine might take a few minutes to respond successfully to requests. If you send a request and get a `503` error, wait a few minutes and try the request again. If you still don't get a successful response, check the Cloud Logging logs. The following are some error messages that you might see in the Cloud Logging logs.

**Error message** | **Troubleshooting**  
---|---  
No service `YOUR_PROJECT_ID.appspot.com` found or permission denied. If this is a new Endpoints service, make sure you've deployed the service config using gcloud.  |  Endpoints Frameworks for Python logs this error when it fails to load the service configuration for the service that you have specified in your `app.yaml` file. This error can happen when you haven't deployed the OpenAPI document for your API by using `gcloud endpoints services deploy`, or the Service Management API isn't enabled. When you deploy the OpenAPI document for your API, the `gcloud` command automatically enables the following: 

  * Service Management API (`servicemanagement.googleapis.com`) 
  * Cloud APIs (`cloudapis.googleapis.com`) 

If you have disabled any of these services, you must reenable them. See [Enabling and disabling APIs](https://docs.cloud.google.com/apis/docs/enable-disable-apis) for more information.   
The service `YOUR_PROJECT_ID.appspot.com` was found, but no service config was found for version `SERVICE_CONFIG_ID`.  |  Endpoints Frameworks for Python logs this error when it fails to find the service configuration ID that you have specified for `ENDPOINTS_SERVICE_VERSION` in your `app.yaml` file. To fix this error: 

  1. [Get the service configuration ID](https://docs.cloud.google.com/endpoints/docs/frameworks/get-service-name-config-id). 
  2. Edit your `app.yaml` file and set `ENDPOINTS_SERVICE_VERSION` to the service configuration ID. 
  3. Redeploy your app:  

         
         gcloud app deploy


  
  
### `404 Not Found`

If you recently migrated to Endpoints Frameworks version 2, and you get the `404 Not Found` error message, see the following sections to troubleshoot the issue:

  * [Java: Troubleshooting](https://docs.cloud.google.com/endpoints/docs/frameworks/java/migrating#api_returns_404_errors_but_api_explorer_still_lists_apis_correctly)
  * [Python: Troubleshooting](https://docs.cloud.google.com/endpoints/docs/frameworks/python/migrating#api_returns_404_errors_but_api_explorer_still_lists_apis_correctly)



## Issues with the example `Invoke-WebRequest`

In some versions of Windows PowerShell, the example `Invoke-WebRequest` in the [tutorials](https://docs.cloud.google.com/endpoints/docs/frameworks/tutorials) fails. We have also received a report that the response contained a list of unsigned bytes that had to be converted to characters. If the example `Invoke-WebRequest` didn't return the expected result, try sending the request using another application. Following are a few suggestions:

  * [Start Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell), and follow the Linux steps in the tutorial that you were using to send the request.
  * Use a third-party application such as the Chrome browser extension Postman (offered by `www.getpostman.com`). When creating the request in Postman:

    * Select `POST` as the HTTP verb.
    * For the header, select the key `content-type` and the value `application/json`.
    * For the body, enter: `{"message":"hello world"}`
    * Enter the URL for the sample application. For example:
          
          https://example-project-12345.appspot.com/_ah/api/echo/v1/echo
          

  * Download and install [`curl`](https://curl.haxx.se/download.html), which you run in the Command prompt. Because Windows doesn't handle double quotation marks nested inside single quotation marks, you have to change the `--data` option in the example, as follows: `--data "{\"message\":\"hello world\"}"`




What's next

  * Get started using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

  * Learn how to [route logs](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

  * Use [filters](https://docs.cloud.google.com/logging/docs/view/advanced_filters) for advanced filtering, such as getting all requests with a latency greater than 300 milliseconds.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
