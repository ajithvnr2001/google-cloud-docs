---
url: https://docs.cloud.google.com/build/docs/view-build-results/
title: View build results \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:08.390786+00:00
---

# View build results  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/view-build-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  View build results Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view information about your Cloud Build builds using the Google Cloud console, the `gcloud` command-line tool, and the Cloud Build API.

## Before you begin

If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://cloud.google.com/sdk).

## View build results

To view build logs, principals require one of the following IAM roles in addition to the [Cloud Build IAM permissions](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-control):

  * If your build logs are in the default Cloud Storage bucket, [grant the **Project > Viewer** role](https://console.cloud.google.com/iam-admin/iam).

  * If your build logs are in a user-specified Cloud Storage bucket, [grant the **Storage Object Viewer** role](https://console.cloud.google.com/iam-admin/iam).




For more information about the necessary permissions to view build logs in Cloud Build or GitHub or GitHub Enterprise following trigger creation, see [Viewing build logs](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#view-cloud-build).

###  Console 

In the Google Cloud console, the **Build History** menu can show you information about a build's status (such as success or failure), source, results, create time, images, and more.

To view the **Build History** menu, open the **Build History** page in the Google Cloud console:

[Open the Build History page](https://console.cloud.google.com/cloud-build/builds)

The **Build history** page is displayed, which shows a list of your recent builds.

You can filter builds using the **Filter** field, or by entering a query.

To view additional columns such as **Trigger description** and **Artifacts** , use the column selector view_column.

To view details about a specific build, go to the **Build history** page and click a specified build. The **Build details** page is displayed, with the **Build Summary** for your build. The **Build Summary** includes:

  * **Build Log** : The log of your build.
  * **Execution Details** : The details of your build including your environment variables and substitutions.
  * **Build dependencies** : If your build has one or more dependencies, then this tab shows dependency information such as repository URL and revision.
  * **Build Artifacts** : The artifacts of your build, such as container images, build logs, or binaries.



You can view the build log or execution details specific to a build step by selecting the step in the **Steps** table to the left.

###  gcloud 

The [`gcloud builds list`](https://docs.cloud.google.com/sdk/gcloud/reference/builds/list) command displays all your builds.

**To view your builds** , run the following command:
    
    
    gcloud builds list
    

You should see an output similar to the following:
    
    
    ID                                    CREATE_TIME                DURATION  SOURCE                                                                                      IMAGES                                              STATUS
    3a2055bc-ccbd-4101-9434-d376b88b8940  2018-02-16T18:33:26+00:00  23S       gs://gcb-docs-project_cloudbuild/source/1518806004.25-db1e250a7b7f496eb8242bfee5ac308e.tgz  us-east1-docker.pkg.dev/gcb-docs-project/quickstart-image (+1 more)  SUCCESS
    900704ca-7a0c-4569-ac08-884593c19aac  2018-02-16T18:32:32+00:00            gs://gcb-docs-project_cloudbuild/source/1518805951.23-03dd53d16f684c568fa2bb7ff7ebda06.tgz  -                                                   FAILURE
    021f9ede-ddaa-4cfb-8988-60142b015ebd  2018-02-14T15:48:44+00:00  10S       gs://gcb-docs-project_cloudbuild/source/1518623322.56-9cd088ffc1e04f5aa6040728772d0c2a.tgz  -                                                   SUCCESS
    8126d538-3c43-4304-a14c-33aceec8cb97  2018-02-14T15:46:13+00:00  10S       gs://gcb-docs-project_cloudbuild/source/1518623172.09-327c02585a4e44e782ac97dd80d5a5d5.tgz  us-east1-docker.pkg.dev/gcb-docs-project/quickstart-image (+1 more)  SUCCESS
    

**To view details about a specific build** , run the following command:
    
    
    gcloud builds describe [BUILD_ID]
    

where [BUILD_ID] is the ID of the build for which you want to get details.

You should see an output similar to the following:
    
    
    createTime: '2018-02-22T14:49:54.066666971Z'
    finishTime: '2018-02-22T14:50:05.463758Z'
    id: bcdb9c48-d92c-4489-a3cb-08d0f0795a0b
    images:
    - us-east1-docker.pkg.dev/gcb-docs-project/quickstart-image
    logUrl: https://console.cloud.google.com/cloud-build/builds/bcdb9c48-d92c-4489-a3cb-08d0f0795a0b?project=gcb-docs-project
    logsBucket: gs://404889597380.cloudbuild-logs.googleusercontent.com
    projectId: gcb-docs-project
    results:
        buildStepImages:
        - sha256:a4363bc75a406c4f8c569b12acdd86ebcf18b6004b4f163e8e6293171462a79d
        images:
        - digest: sha256:1b2a237e74589167e4a54a8824f0d03d9f66d3c7d9cd172b36daa5ac42e94eb9
          name: us-east1-docker.pkg.dev/gcb-docs-project/quickstart-image
          pushTiming:
              endTime: '2018-02-22T14:50:04.731919081Z'
              startTime: '2018-02-22T14:50:00.874058710Z'
        - digest: sha256:1b2a237e74589167e4a54a8824f0d03d9f66d3c7d9cd172b36daa5ac42e94eb9
          name: us-east1-docker.pkg.dev/gcb-docs-project/quickstart-image:latest
          pushTiming:
              endTime: '2018-02-22T14:50:04.731919081Z'
              startTime: '2018-02-22T14:50:00.874058710Z'
    source:
        storageSource:
            bucket: gcb-docs-project_cloudbuild
            generation: '1519310993665963'
            object: source/1519310992.2-8465b08c79e14e89bee09adc8203c163.tgz
    sourceProvenance:
        fileHashes:
            gs://gcb-docs-project_cloudbuild/source/1519310992.2-8465b08c79e14e89bee09adc8203c163.tgz#1519310993665963:
            fileHash:
            - value: -aRYrWp2mtfKhHSyWn6KNQ==
        resolvedStorageSource:
            bucket: gcb-docs-project_cloudbuild
            generation: '1519310993665963'
            object: source/1519310992.2-8465b08c79e14e89bee09adc8203c163.tgz
    startTime: '2018-02-22T14:49:54.966308841Z'
    status: SUCCESS
    steps:
    - args:
      - build
      - --no-cache
      - -t
      - us-east1-docker.pkg.dev/gcb-docs-project/quickstart-image
      - .
      name: gcr.io/cloud-builders/docker
      status: SUCCESS
      timing:
          endTime: '2018-02-22T14:50:00.813257422Z'
          startTime: '2018-02-22T14:50:00.102600442Z'
    timeout: 600s
    timing:
        BUILD:
            endTime: '2018-02-22T14:50:00.873604173Z'
            startTime: '2018-02-22T14:50:00.102589403Z'
        FETCHSOURCE:
            endTime: '2018-02-22T14:50:00.087286880Z'
            startTime: '2018-02-22T14:49:56.962717504Z'
        PUSH:
            endTime: '2018-02-22T14:50:04.731958202Z'
            startTime: '2018-02-22T14:50:00.874057159Z'
    

### Step status and build status

After a build completes, Cloud Build provides an overall [`status`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#Build.Status) for the build and a [`status`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#Build.Status) for each individual build step.

The following table summarizes the statuses when a build or a step succeeds, times out, or fails:

Event | Build Status | Step Status  
---|---|---  
Build succeeds | `SUCCESS` | All steps are marked `SUCCESS`.  
Build succeeds with failed steps permitted | `SUCCESS` | 

  * The build is marked `SUCCESS`.
  * Failed steps configured with [`allowFailure`](https://docs.cloud.google.com/build/docs/build-config-file-schema#allowfailure) or [`allowExitCodes`](https://docs.cloud.google.com/build/docs/build-config-file-schema#allowexitcodes) are marked `FAILED`.

  
Build fails | `FAILURE` | 

  * Failed step is marked `FAILED`.
  * Steps that succeed before the termination of the build are marked `SUCCESS`.
  * Steps in the middle of execution are marked `CANCELLED`.
  * Steps that don't start to execute are marked `QUEUED`.

  
Build is cancelled by the user | `CANCELLED` | 

  * Steps that succeed before the cancellation of the build are marked `SUCCESS`.
  * Steps in the middle of execution are marked `CANCELLED`.
  * Steps that don't start to execute are marked `QUEUED`.

  
Build times out | `TIMEOUT` | 

  * Steps that succeed before the build times out are marked `SUCCESS`.
  * Steps in the middle of execution are marked `CANCELLED`.
  * Steps that don't start to execute are marked `QUEUED`.

  
Step times out | `FAILED` | 

  * The step that times out is marked `TIMEOUT`.
  * Steps that succeed prior to the timed-out step are marked `SUCCESS`.
  * Steps in the middle of execution are marked `CANCELLED`.
  * Steps that don't start to execute are marked `QUEUED`.

  
  
To view per-step and build status, run the `gcloud builds describe` command:
    
    
    gcloud builds describe <var>BUILD_ID</var>
    

where BUILD_ID is the ID of the build.

The following snippet shows the per-step status from a build with a timed-out step:
    
    
    status: FAILURE
    steps:
    - args:
      - sleep
      - '60'
    id: long sleep
    name: alpine
    status: CANCELLED
    timing:
        endTime: '2018-02-26T14:09:18.531368493Z'
        startTime: '2018-02-26T14:09:11.023235026Z'
    waitFor:
    - '-'
    - args:
    - sleep
    - '3'
    id: shorty
    name: alpine
    status: SUCCESS
    timeout: 60s
    timing:
        endTime: '2018-02-26T14:09:15.497724138Z'
        startTime: '2018-02-26T14:09:11.023676903Z'
    waitFor:
    - '-'
    - args:
      - sleep
      - '60'
    name: alpine
    status: TIMEOUT
    timeout: 3s
    timing:
        endTime: '2018-02-26T14:09:18.527488475Z'
        startTime: '2018-02-26T14:09:15.497736775Z'
    waitFor:
    - shorty
    - args:
      - 'false'
    name: alpine
    status: QUEUED
    waitFor:
    - long sleep
    timeout: 60s
    

### Filter build results by using queries

To find information for builds that fit specific criteria, supply a query string in the **Filter Builds** field in the **Build history** page in Google Cloud console. For example, you can query for builds that have failed (that have a `FAILURE` value in the status field), builds that were created after a certain time, tagged builds, and other such conditions.

**Supported fields for queries**

You can query for builds based on the values of the following fields:

  * `status`
  * `build_id`
  * `trigger_id`
  * `source.storage_source.bucket`
  * `source.storage_source.object`
  * `source.repo_source.repo_name`
  * `source.repo_source.branch_name`
  * `source.repo_source.tag_name`
  * `source.repo_source.commit_sha`
  * `source_provenance.resolved_repo_source.commit_sha`
  * `results.images.name`
  * `results.images.digest`
  * `options.requested_verify_option`
  * `tags`
  * `images`
  * `create_time`
  * `start_time`
  * `finish_time`



Fields listed with dot notation (`.`) are subfields.

**Constructing a query string**

Query strings use the general form:
    
    
    field="value"
    

Use dot notation to specify a subfield, such as `results.images.name`. Queries support the `=` and `!=` comparison operators, as well as `>`, `>=`, `<`, and `<=` for fields that have numeric values (such as `create_time`).

You can create compound queries by using the boolean `AND` and `OR` expressions.

**Common example queries**

To query for all successful builds:
    
    
    status="SUCCESS"
    

To query for all builds that have yet to finish:
    
    
    status="QUEUED" OR status="WORKING"
    

To query for builds with a given result image name:
    
    
    (status="SUCCESS" OR status="FAILURE") AND \
        results.images.name="us-east1-docker.pkg.dev/my-project/my-image"
    

To query for all builds with the tag `"prod"`:
    
    
    tags="prod"
    

To query for builds marked as verified:
    
    
    options.requested_verify_option="VERIFIED"
    

To query for builds that come from a source in Cloud Storage (as opposed to a source repository):
    
    
    source.storage_source.bucket!=""
    

To query for builds with a given result digest:
    
    
    results.images.digest="sha256:6c7147fe4c813845ac2a9aa6f937bb272b68784f647c4f64c7325723c7245c88"
    

To query for builds started after a specific time and finished before a specific time (UTC timezone):
    
    
    create_time>"2016-10-12T18:43:49+00:00" AND finish_time<"2016-10-13T18:43:49+00:00"
    

**Note:** This query response is in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601).

### Filter build results by using tags

You can use tags in your config files, which lets you organize your builds into groups and to filter your builds. You can specify strings in tags, such as `"prod"` or `"test"`.

Tags have the following limitations:

  * Each tag's character limit is 128 characters
  * You can define a maximum of 64 tags per build
  * Tags can contain letters, numbers, and underscores in any position of your string.
  * Tags can contain periods and hyphens in any position except the first position of your string.



To **add tags** in your build:

  1. In your build config file, add the `tags` field:
         
         steps:
         - name: 'gcr.io/cloud-builders/docker'
           args: [ 'build', '-t', 'us-east1-docker.pkg.dev/$PROJECT_ID/cb-demo-img', '.' ]
         images:
         - 'us-east1-docker.pkg.dev/$PROJECT_ID/cb-demo-img'
         tags:
         - 'test1'
         - 'test2'
         

  2. To see tagged builds in your cluster, use the `--filter` option in `gcloud builds list`. You can filter builds by specifying a single tag or multiple tags.

     * To filter builds by a single tag, specify the tag as a string in the `tags` field. The following command lists all builds tagged with `'test1'`:
           
           gcloud builds list --filter "tags='test1'"
           

     * To filter builds by multiple tags, use "AND", "OR", or "NOT" to list tags. The following command lists all builds tagged with `'test1'` or `'test2'` and tagged with `'test3'`:
           
           gcloud builds list --filter "tags=('test1' OR 'test2') AND 'test3'"
           

You will see an output similar to the following after running these commands:
    
    ID                                    CREATE_TIME                DURATION  SOURCE                                                                             IMAGES                                 STATUS
    d33a9895-...                          ...                        1M45S     gs://...                                                                           us-east1-docker.pkg.dev/...            SUCCESS
    


**Note:** Build tags are separate from [Docker image tags](https://docs.docker.com/reference/cli/docker/image/tag/). Ensure that you don't conflate these tag types.

## What's next

  * Learn how to [view build results for build triggers](https://docs.cloud.google.com/build/docs/view-build-results-triggers).
  * Learn how to [view build security insights](https://docs.cloud.google.com/build/docs/view-build-security-insights).
  * Learn how to [troubleshoot build errors](https://docs.cloud.google.com/build/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
