---
url: https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.types.RuntimeEnvironment
title: Class RuntimeEnvironment (0.14.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:09.998691+00:00
---

# Class RuntimeEnvironment (0.14.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.types.RuntimeEnvironment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RuntimeEnvironment (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.17  0.7.0  0.6.2  0.5.5  0.4.1  0.3.1  0.2.0  0.1.5 
    
    
    RuntimeEnvironment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The environment values to set at runtime.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`num_workers` |  `int`   
Optional. The initial number of Google Compute Engine instances for the job. The default value is 11.   
`max_workers` |  `int`   
Optional. The maximum number of Google Compute Engine instances to be made available to your pipeline during execution, from 1 to 1000. The default value is 1.   
`zone` |  `str`   
Optional. The Compute Engine `availability zone   
`service_account_email` |  `str`   
Optional. The email address of the service account to run the job as.   
`temp_location` |  `str`   
Required. The Cloud Storage path to use for temporary files. Must be a valid Cloud Storage URL, beginning with `gs://`.   
`bypass_temp_dir_validation` |  `bool`   
Optional. Whether to bypass the safety checks for the job's temporary directory. Use with caution.   
`machine_type` |  `str`   
Optional. The machine type to use for the job. Defaults to the value from the template if not specified.   
`additional_experiments` |  `MutableSequence[str]`   
Optional. Additional experiment flags for the job, specified with the `--experiments` option.   
`network` |  `str`   
Optional. Network to which VMs will be assigned. If empty or unspecified, the service will use the network "default".   
`subnetwork` |  `str`   
Optional. Subnetwork to which VMs will be assigned, if desired. You can specify a subnetwork using either a complete URL or an abbreviated path. Expected to be of the form "https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK" or "regions/REGION/subnetworks/SUBNETWORK". If the subnetwork is located in a Shared VPC network, you must use the complete URL.   
`additional_user_labels` |  `MutableMapping[str, str]`   
Optional. Additional user labels to be specified for the job. Keys and values should follow the restrictions specified in the `labeling restrictions   
`kms_key_name` |  `str`   
Optional. Name for the Cloud KMS key for the job. Key format is: projects/  
`ip_configuration` |  `[google.cloud.dataflow_v1beta3.types.WorkerIPAddressConfiguration](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.types.WorkerIPAddressConfiguration)`   
Optional. Configuration for VM IPs.   
`worker_region` |  `str`   
Required. The Compute Engine region (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1". Mutually exclusive with worker_zone. If neither worker_region nor worker_zone is specified, default to the control plane's region.   
`worker_zone` |  `str`   
Optional. The Compute Engine zone (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1-a". Mutually exclusive with worker_region. If neither worker_region nor worker_zone is specified, a zone in the control plane's region is chosen based on available capacity. If both `worker_zone` and `zone` are set, `worker_zone` takes precedence.   
`enable_streaming_engine` |  `bool`   
Optional. Whether to enable Streaming Engine for the job.   
`disk_size_gb` |  `int`   
Optional. The disk size, in gigabytes, to use on each remote Compute Engine worker instance.   
`streaming_mode` |  `[google.cloud.dataflow_v1beta3.types.StreamingMode](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.types.StreamingMode)`   
Optional. Specifies the Streaming Engine message processing guarantees. Reduces cost and latency but might result in duplicate messages committed to storage. Designed to run simple mapping streaming ETL jobs at the lowest cost. For example, Change Data Capture (CDC) to BigQuery is a canonical use case. For more information, see `Set the pipeline streaming mode   
`additional_pipeline_options` |  `MutableSequence[str]`   
Optional. Additional pipeline option flags for the job.   
  
## Classes 

### AdditionalUserLabelsEntry
    
    
    AdditionalUserLabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
