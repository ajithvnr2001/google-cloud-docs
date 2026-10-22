---
url: https://docs.cloud.google.com/build/docs/configuring-builds/pass-data-between-steps/
title: Passing data between build steps \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:33.333405+00:00
---

# Passing data between build steps  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/configuring-builds/pass-data-between-steps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Passing data between build steps Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to pass data between build steps. If you're new to Cloud Build, read the [Build quickstart](https://docs.cloud.google.com/build/docs/build-push-docker-image) and the [Build configuration overview](https://docs.cloud.google.com/build/docs/build-config) first.

Cloud Build runs your tasks as a series of **build steps** , which execute in isolated and containerized environments. After each step, the container is discarded. This allows you to have totally different tools and environments for each step, and by default, any data created in one step can't contaminate the next step. But sometimes you may need to persist state from one step of a build to use in subsequent steps.

For such cases, Cloud Build provides **volumes** , which are read-write file paths that you can attach to any build step. Volumes retain their contents throughout the duration of the build. You can define your own volume or use **/workspace** , which is the default volume that Cloud Build provides for you. Before executing a build, Cloud Build extracts the source code to /workspace. Anything written to user-defined volumes and /workspace by any step will be available to subsequent steps.

## Passing data using workspaces

To pass data between build steps, store the assets produced by the build step in `/workspace` and these assets will be available to any subsequent build steps.

In the following example build config file, the first build step stores the string "First Value" in `/workspace/first.txt` and the value `2` in `/workspace/second.txt`. The second build step reads and prints the values in `/workspace/first.txt` and `/workspace/second.txt`.

###  YAML 
    
    
    steps:
    - id: "Store Values"
      name: ubuntu
      entrypoint: bash
      args:
        - -c
        - |
          # Save a value to persistent volume mount: "/workspace"
          echo "First Value" > /workspace/first.txt &&
          # Save another
          expr 1 + 1 > /workspace/second.txt
    # In the next step, everything in the environment is discarded
    # EXCEPT items in "/workspace"
    - id: "Read Values"
      name: ubuntu
      entrypoint: bash
      args:
        - -c
        - |
          # Read from "/workspace"
          echo "First we saved " $(cat /workspace/first.txt) &&
          echo "Then we saved " $(cat /workspace/second.txt)
    

###  JSON 
    
    
    {
      "steps": [
      {
        "id": "Store Values",
        "name": "ubuntu",
        "entrypoint": "bash",
        "args": [
          "-c",
          "echo \"First Value\" > /workspace/first.txt &&\nexpr 1 + 1 > /workspace/second.txt\n"
        ]
        },
        {
          "id": "Read Values",
          "name": "ubuntu",
          "entrypoint": "bash",
          "args": [
            "-c",
            "echo \"First we saved \" $(cat /workspace/first.txt) &&\necho \"Then we saved \" $(cat /workspace/second.txt)\n"
          ]
        }
        ]
    }
    

**Note:** The `-c` flag in the code snippets on this page is used to execute multi-line commands. Any string you pass after `-c` is treated as a command. For more information on running bash commands with `-c`, see the [bash documentation](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Invoking-Bash).

## Passing data using user-specified volumes

Instead of using the default `/workspace` volume provided by Cloud Build, you can define your own volume to persist data between build steps.

To define and use your own volume:

  * In the build step where you want to store the data: 
    * Add a `volumes` block and set the following fields: 
      * `name`: Set the value of this field to the desired volume name.
      * `path`: Set the value of this field to the file path to store your data.
    * Store the data in the file path specified in `path`.
  * In the build step where you want to consume the data: 
    * Add a `volumes` block with the values for `name` and `path`.
    * Consume the data from the file path specified in `path`.



In following example build config file, the first build step defines a volume named `myvolume` and stores data in `/persistent_volume/file`. The second build step prints the value stored in `/persistent_volume/file`.

###  YAML 
    
    
    steps:
    - name: 'ubuntu'
      entrypoint: 'bash'
      args:
        - '-c'
        - |
          echo "Hello, world!" > /persistent_volume/file
      volumes:
      - name: 'myvolume'
        path: '/persistent_volume'
    - name: 'ubuntu'
      entrypoint: 'bash'
      args:
        - '-c'
        - |
          cat /persistent_volume/file
      volumes:
      - name: 'myvolume'
        path: '/persistent_volume'
    

###  JSON 
    
    
    {
      "steps": [
      {
        "name": "ubuntu",
        "entrypoint": "bash",
        "args": [
          "-c",
          "echo \"Hello, world!\" > /persistent_volume/file\n"
         ],
         "volumes": [
         {
           "name": "myvolume",
           "path": "/persistent_volume"
         }
         ]
      },
      {
        "name": "ubuntu",
        "entrypoint": "bash",
        "args": [
          "-c",
          "cat /persistent_volume/file\n"
        ],
        "volumes": [
        {
          "name": "myvolume",
          "path": "/persistent_volume"
        }
        ]
      }
    ]
    }
    

## What's next

  * Learn how to [start a build manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually).
  * Learn how to [automate builds using triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * Learn how to [run bash scripts](https://docs.cloud.google.com/build/docs/configuring-builds/run-bash-scripts) within build steps.
  * Learn how to [configure build step order](https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
