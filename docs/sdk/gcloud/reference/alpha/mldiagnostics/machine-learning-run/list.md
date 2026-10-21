---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/machine-learning-run/list/
title: gcloud alpha mldiagnostics machine-learning-run list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:13:18.744188+00:00
---

# gcloud alpha mldiagnostics machine-learning-run list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/machine-learning-run/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha mldiagnostics machine-learning-run list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha mldiagnostics machine-learning-run list - list machine learning runs 
SYNOPSIS
    

`gcloud alpha mldiagnostics machine-learning-run list` [`--location`=`LOCATION`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` List machine learning runs 
EXAMPLES
     To list all machine learning runs, run: 
    
    
    gcloud alpha mldiagnostics machine-learning-run list --location=us-central1 --limit 2
    
    
    Sample output:
      ---
      artifacts:
        gcsPath: gs://diagon-prod-data
      createTime: '2026-02-05T16:25:28.367865234Z'
      displayName: updated-gcloud-cli-run
      endTime: '0001-01-01T00:00:00Z'
      etag: 2a9dad60-a18b-4680-b63d-d0e16214713c
      labels:
        on_demand_xprof: enabled
      name: projects/PROJECT_ID/locations/us-central1/machineLearningRuns/my-run
      orchestrator: GKE
      runPhase: ACTIVE
      runSet: group-gcloud-cli
      tools:
      - xprof: {}
      updateTime: '2026-02-05T16:32:35.885684490Z'
      workloadDetails:
        gke:
          cluster: projects/PROJECT_ID/locations/us-central1/clusters/mldiag-prod-cluster
          id: mldiag-prod-demo-jobset
          kind: JobSet
          namespace: diagon
      ---
      artifacts:
        gcsPath: gs://diagon-prod-data
      configs:
        hardwareConfigs:
          device_type: TPU v5 lite
          devices_per_slice: '8'
          num_slices: '1'
        softwareConfigs:
          framework: JAX
          framework_version: 0.9.0
          libtpu_version: 0.0.34
          xla_flags: default
      createTime: '2026-02-05T11:02:28.961113732Z'
      displayName: demo-run-2026-02-05T11:02:01Z
      endTime: '0001-01-01T00:00:00Z'
      etag: 5ac79afc-1afc-4689-8ccb-06b0c2a5b541
      labels:
        create-tool-mode: regular
        created_by: diagon_sdk
        diagon_sdk_version: 0-5-10
        on_demand_xprof: enabled
      metrics:
        avgHbmUtilization: 0.217357
        avgLatency: 0.502287369s
        avgMfu: 74.8107
        avgStep: 0.082316534s
        avgThroughput: 502.521
      name: projects/PROJECT_ID/locations/us-central1/machineLearningRuns/mldiag-prod-cluster-diagon-jobset-mldiag-prod-demo-jobset-20260205-110201
      orchestrator: GKE
      runPhase: COMPLETED
      runSet: demo-group
      tools:
      - xprof: {}
      updateTime: '2026-02-05T15:50:55.144914944Z'
      workloadDetails:
        gke:
          cluster: projects/PROJECT_ID/locations/us-central1-a/clusters/mldiag-prod-cluster
          id: mldiag-prod-demo-jobset
          kind: JobSet
          labels:
            job-name: mldiag-prod-demo-jobset-tpu-slice-0
            managed-mldiagnostics-gke: 'true'
          namespace: diagon
          parentWorkload: mldiag-prod-demo-jobset-tpu-slice-0

FLAGS
    

Location resource - Parent format: projects/{project}/locations/{location} This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * set the property `compute/region` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line; 
  * set the property `compute/region`. 


LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--uri`
     Print a list of resource URIs instead of the default output, and change the command output to a list of URIs. If this flag is used with `--format`, the formatting is applied on this URI list. To display URIs alongside other keys instead, use the `uri()` transform. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `hypercomputecluster/v1alpha` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/cluster-director/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
