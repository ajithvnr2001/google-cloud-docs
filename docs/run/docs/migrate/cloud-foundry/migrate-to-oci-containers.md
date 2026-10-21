---
url: https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-to-oci-containers/
title: Migrate to OCI containers \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:50.753331+00:00
---

# Migrate to OCI containers  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-to-oci-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Migrate to OCI containers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the build infrastructure required to reproduce the Cloud Foundry build process while generating OCI-compatible application images. If you have already completed the [Spring Music migration guide](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/spring-music-migration-example) you can use this a deep dive into specific migration configurations for your application. 

![Diagram describing how to create OCI images using modern
tooling](https://docs.cloud.google.com/static/run/docs/images/cf-cr-oci.svg)

## Before you start

  1. Make sure you have set up a new project for Cloud Run as described in the [Cloud Run setup](https://docs.cloud.google.com/run/docs/setup) page.
  2. Make sure you have a `REGISTRY_URI` for storing containers. Cloud Run recommends using Artifact Registry. Docker is used to create intermediate images to build the project.



## Setting up a Cloud Foundry compatible build process

You must create two base OCI containers to support this new process:

  * A **builder image** that mirrors Cloud Foundry's build process and is capable of building application source code into Cloud Foundry droplets.
  * A **runtime image** that mirrors the Cloud Foundry application runtime.



This process needs to be done at least once by platform administrators. Once the process is established, the build and run images can can be shared by all Cloud Foundry applications that need to migrate to Cloud Run.

### Create the builder image

This section creates a build image using `cflinux3` as the base image. The build image is used as the build environment for creating the application image.

  1. Create a directory called `build/` and `cd` into it:
         
         mkdir build && cd build
         

  2. In the `build/` folder, create a new file called `Dockerfile` and paste in the following code:
         
         ARG CF_LINUX_FS=cloudfoundry/cflinuxfs3
         
         FROM golang:1.20-bullseye AS builder_build
         WORKDIR /build
         RUN ["git", "clone", "--depth=1", "https://github.com/cloudfoundry/buildpackapplifecycle.git"]
         WORKDIR /build/buildpackapplifecycle
         RUN ["go", "mod", "init", "code.cloudfoundry.org/buildpackapplifecycle"]
         RUN ["go", "mod", "tidy"]
         RUN CGO_ENABLD=0 go build -o /builder ./builder/
         
         FROM $CF_LINUX_FS
         # Set up container tools related to building applications
         WORKDIR /lifecycle
         COPY --from=builder_build /builder /lifecycle/builder
         
         # Set up environment to match Cloud Foundry's build.
         # https://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#app-system-env
         WORKDIR /staging/app
         WORKDIR /tmp
         ENV CF_INSTANCE_ADDR=127.0.0.1:8080 \
         CF_INSTANCE_IP=127.0.0.1 \
         CF_INSTANCE_INTERNAL_IP=127.0.0.1 \
         VCAP_APP_HOST=127.0.0.1 \
         CF_INSTANCE_PORT=8080 \
         LANG=en_US.UTF-8 \
         INSTANCE_GUID=00000000-0000-0000-0000-000000000000 \
         VCAP_APPLICATION={} \
         VCAP_SERVICES={} \
         CF_STACK=cflinuxfs3
         

  3. Use Cloud Build to build and publish the `builder` image
         
         gcloud builds \
             submit --tag "REGISTRY_URI/builder:stable"
         

Replace `REGISTRY_URI` with the address of the Artifact Registry where you want to publish the build image. For example: `REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/builder:stable`.




### Create the runtime image

This section creates a run image using `cflinux3` as the base image. The run image is used as the base image when you create the final application image.

  1. Create a directory called `run/` and `cd` into it:
         
         mkdir run && cd run
         

  2. In the `run/` folder, create a new shell script called `entrypoint.bash` with the following code:
         
         #!/usr/bin/env bash
         set -e
         
         if [[ "$@" == "" ]]; then
         exec /lifecycle/launcher "/home/vcap/app" "" ""
         else
         exec /lifecycle/launcher "/home/vcap/app" "$@" ""
         fi
         

  3. In the `run/` folder, create a new file called `Dockerfile` and paste in the following code:
         
         ARG CF_LINUX_FS=cloudfoundry/cflinuxfs3
         
         FROM golang:1.20-bullseye AS launcher_build
         WORKDIR /build
         RUN ["git", "clone", "--depth=1", "https://github.com/cloudfoundry/buildpackapplifecycle.git"]
         WORKDIR /build/buildpackapplifecycle
         RUN ["go", "mod", "init", "code.cloudfoundry.org/buildpackapplifecycle"]
         RUN ["go", "mod", "tidy"]
         RUN CGO_ENABLD=0 go build -o /launcher ./launcher/
         
         FROM $CF_LINUX_FS
         # Set up container tools related to launching the application
         WORKDIR /lifecycle
         COPY entrypoint.bash /lifecycle/entrypoint.bash
         RUN ["chmod", "+rx", "/lifecycle/entrypoint.bash"]
         COPY --from=launcher_build /launcher /lifecycle/launcher
         
         # Set up environment to match Cloud Foundry
         WORKDIR /home/vcap
         USER vcap:vcap
         ENTRYPOINT ["/lifecycle/entrypoint.bash"]
         
         # Expose 8080 to allow app to be run on Cloud Foundry,
         # and PORT so the container can be run locally.
         # These do nothing on Cloud Run.
         EXPOSE 8080/tcp
         # Set up environment variables similar to Cloud Foundry.
         ENV CF_INSTANCE_ADDR=127.0.0.1:8080 \
         CF_INSTANCE_IP=127.0.0.1 \
         INSTANCE_IP=127.0.0.1 \
         CF_INSTANCE_INTERNAL_IP=127.0.0.1 \
         VCAP_APP_HOST=127.0.0.1 \
         CF_INSTANCE_PORT=80 \
         LANG=en_US.UTF-8 \
         CF_INSTANCE_GUID=00000000-0000-0000-0000-000000000000 \
         INSTANCE_GUID=00000000-0000-0000-0000-000000000000 \
         CF_INSTANCE_INDEX=0 \
         INSTANCE_INDEX=0 \
         PORT=8080 \
         VCAP_APP_PORT=8080 \
         VCAP_APPLICATION={} \
         VCAP_SERVICES={}
         

  4. Use Cloud Build to build and publish the `runtime` image:
         
         gcloud builds submit \
             --tag "REGISTRY_URI/runtime:stable"
         

Replace `REGISTRY_URI` with the address to the Artifact Registry where you want to publish the build image. For example: `REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/runtime:stable.`




## Building Cloud Foundry applications as OCI images

Each application migrated into Cloud Run needs its own Dockerfile that matches how Cloud Foundry runs applications. The Dockerfile does the following:

  * Loads the builder image.
  * Runs the v2 buildpack lifecycle to create a droplet.
  * Extracts the contents of the droplet.
  * Loads the contents of the droplet on the run image to create the runnable application image.



The final application image is compatible with both Cloud Foundry and Cloud Run so you can A/B test your migration to help debug any unexpected behavior.

This process must be done by the application team for each application that needs to be migrated.

### Gather build information from a deployed Cloud Foundry application

  1. Look at the application stack. The stack is provided via the `-s` flag in `cf push` or the `stack` field of the application manifest.

     1. If the stack is Windows, the application is likely incompatible with Cloud Run. You must port the application to Linux before continuing.
     2. If the stack is blank, `cflinuxfs3`, or `cflinuxfs4` the application can be migrated to Cloud Run.
  2. Gather the list of the application buildpacks. Buildpacks are provided via the `-b` flag in `cf push`, the `buildpack` field in the application manifest, or the `buildpacks` field of the application manifest.

     1. If no buildpacks are specified, it means they're being auto-detected. Look at the list of detected buildpack in your most recent application deployment in Cloud Foundry, or specify them explicitly if you know the paths.
     2. If the buildpacks are URLs, make note of the URLs and proceed to the next step.
     3. For any buildpack that uses a short name, use the following table to map them to URLs:

Short Name | URL  
---|---  
`staticfile_buildpack` | https://github.com/cloudfoundry/staticfile-buildpack  
`java_buildpack` | https://github.com/cloudfoundry/java-buildpack  
`ruby_buildpack` | https://github.com/cloudfoundry/ruby-buildpack  
`dotnet_core_buildpack` | https://github.com/cloudfoundry/dotnet-core-buildpack  
`nodejs_buildpack` | https://github.com/cloudfoundry/nodejs-buildpack  
`go_buildpack` | https://github.com/cloudfoundry/go-buildpack  
`python_buildpack` | https://github.com/cloudfoundry/python-buildpack  
`php_buildpack` | https://github.com/cloudfoundry/php-buildpack  
`binary_buildpack` | https://github.com/cloudfoundry/binary-buildpack  
`nginx_buildpack` | https://github.com/cloudfoundry/nginx-buildpack  
  
The source for less common buildpacks can be found in the [Cloud Foundry GitHub organization](https://github.com/orgs/cloudfoundry).

  3. Gather the source code location for the image. Source is provided via the `path` attribute of the application manifest or the `-p` flag of the `cf push` command. If the source is undefined, it refers to the current directory.

  4. Determine whether there is a `.cfignore` file in the source code directory. If it is there, move it to a file named `.gcloudignore.`




### Build the Cloud Foundry application

In this step, you organize the build elements into the following folder structure:
    
    
    .
    ├── cloudbuild.yaml
    ├── Dockerfile
    ├── .gcloudignore
    └── src
        ├── go.mod
        └── main.go
    

  * `cloudbuild.yaml` provides Cloud Build with specific build instructions
  * `Dockerfile` will be using the build and run images from the previous steps to create the application image
  * `src/` contains your application source code


  1. Create a file named `Dockerfile` in the directory with the following contents:
         
         ARG BUILD_IMAGE
         ARG RUN_IMAGE
         FROM $BUILD_IMAGE as build
         
         COPY src /staging/app
         COPY src /tmp/app
         
         ARG BUILDPACKS
         RUN /lifecycle/builder \
         -buildArtifactsCacheDir=/tmp/cache \
         -buildDir=/tmp/app \
         -buildpacksDir=/tmp/buildpacks \
         -outputBuildArtifactsCache=/tmp/output-cache \
         -outputDroplet=/tmp/droplet \
         -outputMetadata=/tmp/result.json \
         "-buildpackOrder=${BUILDPACKS}" \
         "-skipDetect=true"
         
         FROM $RUN_IMAGE
         COPY --from=build /tmp/droplet droplet
         RUN tar -xzf droplet && rm droplet
         

  2. Create a file named `cloudbuild.yaml` in the directory with the following contents:
         
         steps:
         - name: gcr.io/cloud-builders/docker
           args:
           - 'build'
           - '--network'
           - 'cloudbuild'
           - '--tag'
           - '${_TAG}'
           - '--build-arg'
           - 'BUILD_IMAGE=${_BUILD_IMAGE}'
           - '--build-arg'
           - 'RUN_IMAGE=${_RUN_IMAGE}'
           - '--build-arg'
           - 'BUILDPACKS=${_BUILDPACKS}'
           - '.'
         images:
         - "${_TAG}"
         options:
           # Substitute build environment variables as an array of KEY=VALUE formatted strings here.
           env: []
         substitutions:
           _BUILD_IMAGE: BUILD_IMAGE_URI
           _RUN_IMAGE:  RUN_IMAGE_URI
           _BUILDPACKS: BUILDPACK_URL
           _TAG: APP_ARTIFACT_REGISTRY/APP_NAME:latest
         

     * Replace `BUILD_IMAGE_URI` with the URI of the build image created in previous steps.
     * Replace `RUN_IMAGE_URI` with the URI of the run image created in previous steps.
     * Replace `BUILDPACK_URL` with the URLs of the buildpacks used by your application. This can be a comma separated list with multiple buildpacks.
  3. If you have a `.cfignore` file, copy it to the directory with the name `.gcloudignore`.

  4. Create a directory called `src` in the directory.

  5. Copy the contents of your application into `src:`

     1. If the source is a zip file (including `.jar` files), unzip the contents into `src`.
     2. If the source code is a directory, copy the contents into `src`.
  6. Run `gcloud builds submit .` to build your application.




### Known incompatibilities

  * Buildpacks that rely on Cloud Foundry injected environment variables like `VCAP_SERVICES` won't work. You should instead explicitly declare a dependency on what they inject using your language's management system.
  * To patch the images produced in this manner, you must rebuild the image using a newer version of the build and run image. Application images won't be automatically patched by updating BOSH stemcells if you run them on Cloud Foundry.
  * Builds will happen in a different network environment than your Cloud Foundry cluster, you may have to set up custom Cloud Build pools with access to your internal package mirrors.



## What's Next

  * [Migrate application configurations](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-configuration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
