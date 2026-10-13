---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Experiment
title: Class Experiment (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:39.560652+00:00
---

# Class Experiment (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Experiment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Experiment (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    Experiment(
        experiment_name: str,
        *,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    )

Represents a Vertex AI Experiment resource.

## Properties 

### backing_tensorboard_resource_name

The Tensorboard resource associated with this Experiment if there is one.

### dashboard_url

Cloud console URL for this resource.

### name

The name of this experiment.

### resource_name

The Metadata context resource name of this experiment.

## Methods 

### Experiment
    
    
    Experiment(
        experiment_name: str,
        *,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    )
    
    
    my_experiment = aiplatform.Experiment('my-experiment')
    

**Parameters**  
---  
**Name** | **Description**  
`experiment_name` |  `str`   
Required. The name or resource name of this experiment. Resource name is of the format: `projects/123/locations/us-central1/metadataStores/default/contexts/my-experiment`  
`project` |  `str`   
Optional. Project where this experiment is located. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location where this experiment is located. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials used to retrieve this experiment. Overrides credentials set in aiplatform.init.  
  
### assign_backing_tensorboard
    
    
    assign_backing_tensorboard(
        tensorboard: typing.Union[
            google.cloud.aiplatform.tensorboard.tensorboard_resource.Tensorboard, str
        ],
    )

Assigns tensorboard as backing tensorboard to support time series metrics logging.
    
    
    tb = aiplatform.Tensorboard('tensorboard-resource-id')
    my_experiment = aiplatform.Experiment('my-experiment')
    my_experiment.assign_backing_tensorboard(tb)
    

**Parameter**  
---  
**Name** | **Description**  
`tensorboard` |  `Union[aiplatform.Tensorboard, str]`   
Required. Tensorboard resource or resource name to associate to this experiment.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If this experiment already has a previously set backing tensorboard resource.  
`ValueError` | If Tensorboard is not in same project and location as this experiment.  
  
### create
    
    
    create(
        experiment_name: str,
        *,
        description: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> google.cloud.aiplatform.metadata.experiment_resources.Experiment

Creates a new experiment in Vertex AI Experiments.
    
    
    my_experiment = aiplatform.Experiment.create('my-experiment', description='my description')
    

**Parameters**  
---  
**Name** | **Description**  
`experiment_name` |  `str`   
Required. The name of this experiment.  
`description` |  `str`   
Optional. Describes this experiment's purpose.  
`project` |  `str`   
Optional. Project where this experiment will be created. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location where this experiment will be created. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials used to create this experiment. Overrides credentials set in aiplatform.init.  
  
### delete
    
    
    delete(*, delete_backing_tensorboard_runs: bool = False)

Deletes this experiment all the experiment runs under this experiment

Does not delete Pipeline runs, Artifacts, or Executions associated to this experiment or experiment runs in this experiment.
    
    
    my_experiment = aiplatform.Experiment('my-experiment')
    my_experiment.delete(delete_backing_tensorboard_runs=True)
    

**Parameter**  
---  
**Name** | **Description**  
`delete_backing_tensorboard_runs` |  `bool`   
Optional. If True will also delete the Tensorboard Runs associated to the experiment runs under this experiment that we used to store time series metrics.  
  
### get
    
    
    get(
        experiment_name: str,
        *,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> typing.Optional[google.cloud.aiplatform.metadata.experiment_resources.Experiment]

Gets experiment if one exists with this experiment_name in Vertex AI Experiments.

**Parameters**  
---  
**Name** | **Description**  
`experiment_name` |  `str`   
Required. The name of this experiment.  
`project` |  `str`   
Optional. Project used to retrieve this resource. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location used to retrieve this resource. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials used to retrieve this resource. Overrides credentials set in aiplatform.init.  
  
### get_backing_tensorboard_resource
    
    
    get_backing_tensorboard_resource() -> (
        typing.Optional[
            google.cloud.aiplatform.tensorboard.tensorboard_resource.Tensorboard
        ]
    )

Get the backing tensorboard for this experiment if one exists.
    
    
    my_experiment = aiplatform.Experiment('my-experiment')
    tb = my_experiment.get_backing_tensorboard_resource()
    

### get_data_frame
    
    
    get_data_frame(*, include_time_series: bool = True) -> pd.DataFrame

Get parameters, metrics, and time series metrics of all runs in this experiment as Dataframe.
    
    
    my_experiment = aiplatform.Experiment('my-experiment')
    df = my_experiment.get_data_frame()
    

**Parameter**  
---  
**Name** | **Description**  
`include_time_series` |  `bool`   
Optional. Whether or not to include time series metrics in df. Default is True. Setting to False will largely improve execution time and reduce quota contributing calls. Recommended when time series metrics are not needed or number of runs in Experiment is large. For time series metrics consider querying a specific run using get_time_series_data_frame.  
**Exceptions**  
---  
**Type** | **Description**  
`ImportError` | If pandas is not installed.  
**Returns**  
---  
**Type** | **Description**  
`pd.DataFrame` | Pandas Dataframe of Experiment Runs.  
  
### get_or_create
    
    
    get_or_create(
        experiment_name: str,
        *,
        description: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> google.cloud.aiplatform.metadata.experiment_resources.Experiment

Gets experiment if one exists with this experiment_name in Vertex AI Experiments.

Otherwise creates this experiment.
    
    
    my_experiment = aiplatform.Experiment.get_or_create('my-experiment', description='my description')
    

**Parameters**  
---  
**Name** | **Description**  
`experiment_name` |  `str`   
Required. The name of this experiment.  
`description` |  `str`   
Optional. Describes this experiment's purpose.  
`project` |  `str`   
Optional. Project where this experiment will be retrieved from or created. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location where this experiment will be retrieved from or created. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials used to retrieve or create this experiment. Overrides credentials set in aiplatform.init.  
  
### list
    
    
    list(
        *,
        filter: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> typing.List[google.cloud.aiplatform.metadata.experiment_resources.Experiment]

List all Vertex AI Experiments in the given project.
    
    
    my_experiments = aiplatform.Experiment.list()
    

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. A query to filter available resources for matching results.  
`project` |  `str`   
Optional. Project to list these experiments from. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location to list these experiments from. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to list these experiments. Overrides credentials set in aiplatform.init.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
