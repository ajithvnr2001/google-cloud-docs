---
url: https://docs.cloud.google.com/build/docs/securing-builds/use-secrets/
title: Use secrets from Secret Manager \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:09.189553+00:00
---

# Use secrets from Secret Manager  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/use-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Use secrets from Secret Manager Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to include sensitive information such as passwords and API keys in Cloud Build.

[Secret Manager](https://docs.cloud.google.com/secret-manager/docs) is a Google Cloud service that securely stores API keys, passwords, and other sensitive data. To include sensitive information in your builds, you can store the information in Secret Manager and then configure your build to access the information from Secret Manager.

## Before you begin

  * Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/securing-builds/use-secrets)

  * To use the command-line examples in this guide, install and configure the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

**Note:** If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
  * Make sure you've stored the secret in Secret Manager. For instructions, see [Creating a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create).

    * Note down the secret name and secret version of your secret. You'll need this information to configure Cloud Build to access the secret.



### Required IAM permissions

Grant the [Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager) IAM role for the secret to the service account you are using for the build:

  1. Open the Secret Manager page in the Google Cloud console:

[Go to the Secret Manager page](https://console.cloud.google.com/security/secret-manager)

  2. Select the checkbox of the secret you wish to use in your build.

  3. If it is not already open, click **Show info panel** to open the panel.

  4. In the panel, under **Permissions** , click **Add principal**.

  5. In the **New principals** field, enter the email address of your service account.

  6. In the **Select a role** drop-down box, select **Secret Manager Secret Accessor**.

  7. Click **Save**.


**Warning:** Granting Secret Manager Secret Accessor role to the legacy Cloud Build service account allows the service account to access the secret. If [Build trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers) is configured to use the legacy Cloud Build service account to execute builds, any user who uses build triggers to run builds will have permissions granted to the service account at build time. This allows users without the Secret Accessor role to use build triggers to perform a build that accesses the secret. This action is logged in the project's [build history](https://console.cloud.google.com/cloud-build/builds).

## Configuring builds to access UTF-8 secrets from Secret Manager

  1. In your project root directory, create a Cloud Build config file named `cloudbuild.yaml` or `cloudbuild.json`.

  2. In the build config file:

     * After all the build `steps`, add an `availableSecrets` field that contains a `secretManager` field. The `secretManager` field contains one or more pairs of the `versionName` and `env` fields:

       * `versionName`: the path to the secret in Secret Manager. You can include [substitution variables](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values) in the value of this field.
       * `env`: a local name (environment variable) that build steps can use to reference the secret.
     * In the build step where you want to specify the secret:

       * Add an `entrypoint` field pointing to `bash` to use the bash tool in the build step. This is **required** to refer to the environment variable for the secret.
       * Add a `secretEnv` field. This field specifies which environment variables can be used in that step.
       * In the `args` field, add a `-c` flag as the first argument. Any string you pass after `-c` is treated as a command. For more information on running bash commands with `-c`, see the [bash documentation](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Invoking-Bash).
       * When specifying the secret in the `args` field, specify it using the environment variable prefixed with `$$`.
**Note:** You can refer to secrets only in the `args` field of a build step.

The following example build config file shows how to login to Docker using the Docker username and password stored in Secret Manager:

###  YAML 
    
    steps:
    - name: 'gcr.io/cloud-builders/docker'
      entrypoint: 'bash'
      args: ['-c', 'docker login --username=$$USERNAME --password=$$PASSWORD']
      secretEnv: ['USERNAME', 'PASSWORD']
    availableSecrets:
      secretManager:
      - versionName: projects/PROJECT_ID/secrets/DOCKER_PASSWORD_SECRET_NAME/versions/DOCKER_PASSWORD_SECRET_VERSION
        env: 'PASSWORD'
      - versionName: projects/PROJECT_ID/secrets/DOCKER_USERNAME_SECRET_NAME/versions/DOCKER_USERNAME_SECRET_VERSION
        env: 'USERNAME'
    

###  JSON 
    
    {
      "steps": [
      {
        "name": "gcr.io/cloud-builders/docker",
        "entrypoint": "bash",
        "args": [
          "-c",
          "docker login --username=$$USERNAME --password=$$PASSWORD"
        ],
        "secretEnv": [
          "USERNAME",
          "PASSWORD"
        ]
      }
      ],
      "availableSecrets": {
        "secretManager": [{
          "versionName": "projects/PROJECT_ID/secrets/DOCKER_PASSWORD_SECRET_NAME/versions/DOCKER_PASSWORD_SECRET_VERSION",
          "env": "PASSWORD"
      }, {
        "versionName": "projects/PROJECT_ID/secrets/DOCKER_USERNAME_SECRET_NAME/versions/DOCKER_USERNAME_SECRET_VERSION",
        "env": "USERNAME"
         }]
      }
    }
    

Replace the placeholder values in the preceding commands with the following:

     * `PROJECT_ID`: The [project ID or project number](https://docs.cloud.google.com/docs/overview#projects) of the Google Cloud project where you've stored your secrets.
     * `DOCKER_USERNAME_SECRET_NAME`: The secret name corresponding to your Docker username. You can get the secret name from the [**Secret Manager** page](https://console.cloud.google.com/security/secret-manager) in the Google Cloud console.
     * `DOCKER_USERNAME_SECRET_VERSION`: The secret version of your Docker username. You can get the secret version by clicking on a secret name on the [**Secret Manager** page](https://console.cloud.google.com/security/secret-manager) in the Google Cloud console.
     * `DOCKER_PASSWORD_SECRET_NAME`: The secret name corresponding to your Docker password. You can get the secret name from the [**Secret Manager** page](https://console.cloud.google.com/security/secret-manager) in the Google Cloud console.
     * `DOCKER_PASSWORD_SECRET_VERSION`: The secret version of your Docker password. You can get the secret version by clicking on a secret name on the [**Secret Manager** page](https://console.cloud.google.com/security/secret-manager) in the Google Cloud console.
  3. Use the build config file to [start a build using the command line](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or to [automate builds using triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).




### Example: Accessing secrets from scripts and processes

In this example, a secret is defined in the build step so that it can be used later in a script:

###  YAML 
    
    
    steps:
    - name: python:slim
      entrypoint: python
      args: ['main.py']
      secretEnv: ['MYSECRET']
    availableSecrets:
      secretManager:
      - versionName: projects/$PROJECT_ID/secrets/mySecret/versions/latest
        env: 'MYSECRET'
    

###  JSON 
    
    
    {
      "steps": [
      {
        "name": "python:slim",
        "entrypoint": "python",
        "args": [
            "main.py"
        ],
        "secretEnv": [
            "MYSECRET"
        ]
    }
    ],
    "availableSecrets": {
      "secretManager": [
        {
            "versionName": "projects/$PROJECT_ID/secrets/mySecret/versions/latest",
            "env": "MYSECRET"
        }
      ]
    }
    }
    

The following contents of `main.py` prints the first five characters of the secret:
    
    
    import os
    print(os.environ.get("MYSECRET", "Not Found")[:5], "...")
    

### Example: authenticating to Docker

In some situations, before interacting with Docker images, your build would need to authenticate to Docker. For example, Docker authentication is required for builds to pull private images and push private or public images to Docker Hub. In these cases, you can store your Docker username and password in Secret Manager and then configure Cloud Build to access the username and password from Secret Manager. For instructions on doing this see [Interacting with Docker Hub images](https://docs.cloud.google.com/build/docs/interacting-with-dockerhub-images).

### Example: GitHub pull request creation

Another example where you might want to configure your build to access a sensitive information from Secret Manager is for creating a GitHub pull request in response to builds. To do this:

  * Create a [GitHub token](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token).
  * Store the GitHub token in Secret Manager.
  * In your build config file: 
    * After all the build `steps`, add an `availableSecrets` field to specify the secret version and the environment variable to use for the GitHub token.
    * Add a build step to invoke the [command to create a GitHub pull request](https://docs.github.com/en/free-pro-team@latest/rest/reference/pulls#create-a-pull-request).
  * Create a [GitHub app trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-github-app-triggers) and use the build config file to invoke the trigger.



The following example config file shows how to create a GitHub pull request using the GitHub token:

###  YAML 
    
    
    steps:
    - name: 'launcher.gcr.io/google/ubuntu1604'
      id: Create GitHub pull request
      entrypoint: bash
      args:
      - -c
      - curl -X POST -H "Authorization:Bearer $$GH_TOKEN" -H 'Accept:application/vnd.github.v3+json' https://api.github.com/repos/GITHUB_USERNAME/REPO_NAME/pulls -d '{"head":"HEAD_BRANCH","base":"BASE_BRANCH", "title":"NEW_PR"}'
      secretEnv: ['GH_TOKEN']
    availableSecrets:
      secretManager:
      - versionName: projects/PROJECT_ID/secrets/GH_TOKEN_SECRET_NAME/versions/latest
        env: GH_TOKEN
    

###  JSON 
    
    
    {
      "steps": [
      {
        "name": "launcher.gcr.io/google/ubuntu1604",
        "id": "Create GitHub pull request",
        "entrypoint": "bash",
        "args": [
          "-c",
           "curl -X POST -H \"Authorization:Bearer $$GH_TOKEN\" -H 'Accept:application/vnd.github.v3+json' https://api.github.com/repos/GITHUB_USERNAME/REPO_NAME -d '{\"head\":\"HEAD_BRANCH\",\"base\":\"BASE_BRANCH\", \"title\":\"NEW_PR\"}'
        ],
        "secretEnv": ['GH_TOKEN']
    }
    ],
    "availableSecrets": {
      "secretManager": [
      {
        "versionName": "projects/PROJECT_ID/secrets/GH_TOKEN_SECRET_NAME/versions/latest",
        "env": "GH_TOKEN"
      }
      ]
    }
    }
    

Replace the placeholder values in the preceding commands with the following:

  * `PROJECT_ID`: The [project ID or project number](https://docs.cloud.google.com/docs/overview#projects) of the Google Cloud project where you've stored your secrets.
  * `GITHUB_USERNAME`: The GitHub username of the repository owner.
  * `REPO_NAME`: The name of the GitHub repository.
  * `HEAD_BRANCH`: The name of the branch where the changes are implemented. For cross-repository pull requests in the same network, namespace `head` with a user like this: `username:branch`.
  * `BASE_BRANCH`: The name of the branch you want the changes pulled into. This should be an existing branch on the current repository. You cannot submit a pull request to one repository that requests a merge to a base of another repository.
  * `GH_TOKEN_SECRET_NAME`: The secret name corresponding to your GitHub token.
  * `NEW_PR`: The new pull request you want to create.



## Configuring builds to access non-UTF-8 secrets from Secret Manager

  1. In your build config file, add a build step to access the secret version in Secret Manager and store it in a file. The following build step accesses secret-name and stores it in a file named decrypted-data.txt:

###  YAML 
         
         steps:
         - name: gcr.io/cloud-builders/gcloud
           entrypoint: 'bash'
           args: [ '-c', "gcloud secrets versions access latest --secret=secret-name --format='get(payload.data)' | tr '_-' '/+' | base64 -d > decrypted-data.txt" ]
         

###  JSON 
         
         {
           "steps": [
           {
             "name": "gcr.io/cloud-builders/gcloud",
             "entrypoint": "bash",
             "args": [
               "-c",
               "gcloud secrets versions access latest --secret=secret-name --format='get(payload.data)' | tr '_-' '/+' | base64 -d > decrypted-data.txt"
             ]
           }
           ]
         }
         

  2. Use the file with the decrypted data in a build step. The following code snippet uses decrypted-data.txt to login to a private Docker registry:

###  YAML 
         
         steps:
         - name: gcr.io/cloud-builders/gcloud
           entrypoint: 'bash'
           args: [ '-c', "gcloud secrets versions access latest --secret=secret-name --format='get(payload.data)' | tr '_-' '/+' | base64 -d > decrypted-data.txt" ]
         - name: gcr.io/cloud-builders/docker
           entrypoint: 'bash'
           args: [ '-c', 'docker login --username=my-user --password-stdin < decrypted-data.txt']
         

###  JSON 
         
         {
           "steps": [
           {
             "name": "gcr.io/cloud-builders/gcloud",
             "entrypoint": "bash",
             "args": [
               "-c",
               "gcloud secrets versions access latest --secret=secret-name --format='get(payload.data)' | tr '_-' '/+' | base64 -d > password.txt"
              ]
           },
           {
             "name": "gcr.io/cloud-builders/docker",
             "entrypoint": "bash",
             "args": [
               "-c",
               "docker login --username=my-user --password-stdin < decrypted-data.txt"
              ]
           }
           ]
         }
         

**Note:** To use the secret in an environment variable, you must prefix the variable name with an underscore "_" and escape the value using `$$`. For example: `_VARIABLE_NAME=$(cat password.txt) && echo -n $$_VARIABLE_NAME`.
  3. Use the build config file to [start a build using the command line](https://docs.cloud.google.com/cloud-build/docs/running-builds/start-build-manually) or to [automate builds using triggers](https://docs.cloud.google.com/cloud-build/docs/automating-builds/create-manage-triggers).




## What's next

  * Learn how to use [encrypted credentials in builds](https://docs.cloud.google.com/build/docs/securing-builds/use-encrypted-credentials).
  * Learn how to [access private GitHub repositories](https://docs.cloud.google.com/build/docs/access-private-github-repos).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
