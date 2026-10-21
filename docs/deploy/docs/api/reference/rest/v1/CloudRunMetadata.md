---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CloudRunMetadata/
title: CloudRunMetadata \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:02.789206+00:00
---

# CloudRunMetadata  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CloudRunMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  CloudRunMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



CloudRunMetadata contains information from a Cloud Run deployment.

JSON representation  
---  
      
    
    {
      "service": string,
      "serviceUrls": [
        string
      ],
      "revision": string,
      "previousRevision": string,
      "job": string,
      "workerPool": string
    }  
  
Fields  
---  
`service` |  `string` Output only. The name of the Cloud Run Service that is associated with a `Rollout`. Format is `projects/{project}/locations/{location}/services/{service}`.  
`serviceUrls[]` |  `string` Output only. The Cloud Run Service urls that are associated with a `Rollout`.  
`revision` |  `string` Output only. The Cloud Run Revision id associated with a `Rollout`.  
`previousRevision` |  `string` Output only. The previous Cloud Run Revision name associated with a `Rollout`. Only set when a canary deployment strategy is configured. Format for service is projects/{project}/locations/{location}/services/{service}/revisions/{revision}. Format for worker pool is projects/{project}/locations/{location}/workerPools/{workerpool}/revisions/{revision}.  
`job` |  `string` Output only. The name of the Cloud Run job that is associated with a `Rollout`. Format is `projects/{project}/locations/{location}/jobs/{jobName}`.  
`workerPool` |  `string` Output only. The Cloud Run worker pool associated with a `Rollout`. Format is `projects/{project}/locations/{location}/workerPools/{workerPool}`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
