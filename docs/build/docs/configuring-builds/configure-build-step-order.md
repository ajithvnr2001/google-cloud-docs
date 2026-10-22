---
url: https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order/
title: Configuring the order of build steps \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:29.345683+00:00
---

# Configuring the order of build steps  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Configuring the order of build steps Stay organized with collections  Save and categorize content based on your preferences. 

You can specify the order in which your build steps are executed. By default, build steps run sequentially, but you can configure them to run concurrently.

This page explains how to configure the order of the build steps.

### Build step order and dependencies

Use the `waitFor` field in a build step to specify which steps _must run_ before the build step is run. If no values are provided for `waitFor`, the build step waits for _all prior_ build steps in the build request to complete successfully before running.

To run a build step _immediately_ at build time, use `-` in the `waitFor` field.

The order of the build steps in the `steps` field relates to the order in which the steps are executed. Steps will run serially or concurrently based on the dependencies defined in their `waitFor` fields.

A step is dependent on every `id` in its `waitFor` and will not launch until each dependency has completed successfully.

**Note:** Steps must be defined with the `id` field prior to being used as `waitFor` dependencies.

Steps without the optional `waitFor` field (or with an empty `waitFor`) will wait for _all prior steps to complete successfully_ before executing. Therefore, if no step contains an `id` in its `waitFor` field, then all steps will _execute serially in the order they are defined_.

Steps can depend on the start of the build by having `waitFor` contain only `-`. By declaring that a step depends only on `-`, the step _runs immediately when the build starts_. The first step defined depends implicitly on start.

The following snippet shows a build config with two steps that runs serially:

###  YAML 
    
    
    steps:
    - name: foo
    - name: bar
    

###  JSON 
    
    
    {
        "steps": [{
            "name": "foo"
        },
        {
            "name": "bar"
        }
        ]
    }
    

The following snippet shows two concurrent steps that both depend on start; the third step waits for the first two to complete successfully before launching. This concurrent build runs steps `A` and `B` at the start of the build. The third step will wait implicitly until both previous steps are finished before starting. This example could be simplified by omitting the `id` fields, which are not referenced in a subsequent `waitFor`.

###  YAML 
    
    
    steps:
    - name: foo
      id: A
    - name: bar
      id: B
      waitFor: ['-']
    - name: baz
    

###  JSON 
    
    
    {
        "steps": [
        {
            "name": "foo",
            "id": "A"
        },
        {
            "name": "bar",
            "id": "B",
            "waitFor": ["-"]
        },
        {
            "name": "baz"
        }
        ]
    }
    

The following snippet shows concurrent steps that depend on a previous step. Step `A` runs immediately when the build starts. Steps `B` and `C` run concurrently after `A` has completed successfully. Note that the `id` and `waitFor` fields in step `B`, and the `id` field in step `C`, could be omitted without changing the order of execution.

###  YAML 
    
    
    steps:
    - name: foo
      id: A
    - name: bar
      id: B
      waitFor:
      - A
    - name: baz
      id: C
      waitFor:
      - A
    

###  JSON 
    
    
    {
        "steps": [
        {
            "name": "foo",
            "id": "A"
        },
        {
            "name": "bar",
            "id": "B",
            "waitFor": [
                "A"
            ]
        },
        {
            "name": "baz",
            "id": "C",
            "waitFor": [
                "A"
            ]
        }
        ]
    }
    

## Examples

The following example calls the `gcloud storage` and `wget` steps concurrently. After these steps have completed, the `ubuntu` step is called.

### YAML
    
    
    steps:
    # Download the binary and the data in parallel.
    - name: 'gcr.io/cloud-builders/wget'
      args: ['https://example.com/binary']
    - name: 'gcr.io/cloud-builders/gcloud'
      args: ['storage', 'cp', 'gs://$PROJECT_ID-data/rawdata.tgz', '.']
      waitFor: ['-']  # The '-' indicates that this step begins immediately.
    
    # Run the binary on the data, once both are downloaded.
    - name: 'ubuntu'
      args: ['./binary', 'rawdata.tgz']
    

### JSON
    
    
    {
      "steps": [
        {
          "name": "gcr.io/cloud-builders/wget",
          "args": [
            "https://example.com/binary"
          ]
        },
        {
          "name": "gcr.io/cloud-builders/gcloud",
          "args": [
            "storage",
            "cp",
            "gs://$PROJECT_ID-data/rawdata.tgz",
            "."
          ],
          "waitFor": [
            "-"
          ]
        },
        {
          "name": "ubuntu",
          "args": [
            "./binary",
            "rawdata.tgz"
          ]
        }
      ]
    }
    

The example below uses the `id` field to identify certain build steps. The values from `id` are used in `waitFor` to define build step order:

  * First, `fetch-resources` step uses `gcloud storage` to copy the local resources from Cloud Storage. Concurrently, `go` generates, tests, and installs the source code.
  * Then, the `docker` build step builds the image after all other steps are complete.




###  YAML 
    
    
    steps:
    - name: 'gcr.io/cloud-builders/go'
      args: ['generate']
    - name: 'gcr.io/cloud-builders/go'
      args: ['test', './...']
    - name: 'gcr.io/cloud-builders/go'
      args: ['install', 'mytarget']
      id: 'go-install'
    
    - name: 'gcr.io/cloud-builders/gcloud'
      args: ['storage', 'cp', '-r', './somefiles', 'gs://my-resource-bucket/somefiles']
      waitFor: ['-']  # The '-' indicates that this step begins immediately.
      id: 'fetch-resources'
    
    - name: 'gcr.io/cloud-builders/docker'
      args: ['build', '-t', 'gcr.io/$PROJECT_ID/mytarget', '.']
      waitFor: ['go-install', 'fetch-resources']
    
    images: ['gcr.io/$PROJECT_ID/mytarget']
    

###  JSON 
    
    
    {
      "steps": [
        {
          "name": "gcr.io/cloud-builders/go",
          "args": [
            "generate"
          ]
        },
        {
          "name": "gcr.io/cloud-builders/go",
          "args": [
            "test",
            "./..."
          ]
        },
        {
          "name": "gcr.io/cloud-builders/go",
          "args": [
            "install",
            "mytarget"
          ],
          "id": "go-install"
        },
        {
          "name": "gcr.io/cloud-builders/gcloud",
          "args": [
            "storage",
            "cp",
            "-r",
            "./somefiles",
            "gs://my-resource-bucket/somefiles"
          ],
          "waitFor": [
            "-"
          ],
          "id": "fetch-resources"
        },
        {
          "name": "gcr.io/cloud-builders/docker",
          "args": [
            "build",
            "-t",
            "gcr.io/$PROJECT_ID/mytarget",
            "."
          ],
          "waitFor": [
            "go-install",
            "fetch-resources"
          ]
        }
      ],
      "images": [
        "gcr.io/$PROJECT_ID/mytarget"
      ]
    }
    

## What's next

  * Configure Cloud Build to [build, test, and deploy artifacts](https://docs.cloud.google.com/build/docs/configuring-builds/build-test-deploy-artifacts).
  * Learn how to run builds [manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) and using [triggers](https://docs.cloud.google.com/build/docs/running-builds/automate-builds).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
