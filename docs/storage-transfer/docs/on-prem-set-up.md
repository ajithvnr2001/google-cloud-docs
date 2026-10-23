---
url: https://docs.cloud.google.com/storage-transfer/docs/on-prem-set-up/
title: Requirements for file system transfers \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:19.318716+00:00
---

# Requirements for file system transfers  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/on-prem-set-up/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Requirements for file system transfers Stay organized with collections  Save and categorize content based on your preferences. 

Before you create a file system transfer job, you'll need to enable required APIs and install Docker.

If you receive errors while performing first-time setup, confirm that the user you logged in with has permissions required to perform the set up steps. In many cases, these permissions are not available to all users, and you may need to contact a project administrator for assistance.

## System requirements

To use Storage Transfer Service for file system transfers, you need:

  * A POSIX-compliant source and/or destination.

  * A Cloud Storage bucket without a [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock). To transfer to a bucket with a retention policy, see [Transfer to a bucket with a retention policy](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#retention_policy).

  * TCP port 443 (HTTPS) open for outbound connections.




The transfer agent machine requirements are listed below:

  * A [Docker](https://docker.com)-supported 64-bit Linux server or virtual machine that can access the data you plan to transfer. [Docker Community Edition](https://docs.docker.com/install/linux/docker-ce/binaries/), supports CentOs, Debian, Fedora, and Ubuntu operating systems.

To use other Linux operating systems, see [Docker Enterprise](https://docs.docker.com/ee/supported-platforms/).

  * At least 8 GB of memory per container and at least four CPUs to be most effective.

  * Any system-level or user-level constraints on the number of allowed process IDs, such as configured with `ulimit -u`, must account for the number of agents you plan to run. Each agent process can create up to many hundreds of threads. We recommend removing process ID limits when running transfer agents.

Customers using [Podman](https://podman.io/) to create agent containers should specify a `--pids-limit` value high enough to accommodate Storage Transfer Service agent threads. The default `--pids-limit` value is 2048, which may cause issues when running more than one agent. We recommend setting `--pids-limit=-1` to allow unlimited process IDs per container.




## Required endpoints

The following DNS endpoints must be accessible to the transfer agent. While an agent may only use a subset of these endpoints depending on its configuration, all of the endpoints should be permitted to ensure full functionality.

### Google endpoints

This list of required endpoints is subject to change. To prevent transfer disruptions, we recommend allowing the base `googleapis.com` domain and `gcr.io`, provided your organization's security policies permit it.

Endpoint | Service | Purpose  
---|---|---  
`storagetransfer.googleapis.com` | Storage Transfer Service | Used by the agent to connect to the Storage Transfer Service, receive transfer tasks, and report its health status.  
`storage.googleapis.com` | Cloud Storage | Used to perform core data transfer operations, including listing, reading, and writing objects to your Cloud Storage buckets.  
`www.googleapis.com` | Google APIs | Used to download version updates for the transfer agent.  
`monitoring.googleapis.com` | Cloud Monitoring | Used to export transfer performance and agent health metrics.  
`logging.googleapis.com` | Cloud Logging | Used to publish agent system and activity logs.  
`oauth2.googleapis.com` | Google OAuth 2.0 | Used to securely exchange credentials and retrieve short-lived access tokens for API authorization.  
`iamcredentials.googleapis.com` | IAM Service Account Credentials | Used to generate temporary credentials when the agent is configured to impersonate a specific service account.  
`cloudresourcemanager.googleapis.com` | Resource Manager | Used during agent installation and setup to verify project configuration and permissions.  
`gcr.io` | Container Registry | Used to download the Storage Transfer Service agent container image during installation.  
  
To optimize transfer performance, the agent may use different HTTP protocols, including HTTP/1.1 and HTTP/2 at a minimum, when communicating with various endpoints. Ensure that your configured proxies or firewalls properly support and are performant across all of these protocol types.

### Regional Endpoints

If you've configured your agents to use [regional endpoints](https://docs.cloud.google.com/storage-transfer/docs/regional-endpoints) (e.g., `storage.REGION.rep.googleapis.com`), those specific domain names must be permitted by your proxy or firewall rules instead of the standard `storage.googleapis.com` endpoint.

### Source and destination storage endpoints

The agent also requires network access to the specific source and destination storage systems, such as S3-compatible APIs, HDFS clusters, or NFS for POSIX.

## Scaling restrictions on jobs and agents

Storage Transfer Service has the following scale restrictions on transfer jobs and agents:

  * Fewer than one billion files per job
  * Bandwidth cap must be over 1MBps
  * Up to 100 agents per agent pool
  * Up to 800 agent pools per project



## Enable APIs

  1. Enable the Google Storage Transfer API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=storagetransfer)




## Install Docker

If you're using Google Cloud CLI or Docker to [install and run transfer agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#install-agent), install Docker Engine on a physical or virtual Linux machine.

If you're using Podman to install and run transfer agents, skip directly to the [Podman-specific installation instructions](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#podman).
    
    
    curl -fsSL https://get.docker.com -o get-docker.sh
    
    
    
    sudo sh get-docker.sh
    
    
    
    sudo systemctl enable docker --now
    

If you encounter an installation error, see [Troubleshooting](https://docs.docker.com/install/linux/linux-postinstall/#troubleshooting).

## Allow Docker to authenticate

To allow the Docker container to authenticate with your `gcloud` default credentials, create a Docker volume containing a file with your application default credentials by running the following command:
    
    
    sudo docker run -ti --name gcloud-config google/cloud-sdk gcloud auth application-default login
    

## What's next?

  * [Configure Google Cloud permissions](https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions)
  * [Create an agent pool](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools)
  * [Install transfer agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents)
  * [Create a transfer job](https://docs.cloud.google.com/storage-transfer/docs/create-transfers)
  * [Maximize transfer agent performance](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
