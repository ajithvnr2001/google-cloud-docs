---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-bigquery-load/
title: Load data from Cloud Storage to BigQuery using a workflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:03.851676+00:00
---

# Load data from Cloud Storage to BigQuery using a workflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-bigquery-load/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Load data from Cloud Storage to BigQuery using a workflow Stay organized with collections  Save and categorize content based on your preferences. 

Runs a series of steps to orchestrate loading and then transforming data in BigQuery by calling Cloud Functions.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Load data from Cloud Storage to BigQuery using Workflows](https://docs.cloud.google.com/workflows/docs/tutorials/load-data-from-cloud-storage-to-bigquery-using-workflows)



## Code sample

### YAML
    
    
    main:
      steps:
        - constants:
            assign:
              - create_job_url: CREATE_JOB_URL
              - poll_job_url: POLL_BIGQUERY_JOB_URL
              - run_job_url: RUN_BIGQUERY_JOB_URL
              - create_query_url: CREATE_QUERY_URL
              - region: BQ_REGION
              - table_name: BQ_DATASET_TABLE_NAME
            next: createJob
    
        - createJob:
            call: http.get
            args:
              url: ${create_job_url}
              auth:
                  type: OIDC
              query:
                  region: ${region}
                  table_name: ${table_name}
            result: job
            next: setJobId
    
        - setJobId:
            assign:
              - job_id: ${job.body.job_id}
            next: jobCreateCheck
    
        - jobCreateCheck:
            switch:
              - condition: ${job_id == Null}
                next: noOpJob
            next: runLoadJob
    
        - runLoadJob:
            call: runBigQueryJob
            args:
                job_id: ${job_id}
                run_job_url: ${run_job_url}
                poll_job_url: ${poll_job_url}
            result: jobStatus
            next: loadRunCheck
    
        - loadRunCheck:
            switch:
              - condition: ${jobStatus == 2}
                next: createQueryJob
            next: failedLoadJob
    
        - createQueryJob:
            call: http.get
            args:
              url: ${create_query_url}
              query:
                  qs: "select count(*) from serverless_elt_dataset.word_count"
                  region: "US"
              auth:
                  type: OIDC
            result: queryjob
            next: setQueryJobId
    
        - setQueryJobId:
            assign:
              - qid: ${queryjob.body.job_id}
            next: queryCreateCheck
    
        - queryCreateCheck:
            switch:
              - condition: ${qid == Null}
                next: failedQueryJob
            next: runQueryJob
    
        - runQueryJob:
            call: runBigQueryJob
            args:
              job_id: ${qid}
              run_job_url: ${run_job_url}
              poll_job_url: ${poll_job_url}
            result: queryJobState
            next: runQueryCheck
    
        - runQueryCheck:
            switch:
              - condition: ${queryJobState == 2}
                next: allDone
            next: failedQueryJob
    
        - noOpJob:
            return: "No files to import"
            next: end
    
        - allDone:
            return: "All done!"
            next: end
    
        - failedQueryJob:
            return: "Query job failed"
            next: end
    
        - failedLoadJob:
            return: "Load job failed"
            next: end
    
    
    runBigQueryJob:
      params: [job_id, run_job_url, poll_job_url]
      steps:
        - startBigQueryJob:
            try:
              call: http.get
              args:
                  url: ${run_job_url}
                  query:
                    job_id: ${job_id}
                  auth:
                    type: OIDC
                  timeout: 600
              result: submitJobState
            retry: ${http.default_retry}
            next: validateSubmit
    
        - validateSubmit:
            switch:
              - condition: ${submitJobState.body.status == 1}
                next: sleepAndPollLoad
            next: returnState
    
        - returnState:
            return: ${submitJobState.body.status}
    
        - sleepAndPollLoad:
            call: sys.sleep
            args:
              seconds: 5
            next: pollJob
    
        - pollJob:
            try:
              call: http.get
              args:
                url: ${poll_job_url}
                query:
                  job_id: ${job_id}
                auth:
                  type: OIDC
                timeout: 600
              result: pollJobState
            retry:
              predicate: ${http.default_retry_predicate}
              max_retries: 10
              backoff:
                initial_delay: 1
                max_delay: 60
                multiplier: 2
            next: stateCheck
    
        - stateCheck:
            switch:
              - condition: ${pollJobState.body.status == 2}
                return: ${pollJobState.body.status}
              - condition: ${pollJobState.body.status == 3}
                return: ${pollJobState.body.status}
            next: sleepAndPollLoad

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
