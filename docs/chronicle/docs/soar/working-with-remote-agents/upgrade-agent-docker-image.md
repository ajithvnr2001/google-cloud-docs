---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-docker-image/
title: Perform a major upgrade of a Docker image \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:40.050448+00:00
---

# Perform a major upgrade of a Docker image  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-docker-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Perform a major upgrade of a Docker image 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to perform a major upgrade for an existing Remote Agent using its Docker image. This procedure covers pulling the latest image, creating a backup of the existing container, preserving essential environment variables, and restarting the newly upgraded agent.

## Before you begin

This procedure assumes you've already selected the Remote Agent upgrade option and are viewing the **Major Upgrade** dialog. 

In the **Major Upgrade** dialog, copy the Docker command and paste it here. This command will be automatically populated in Step 7:
    
    
    DOCKER_COMMAND

## Upgrade existing Remote Agent

To upgrade an existing Remote Agent using its Docker image, follow these steps:

  1. Run the following command to list the current running Docker containers to identify your agent's container ID and name: 
         
         docker ps

  2. Enter your agent's container ID and name: 
         
         CONTAINER_ID
         
         AGENT_NAME

  3. Run the following command to pull the latest Docker image to your machine: You can change the `latest` tag to a specific version, such as `1.4.8.3`. 
         
         docker pull us-docker.pkg.dev/siem-ar-public/images/agent:latest

  4. Run the following command to copy the modified environment variables to a local temporary file: 
         
         docker exec CONTAINER_ID cat /home/siemplify_agent/.bash_profile > temp_bash_profile.txt

  5. Run the following command to stop the agent's Docker container: 
         
         docker stop CONTAINER_ID

  6. Run the following command to rename the container to create a backup: 
         
         docker rename AGENT_NAME AGENT_NAME_backup

  7. Run the new agent image. If you used a specific version for the `latest` tag in Step 3, use the same tag here: 

_Note: This command is populated from theBefore you begin section._
         
         DOCKER_COMMAND

  8. Run the following command to list the running Docker containers to find the new container ID: 
         
         docker ps

  9. Enter your agent's new container ID: 
         
         NEW_CONTAINER_ID

  10. Run the following command to copy the original contents of `.bash_profile` to the new container: 
         
         cat temp_bash_profile.txt | docker exec -i
             NEW_CONTAINER_ID sh -c 'cat > /home/siemplify_agent/.bash_profile'

  11. Run the following command to restart the agent service to apply the modified environment variables: 
         
         docker exec NEW_CONTAINER_ID supervisorctl restart all




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
