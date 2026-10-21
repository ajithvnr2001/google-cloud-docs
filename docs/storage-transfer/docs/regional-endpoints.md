---
url: https://docs.cloud.google.com/storage-transfer/docs/regional-endpoints/
title: Regional endpoints \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:45.555671+00:00
---

# Regional endpoints  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/regional-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Regional endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service agent-based transfers support [Cloud Storage regional endpoints](https://docs.cloud.google.com/storage/docs/regional-endpoints). When a Cloud Storage regional endpoint is specified, all data transfer traffic through the agent to or from a Cloud Storage bucket remains within that Google Cloud region. Any Cloud Storage buckets involved in the transfer, including intermediate buckets for inter-file system transfers, must be located in the specified region, or the transfer fails.

When a regional endpoint is not specified, the transfer agent connects to the global endpoint, which routes traffic optimally but does not guarantee regional confinement of the data in transit.

Regional endpoints are not supported in agentless transfers.

## Specify a regional endpoint

Endpoints are specified at the transfer agent level. The agent must be installed using the `docker` command.

To specify a regional endpoint, use the `--gcs-api-endpoint` flag when installing a transfer agent using `docker run`:
    
    
    sudo docker run --ulimit memlock=64000000 -d --rm \
    --volumes-from gcloud-config \
    -v HOST_DIRECTORY:CONTAINER_DIRECTORY \
    gcr.io/cloud-ingest/tsop-agent:latest \
    --project-id=PROJECT_ID \
    --hostname=$(hostname) \
    --agent-pool=POOL_NAME \
    --gcs-api-endpoint=storage.LOCATION.rep.googleapis.com
    

The flag accepts all Cloud Storage single regions, as well as the `US` multi-region and the `EU` multi-region. See [Bucket locations](https://docs.cloud.google.com/storage/docs/locations) for a complete list.

## Regional endpoint consistency in agent pools

When specifying an agent pool for a transfer agent, be aware that Storage Transfer Service doesn't enforce uniform regional endpoints across all agents in that pool. This means you could inadvertently mix agents that have a specific regional endpoint with agents that don't within the same pool; as a result, the pool may route traffic through the global endpoint.

To ensure traffic remains within the desired region, only include agents with the same regional endpoint in a given agent pool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
