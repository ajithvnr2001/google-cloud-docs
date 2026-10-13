---
url: https://docs.cloud.google.com/sdk/docs/dockerfile_example/
title: Example Dockerfiles \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:30.207711+00:00
---

# Example Dockerfiles  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/dockerfile_example/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)



Send feedback 

#  Example Dockerfiles Stay organized with collections  Save and categorize content based on your preferences. 

## Build your own gcloud Docker Image including `docker` and `docker-buildx`

  * To get `docker` and / or `docker-buildx` dependency on the gcloud `:alpine` image, use the following Dockerfile:


    
    
    FROM docker:28.2.2 as static-docker-source # get latest docker
    FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:alpine
    # Comment the line below if you don't want `docker`
    COPY --from=static-docker-source /usr/local/bin/docker /usr/local/bin/docker
    # Comment the line below if you don't want `docker-buildx`
    COPY --from=static-docker-source /usr/local/libexec/docker/cli-plugins/docker-buildx /usr/local/libexec/docker/cli-plugins/docker-buildx
    

  * To get `docker` and / or `docker-buildx` dependency on the gcloud `:debian_component_based` image, use the following Dockerfile:


    
    
    FROM docker:28.2.2 as static-docker-source # get latest docker
    FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:debian_component_based
    # Comment the line below if you don't want `docker`
    COPY --from=static-docker-source /usr/local/bin/docker /usr/local/bin/docker
    # Comment the line below if you don't want `docker-buildx`
    COPY --from=static-docker-source /usr/local/libexec/docker/cli-plugins/docker-buildx /usr/local/libexec/docker/cli-plugins/docker-buildx
    

  * To get `docker` and / or `docker-buildx` dependency on the gcloud `:latest` image, use the following Dockerfile:


    
    
    FROM docker:28.2.2 as static-docker-source # get latest docker
    FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:latest
    # Comment the line below if you don't want `docker`
    COPY --from=static-docker-source /usr/local/bin/docker /usr/local/bin/docker
    # Comment the line below if you don't want `docker-buildx`
    COPY --from=static-docker-source /usr/local/libexec/docker/cli-plugins/docker-buildx /usr/local/libexec/docker/cli-plugins/docker-buildx
    

  * To get `docker` and / or `docker-buildx` dependency on the gcloud `:slim` image, use the following Dockerfile:


    
    
    FROM docker:28.2.2 as static-docker-source # get latest docker
    FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:slim
    # Comment the line below if you don't want `docker`
    COPY --from=static-docker-source /usr/local/bin/docker /usr/local/bin/docker
    # Comment the line below if you don't want `docker-buildx`
    COPY --from=static-docker-source /usr/local/libexec/docker/cli-plugins/docker-buildx /usr/local/libexec/docker/cli-plugins/docker-buildx
    

## Build your own gcloud Docker Image with `make`

  * To get `make` on the gcloud `:latest` image, use the following Dockerfile:


    
    
    FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:latest
    RUN apt-get update -qqy && apt-get -qqy upgrade && apt-get install -qqy make
    

  * To get `make` on the gcloud `:debian_component_based` image, use the following Dockerfile:


    
    
    FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:debian_component_based
    RUN apt-get update -qqy && apt-get -qqy upgrade && apt-get install -qqy make
    

## Build your own gcloud Docker Image with Java 21

  * To upgrade to Java 21 on the gcloud `:latest` image, use the following Dockerfile:


    
    
    FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:latest
    RUN curl -O https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.deb && \
    apt install ./jdk-21_linux-x64_bin.deb
    

  * To upgrade to Java 21 on the gcloud `:emulators` image, use the following Dockerfile:


    
    
    FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:emulators
    RUN curl -O https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.deb && \
    apt install ./jdk-21_linux-x64_bin.deb
    

  * To upgrade to Java 21 on the gcloud `:debian_component_based` image, use the following Dockerfile:


    
    
    FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:debian_component_based
    RUN curl -O https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.deb && \
    apt install ./jdk-21_linux-x64_bin.deb
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
