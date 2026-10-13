---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient
title: Class TablesClient (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:42.196978+00:00
---

# Class TablesClient (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TablesClient (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    TablesClient(
        *,
        project=None,
        region="us-central1",
        credentials=None,
        client=None,
        prediction_client=None,
        gcs_client=None,
        **kwargs
    )

AutoML Tables API helper.

This is intended to simplify usage of the auto-generated python client, in particular for the `AutoML Tables product <https://cloud.google.com/automl-tables/>`_.

## Methods 

### TablesClient
    
    
    TablesClient(
        *,
        project=None,
        region="us-central1",
        credentials=None,
        client=None,
        prediction_client=None,
        gcs_client=None,
        **kwargs
    )

Constructor.

Example for US region:

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ...

Example for EU region:

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client_options = {'api_endpoint': 'eu-automl.googleapis.com:443'} client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='eu', client_options=client_options) ...

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The project ID of the GCP project all future calls will default to. Most methods take `project` as an optional parameter, and can override your choice of `project` supplied here.  
`region` |  `Optional[str]`   
The region all future calls will default to. Most methods take `region` as an optional parameter, and can override your choice of `region` supplied here. Note, only `us-central1` is supported to-date.  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify this application to the service. If none are specified, the client will attempt to ascertain the credentials from the environment. This argument is mutually exclusive with providing a transport instance to `transport`; doing so will raise an exception.  
`client` |  `Optional[google.automl_v1beta1.AutoMlClient]`   
An AutoMl Client to use for requests.  
`prediction_client` |  `Optional[google.automl_v1beta1.PredictionClient]`   
A Prediction Client to use for requests.  
`gcs_client` |  `Optional[google.automl_v1beta1.GcsClient]`   
A Storage client to use for requests.  
`client_options` |  `Union[dict, google.api_core.client_options.ClientOptions]`   
Custom options for the client.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests.  
  
### batch_predict
    
    
    batch_predict(
        *,
        pandas_dataframe=None,
        bigquery_input_uri=None,
        bigquery_output_uri=None,
        gcs_input_uris=None,
        gcs_output_uri_prefix=None,
        model=None,
        model_name=None,
        model_display_name=None,
        project=None,
        region=None,
        credentials=None,
        inputs=None,
        params={},
        **kwargs
    )

Makes a batch prediction on a model. This does _not_ require the model to be deployed.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... client.batch_predict( ... gcs_input_uris='gs://inputs/input.csv', ... gcs_output_uri_prefix='gs://outputs/', ... model_display_name='my_model' ... ).result() ...

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the model. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify this application to the service. If none are specified, the client will attempt to ascertain the credentials from the environment.  
`pandas_dataframe` |  `Optional[pandas.DataFrame]`   
A Pandas Dataframe object containing the data you want to predict off of. The data will be converted to CSV, and this CSV will be staged to GCS in `gs://{project}-automl-tables-staging/{uploaded_csv_name}` This must be supplied if neither `gcs_input_uris` nor `bigquery_input_uri` is supplied.  
`gcs_input_uris` |  `Optional(Union[List[str], str])`   
Either a list of or a single GCS URI containing the data you want to predict off of. This must be supplied if neither `pandas_dataframe` nor `bigquery_input_uri` is supplied.  
`gcs_output_uri_prefix` |  `Optional[str]`   
The folder in GCS you want to write output to. This must be supplied if `bigquery_output_uri` is not.  
`bigquery_input_uri` |  `Optional[str]`   
The BigQuery table to input data from. This must be supplied if neither `pandas_dataframe` nor `gcs_input_uris` is supplied.  
`bigquery_output_uri` |  `Optional[str]`   
The BigQuery table to output data to. This must be supplied if `gcs_output_uri_prefix` is not.  
`model_display_name` |  `Optional[str]`   
The human-readable name given to the model you want to predict with. This must be supplied if `model` or `model_name` are not supplied.  
`model_name` |  `Optional[str]`   
The AutoML-assigned name given to the model you want to predict with. This must be supplied if `model_display_name` or `model` are not supplied.  
`model` |  `Optional[model]`   
The `model` instance you want to predict with . This must be supplied if `model_display_name` or `model_name` are not supplied.  
`params` |  `Optional[dict]`   
Additional domain-specific parameters for the predictions, any string must be up to 25000 characters long.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An operation future that can be used to check for completion synchronously or asynchronously.  
  
### clear_test_train_column
    
    
    clear_test_train_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        project=None,
        region=None,
        **kwargs
    )

Clears the test/train (ml_use) column which designates which data belongs to the test and train sets.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... client.clear_test_train_column(dataset_display_name='my_dataset')

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the table. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to update the test/train column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the test/train column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to update the test/train column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the test/train column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_display_name` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to update the test/train column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the test/train column of. This must be supplied if `table_spec_name`, `dataset_name` or `dataset_display_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### clear_time_column
    
    
    clear_time_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        project=None,
        region=None,
        **kwargs
    )

Clears the time column which designates which data will be of type timestamp and will be used for the timeseries data.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... client.clear_time_column(dataset_display_name='my_dataset')

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the table. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to update the time column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the time column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to update the time column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the time column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_display_name` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to update the time column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the time column of. This must be supplied if `table_spec_name`, `dataset_name` or `dataset_display_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### clear_weight_column
    
    
    clear_weight_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        project=None,
        region=None,
        **kwargs
    )

Clears the weight column for a given dataset.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... client.clear_weight_column(dataset_display_name='my_dataset')

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the table. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to update the weight column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the weight column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to update the weight column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the weight column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_display_name` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to update the weight column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the weight column of. This must be supplied if `table_spec_name`, `dataset_name` or `dataset_display_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### create_dataset
    
    
    create_dataset(
        dataset_display_name, *, metadata={}, project=None, region=None, **kwargs
    )

Create a dataset. Keep in mind, importing data is a separate step.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... d = client.create_dataset(dataset_display_name='my_dataset')

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that will own the dataset. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`dataset_display_name` |  `str`   
A human-readable name to refer to this dataset by.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### create_model
    
    
    create_model(
        model_display_name,
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        train_budget_milli_node_hours=None,
        optimization_objective=None,
        project=None,
        region=None,
        model_metadata=None,
        include_column_spec_names=None,
        exclude_column_spec_names=None,
        disable_early_stopping=False,
        **kwargs
    )

Create a model. This will train your model on the given dataset.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... m = client.create_model( ... 'my_model', ... dataset_display_name='my_dataset', ... train_budget_milli_node_hours=1000 ... )
>>> 
>>> m.result() # blocks on result

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that will own the model. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`model_display_name` |  `str`   
A human-readable name to refer to this model by.  
`train_budget_milli_node_hours` |  `int`   
The amount of time (in thousandths of an hour) to spend training. This value must be between 1,000 and 72,000 inclusive (between 1 and 72 hours).  
`optimization_objective` |  `str`   
The metric AutoML tables should optimize for.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to train your model on. This must be supplied if `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to train your model on. This must be supplied if `dataset_display_name` or `dataset` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to train your model on. This must be supplied if `dataset_display_name` or `dataset_name` are not supplied.  
`model_metadata` |  `Optional[Dict]`   
Optional model metadata to supply to the client.  
`include_column_spec_names` |  `Optional[str]`   
The list of the names of the columns you want to include to train your model on.  
`exclude_column_spec_names` |  `Optional[str]`   
The list of the names of the columns you want to exclude and not train your model on.  
`disable_early_stopping` |  `Optional[bool]`   
True if disable early stopping. By default, the early stopping feature is enabled, which means that AutoML Tables might stop training before the entire training budget has been used.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An operation future that can be used to check for completion synchronously or asynchronously.  
  
### delete_dataset
    
    
    delete_dataset(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        project=None,
        region=None,
        **kwargs
    )

Deletes a dataset. This does not delete any models trained on this dataset.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... op = client.delete_dataset(dataset_display_name='my_dataset')
>>> 
>>> op.result() # blocks on delete request

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the dataset. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to delete. This must be supplied if `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to delete. This must be supplied if `dataset_display_name` or `dataset` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to delete. This must be supplied if `dataset_display_name` or `dataset_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An operation future that can be used to check for completion synchronously or asynchronously.  
  
### delete_model
    
    
    delete_model(
        *,
        model=None,
        model_display_name=None,
        model_name=None,
        project=None,
        region=None,
        **kwargs
    )

Deletes a model. Note this will not delete any datasets associated with this model.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... op = client.delete_model(model_display_name='my_model')
>>> 
>>> op.result() # blocks on delete request

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the model. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`model_display_name` |  `Optional[str]`   
The human-readable name given to the model you want to delete. This must be supplied if `model` or `model_name` are not supplied.  
`model_name` |  `Optional[str]`   
The AutoML-assigned name given to the model you want to delete. This must be supplied if `model_display_name` or `model` are not supplied.  
`model` |  `Optional[model]`   
The `model` instance you want to delete. This must be supplied if `model_display_name` or `model_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An operation future that can be used to check for completion synchronously or asynchronously.  
  
### deploy_model
    
    
    deploy_model(
        *,
        model=None,
        model_name=None,
        model_display_name=None,
        project=None,
        region=None,
        **kwargs
    )

Deploys a model. This allows you make online predictions using the model you've deployed.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... op = client.deploy_model(model_display_name='my_model')
>>> 
>>> op.result() # blocks on deploy request

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the model. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`model_display_name` |  `Optional[str]`   
The human-readable name given to the model you want to deploy. This must be supplied if `model` or `model_name` are not supplied.  
`model_name` |  `Optional[str]`   
The AutoML-assigned name given to the model you want to deploy. This must be supplied if `model_display_name` or `model` are not supplied.  
`model` |  `Optional[model]`   
The `model` instance you want to deploy. This must be supplied if `model_display_name` or `model_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An operation future that can be used to check for completion synchronously or asynchronously.  
  
### export_data
    
    
    export_data(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        gcs_output_uri_prefix=None,
        bigquery_output_uri=None,
        project=None,
        region=None,
        **kwargs
    )

Exports data from a dataset.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... d = client.create_dataset(dataset_display_name='my_dataset')
>>> 
>>> response = client.export_data(dataset=d, ... gcs_output_uri_prefix='gs://cloud-ml-tables-data/bank-marketing.csv') ... def callback(operation_future): ... result = operation_future.result() ... response.add_done_callback(callback)

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the dataset. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to export data from. This must be supplied if `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to export data from. This must be supplied if `dataset_display_name` or `dataset` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to export data from. This must be supplied if `dataset_display_name` or `dataset_name` are not supplied.  
`gcs_output_uri_prefix` |  `Optional[Union[str, Sequence[str]]]`   
A single `gs://..` prefixed URI to export to. This must be supplied if `bigquery_output_uri` is not.  
`bigquery_output_uri` |  `Optional[str]`   
A URI pointing to the BigQuery table containing the data to export. This must be supplied if `gcs_output_uri_prefix` is not.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An operation future that can be used to check for completion synchronously or asynchronously.  
  
### get_column_spec
    
    
    get_column_spec(column_spec_name, *, project=None, region=None, **kwargs)

Gets a single column spec in a particular project and region.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... d = client.get_column_spec('my_column_spec')

**Parameters**  
---  
**Name** | **Description**  
`column_spec_name` |  `str`   
This is the fully-qualified name generated by the AutoML API for this column spec.  
`project` |  `Optional[str]`   
The ID of the project that owns the column. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### get_dataset
    
    
    get_dataset(
        *, project=None, region=None, dataset_name=None, dataset_display_name=None, **kwargs
    )

Gets a single dataset in a particular project and region.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... d = client.get_dataset(dataset_display_name='my_dataset')

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the dataset. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`dataset_name` |  `Optional[str]`   
This is the fully-qualified name generated by the AutoML API for this dataset. This is not to be confused with the human-assigned `dataset_display_name` that is provided when creating a dataset. Either `dataset_name` or `dataset_display_name` must be provided.  
`dataset_display_name` |  `Optional[str]`   
This is the name you provided for the dataset when first creating it. Either `dataset_name` or `dataset_display_name` must be provided.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### get_model
    
    
    get_model(
        *, project=None, region=None, model_name=None, model_display_name=None, **kwargs
    )

Gets a single model in a particular project and region.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... d = client.get_model(model_display_name='my_model')

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the model. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`model_name` |  `Optional[str]`   
This is the fully-qualified name generated by the AutoML API for this model. This is not to be confused with the human-assigned `model_display_name` that is provided when creating a model. Either `model_name` or `model_display_name` must be provided.  
`model_display_name` |  `Optional[str]`   
This is the name you provided for the model when first creating it. Either `model_name` or `model_display_name` must be provided.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### get_model_evaluation
    
    
    get_model_evaluation(model_evaluation_name, *, project=None, region=None, **kwargs)

Gets a single evaluation model in a particular project and region.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... d = client.get_model_evaluation('my_model_evaluation')

**Parameters**  
---  
**Name** | **Description**  
`model_evaluation_name` |  `str`   
This is the fully-qualified name generated by the AutoML API for this model evaluation.  
`project` |  `Optional[str]`   
The ID of the project that owns the model. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### get_table_spec
    
    
    get_table_spec(table_spec_name, *, project=None, region=None, **kwargs)

Gets a single table spec in a particular project and region.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... d = client.get_table_spec('my_table_spec')

**Parameters**  
---  
**Name** | **Description**  
`table_spec_name` |  `str`   
This is the fully-qualified name generated by the AutoML API for this table spec.  
`project` |  `Optional[str]`   
The ID of the project that owns the table. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### import_data
    
    
    import_data(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        pandas_dataframe=None,
        gcs_input_uris=None,
        bigquery_input_uri=None,
        project=None,
        region=None,
        credentials=None,
        **kwargs
    )

Imports data into a dataset.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... d = client.create_dataset(dataset_display_name='my_dataset')
>>> 
>>> response = client.import_data(dataset=d, ... gcs_input_uris='gs://cloud-ml-tables-data/bank-marketing.csv') ... def callback(operation_future): ... result = operation_future.result() ... response.add_done_callback(callback)

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the dataset. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify this application to the service. If none are specified, the client will attempt to ascertain the credentials from the environment.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to import data into. This must be supplied if `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to import data into. This must be supplied if `dataset_display_name` or `dataset` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to import data into. This must be supplied if `dataset_display_name` or `dataset_name` are not supplied.  
`pandas_dataframe` |  `Optional[pandas.DataFrame]`   
A Pandas Dataframe object containing the data to import. The data will be converted to CSV, and this CSV will be staged to GCS in `gs://{project}-automl-tables-staging/{uploaded_csv_name}` This parameter must be supplied if neither `gcs_input_uris` nor `bigquery_input_uri` is supplied.  
`gcs_input_uris` |  `Optional[Union[str, Sequence[str]]]`   
Either a single `gs://..` prefixed URI, or a list of URIs referring to GCS-hosted CSV files containing the data to import. This must be supplied if neither `bigquery_input_uri` nor `pandas_dataframe` is supplied.  
`bigquery_input_uri` |  `Optional[str]`   
A URI pointing to the BigQuery table containing the data to import. This must be supplied if neither `gcs_input_uris` nor `pandas_dataframe` is supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An operation future that can be used to check for completion synchronously or asynchronously.  
  
### list_column_specs
    
    
    list_column_specs(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        table_spec_name=None,
        table_spec_index=0,
        project=None,
        region=None,
        **kwargs
    )

Lists column specs.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... for s in client.list_column_specs(dataset_display_name='my_dataset') ... # process the spec ... pass ...

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the columns. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`table_spec_name` |  `Optional[str]`   
The AutoML-assigned name for the table whose specs you want to read. If not supplied, the client can determine this name from a source `Dataset` object.  
`table_spec_index` |  `Optional[int]`   
If no `table_spec_name` was provided, we use this index to determine which table to read column specs from.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to read specs from. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to read specs from. This must be supplied if `table_spec_name`, `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to read specs from. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to read specs from. This must be supplied if `table_spec_name`, `dataset` or `dataset_display_name` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to read specs from. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to read specs from. This must be supplied if `table_spec_name`, `dataset_name` or `dataset_display_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### list_datasets
    
    
    list_datasets(*, project=None, region=None, **kwargs)

List all datasets in a particular project and region.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... ds = client.list_datasets()
>>> 
>>> for d in ds: ... # do something ... pass ...

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the datasets. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### list_model_evaluations
    
    
    list_model_evaluations(
        *,
        project=None,
        region=None,
        model=None,
        model_display_name=None,
        model_name=None,
        **kwargs
    )

List all model evaluations for a given model.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... ms = client.list_model_evaluations(model_display_name='my_model')
>>> 
>>> for m in ms: ... # do something ... pass ...

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the model. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`model_display_name` |  `Optional[str]`   
The human-readable name given to the model you want to list evaluations for. This must be supplied if `model` or `model_name` are not supplied.  
`model_name` |  `Optional[str]`   
The AutoML-assigned name given to the model you want to list evaluations for. This must be supplied if `model_display_name` or `model` are not supplied.  
`model` |  `Optional[model]`   
The `model` instance you want to list evaluations for. This must be supplied if `model_display_name` or `model_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### list_models
    
    
    list_models(*, project=None, region=None, **kwargs)

List all models in a particular project and region.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... ms = client.list_models()
>>> 
>>> for m in ms: ... # do something ... pass ...

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the models. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### list_table_specs
    
    
    list_table_specs(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        project=None,
        region=None,
        **kwargs
    )

Lists table specs.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... for s in client.list_table_specs(dataset_display_name='my_dataset') ... # process the spec ... pass ...

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the dataset. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to read specs from. This must be supplied if `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to read specs from. This must be supplied if `dataset_display_name` or `dataset` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to read specs from. This must be supplied if `dataset_display_name` or `dataset_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### predict
    
    
    predict(
        inputs,
        *,
        model=None,
        model_name=None,
        model_display_name=None,
        feature_importance=False,
        project=None,
        region=None,
        **kwargs
    )

Makes a prediction on a deployed model. This will fail if the model was not deployed.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... client.predict(inputs={'Age': 30, 'Income': 12, 'Category': 'A'} ... model_display_name='my_model') ... client.predict([30, 12, 'A'], model_display_name='my_model')

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the model. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`inputs` |  `Union[List[str], Dict[str, str]]`   
Either the sorted list of column values to predict with, or a key-value map of column display name to value to predict with.  
`model_display_name` |  `Optional[str]`   
The human-readable name given to the model you want to predict with. This must be supplied if `model` or `model_name` are not supplied.  
`model_name` |  `Optional[str]`   
The AutoML-assigned name given to the model you want to predict with. This must be supplied if `model_display_name` or `model` are not supplied.  
`model` |  `Optional[model]`   
The `model` instance you want to predict with . This must be supplied if `model_display_name` or `model_name` are not supplied.  
`feature_importance` |  `bool`   
True if enable feature importance explainability. The default is False.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### set_target_column
    
    
    set_target_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        table_spec_name=None,
        table_spec_index=0,
        column_spec_name=None,
        column_spec_display_name=None,
        project=None,
        region=None,
        **kwargs
    )

Sets the target column for a given table.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... client.set_target_column(dataset_display_name='my_dataset', ... column_spec_display_name='Income') ...

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the table. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`column_spec_name` |  `Optional[str]`   
The name AutoML-assigned name for the column you want to set as the target column.  
`column_spec_display_name` |  `Optional[str]`   
The human-readable name of the column you want to set as the target column. If this is supplied in place of `column_spec_name`, you also need to provide either a way to lookup the source dataset (using one of the `dataset*` kwargs), or the `table_spec_name` of the table this column belongs to.  
`table_spec_name` |  `Optional[str]`   
The AutoML-assigned name for the table whose target column you want to set . If not supplied, the client can determine this name from a source `Dataset` object.  
`table_spec_index` |  `Optional[int]`   
If no `table_spec_name` or `column_spec_name` was provided, we use this index to determine which table to set the target column on.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to update the target column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the target column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to update the target column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the target column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_display_name` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to update the target column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the target column of. This must be supplied if `table_spec_name`, `dataset_name` or `dataset_display_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### set_test_train_column
    
    
    set_test_train_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        table_spec_name=None,
        table_spec_index=0,
        column_spec_name=None,
        column_spec_display_name=None,
        project=None,
        region=None,
        **kwargs
    )

Sets the test/train (ml_use) column which designates which data belongs to the test and train sets. This column must be categorical.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... client.set_test_train_column(dataset_display_name='my_dataset', ... column_spec_display_name='TestSplit') ...

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the table. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`column_spec_name` |  `Optional[str]`   
The name AutoML-assigned name for the column you want to set as the test/train column.  
`column_spec_display_name` |  `Optional[str]`   
The human-readable name of the column you want to set as the test/train column. If this is supplied in place of `column_spec_name`, you also need to provide either a way to lookup the source dataset (using one of the `dataset*` kwargs), or the `table_spec_name` of the table this column belongs to.  
`table_spec_name` |  `Optional[str]`   
The AutoML-assigned name for the table whose test/train column you want to set . If not supplied, the client can determine this name from a source `Dataset` object.  
`table_spec_index` |  `Optional[int]`   
If no `table_spec_name` or `column_spec_name` was provided, we use this index to determine which table to set the test/train column on.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to update the test/train column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the test/train column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to update the test/train column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the test/train column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_display_name` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to update the test/train column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the test/train column of. This must be supplied if `table_spec_name`, `dataset_name` or `dataset_display_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### set_time_column
    
    
    set_time_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        table_spec_name=None,
        table_spec_index=0,
        column_spec_name=None,
        column_spec_display_name=None,
        project=None,
        region=None,
        **kwargs
    )

Sets the time column which designates which data will be of type timestamp and will be used for the timeseries data. This column must be of type timestamp.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... client.set_time_column(dataset_display_name='my_dataset', ... column_spec_display_name='Unix Time') ...

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the table. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`column_spec_name` |  `Optional[str]`   
The name AutoML-assigned name for the column you want to set as the time column.  
`column_spec_display_name` |  `Optional[str]`   
The human-readable name of the column you want to set as the time column. If this is supplied in place of `column_spec_name`, you also need to provide either a way to lookup the source dataset (using one of the `dataset*` kwargs), or the `table_spec_name` of the table this column belongs to.  
`table_spec_name` |  `Optional[str]`   
The AutoML-assigned name for the table whose time column you want to set . If not supplied, the client can determine this name from a source `Dataset` object.  
`table_spec_index` |  `Optional[int]`   
If no `table_spec_name` or `column_spec_name` was provided, we use this index to determine which table to set the time column on.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to update the time column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the time column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to update the time column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the time column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_display_name` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to update the time column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the time column of. This must be supplied if `table_spec_name`, `dataset_name` or `dataset_display_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### set_weight_column
    
    
    set_weight_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        table_spec_name=None,
        table_spec_index=0,
        column_spec_name=None,
        column_spec_display_name=None,
        project=None,
        region=None,
        **kwargs
    )

Sets the weight column for a given table.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... client.set_weight_column(dataset_display_name='my_dataset', ... column_spec_display_name='Income') ...

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the table. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`column_spec_name` |  `Optional[str]`   
The name AutoML-assigned name for the column you want to set as the weight column.  
`column_spec_display_name` |  `Optional[str]`   
The human-readable name of the column you want to set as the weight column. If this is supplied in place of `column_spec_name`, you also need to provide either a way to lookup the source dataset (using one of the `dataset*` kwargs), or the `table_spec_name` of the table this column belongs to.  
`table_spec_name` |  `Optional[str]`   
The AutoML-assigned name for the table whose weight column you want to set . If not supplied, the client can determine this name from a source `Dataset` object.  
`table_spec_index` |  `Optional[int]`   
If no `table_spec_name` or `column_spec_name` was provided, we use this index to determine which table to set the weight column on.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to update the weight column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the weight column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to update the weight column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the weight column of. This must be supplied if `table_spec_name`, `dataset` or `dataset_display_name` are not supplied.  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to update the weight column of. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update the weight column of. This must be supplied if `table_spec_name`, `dataset_name` or `dataset_display_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
### undeploy_model
    
    
    undeploy_model(
        *,
        model=None,
        model_name=None,
        model_display_name=None,
        project=None,
        region=None,
        **kwargs
    )

Undeploys a model.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... op = client.undeploy_model(model_display_name='my_model')
>>> 
>>> op.result() # blocks on undeploy request

**Parameters**  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The ID of the project that owns the model. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
`model_display_name` |  `Optional[str]`   
The human-readable name given to the model you want to undeploy. This must be supplied if `model` or `model_name` are not supplied.  
`model_name` |  `Optional[str]`   
The AutoML-assigned name given to the model you want to undeploy. This must be supplied if `model_display_name` or `model` are not supplied.  
`model` |  `Optional[model]`   
The `model` instance you want to undeploy. This must be supplied if `model_display_name` or `model_name` are not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An operation future that can be used to check for completion synchronously or asynchronously.  
  
### update_column_spec
    
    
    update_column_spec(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        table_spec_name=None,
        table_spec_index=0,
        column_spec_name=None,
        column_spec_display_name=None,
        type_code=None,
        nullable=None,
        project=None,
        region=None,
        **kwargs
    )

Updates a column's specs.

.. rubric:: Example

> > > from google.cloud import automl_v1beta1
>>> 
>>> from google.oauth2 import service_account
>>> 
>>> client = automl_v1beta1.TablesClient( ... credentials=service_account.Credentials.from_service_account_file('`/.gcp/account.json'), ... project='my-project', region='us-central1') ... client.update_column_spec(dataset_display_name='my_dataset', ... column_spec_display_name='Outcome', ... type_code=automl_v1beta1.TypeCode.CATEGORY) ...

**Parameters**  
---  
**Name** | **Description**  
`dataset` |  `Optional[Dataset]`   
The `Dataset` instance you want to update specs on. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update specs on. This must be supplied if `table_spec_name`, `dataset_name` or `dataset_display_name` are not supplied.  
`dataset_display_name` |  `Optional[str]`   
The human-readable name given to the dataset you want to update specs on. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update specs on. This must be supplied if `table_spec_name`, `dataset` or `dataset_name` are not supplied.  
`dataset_name` |  `Optional[str]`   
The AutoML-assigned name given to the dataset you want to update specs one. If no `table_spec_name` is supplied, this will be used together with `table_spec_index` to infer the name of table to update specs on. This must be supplied if `table_spec_name`, `dataset` or `dataset_display_name` are not supplied.  
`table_spec_name` |  `Optional[str]`   
The AutoML-assigned name for the table whose specs you want to update. If not supplied, the client can determine this name from a source `Dataset` object.  
`table_spec_index` |  `Optional[int]`   
If no `table_spec_name` was provided, we use this index to determine which table to update column specs on.  
`column_spec_name` |  `Optional[str]`   
The name AutoML-assigned name for the column you want to update.  
`column_spec_display_name` |  `Optional[str]`   
The human-readable name of the column you want to update. If this is supplied in place of `column_spec_name`, you also need to provide either a way to lookup the source dataset (using one of the `dataset*` kwargs), or the `table_spec_name` of the table this column belongs to.  
`type_code` |  `Optional[str]`   
The desired 'type_code' of the column. For more information on the available types, please see the documentation: <https://cloud.google.com/automl-tables/docs/reference/rpc/google.cloud.automl.v1beta1#typecode>  
`nullable` |  `Optional[bool]`   
Set to `True` or `False` to specify if this column's value must expected to be present in all rows or not.  
`project` |  `Optional[str]`   
The ID of the project that owns the columns. If you have initialized the client with a value for `project` it will be used if this parameter is not supplied. Keep in mind, the service account this client was initialized with must have access to this project.  
`region` |  `Optional[str]`   
If you have initialized the client with a value for `region` it will be used if this parameter is not supplied.  
**Exceptions**  
---  
**Type** | **Description**  
`google.api_core.exceptions.GoogleAPICallError` | If the request failed for any reason.  
`google.api_core.exceptions.RetryError` | If the request failed due to a retryable error and retry attempts failed.  
`ValueError` | If required parameters are missing.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
