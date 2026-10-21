---
url: https://docs.cloud.google.com/build/docs/securing-builds/use-encrypted-credentials/
title: Use encrypted credentials from Cloud KMS \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:09.396336+00:00
---

# Use encrypted credentials from Cloud KMS  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/use-encrypted-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Use encrypted credentials from Cloud KMS Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Key Management Service](https://docs.cloud.google.com/kms) is a Google Cloud service that enables you to manage and use cryptographic keys. This page explains how to use encrypted information from Cloud KMS in Cloud Build.

**Note:** Secret Manager is the recommended technique for managing sensitive data with Cloud Build. For existing projects, you can continue using Cloud KMS, but for new projects, use Secret Manager. For instructions on configuring builds to access secrets from Secret Manager, see [Using secrets from Secret Manager](https://docs.cloud.google.com/build/docs/securing-builds/use-secrets).

## Before you begin

  * Enable the Cloud Build and Cloud KMS APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,cloudkms.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/securing-builds/use-encrypted_credentials)

  * To use the command-line examples in this guide, install and configure the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

**Note:** If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
  * Encrypt the sensitive information using [Cloud KMS](https://docs.cloud.google.com/kms/docs/quickstart). Cloud KMS saves your encrypted content in a file.

  * [OPTIONAL] To configure builds to use encrypted data, convert the ENCRYPTED_FILE to base64 (this step is not required for build configs that use encrypted files):
        
        base64 ENCRYPTED_FILE
        




### Required IAM permissions

Grant the [Cloud KMS CryptoKey Decrypter (`roles/cloudkms.cryptoKeyDecrypter`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) IAM role to the build service account:

  1. In the Google Cloud console, go to the Cloud Build **Settings** page:

[ Open the Settings page](https://console.cloud.google.com/cloud-build/settings)

  2. Locate the row with the **Cloud KMS CryptoKey Decrypter** role and set its **Status** to **ENABLED**.


**Warning:** Granting the Cloud KMS CryptoKey Decrypter role to the default Cloud Build service account allows the service account to decrypt the encrypted information. [Build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers) use the default Cloud Build service account to execute builds. Therefore, any user who uses build triggers to run builds will have permissions granted to the service account at build time. This allows users without the CryptoKey Decrypter role to use build triggers to perform a build that decrypts the encrypted information. This action is logged in the project's [build history](https://console.cloud.google.com/cloud-build/builds).

## Configuring builds to use encrypted data

  1. In your project root directory, create a Cloud Build build config file named `cloudbuild.yaml` or `cloudbuild.json`.

  2. In your build config file:

     * After all the build `steps`, add an `availableSecrets` field to specify the encrypted value as an environment variable and the `kmsKeyName` to use to decrypt it. You can use [substitution variables](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values) in the value of `kmsKeyName`.
     * In the build step where you want to specify the secret: 
       * Add an `entrypoint` field pointing to `bash` to use the bash tool in the build step. This is required to refer to the environment variable for the secret.
       * Add a `secretEnv` field specifying the environment variable for the encrypted value.
       * In the `args` field, add a `-c` flag as the first argument. Any string you pass after -c is treated as a command. For more information on running bash commands with -c, see the [bash documentation](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Invoking-Bash).
       * When specifying the encrypted value in the `args` field, specify it using the environment variable prefixed with `$$`.
**Note:** You can refer to encrypted values using environment variables only in the `args` field of a build step.

The following example build config file shows how to login to Docker and pull a private image:

###  YAML
    
    steps:
     - name: 'gcr.io/cloud-builders/docker'
       entrypoint: 'bash'
       args: ['-c', 'docker login --username=$$USERNAME --password=$$PASSWORD']
       secretEnv: ['USERNAME', 'PASSWORD']
     - name: 'gcr.io/cloud-builders/docker'
       entrypoint: 'bash'
       args: ['-c', 'docker pull $$USERNAME/IMAGE:TAG']
       secretEnv: ['USERNAME']
     availableSecrets:
       inline:
       - kmsKeyName: projects/PROJECT_ID/locations/global/keyRings/USERNAME_KEYRING_NAME/cryptoKeys/USERNAME_KEY_NAME
         envMap:
           USERNAME: 'ENCRYPTED_USERNAME'
       - kmsKeyName: projects/PROJECT_ID/locations/global/keyRings/PASSWORD_KEYRING_NAME/cryptoKeys/PASSWORD_KEY_NAME
         envMap:
           PASSWORD: 'ENCRYPTED_PASSWORD'
    

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
      },
      {
        "name": "gcr.io/cloud-builders/docker",
        "entrypoint": "bash",
        "args": [
          "-c",
          "docker pull $$USERNAME/REPOSITORY:TAG"
         ],
         "secretEnv": [
          "USERNAME"
        ]
      }
      ],
      "availableSecrets": {
        "inline": [{
          "kmsKeyName":  "projects/PROJECT_ID/locations/global/keyRings/USERNAME_KEYRING_NAME/cryptoKeys/USERNAME_KEY_NAME",
          "envMap": {
            "USERNAME": "ENCRYPTED_USERNAME"
           }
       },
       {
        "kmsKeyName": "projects/PROJECT_ID/locations/global/keyRings/PASSWORD_KEYRING_NAME/cryptoKeys/PASSWORD_KEY_NAME",
        "envMap": {
            "PASSWORD": "ENCRYPTED_PASSWORD"
           }
       }]
     }
    }
    

Replace the placeholder values in the above commands with the following:

     * `PROJECT_ID`: The ID of the Google Cloud project which contains your Cloud KMS service.
     * `USERNAME_KEYRING_NAME`: The key ring name of your Docker username.
     * `USERNAME_KEY_NAME`: The key name of your Docker username.
     * `ENCRYPTED_USERNAME`: Your encrypted Docker username in base64 format.
     * `PASSWORD_KEYRING_NAME`: The key ring name of your Docker password.
     * `PASSWORD_KEY_NAME`: The key name of your Docker password.
     * `ENCRYPTED_PASSWORD`: Your encrypted Docker password in base64 format.
     * `REPOSITORY`: The name of your Docker repository from where you're pulling the image.
     * `TAG`: The tag name of your image.

**Note:** The `secretEnv` field does not support substitution variables. If the Google Cloud project hosting the key changes, the encrypted contents within that project also change.
  3. Use the build config file to [manually start a build](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or to [automate builds using triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).




## Configuring builds to use encrypted files

  1. In your project root directory, create a Cloud Build build config file named `cloudbuild.yaml` or `cloudbuild.json`.

  2. In your build config file, before any build steps that interact with the decrypted file, add a `gcloud` build step to decrypt the encrypted file using the encryption key. The following example build config file shows how to login to Docker using the encrypted file with Docker password:

###  YAML 
         
         steps:
         - name: gcr.io/cloud-builders/gcloud
           args:
           - kms
           - decrypt
           - "--ciphertext-file=ENCRYPTED_PASSWORD_FILE"
           - "--plaintext-file=PLAINTEXT_PASSWORD_FILE"
           - "--location=global"
           - "--keyring=KEYRING_NAME"
           - "--key=KEY_NAME"
         - name: gcr.io/cloud-builders/docker
           entrypoint: bash
           args:
           - "-c"
           - docker login --username=DOCKER_USERNAME --password-stdin < PLAINTEXT_PASSWORD_FILE
         

###  JSON 
         
         {
           "steps": [
           {
             "name": "gcr.io/cloud-builders/gcloud",
             "args": [
               "kms",
               "decrypt",
               "--ciphertext-file=ENCRYPTED_PASSWORD_FILE",
               "--plaintext-file=PLAINTEXT_PASSWORD_FILE",
               "--location=global",
               "--keyring=KEYRING_NAME",
               "--key=KEY_NAME"
             ]
           },
           {
             "name": "gcr.io/cloud-builders/docker",
             "entrypoint": "bash",
             "args": [
               "-c",
               "docker login --username=DOCKER_USERNAME --password-stdin < PLAINTEXT_PASSWORD_FILE"
             ]
            }
           ]
         }
         

Replace the placeholder values in the above commands with the following:

     * `KEYRING_NAME`: The key ring name of your Docker password.
     * `KEY_NAME`: The key name of your Docker password.
     * `ENCRYPTED_PASSWORD_FILE`: Encrypted file with your Docker password.
     * `PLAINTEXT_PASSWORD_FILE`: Plaintext file with your Docker password.
  3. Use the build config file to [manually start a build](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or to [automate builds using triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).




## Configuring builds to use encrypted data (legacy)

**Warning:** This is the legacy method of using Cloud KMS with Cloud Build. This method will continue to work, but we recommend that you use the newer way of configuring builds to use encrypted data.

To encrypt sensitive data using Cloud KMS and use that data in a build config file:

  1. In your build config file, add a `secrets` field to specify the encrypted value and the `CryptoKey` to use to decrypt it. Then, in the build step where you want to use the encrypted variable, add a `secretEnv` field to specify the variable as an environment variable. Include the variable's name in the `secretEnv` field. If you specify the variable value, or a non-secret environment variable with the same name, Cloud Build throws an error.

###  YAML
         
         steps:
         - name: 'gcr.io/cloud-builders/docker'
           entrypoint: 'bash'
           args: ['-c', 'docker login --username=user-name --password=$$PASSWORD']
           secretEnv: ['PASSWORD']
         - name: 'gcr.io/cloud-builders/docker'
           args: ['push', 'user-name/myubuntu']
         secrets:
         - kmsKeyName: projects/project-id/locations/global/keyRings/keyring-name/cryptoKeys/key-name
           secretEnv:
             PASSWORD: 'encrypted-password'
         

###  JSON 
         
         {
           "steps": [
           {
             "name": "gcr.io/cloud-builders/docker",
             "entrypoint": "bash",
             "args": [
               "-c",
               "docker login --username=user-name --password=$$PASSWORD"
             ],
             "secretEnv": [
               "PASSWORD"
              ]
            },
            {
              "name": "gcr.io/cloud-builders/docker",
              "args": [
                "push",
                "user-name/myubuntu"
               ]
            }
            ],
            "secrets": [
            {
              "kmsKeyName": "projects/project-id/locations/global/keyRings/keyring-name/cryptoKeys/key-name",
              "secretEnv": {
                "PASSWORD": "encrypted-password"
              }
            }
            ]
         }
         




## What's next

  * Learn how to [configure builds to access secrets from Secret Manager](https://docs.cloud.google.com/build/docs/securing-builds/use-secrets).
  * Learn how to [access private GitHub repositories](https://docs.cloud.google.com/build/docs/access-private-github-repos).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
