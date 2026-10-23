---
url: https://docs.cloud.google.com/web-risk/docs/long-running-operations/
title: Long-running Operations \u00a0|\u00a0 Web Risk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:47.928800+00:00
---

# Long-running Operations  |  Web Risk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/long-running-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Web Risk ](https://docs.cloud.google.com/web-risk/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Long-running Operations

The Submission API is asynchronous and returns a long-running operation. The operation might not be completed when the method returns a response.

## Get an operation status

The following shows how to poll an operation's status.

Call the `GET` method for the Operations type.

Before using any of the request data, make the following replacements: 

  * project-number: your Google Cloud project number
  * operation-id: your operation ID



HTTP method and URL: 
    
    
    GET https://webrisk.googleapis.com/v1/projects/project-number/operations/operation-id

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://webrisk.googleapis.com/v1/projects/project-number/operations/operation-id"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://webrisk.googleapis.com/v1/projects/project-number/operations/operation-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-number/operations/operation-id",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.webrisk.v1.SubmitUriMetadata",
        "state": "RUNNING"
      }
      "done": false,
      ...
    }
    

## Understanding Operation Status

The `metadata.state` field in the response indicates the current status of the submission. When the operation is completed, the `state` field in the `SubmitUriMetadata` is updated. The possible states are the following:

  * `SUCCEEDED`: Indicates that the submitted URL was added to the Safe Browsing Blocklist.
  * `CLOSED`: Indicates that the submitted URL was not added to the Safe Browsing blocklist because it was not found to violate Safe Browsing policies.
  * `RUNNING`: Indicates that the submission is still being processed.



### Understanding CLOSED reasons

When the operation state is `CLOSED`, the `SubmitUriMetadata` might include a `closed_reason` field. This field provides additional context on why the submission was closed without the URL being added to a blocklist.

The possible values for `closed_reason` are the following:

  * **`CLOSED_REASON_UNSPECIFIED`** : The reason is not specified.
  * **`NO_THREAT_DETECTED`** : 
    * **Description** : The submitted URL was successfully analyzed and was not found to contain malicious content. This indicates that, based on our analysis, the URL does not meet the criteria for blocklisting.
    * **Recommended User Action** : No further action is typically needed for this URL, as it was not found to be a threat. Don't repeatedly resubmit unless the content changes and new evidence of malicious activity emerges.
  * **`HOST_UNRESOLVABLE`** : 
    * **Description** : We could not complete the analysis because the URL's hostname couldn't be resolved by DNS. This often means the website is down, the domain no longer exists, or there was a temporary DNS issue. We cannot add inactive or placeholder URLs to the blocklist.
    * **Recommended User Action** : 
      * **Verify the URL** : Ensure the hostname is correct and the website is active and publicly accessible.
      * **Resubmit** : You may resubmit the URL later if you confirm the site is active.
  * **`CONTENT_UNREACHABLE`** : 
    * **Description** : Analysis could not be completed because the website's content couldn't be reached. This can happen for several reasons, such as: 
      * The web page no longer exists (this is a "404 Not Found" error).
      * The website's server encountered an error (this is a "5xx Server Error").
      * The website might be showing different content to our analysis system than it would to a regular visitor (this is cloaking), preventing a full assessment.
    * **Recommended User Action** : 
      * **Check Accessibility** : Confirm that the malicious content is reachable. Note that some sites may only show malicious content under specific conditions (this is certain geographic locations, devices, or browsers).
      * **Provide More Context** : If the URL is accessible under specific conditions, resubmit it. Use the [`ThreatDiscovery`](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.uris/submit#threatdiscovery) fields in the `SubmitUriRequest` to provide additional details, such as the region and platform where the threat was observed. This information can increase the likelihood of a successful analysis.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
