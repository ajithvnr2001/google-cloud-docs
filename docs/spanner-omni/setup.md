---
url: https://docs.cloud.google.com/spanner-omni/setup/
title: Set up Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:57.143988+00:00
---

# Set up Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Set up Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

[Download Spanner Omni](https://docs.cloud.google.com/spanner-omni/download) to try it out at no charge. If you decide you want to use Spanner Omni for production use, [contact Google](https://cloud.google.com/consulting/spanner-omni) to learn about acquiring a license for the [commercial edition](https://docs.cloud.google.com/spanner-omni/editions-overview#commercial-edition). 

This page describes how to start Spanner Omni in single-server mode. You can either install it using a TAR file or run it as a container using Docker.

## Before you begin

Before you set up your Spanner Omni instance, ensure you meet the following requirements:

  * Verify your machine meets the [system requirements](https://docs.cloud.google.com/spanner-omni/system-requirements).

  * Ensure you have `sudo` access in your environment to set up the Spanner Omni binary.

  * Ensure [Docker](https://docs.docker.com/get-docker/) is installed on your machine for container-based installations.




## Run using Docker

We recommend storing Spanner data in a [Docker volume](https://docs.docker.com/storage/volumes/) to ensure data persistence if you delete the container.

  1. Create a Docker volume:
         
         docker volume create spanner
         

  2. Start the Spanner Omni server container. Replace VERSION_TAG with the Spanner Omni version you want to use. The current version is `2026.r4-lts`.
         
         docker run -d --network host \
             --name spanneromni \
             -v "spanner:/spanner" \
             us-docker.pkg.dev/spanner-omni/images/spanner-omni:VERSION_TAG \
             start-single-server
         

The `--network host` flag maps the Spanner Omni ports to the host machine.

  3. Verify that the container is running:
         
         docker ps
         

Check the **STATUS** field in the output to ensure the container is healthy.




### Interact with the containerized server

You can use `docker exec` to run Spanner Omni CLI commands inside the container:

  1. Create a database:
         
         docker exec -it spanneromni /google/spanner/bin/spanner databases create DATABASE_NAME
         

  2. Open the SQL shell:
         
         docker exec -it spanneromni /google/spanner/bin/spanner sql --database=DATABASE_NAME
         

  3. List databases:
         
         docker exec -it spanneromni /google/spanner/bin/spanner databases list
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
