---
url: https://docs.cloud.google.com/migrate/containers/docs/about-linux-system-containers/
title: About Linux system containers \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:44.069450+00:00
---

# About Linux system containers  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/about-linux-system-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Resources ](https://docs.cloud.google.com/migrate/containers/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About Linux system containers

The Migrate to Containers CLI lets you migrate Linux-based applications to containerized environments. It uses a prebuilt Linux system container that functions as a bootloader for the services required by the modernized application. Using Migrate to Containers for Linux applications, you can modernize a wide range of stateless applications to run on Google Kubernetes Engine (GKE), Cloud Run, and GKE clusters.

For more information, see [Migrate to Containers CLI architecture](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/architecture).

This document provides details about Migrate to Containers Linux system containers that are used as a part of the solution for running applications migrated using Migrate to Containers.

## Migration using Linux system container

Migrate to Containers discovers the source application files and processes. It then generates artifacts which include a Dockerfile, Kubernetes manifest, and Skaffold configuration.

The main function of a Linux system container is to initiate the services that were originally run at the source virtual machine (VM) instance, including relevant operating system and application services.

The Dockerfile is used to build the image for your migrated VM. A Linux system container Dockerfile usually looks similar to the following:
    
    
    # Please refer to the documentation:
    # https://cloud.google.com/migrate/anthos/docs/dockerfile-reference
    
    FROM us-docker.pkg.dev/migrate-modernize-public/modernize-plugins-prod/service-manager-runtime:1.0.0 as service-manager-runtime
    
    FROM scratch
    
    # Tar containing data captured from the source VM
    ADD vmFiles.tar.gz /
    
    COPY --from=service-manager-runtime / /
    
    ADD blocklist.yaml /.m4a/blocklist.yaml
    
    ADD logs.yaml /code/config/logs/logsArtifact.yaml
    
    ADD services-config.yaml /.m4a/
    
    ADD tempfiles.yaml  /.m4a/
    
    # If you want to update parts of the image, add your commands here.
    # For example:
    # RUN apt-get update
    # RUN apt-get install -y \
    #       package1=version \
    #       package2=version \
    #       package3=version
    # RUN yum update
    # RUN wget http://github.com
    
    ENTRYPOINT ["/ko-app/service-manager-runtime", "start", "-c", "/.m4a/"]
    

When you execute a migration, the following Dockerfile statements copy or add the VM data from the original source to the Docker image:

  * The following statement adds the tar file that contains the data captured from the source VM to the Docker image:
        
        ADD vmFiles.tar.gz /
        

This tar is created by Migrate to Containers. It contains the root file system of the source VM with everything provided in filters in the migration plan and any folder provided in the data migration plan filtered out.

  * The following statement imports the Migrate to Containers runtime from the Docker repository into the Docker image:
        
        FROM us-docker.pkg.dev/migrate-modernize-public/modernize-plugins-prod/service-manager-runtime:1.0.0 as service-manager-runtime
        

  * The following statement then copies the Migrate to Containers runtime into the Docker image:
        
        COPY --from=service-manager-runtime / /
        




#### Click to view details about the Migrate to Containers runtime file

`/ko-app/service-manager-runtime` is the main Migrate to Containers runtime file. This is an initialization system that is made for containers. It does the following:

  * Reads the `/.m4a/services-config.yaml` file, and runs the specified binaries in order according to the specified run method such as daemonize, not daemonize, wait for finish.
  * Collects logs specified in the `/code/config/logs/logsArtifact.yaml` file and prints them to `stdout` of the container. For GKE and GKE clusters, it also ensures that the logs are sent to Cloud Logging.



## Maintenance of migrated workloads

You can create a new pipeline for your application from the migrated artifacts. You might have a different pipeline for different applications. You can keep your existing continuous integration and deployment pipeline which generated the original VM-based application, and add the relevant steps that transform the generated executables into Linux system containers.

The following diagram illustrates a sample pipeline using Migrate to Containers:

![Automated CI/CD flow for application replatforming using Migrate to Containers](https://docs.cloud.google.com/static/migrate/containers/docs/images/linux-system-container-pipeline.png)

This diagram shows the change process of an existing application.

A change to source code or new OS path is pushed to the existing Git repository. The source is compiled based on the existing setup and a new image is built. The new image includes the Migrate to Containers runtime layer.

In the test environment, a developer runs preliminary tests to confirm whether the new image is working as expected. After the test phase, a new system container image is created and pushed to the development or test environment, which is later rolled out to production.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
