---
url: https://docs.cloud.google.com/build/docs/optimize-builds/building-leaner-containers/
title: Building leaner containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:57.051813+00:00
---

# Building leaner containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/optimize-builds/building-leaner-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Building leaner containers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to build leaner Docker images.

## Building leaner containers

When you containerize an application, files that are not needed at runtime, such as build-time dependencies and intermediate files, can be inadvertently included in the container image. These unneeded files can increase the size of the container image and thus add extra time and cost as the image moves between your Docker registry and your container runtime.

To help reduce the size of your container image, separate the building of the application, along with the tools used to build it, from the assembly of the runtime container.

Cloud Build provides a [series of Docker containers](https://github.com/GoogleCloudPlatform/cloud-builders) with common developer tools such as Git, Docker, and the Google Cloud CLI. Use these tools to define a build config file with one step to build the application, and another step to assemble its final runtime environment.

For example, if you're building a Java application, which requires files such as the source code, application libraries, build systems, build system dependencies, and the JDK, you might have a Dockerfile that looks like the following:
    
    
    FROM java:8
    
    COPY . workdir/
    
    WORKDIR workdir
    
    RUN GRADLE_USER_HOME=cache ./gradlew buildDeb -x test
    
    RUN dpkg -i ./gate-web/build/distributions/*.deb
    
    CMD ["/opt/gate/bin/gate"]
    

In the above example, Gradle, which is used to build the package, downloads a large number of libraries in order to function. These libraries are essential to the building of the package, but are not needed at runtime. All of the runtime dependencies are bundled up in the package.

Each command in the `Dockerfile` creates a new layer in the container. If data is generated in that layer and is not deleted in the same command, that space cannot be recovered. In this case Gradle is downloading hundreds of megabytes of libraries to the `cache` directory in order to perform the build, but the libraries are not deleted.

A more efficient way to perform the build is to use Cloud Build to separate building the application from building its runtime layer.

The following example separates the step for building the Java application from the step for assembling the runtime container:

### YAML

  1. **Build the application** : In `cloudbuild.yaml`, add a step to build the application.

The following code adds a step that builds the `java:8` image, which contains the Java code.
         
         steps:
         **- name: 'java:8'
           env: ['GRADLE_USER_HOME=cache']
           entrypoint: 'bash'
           args: ['-c', './gradlew gate-web:installDist -x test']**
         

  2. **Assemble the runtime container** : In `cloudbuild.yaml`, add a step to assemble the runtime container. 

The following code adds a step named `gcr.io/cloud-builders/docker` that assembles the runtime container. It defines the runtime container in a separate file named `Dockerfile.slim`.

The example uses the Alpine Linux base layer `openjdk:8u111-jre-alpine`, which is incredibly lean. Also, it includes the JRE, instead of the bulkier JDK that was necessary to build the application.
         
         **cloudbuild.yaml**
         
         steps:
         - name: 'java:8'
           env: ['GRADLE_USER_HOME=cache']
           entrypoint: 'bash'
           args: ['-c',
                  './gradlew gate-web:installDist -x test']
         **- name: 'gcr.io/cloud-builders/docker'
           args: ['build',
                  '-t', 'gcr.io/$PROJECT_ID/$REPO_NAME:$COMMIT_SHA',
                  '-t', 'gcr.io/$PROJECT_ID/$REPO_NAME:latest',
                  '-f', 'Dockerfile.slim',
                  '.'
           ]**
         
         **Dockerfile.slim**
         
         FROM openjdk:8-jre-alpine
         
         COPY ./gate-web/build/install/gate /opt/gate
         
         CMD ["/opt/gate/bin/gate"]
         

  3. **Create the Docker images** : In `cloudbuild.yaml`, add a step to create the images. 
         
         steps:
         - name: 'java:8'
           env: ['GRADLE_USER_HOME=cache']
           entrypoint: 'bash'
           args: ['-c', './gradlew gate-web:installDist -x test']
         - name: 'gcr.io/cloud-builders/docker'
           args: ['build',
                  '-t', 'gcr.io/$PROJECT_ID/$REPO_NAME:$COMMIT_SHA',
                  '-t', 'gcr.io/$PROJECT_ID/$REPO_NAME:latest',
                  '-f', 'Dockerfile.slim', '.']
         **images:
         - 'gcr.io/$PROJECT_ID/$REPO_NAME:$COMMIT_SHA'
         - 'gcr.io/$PROJECT_ID/$REPO_NAME:latest'**
         




### JSON

  1. **Build the application** : In `cloudbuild.json`, add a step to build the application.

The following code adds a step named `java:8` for building the Java code.
         
         {
             "steps": [
             {
                 **"name": "java:8",
                 "env": [
                     "GRADLE_USER_HOME=cache"
                 ],
                 "entrypoint": "bash",
                 "args": [
                     "-c",
                     "./gradlew gate-web:installDist -x test"
                 ]**
             },
         }
         

  2. **Assemble the runtime container** : In `cloudbuild.json`, add a step to assemble the runtime container.

The following code adds a step named `gcr.io/cloud-builders/docker` that assembles the runtime container. It defines the runtime container in a separate file named `Dockerfile.slim`.

The example uses the Alpine Linux base layer `openjdk:8u111-jre-alpine`, which is incredibly lean. Also, it includes the JRE, instead of the bulkier JDK that was necessary to build the application.
         
         **cloudbuild.json:**
         
         {
             "steps": [
             {
                 "name": "java:8",
                 "env": [
                     "GRADLE_USER_HOME=cache"
                 ],
                 "entrypoint": "bash",
                 "args": [
                     "-c",
                     "./gradlew gate-web:installDist -x test"
                 ]
             },
             {
                 **"name": "gcr.io/cloud-builders/docker",
                 "args": [
                     "build",
                     "-t",
                     "gcr.io/$PROJECT_ID/$REPO_NAME:$COMMIT_SHA",
                     "-t",
                     "gcr.io/$PROJECT_ID/$REPO_NAME:latest",
                     "-f",
                     "Dockerfile.slim",
                     "."
                 ]**
             }
             ],
         }
         
         **Dockerfile.slim:**
         
         FROM openjdk:8u111-jre-alpine
         
         COPY ./gate-web/build/install/gate /opt/gate
         
         CMD ["/opt/gate/bin/gate"]
         

  3. **Create the Docker images** : In `cloudbuild.json`, add a step to create the images. 
         
         {
             "steps": [
             {
                 "name": "java:8",
                 "env": [
                     "GRADLE_USER_HOME=cache"
                 ],
                 "entrypoint": "bash",
                 "args": [
                     "-c",
                     "./gradlew gate-web:installDist -x test"
                 ]
             },
             {
                 "name": "gcr.io/cloud-builders/docker",
                 "args": [
                     "build",
                     "-t",
                     "gcr.io/$PROJECT_ID/$REPO_NAME:$COMMIT_SHA",
                     "-t",
                     "gcr.io/$PROJECT_ID/$REPO_NAME:latest",
                     "-f",
                     "Dockerfile.slim",
                     "."
                 ]
             }
             ],
             **"images": [
                 "gcr.io/$PROJECT_ID/$REPO_NAME:$COMMIT_SHA",
                 "gcr.io/$PROJECT_ID/$REPO_NAME:latest"
             ]**
         }
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
