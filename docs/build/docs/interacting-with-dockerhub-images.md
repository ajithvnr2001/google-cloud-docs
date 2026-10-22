---
url: https://docs.cloud.google.com/build/docs/interacting-with-dockerhub-images/
title: Interacting with Docker Hub images \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:27.004618+00:00
---

# Interacting with Docker Hub images  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/interacting-with-dockerhub-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Interacting with Docker Hub images Stay organized with collections  Save and categorize content based on your preferences. 

You can use container images from [Docker Hub](https://hub.docker.com/) to execute your tasks in Cloud Build. Additionally, if your build produces images, you can push them to Docker Hub. This page describes how to write build config files to push and pull Docker Hub images. For an overview of all the fields available in a build config file, see [Build Configuration Overview](https://docs.cloud.google.com/build/docs/build-config).

## Pulling public images from Docker Hub

You can pull [official Docker images](https://hub.docker.com/search/?type=image&image_filter=official), [Docker-certified images](https://hub.docker.com/search/?type=image&certification_status=certified), and custom images stored in Docker Hub in your build step by specifying the name of the image in the `name` field. Cloud Build will first pull the specified image from Docker Hub and then use the image to run the build step.

**Note:** When you pull a public container image from Docker Hub to use in your build config file, Cloud Build automatically checks the caching proxy `mirror.gcr.io` for a cached copy of the container image. If a cached copy is unavailable, Cloud Build pulls your requested image from Docker Hub and the caching proxy might cache the image for future use. For more information, see [Pull cached Docker Hub images](https://docs.cloud.google.com/artifact-registry/docs/pull-cached-dockerhub-images).

In the example below, Cloud Build pulls the Docker image for [`maven`](https://hub.docker.com/_/maven) to run the `mvn` command specified in `args`:

###  YAML 
    
    
    steps:
    - name: "maven"
      args: ["mvn", "--version"]
    

###  JSON 
    
    
    {
       "steps": [
          {
             "name": "maven",
             "args": [
                "mvn",
                "--version"
             ]
          }
       ]
    }
    

## Storing Docker credentials in Secret Manager

To pull private images and to push public and private images to Docker Hub, Cloud Build will need to authenticate to Docker with your credentials. To include Docker credentials in your builds, you must first store your credentials in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs), and then grant permission for Cloud Build to access the secret from Secret Manager.

To store Docker credentials in Secret Manager:

  1. Go to the Secret Manager page in the Google Cloud console:

[Go to the Secret Manager page](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click **Create Secret**.

  3. On the **Create secret** page, under **Name** , enter `docker-username`.

  4. In the **Secret value** field, enter your Docker username.

  5. Leave the **Regions** section unchanged.

  6. Click the **Create secret** button.




Repeat the steps above to store your Docker password in Secret Manager.

To grant the [Secret Manager Secret Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager) IAM role for the secret to the service account you are using for the build:

  1. Open the Secret Manager page in the Google Cloud console:

[Go to the Secret Manager page](https://console.cloud.google.com/security/secret-manager)

  2. Select the checkbox of the secret corresponding to your Docker username and password.

  3. If it is not already open, click **Show info panel** to open the panel.

  4. In the panel, under **Permissions** , click **Add principal**.

  5. In the **New principals** field, enter the email address of your service account.

  6. In the **Select a role** drop-down box, select **Secret Manager Secret Accessor** role.

  7. Click **Save**.




## Pulling private images from Docker Hub

To pull private images from Docker Hub:

  1. Make sure you've stored your Docker credentials in Secret Manager and granted permissions for Cloud Build to access the secret.

  2. In the build config file:

     * After all the build `steps`, add an `availableSecrets` field specifying the secret version and the env variable for the Docker username and password.
     * In the build step where you want to specify the username and password: 
       * Add an `entrypoint` field pointing to `bash` to use the bash tool in the build step. This is required to refer to the environment variable for the secret.
       * Add a `secretEnv` field specifying the environment variable for username and password.
       * In the `args` field, add a `-c` flag as the first argument. Any string you pass after -c is treated as a command. For more information on running bash commands with -c, see the [bash documentation](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Invoking-Bash).
       * When specifying the secret in the `args` field, specify it using the environment variable prefixed with `$$`.

The following build config file shows how to login to Docker using the Docker username and password stored in Secret Manager, and run a private image.

###  YAML 
    
    steps:
     - name: 'gcr.io/cloud-builders/docker'
       entrypoint: 'bash'
       args: ['-c', 'docker login --username=$$USERNAME --password=$$PASSWORD']
       secretEnv: ['USERNAME', 'PASSWORD']
     - name: "gcr.io/cloud-builders/docker"
       entrypoint: 'bash'
       args: ['-c', 'docker run $$USERNAME/REPOSITORY:TAG']
       secretEnv: ['USERNAME']
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
      },
      {
        "name": "gcr.io/cloud-builders/docker",
        "entrypoint": "bash",
        "args": [
          "-c",
          "docker run $$USERNAME/REPOSITORY:TAG"
         ],
         "secretEnv": [
          "USERNAME"
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
    

Replace the placeholder values in the above commands with the following:

     * `PROJECT_ID`: The ID of the Google Cloud project where you've stored your secrets.
     * `DOCKER_USERNAME_SECRET_NAME`: The secret name corresponding to your Docker username.
     * `DOCKER_USERNAME_SECRET_VERSION`: The secret version of your Docker username.
     * `DOCKER_PASSWORD_SECRET_NAME`: The secret name corresponding to your Docker password.
     * `DOCKER_PASSWORD_SECRET_VERSION`: The secret version of your Docker password.
     * `REPOSITORY`: The name of your Docker repository from where you're pulling the image.
     * `TAG`: The tag name of your image.
  3. Use the build config file to [manually start a build](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or to [automate builds using triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).




## Pushing images to Docker Hub

To push public and private images to Docker Hub:

  1. Make sure you've [stored your Docker credentials in Secret Manager and granted permissions for Cloud Build to access the secret](https://docs.cloud.google.com/build/docs/interacting-with-dockerhub-images#storing_docker_credentials_in).

  2. In the build config file:

     * After all the build `steps`, add an `availableSecrets` field specifying the secret version and the env variable for the Docker username and password.
     * In the build step where you want to specify the username and password: 
       * Add an `entrypoint` field pointing to `bash` to use the bash tool in the build step. This is required to refer to the environment variable for the secret.
       * Add a `secretEnv` field specifying the environment variable for username and password.
       * In the `args` field, add a `-c` flag as the first argument. Any string you pass after `-c` is treated as a command. For more information on running bash commands with -c, see the [bash documentation](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Invoking-Bash).
       * When specifying the secret in the `args` field, specify it using the environment variable prefixed with `$$`.

The following example build config file shows how to login to Docker, build an image with source code stored locally, and then push the image to Docker repository.

###  YAML 
    
    steps:
     - name: 'gcr.io/cloud-builders/docker'
       entrypoint: 'bash'
       args: ['-c', 'docker login --username=$$USERNAME --password=$$PASSWORD']
       secretEnv: ['USERNAME', 'PASSWORD']
     - name: 'gcr.io/cloud-builders/docker'
       entrypoint: 'bash'
       args: ['-c', 'docker build -t $$USERNAME/REPOSITORY:TAG .']
       secretEnv: ['USERNAME']
     - name: 'gcr.io/cloud-builders/docker'
       entrypoint: 'bash'
       args: ['-c', 'docker push $$USERNAME/REPOSITORY:TAG']
       secretEnv: ['USERNAME']
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
      },
      {
        "name": "gcr.io/cloud-builders/docker",
        "entrypoint": "bash",
        "args": [
          "-c",
          "docker build -t $$USERNAME/REPOSITORY:TAG ."
         ],
         "secretEnv": [
          "USERNAME"
        ]
      },
      {
        "name": "gcr.io/cloud-builders/docker",
        "entrypoint": "bash",
        "args": [
          "-c",
          "docker push $$USERNAME/REPOSITORY:TAG"
         ],
         "secretEnv": [
          "USERNAME"
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
    

Replace the placeholder values in the above commands with the following:

     * `PROJECT_ID`: The ID of the Google Cloud project where you've stored your secrets.
     * `DOCKER_USERNAME_SECRET_NAME`: The secret name corresponding to your Docker username.
     * `DOCKER_USERNAME_SECRET_VERSION`: The secret version of your Docker username.
     * `DOCKER_PASSWORD_SECRET_NAME`: The secret name corresponding to your Docker password.
     * `DOCKER_PASSWORD_SECRET_VERSION`: The secret version of your Docker password.
     * `REPOSITORY`: The name of your Docker repository to which you're pushing the image.
     * `TAG`: The tag name of your image.
  3. Use the build config file to [manually start a build](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or to [automate builds using triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).




### Working with Docker client versions

The supported Docker builder for Cloud Build, `gcr.io/cloud-builders/docker` uses Docker 20.10.14. With this version, if you don't specify a tag when pushing an image to Docker, Docker pushes only the image with the `latest` tag. If the `latest` tag doesn't exist, the push fails. 

To push an image with a specific tag to Docker, specify the tag in the `docker push` build step. The following example pushes an image tagged `prod`:

###  YAML 
    
    
    steps:
    ...
    - name: 'gcr.io/cloud-builders/docker'
      args: ['docker', 'push', '$$USERNAME/myrepo:prod']
    ...
    

###  JSON 
    
    
    {
      ...
      {
        "name": "gcr.io/cloud-builders/docker",
        "args": [
          "docker",
          "push", 
          "$$USERNAME/myrepo:prod"
          ],
      }
      ...
    }
    

To push all tags of an image to Docker, add the `-a` flag to the list of args in the `docker push` build step:

###  YAML 
    
    
    steps:
    ...
    - name: 'gcr.io/cloud-builders/docker'
      args: ['docker', 'push', '-a', '$$USERNAME/myrepo']
    ...
    

###  JSON 
    
    
    {
      ...
      {
        "name": "gcr.io/cloud-builders/docker",
        "args": [
          "docker",
          "push",
          "-a",
          "$$USERNAME/myrepo"
          ],
      }
      ...
    }
    

You can use Docker client 19.03.9 by tagging the version in the Docker builder:

###  YAML 
    
    
    steps:
    ...
    - name: 'gcr.io/cloud-builders/docker:19.03.9'
      args: ['docker', 'push', '$$USERNAME/myrepo:prod']
    ...
    

###  JSON 
    
    
    {
      ...
      {
        "name": "gcr.io/cloud-builders/docker:19.03.9",
        "args": [
          "docker",
          "push",
          "$$USERNAME/myrepo:prod"
          ],
      }
      ...
    }
    

## What's next

  * Learn how to [write a basic build configuration file](https://docs.cloud.google.com/build/docs/configuring-builds/create-basic-configuration).
  * Learn how to [run builds manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually) or [automate using build triggers](https://docs.cloud.google.com/build/docs/running-builds/automate-builds).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
