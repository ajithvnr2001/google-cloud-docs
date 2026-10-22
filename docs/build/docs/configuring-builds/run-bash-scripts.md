---
url: https://docs.cloud.google.com/build/docs/configuring-builds/run-bash-scripts/
title: Running bash scripts \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:43.667772+00:00
---

# Running bash scripts  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/configuring-builds/run-bash-scripts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Running bash scripts Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure Cloud Build to run bash scripts within a build step. If you're new to Cloud Build, read the [quickstarts](https://docs.cloud.google.com/build/docs/quickstarts) and the [Build configuration overview](https://docs.cloud.google.com/build/docs/build-config) first.

You can run bash scripts within a build step to configure a number of workflows including:

  * Running multiple commands in one build step.
  * Reading from the filesystem.
  * Building in logic such as retries or conditionals.
  * Outputting to the log, for example, running `echo $VARNAME`.



## Using the `script` field

Cloud Build provides a `script` field that you can use to specify shell scripts to execute in a build step. The `script` field takes a single string value.

You can prefix the string value with a [shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29) to specify the shell to interpret the script. For example, add `#!/usr/bin/env bash` to [specify the Bash shell](https://hub.docker.com/_/bash). If you don't prefix the script string with a shebang, Cloud Build uses `#!/bin/sh` which is the basic sh shell, not Bash shell.

If you specify `script` in a build step, you cannot specify `args` or `entrypoint` in the same step.

The following snippet demonstrates the `script` field:

###  YAML 
    
    
    steps:
    - name: 'bash'
      script: |
        #!/usr/bin/env bash
        echo "Hello World"
    - name: 'ubuntu'
      script: echo hello
    - name: 'python'
      script: |
        #!/usr/bin/env python
        print('hello from python')
    

###  JSON 
    
    
    {
      "steps": [
      {
        "name": "bash",
        "script": "#!/usr/bin/env bash echo 'Hello World'"
      },
      {
        "name": "ubuntu",
        "script": "echo hello"
      },
      {
        "name": "python",
        "script": "#!/usr/bin/env python\nprint('hello from python')\n"
      }
      ]
    }
    

## Using substitutions with the `script` field

Scripts don't directly support substitutions, but they support environment variables. You can map substitutions to environment variables, either automatically all at once, or manually by defining every environment variable yourself.

### Map substitutions automatically

  * **At the build level**. To automatically map all the substitutions to environment variables, which will be available throughout the entire build, set `automapSubstitutions` to `true` as an option at the build level. For example, the following build config file shows the user-defined substitution `$_USER` and the default substitution `$PROJECT_ID` mapped to environment variables:

###  YAML 
        
        steps:
        - name: 'ubuntu'
          script: |
            #!/usr/bin/env bash
            echo "Hello $_USER"
        - name: 'ubuntu'
          script: |
            #!/usr/bin/env bash
            echo "Your project ID is $PROJECT_ID"
        options:
          automapSubstitutions: true
        substitutions:
          _USER: "Google Cloud"
        

###  JSON 
        
        {
          "steps": [
            {
              "name": "ubuntu",
              "script": "#!/usr/bin/env bash echo 'Hello $_USER'"
            },
            {
              "name": "ubuntu",
              "script": "#!/usr/bin/env bash echo 'Your project ID is $PROJECT_ID'"
            }
          ],
          "options": {
            "automap_substitutions": true
          },
          "substitutions": {
            "_USER": "Google Cloud"
          }
        }
        

  * **At the step level**. To automatically map all the substitutions and make them available as environment variables in a single step, set the `automapSubstitutions` field to `true` in that step. In the following example, only the second step will show the substitutions correctly, because it's the only one with automatic substitutions mapping enabled:

###  YAML 
        
        steps:
        - name: 'ubuntu'
          script: |
            #!/usr/bin/env bash
            echo "Hello $_USER"
        - name: 'ubuntu'
          script: |
            #!/usr/bin/env bash
            echo "Your project ID is $PROJECT_ID"
          automapSubstitutions: true
        substitutions:
          _USER: "Google Cloud"
        

###  JSON 
        
        {
          "steps": [
            {
              "name": "ubuntu",
              "script": "#!/usr/bin/env bash echo 'Hello $_USER'"
            },
            {
              "name": "ubuntu",
              "script": "#!/usr/bin/env bash echo 'Your project ID is $PROJECT_ID'",
              "automap_substitutions": true
            }
          ],
          },
          "substitutions": {
            "_USER": "Google Cloud"
          }
        

Additionally, you can make the substitutions available as environment variables in the entire build, then ignore them in one step. Set `automapSubstitutions` to `true` at the build level, then set the same field to `false` in the step where you want to ignore the substitutions. In the following example, even though mapping substitutions is enabled at the build level, the project ID will not be printed in the second step, because `automapSubstitutions` is set to `false` in that step:

###  YAML 
        
        steps:
        - name: 'ubuntu'
          script: |
            #!/usr/bin/env bash
            echo "Hello $_USER"
        - name: 'ubuntu'
          script: |
            #!/usr/bin/env bash
            echo "Your project ID is $PROJECT_ID"
          automapSubstitutions: false
        options:
          automapSubstitutions: true
        substitutions:
          _USER: "Google Cloud"
        

###  JSON 
        
        {
          "steps": [
            {
              "name": "ubuntu",
              "script": "#!/usr/bin/env bash echo 'Hello $_USER'"
            },
            {
              "name": "ubuntu",
              "script": "#!/usr/bin/env bash echo 'Your project ID is $PROJECT_ID'",
              "automap_substitutions": false
            }
          ],
          "options": {
            "automap_substitutions": true
          },
          },
          "substitutions": {
            "_USER": "Google Cloud"
          }
        




### Map substitutions manually

You can manually map the substitutions to environment variables. Every environment variable is defined at the step level using [the `env` field](https://docs.cloud.google.com/build/docs/build-config-file-schema#env), and the scope of the variables is restricted to the step where they are defined. This field takes a list of keys and values.

The following example shows how to map the substitution `$PROJECT_ID` to the environment variable `BAR`:

###  YAML 
    
    
    steps:
    - name: 'ubuntu'
      env:
      - 'BAR=$PROJECT_ID'
      script: 'echo $BAR'
    

###  JSON 
    
    
    {
      "steps": [
        {
          "name": "ubuntu",
          "env": [
            "BAR=$PROJECT_ID"
          ],
          "script": "echo $BAR"
        }
      ]
    }
    

## Running bash scripts on disk

If you have your bash script saved in a file, store the file along with your build source, and reference the script file within your build config file:

###  YAML 
    
    
    steps:
    - name: 'bash'
      args: ['./myscript.bash']
    

###  JSON 
    
    
    {
      "steps": [
      {
        "name": "bash",
        "args": [
          "./myscript.bash"
         ]
      }
      ]
    }
    

To use a bash script on file if bash is not the default entrypoint of the image you're using, add an `entrypoint` field pointing to bash:

###  YAML 
    
    
    steps:
    - name: 'gcr.io/cloud-builders/gcloud'
      entrypoint: 'bash'
      args: ['tools/myScript.sh','--foo']
    

###  JSON 
    
    
    {
      "steps": [
      {
        "name": "gcr.io/cloud-builders/gcloud",
        "entrypoint": "bash",
        "args": [
          "tools/myScript.sh",
          "--foo"
        ]
      }
      ]
    }
    

## Running inline bash scripts

To run bash commands using the `bash` image, specify `bash` as the `name` of the build step, and the command in the args field:

###  YAML 
    
    
    steps:
    - name: 'bash'
      args: ['echo', 'I am running a bash command']
    

###  JSON 
    
    
    {
      "steps": [
        {
          "name": "bash",
          "args": [
            "echo",
            "I am running a bash command"
           ]
        }
      ]
    }
    

If the image you're using comes prepackaged with `bash` but if `bash` is not the default entrypoint, add an `entrypoint` field pointing to `bash`. In the example below, the `bash` entrypoint is used to run `gcloud` commands that query Cloud Build for build status, listing builds with a failed status.

###  YAML 
    
    
    steps:
    - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
      entrypoint: 'bash'
      args:
      - '-eEuo'
      - 'pipefail'
      - '-c'
      - |-
        gcloud builds list > builds.txt
        while read line; do
            if grep -q "FAILURE" <<< "$line"; then
                echo "$line"
            fi
        done < builds.txt
    

###  JSON 
    
    
    {
      "steps": [
      {
        "name": "gcr.io/google.com/cloudsdktool/cloud-sdk",
        "entrypoint": "bash",
        "args": [
          "-eEuo",
          "pipefail",
          "-c",
          "gcloud builds list > builds.txt\nwhile read line; do\n    if grep -q \"FAILURE\" <<< \"$line\"; then\n        echo \"$line\"\n    fi\ndone < builds.txt"
        ]
      }
      ]
    }
    

The `-c` flag in the code above is used to execute multi-line commands. Any string you pass after `-c` is treated as a command. For more information on running bash commands with `-c`, see the [bash documentation](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Invoking-Bash).

## What's next

  * Learn how to [start a build manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually).
  * Learn how to [automate builds using triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * Learn how to [configure build step order](https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order).
  * Learn how to [use community-contributed builders and custom builders](https://docs.cloud.google.com/build/docs/configuring-builds/use-community-and-custom-builders).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
