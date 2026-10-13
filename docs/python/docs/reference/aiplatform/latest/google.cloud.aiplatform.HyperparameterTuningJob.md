---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.HyperparameterTuningJob
title: Class HyperparameterTuningJob (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:43.030462+00:00
---

# Class HyperparameterTuningJob (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.HyperparameterTuningJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class HyperparameterTuningJob (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    HyperparameterTuningJob(
        display_name: str,
        custom_job: google.cloud.aiplatform.jobs.CustomJob,
        metric_spec: typing.Dict[str, str],
        parameter_spec: typing.Dict[
            str, google.cloud.aiplatform.hyperparameter_tuning._ParameterSpec
        ],
        max_trial_count: int,
        parallel_trial_count: int,
        max_failed_trial_count: int = 0,
        search_algorithm: typing.Optional[str] = None,
        measurement_selection: typing.Optional[str] = "best",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
    )

Vertex AI Hyperparameter Tuning Job.

## Properties 

### create_time

Time this resource was created.

### display_name

Display name of this resource.

### encryption_spec

Customer-managed encryption key options for this Vertex AI resource.

If this is set, then all resources created by this Vertex AI resource will be encrypted with the provided encryption key.

### end_time

Time when the Job resource entered the `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, or `JOB_STATE_CANCELLED` state.

### error

Detailed error info for this Job resource. Only populated when the Job's state is `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.

### gca_resource

The underlying resource proto representation.

### labels

User-defined labels containing metadata about this resource.

Read more about labels at <https://goo.gl/xmQnxf>

### name

Name of this resource.

### network

The full name of the Google Compute Engine [network](https://cloud.google.com/vpc/docs/vpc#networks) to which this HyperparameterTuningJob should be peered.

Takes the format `projects/{project}/global/networks/{network}`. Where {project} is a project number, as in `12345`, and {network} is a network name.

Private services access must already be configured for the network. If left unspecified, the HyperparameterTuningJob is not peered with any network.

### preview

Exposes features available in preview for this class.

### resource_name

Full qualified resource name.

### start_time

Time when the Job resource entered the `JOB_STATE_RUNNING` for the first time.

### state

Fetch Job again and return the current JobState.

**Returns**  
---  
**Type** | **Description**  
`state (job_state.JobState)` | Enum that describes the state of a Vertex AI job.  
  
### update_time

Time this resource was last updated.

### web_access_uris

Fetch the runnable job again and return the latest web access uris.

**Returns**  
---  
**Type** | **Description**  
`(Dict[str, Union[str, Dict[str, str]]])` | Web access uris of the runnable job.  
  
## Methods 

### HyperparameterTuningJob
    
    
    HyperparameterTuningJob(
        display_name: str,
        custom_job: google.cloud.aiplatform.jobs.CustomJob,
        metric_spec: typing.Dict[str, str],
        parameter_spec: typing.Dict[
            str, google.cloud.aiplatform.hyperparameter_tuning._ParameterSpec
        ],
        max_trial_count: int,
        parallel_trial_count: int,
        max_failed_trial_count: int = 0,
        search_algorithm: typing.Optional[str] = None,
        measurement_selection: typing.Optional[str] = "best",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
    )

Configures a HyperparameterTuning Job.

Example usage:
    
    
    from google.cloud.aiplatform import hyperparameter_tuning as hpt
    
    worker_pool_specs = [
            {
                "machine_spec": {
                    "machine_type": "n1-standard-4",
                    "accelerator_type": "NVIDIA_TESLA_K80",
                    "accelerator_count": 1,
                },
                "replica_count": 1,
                "container_spec": {
                    "image_uri": container_image_uri,
                    "command": [],
                    "args": [],
                },
            }
        ]
    
    custom_job = aiplatform.CustomJob(
        display_name='my_job',
        worker_pool_specs=worker_pool_specs,
        labels={'my_key': 'my_value'},
    )
    
    
    hp_job = aiplatform.HyperparameterTuningJob(
        display_name='hp-test',
        custom_job=job,
        metric_spec={
            'loss': 'minimize',
        },
        parameter_spec={
            'lr': hpt.DoubleParameterSpec(min=0.001, max=0.1, scale='log'),
            'units': hpt.IntegerParameterSpec(min=4, max=128, scale='linear'),
            'activation': hpt.CategoricalParameterSpec(values=['relu', 'selu']),
            'batch_size': hpt.DiscreteParameterSpec(values=[128, 256], scale='linear')
        },
        max_trial_count=128,
        parallel_trial_count=8,
        labels={'my_key': 'my_value'},
        )
    
    hp_job.run()
    
    print(hp_job.trials)
    

For more information on using hyperparameter tuning please visit: <https://cloud.google.com/ai-platform-unified/docs/training/using-hyperparameter-tuning>

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Required. The user-defined name of the HyperparameterTuningJob. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`custom_job` |  `aiplatform.CustomJob`   
Required. Configured CustomJob. The worker pool spec from this custom job applies to the CustomJobs created in all the trials. A persistent_resource_id can be specified on the custom job to be used when running this Hyperparameter Tuning job.  
`parameter_spec` |  `Dict[str, hyperparameter_tuning._ParameterSpec]`   
Required. Dictionary representing parameters to optimize. The dictionary key is the metric_id, which is passed into your training job as a command line key word argument, and the dictionary value is the parameter specification of the metric. from google.cloud.aiplatform import hyperparameter_tuning as hpt parameter_spec={ 'decay': hpt.DoubleParameterSpec(min=1e-7, max=1, scale='linear'), 'learning_rate': hpt.DoubleParameterSpec(min=1e-7, max=1, scale='linear') 'batch_size': hpt.DiscreteParamterSpec(values=[4, 8, 16, 32, 64, 128], scale='linear') } Supported parameter specifications can be found until aiplatform.hyperparameter_tuning. These parameter specification are currently supported: DoubleParameterSpec, IntegerParameterSpec, CategoricalParameterSpace, DiscreteParameterSpec  
`max_trial_count` |  `int`   
Required. The desired total number of Trials.  
`parallel_trial_count` |  `int`   
Required. The desired number of Trials to run in parallel.  
`max_failed_trial_count` |  `int`   
Optional. The number of failed Trials that need to be seen before failing the HyperparameterTuningJob. If set to 0, Vertex AI decides how many Trials must fail before the whole job fails.  
`search_algorithm` |  `str`   
The search algorithm specified for the Study. Accepts one of the following: `None` \- If you do not specify an algorithm, your job uses the default Vertex AI algorithm. The default algorithm applies Bayesian optimization to arrive at the optimal solution with a more effective search over the parameter space. 'grid' - A simple grid search within the feasible space. This option is particularly useful if you want to specify a quantity of trials that is greater than the number of points in the feasible space. In such cases, if you do not specify a grid search, the Vertex AI default algorithm may generate duplicate suggestions. To use grid search, all parameter specs must be of type `IntegerParameterSpec`, `CategoricalParameterSpace`, or `DiscreteParameterSpec`. 'random' - A simple random search within the feasible space.  
`measurement_selection` |  `str`   
This indicates which measurement to use if/when the service automatically selects the final measurement from previously reported intermediate measurements. Accepts: 'best', 'last' Choose this based on two considerations: A) Do you expect your measurements to monotonically improve? If so, choose 'last'. On the other hand, if you're in a situation where your system can "over-train" and you expect the performance to get better for a while but then start declining, choose 'best'. B) Are your measurements significantly noisy and/or irreproducible? If so, 'best' will tend to be over-optimistic, and it may be better to choose 'last'. If both or neither of (A) and (B) apply, it doesn't matter which selection type is chosen.  
`project` |  `str`   
Optional. Project to run the HyperparameterTuningjob in. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location to run the HyperparameterTuning in. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to run call HyperparameterTuning service. Overrides credentials set in aiplatform.init.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize HyperparameterTuningJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`encryption_spec_key_name` |  `str`   
Optional. Customer-managed encryption key options for a HyperparameterTuningJob. If this is set, then all resources created by the HyperparameterTuningJob will be encrypted with the provided encryption key.  
  
### cancel
    
    
    cancel() -> None

Cancels this Job.

Success of cancellation is not guaranteed. Use `Job.state` property to verify if cancellation was successful.

### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

### done
    
    
    done() -> bool

Method indicating whether a job has completed.

### get
    
    
    get(
        resource_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> google.cloud.aiplatform.jobs._RunnableJob

Get a Vertex AI Job for the given resource_name.

**Parameters**  
---  
**Name** | **Description**  
`resource_name` |  `str`   
Required. A fully-qualified resource name or ID.  
`project` |  `str`   
Optional. project to retrieve dataset from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. location to retrieve dataset from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Custom credentials to use to upload this model. Overrides credentials set in aiplatform.init.  
  
### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

List all instances of this Job Resource.

Example Usage:

aiplatform.BatchPredictionJobs.list( filter='state="JOB_STATE_SUCCEEDED" AND display_name="my_job"', )

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.  
`order_by` |  `str`   
Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: `display_name`, `create_time`, `update_time`  
`project` |  `str`   
Optional. Project to retrieve list from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve list from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve list. Overrides credentials set in aiplatform.init.  
  
### run
    
    
    run(
        service_account: typing.Optional[str] = None,
        network: typing.Optional[str] = None,
        timeout: typing.Optional[int] = None,
        restart_job_on_worker_restart: bool = False,
        enable_web_access: bool = False,
        tensorboard: typing.Optional[str] = None,
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
        disable_retries: bool = False,
        scheduling_strategy: typing.Optional[
            google.cloud.aiplatform_v1.types.custom_job.Scheduling.Strategy
        ] = None,
        max_wait_duration: typing.Optional[int] = None,
    ) -> None

Run this configured CustomJob.

**Parameters**  
---  
**Name** | **Description**  
`service_account` |  `str`   
Optional. Specifies the service account for workload run-as account. Users submitting jobs must have act-as permission on this run-as account.  
`network` |  `str`   
Optional. The full name of the Compute Engine network to which the job should be peered. For example, projects/12345/global/networks/myVPC. Private services access must already be configured for the network. If left unspecified, the network set in aiplatform.init will be used. Otherwise, the job is not peered with any network.  
`timeout` |  `int`   
Optional. The maximum job running time in seconds. The default is 7 days.  
`restart_job_on_worker_restart` |  `bool`   
Restarts the entire CustomJob if a worker gets restarted. This feature can be used by distributed training jobs that are not resilient to workers leaving and joining a job.  
`enable_web_access` |  `bool`   
Whether you want Vertex AI to enable interactive shell access to training containers. <https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell>  
`tensorboard` |  `str`   
Optional. The name of a Vertex AI Tensorboard resource to which this CustomJob will upload Tensorboard logs. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}` The training script should write Tensorboard to following Vertex AI environment variable: AIP_TENSORBOARD_LOG_DIR `service_account` is required with provided `tensorboard`. For more information on configuring your service account please visit: <https://cloud.google.com/vertex-ai/docs/experiments/tensorboard-training>  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will unblock and it will be executed in a concurrent Future.  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
`disable_retries` |  `bool`   
Indicates if the job should retry for internal errors after the job starts running. If True, overrides `restart_job_on_worker_restart` to False.  
`scheduling_strategy` |  `gca_custom_job_compat.Scheduling.Strategy`   
Optional. Indicates the job scheduling strategy.  
`max_wait_duration` |  `int`   
This is the maximum duration that a job will wait for the requested resources to be provisioned in seconds. If set to 0, the job will wait indefinitely. The default is 1 day.  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

### wait_for_completion
    
    
    wait_for_completion() -> None

Waits for job to complete.

**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If job failed or cancelled.  
  
### wait_for_resource_creation
    
    
    wait_for_resource_creation() -> None

Waits until resource has been created.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
