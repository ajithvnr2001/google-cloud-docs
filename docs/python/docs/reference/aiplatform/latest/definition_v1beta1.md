---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/definition_v1beta1/
title: Types for Google Cloud Aiplatform V1beta1 Schema Trainingjob Definition v1beta1 API \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:10.664144+00:00
---

# Types for Google Cloud Aiplatform V1beta1 Schema Trainingjob Definition v1beta1 API  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/definition_v1beta1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Types for Google Cloud Aiplatform V1beta1 Schema Trainingjob Definition v1beta1 API Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecasting(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

A TrainingJob that trains and uploads an AutoML Forecasting Model.

#### inputs()

The input parameters of this TrainingJob.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs)




#### metadata()

The metadata information.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingMetadata](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingMetadata)




#### inputs(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_time_series_forecasting.AutoMlForecastingInputs](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs_ )

#### metadata(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_time_series_forecasting.AutoMlForecastingMetadata](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingMetadata_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

#### target_column()

The name of the column that the model is to predict.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_series_identifier_column()

The name of the column that identifies the time series.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_column()

The name of the column that identifies time order in the time series.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### transformations()

Each transformation will apply transform function to given input column. And the result will be used for training. When creating transformation for BigQuery Struct column, the column should be flattened using “.” as the delimiter.

  * **Type**

MutableSequence[[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation)]




#### optimization_objective()

Objective function the model is optimizing towards. The training process creates a model that optimizes the value of the objective function over the validation set.

The supported optimization objectives:

  * “minimize-rmse” (default) - Minimize root-mean-squared error (RMSE).

  * “minimize-mae” - Minimize mean-absolute error (MAE).

  * “minimize-rmsle” - Minimize root-mean-squared log error (RMSLE).

  * “minimize-rmspe” - Minimize root-mean-squared percentage error (RMSPE).

  * “minimize-wape-mae” - Minimize the combination of weighted absolute percentage error (WAPE) and mean-absolute-error (MAE).

  * “minimize-quantile-loss” - Minimize the quantile loss at the quantiles defined in `quantiles`.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### train_budget_milli_node_hours()

Required. The train budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour.

The training cost of the model will not exceed this budget. The final cost will be attempted to be close to the budget, though may end up being (even) noticeably smaller - at the backend’s discretion. This especially may happen when further model training ceases to provide any improvements.

If the budget is set to a value known to be insufficient to train a model for the given dataset, the training won’t be attempted and will error.

The train budget must be between 1,000 and 72,000 milli node hours, inclusive.

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### weight_column()

Column name that should be used as the weight column. Higher values in this column give more importance to the row during model training. The column must have numeric values between 0 and 10000 inclusively; 0 means the row is ignored for training. If weight column field is not set, then all rows are assumed to have equal weight of 1.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_series_attribute_columns()

Column names that should be used as attribute columns. The value of these columns does not vary as a function of time. For example, store ID or item color.

  * **Type**

MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]




#### unavailable_at_forecast_columns()

Names of columns that are unavailable when a forecast is requested. This column contains information for the given entity (identified by the time_series_identifier_column) that is unknown before the forecast For example, actual weather on a given day.

  * **Type**

MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]




#### available_at_forecast_columns()

Names of columns that are available and provided when a forecast is requested. These columns contain information for the given entity (identified by the time_series_identifier_column column) that is known at forecast. For example, predicted weather for a specific day.

  * **Type**

MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]




#### data_granularity()

Expected difference in time granularity between rows in the data.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Granularity](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Granularity)




#### forecast_horizon()

The amount of time into the future for which forecasted values for the target are returned. Expressed in number of units defined by the `data_granularity` field.

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### context_window()

The amount of time into the past training and prediction data is used for model training and prediction respectively. Expressed in number of units defined by the `data_granularity` field.

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### export_evaluated_data_items_config()

Configuration for exporting test set predictions to a BigQuery table. If this configuration is absent, then the export is not performed.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.ExportEvaluatedDataItemsConfig](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.ExportEvaluatedDataItemsConfig)




#### quantiles()

Quantiles to use for minimize-quantile-loss `optimization_objective`. Up to 5 quantiles are allowed of values between 0 and 1, exclusive. Required if the value of optimization_objective is minimize-quantile-loss. Represents the percent quantiles to use for that objective. Quantiles must be unique.

  * **Type**

MutableSequence[[float](https://docs.python.org/3/builtins/functions.html#float)]




#### validation_options()

Validation options for the data validation component. The available options are:

  * “fail-pipeline” - default, will validate against the validation and fail the pipeline if it fails.

  * “ignore-validation” - ignore the results of the validation and continue

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### additional_experiments()

Additional experiment flags for the time series forcasting training.

  * **Type**

MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]




#### _class_ Granularity(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

A duration of time expressed in time granularity units.

#### unit()

The time granularity unit of this time period. The supported units are:

  * “minute”

  * “hour”

  * “day”

  * “week”

  * “month”

  * “year”.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### quantity()

The number of granularity_units between data points in the training data. If `granularity_unit` is `minute`, can be 1, 5, 10, 15, or 30. For all other values of `granularity_unit`, must be 1.

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### quantity(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

#### unit(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### _class_ Transformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

This message has [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

#### auto()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.AutoTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.AutoTransformation)




#### numeric()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.NumericTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.NumericTransformation)




#### categorical()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.CategoricalTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.CategoricalTransformation)




#### timestamp()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.TimestampTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.TimestampTransformation)




#### text()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.TextTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.TextTransformation)




#### _class_ AutoTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Training pipeline will infer the proper transformation based on the statistic of dataset.

#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### _class_ CategoricalTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Training pipeline will perform following transformation functions.

  * The categorical string as is–no change to case, punctuation, spelling, tense, and so on.

  * Convert the category name to a dictionary lookup index and generate an embedding for each index.

  * Categories that appear less than 5 times in the training dataset are treated as the “unknown” category. The “unknown” category gets its own special lookup index and resulting embedding.




#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### _class_ NumericTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Training pipeline will perform following transformation functions.

  * The value converted to float32.

  * The z_score of the value.

  * log(value+1) when the value is greater than or equal to 0. Otherwise, this transformation is not applied and the value is considered a missing value.

  * z_score of log(value+1) when the value is greater than or equal to

  * Otherwise, this transformation is not applied and the value is considered a missing value.

  * A boolean value that indicates whether the value is valid.




#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### _class_ TextTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Training pipeline will perform following transformation functions.

  * The text as is–no change to case, punctuation, spelling, tense, and so on.

  * Convert the category name to a dictionary lookup index and generate an embedding for each index.




#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### _class_ TimestampTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Training pipeline will perform following transformation functions.

  * Apply the transformation functions for Numerical columns.

  * Determine the year, month, day,and weekday. Treat each value from the timestamp as a Categorical column.

  * Invalid numerical values (for example, values that fall outside of a typical timestamp range, or are extreme values) receive no special treatment and are not removed.




#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_format()

The format in which that time field is expressed. The time_format must either be one of:

  * `unix-seconds`

  * `unix-milliseconds`

  * `unix-microseconds`

  * `unix-nanoseconds`




(for respectively number of seconds, milliseconds, microseconds and nanoseconds since start of the Unix epoch);

or be written in `strftime` syntax.

If time_format is not set, then the default format is RFC 3339 `date-time` format, where `time-offset` = `"Z"` (e.g. 1985-04-12T23:20:50.52Z)

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### time_format(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### auto(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_time_series_forecasting.AutoMlForecastingInputs.Transformation.AutoTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.AutoTransformation_ )

#### categorical(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_time_series_forecasting.AutoMlForecastingInputs.Transformation.CategoricalTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.CategoricalTransformation_ )

#### numeric(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_time_series_forecasting.AutoMlForecastingInputs.Transformation.NumericTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.NumericTransformation_ )

#### text(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_time_series_forecasting.AutoMlForecastingInputs.Transformation.TextTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.TextTransformation_ )

#### timestamp(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_time_series_forecasting.AutoMlForecastingInputs.Transformation.TimestampTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation.TimestampTransformation_ )

#### additional_experiments(_: MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)_ )

#### available_at_forecast_columns(_: MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)_ )

#### context_window(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

#### data_granularity(_: [Granularity](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Granularity_ )

#### export_evaluated_data_items_config(_: gcastd_export_evaluated_data_items_config.ExportEvaluatedDataItemsConfi_ )

#### forecast_horizon(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

#### optimization_objective(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### quantiles(_: MutableSequence[[float](https://docs.python.org/3/builtins/functions.html#float)_ )

#### target_column(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### time_column(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### time_series_attribute_columns(_: MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)_ )

#### time_series_identifier_column(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### train_budget_milli_node_hours(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

#### transformations(_: MutableSequence[[Transformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingInputs.Transformation)_ )

#### unavailable_at_forecast_columns(_: MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)_ )

#### validation_options(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### weight_column(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlForecastingMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Model metadata specific to AutoML Forecasting.

#### train_cost_milli_node_hours()

Output only. The actual training cost of the model, expressed in milli node hours, i.e. 1,000 value in this field means 1 node hour. Guaranteed to not exceed the train budget.

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### train_cost_milli_node_hours(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassification(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

A TrainingJob that trains and uploads an AutoML Image Classification Model.

#### inputs()

The input parameters of this TrainingJob.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationInputs](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationInputs)




#### metadata()

The metadata information.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationMetadata](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationMetadata)




#### inputs(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_image_classification.AutoMlImageClassificationInputs](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationInputs_ )

#### metadata(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_image_classification.AutoMlImageClassificationMetadata](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationMetadata_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

#### model_type()

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationInputs.ModelType](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationInputs.ModelType)




#### base_model_id()

The ID of the `base` model. If it is specified, the new model will be trained based on the `base` model. Otherwise, the new model will be trained from scratch. The `base` model must be in the same Project and Location as the new Model to train, and have the same modelType.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### budget_milli_node_hours()

The training budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The actual metadata.costMilliNodeHours will be equal or less than this value. If further model training ceases to provide any improvements, it will stop without using the full budget and the metadata.successfulStopReason will be `model-converged`. Note, node_hour = actual_hour * number_of_nodes_involved. For modelType `cloud`(default), the budget must be between 8,000 and 800,000 milli node hours, inclusive. The default value is 192,000 which represents one day in wall time, considering 8 nodes are used. For model types `mobile-tf-low-latency-1`, `mobile-tf-versatile-1`, `mobile-tf-high-accuracy-1`, the training budget must be between 1,000 and 100,000 milli node hours, inclusive. The default value is 24,000 which represents one day in wall time on a single node that is used.

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### disable_early_stopping()

Use the entire training budget. This disables the early stopping feature. When false the early stopping feature is enabled, which means that AutoML Image Classification might stop training before the entire training budget has been used.

  * **Type**

[bool](https://docs.python.org/3/builtins/functions.html#bool)




#### multi_label()

If false, a single-label (multi-class) Model will be trained (i.e. assuming that for each image just up to one annotation may be applicable). If true, a multi-label Model will be trained (i.e. assuming that for each image multiple annotations may be applicable).

  * **Type**

[bool](https://docs.python.org/3/builtins/functions.html#bool)




#### _class_ ModelType(value)

Bases: [`proto.enums.Enum`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.enums.Enum)

Values:
    
    
    MODEL_TYPE_UNSPECIFIED (0):
    
        Should not be set.
    
    CLOUD (1):
    
        A Model best tailored to be used within
        Google Cloud, and which cannot be exported.
        Default.
    
    MOBILE_TF_LOW_LATENCY_1 (2):
    
        A model that, in addition to being available
        within Google Cloud, can also be exported (see
        ModelService.ExportModel) as TensorFlow or Core
        ML model and used on a mobile or edge device
        afterwards. Expected to have low latency, but
        may have lower prediction quality than other
        mobile models.
    
    MOBILE_TF_VERSATILE_1 (3):
    
        A model that, in addition to being available
        within Google Cloud, can also be exported (see
        ModelService.ExportModel) as TensorFlow or Core
        ML model and used on a mobile or edge device
        with afterwards.
    
    MOBILE_TF_HIGH_ACCURACY_1 (4):
    
        A model that, in addition to being available
        within Google Cloud, can also be exported (see
        ModelService.ExportModel) as TensorFlow or Core
        ML model and used on a mobile or edge device
        afterwards. Expected to have a higher latency,
        but should also have a higher prediction quality
        than other mobile models.
    

#### CLOUD(_=_ )

#### MOBILE_TF_HIGH_ACCURACY_1(_=_ )

#### MOBILE_TF_LOW_LATENCY_1(_=_ )

#### MOBILE_TF_VERSATILE_1(_=_ )

#### MODEL_TYPE_UNSPECIFIED(_=_ )

#### base_model_id(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### budget_milli_node_hours(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

#### disable_early_stopping(_: [bool](<https://docs.python.org/3/builtins/functions.html#bool>_ )

#### model_type(_: [ModelType](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationInputs.ModelType_ )

#### multi_label(_: [bool](<https://docs.python.org/3/builtins/functions.html#bool>_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

#### cost_milli_node_hours()

The actual training cost of creating this model, expressed in milli node hours, i.e. 1,000 value in this field means 1 node hour. Guaranteed to not exceed inputs.budgetMilliNodeHours.

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### successful_stop_reason()

For successful job completions, this is the reason why the job has finished.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationMetadata.SuccessfulStopReason](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationMetadata.SuccessfulStopReason)




#### _class_ SuccessfulStopReason(value)

Bases: [`proto.enums.Enum`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.enums.Enum)

Values:
    
    
    SUCCESSFUL_STOP_REASON_UNSPECIFIED (0):
    
        Should not be set.
    
    BUDGET_REACHED (1):
    
        The inputs.budgetMilliNodeHours had been
        reached.
    
    MODEL_CONVERGED (2):
    
        Further training of the Model ceased to
        increase its quality, since it already has
        converged.
    

#### BUDGET_REACHED(_=_ )

#### MODEL_CONVERGED(_=_ )

#### SUCCESSFUL_STOP_REASON_UNSPECIFIED(_=_ )

#### cost_milli_node_hours(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

#### successful_stop_reason(_: [SuccessfulStopReason](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageClassificationMetadata.SuccessfulStopReason_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetection(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

A TrainingJob that trains and uploads an AutoML Image Object Detection Model.

#### inputs()

The input parameters of this TrainingJob.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionInputs)




#### metadata()

The metadata information

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionMetadata](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionMetadata)




#### inputs(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_image_object_detection.AutoMlImageObjectDetectionInputs](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionInputs_ )

#### metadata(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_image_object_detection.AutoMlImageObjectDetectionMetadata](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionMetadata_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

#### model_type()

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionInputs.ModelType](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionInputs.ModelType)




#### budget_milli_node_hours()

The training budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The actual metadata.costMilliNodeHours will be equal or less than this value. If further model training ceases to provide any improvements, it will stop without using the full budget and the metadata.successfulStopReason will be `model-converged`. Note, node_hour = actual_hour * number_of_nodes_involved. For modelType `cloud`(default), the budget must be between 20,000 and 900,000 milli node hours, inclusive. The default value is 216,000 which represents one day in wall time, considering 9 nodes are used. For model types `mobile-tf-low-latency-1`, `mobile-tf-versatile-1`, `mobile-tf-high-accuracy-1` the training budget must be between 1,000 and 100,000 milli node hours, inclusive. The default value is 24,000 which represents one day in wall time on a single node that is used.

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### disable_early_stopping()

Use the entire training budget. This disables the early stopping feature. When false the early stopping feature is enabled, which means that AutoML Image Object Detection might stop training before the entire training budget has been used.

  * **Type**

[bool](https://docs.python.org/3/builtins/functions.html#bool)




#### _class_ ModelType(value)

Bases: [`proto.enums.Enum`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.enums.Enum)

Values:
    
    
    MODEL_TYPE_UNSPECIFIED (0):
    
        Should not be set.
    
    CLOUD_HIGH_ACCURACY_1 (1):
    
        A model best tailored to be used within
        Google Cloud, and which cannot be exported.
        Expected to have a higher latency, but should
        also have a higher prediction quality than other
        cloud models.
    
    CLOUD_LOW_LATENCY_1 (2):
    
        A model best tailored to be used within
        Google Cloud, and which cannot be exported.
        Expected to have a low latency, but may have
        lower prediction quality than other cloud
        models.
    
    MOBILE_TF_LOW_LATENCY_1 (3):
    
        A model that, in addition to being available
        within Google Cloud can also be exported (see
        ModelService.ExportModel) and used on a mobile
        or edge device with TensorFlow afterwards.
        Expected to have low latency, but may have lower
        prediction quality than other mobile models.
    
    MOBILE_TF_VERSATILE_1 (4):
    
        A model that, in addition to being available
        within Google Cloud can also be exported (see
        ModelService.ExportModel) and used on a mobile
        or edge device with TensorFlow afterwards.
    
    MOBILE_TF_HIGH_ACCURACY_1 (5):
    
        A model that, in addition to being available
        within Google Cloud, can also be exported (see
        ModelService.ExportModel) and used on a mobile
        or edge device with TensorFlow afterwards.
        Expected to have a higher latency, but should
        also have a higher prediction quality than other
        mobile models.
    

#### CLOUD_HIGH_ACCURACY_1(_=_ )

#### CLOUD_LOW_LATENCY_1(_=_ )

#### MOBILE_TF_HIGH_ACCURACY_1(_=_ )

#### MOBILE_TF_LOW_LATENCY_1(_=_ )

#### MOBILE_TF_VERSATILE_1(_=_ )

#### MODEL_TYPE_UNSPECIFIED(_=_ )

#### budget_milli_node_hours(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

#### disable_early_stopping(_: [bool](<https://docs.python.org/3/builtins/functions.html#bool>_ )

#### model_type(_: [ModelType](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionInputs.ModelType_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

#### cost_milli_node_hours()

The actual training cost of creating this model, expressed in milli node hours, i.e. 1,000 value in this field means 1 node hour. Guaranteed to not exceed inputs.budgetMilliNodeHours.

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### successful_stop_reason()

For successful job completions, this is the reason why the job has finished.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionMetadata.SuccessfulStopReason](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionMetadata.SuccessfulStopReason)




#### _class_ SuccessfulStopReason(value)

Bases: [`proto.enums.Enum`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.enums.Enum)

Values:
    
    
    SUCCESSFUL_STOP_REASON_UNSPECIFIED (0):
    
        Should not be set.
    
    BUDGET_REACHED (1):
    
        The inputs.budgetMilliNodeHours had been
        reached.
    
    MODEL_CONVERGED (2):
    
        Further training of the Model ceased to
        increase its quality, since it already has
        converged.
    

#### BUDGET_REACHED(_=_ )

#### MODEL_CONVERGED(_=_ )

#### SUCCESSFUL_STOP_REASON_UNSPECIFIED(_=_ )

#### cost_milli_node_hours(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

#### successful_stop_reason(_: [SuccessfulStopReason](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageObjectDetectionMetadata.SuccessfulStopReason_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

A TrainingJob that trains and uploads an AutoML Image Segmentation Model.

#### inputs()

The input parameters of this TrainingJob.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationInputs](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationInputs)




#### metadata()

The metadata information.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationMetadata](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationMetadata)




#### inputs(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_image_segmentation.AutoMlImageSegmentationInputs](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationInputs_ )

#### metadata(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_image_segmentation.AutoMlImageSegmentationMetadata](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationMetadata_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

#### model_type()

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationInputs.ModelType](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationInputs.ModelType)




#### budget_milli_node_hours()

The training budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The actual metadata.costMilliNodeHours will be equal or less than this value. If further model training ceases to provide any improvements, it will stop without using the full budget and the metadata.successfulStopReason will be `model-converged`. Note, node_hour = actual_hour * number_of_nodes_involved. Or actaul_wall_clock_hours = train_budget_milli_node_hours / (number_of_nodes_involved * 1000) For modelType `cloud-high-accuracy-1`(default), the budget must be between 20,000 and 2,000,000 milli node hours, inclusive. The default value is 192,000 which represents one day in wall time (1000 milli * 24 hours * 8 nodes).

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### base_model_id()

The ID of the `base` model. If it is specified, the new model will be trained based on the `base` model. Otherwise, the new model will be trained from scratch. The `base` model must be in the same Project and Location as the new Model to train, and have the same modelType.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### _class_ ModelType(value)

Bases: [`proto.enums.Enum`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.enums.Enum)

Values:
    
    
    MODEL_TYPE_UNSPECIFIED (0):
    
        Should not be set.
    
    CLOUD_HIGH_ACCURACY_1 (1):
    
        A model to be used via prediction calls to
        uCAIP API. Expected to have a higher latency,
        but should also have a higher prediction quality
        than other models.
    
    CLOUD_LOW_ACCURACY_1 (2):
    
        A model to be used via prediction calls to
        uCAIP API. Expected to have a lower latency but
        relatively lower prediction quality.
    
    MOBILE_TF_LOW_LATENCY_1 (3):
    
        A model that, in addition to being available
        within Google Cloud, can also be exported (see
        ModelService.ExportModel) as TensorFlow model
        and used on a mobile or edge device afterwards.
        Expected to have low latency, but may have lower
        prediction quality than other mobile models.
    

#### CLOUD_HIGH_ACCURACY_1(_=_ )

#### CLOUD_LOW_ACCURACY_1(_=_ )

#### MOBILE_TF_LOW_LATENCY_1(_=_ )

#### MODEL_TYPE_UNSPECIFIED(_=_ )

#### base_model_id(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### budget_milli_node_hours(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

#### model_type(_: [ModelType](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationInputs.ModelType_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

#### cost_milli_node_hours()

The actual training cost of creating this model, expressed in milli node hours, i.e. 1,000 value in this field means 1 node hour. Guaranteed to not exceed inputs.budgetMilliNodeHours.

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### successful_stop_reason()

For successful job completions, this is the reason why the job has finished.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationMetadata.SuccessfulStopReason](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationMetadata.SuccessfulStopReason)




#### _class_ SuccessfulStopReason(value)

Bases: [`proto.enums.Enum`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.enums.Enum)

Values:
    
    
    SUCCESSFUL_STOP_REASON_UNSPECIFIED (0):
    
        Should not be set.
    
    BUDGET_REACHED (1):
    
        The inputs.budgetMilliNodeHours had been
        reached.
    
    MODEL_CONVERGED (2):
    
        Further training of the Model ceased to
        increase its quality, since it already has
        converged.
    

#### BUDGET_REACHED(_=_ )

#### MODEL_CONVERGED(_=_ )

#### SUCCESSFUL_STOP_REASON_UNSPECIFIED(_=_ )

#### cost_milli_node_hours(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

#### successful_stop_reason(_: [SuccessfulStopReason](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlImageSegmentationMetadata.SuccessfulStopReason_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTables(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

A TrainingJob that trains and uploads an AutoML Tables Model.

#### inputs()

The input parameters of this TrainingJob.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs)




#### metadata()

The metadata information.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesMetadata](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesMetadata)




#### inputs(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_tables.AutoMlTablesInputs](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs_ )

#### metadata(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_tables.AutoMlTablesMetadata](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesMetadata_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

This message has [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

#### optimization_objective_recall_value()

Required when optimization_objective is “maximize-precision-at-recall”. Must be between 0 and 1, inclusive.

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `additional_optimization_objective_config`.

  * **Type**

[float](https://docs.python.org/3/builtins/functions.html#float)




#### optimization_objective_precision_value()

Required when optimization_objective is “maximize-recall-at-precision”. Must be between 0 and 1, inclusive.

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `additional_optimization_objective_config`.

  * **Type**

[float](https://docs.python.org/3/builtins/functions.html#float)




#### prediction_type()

The type of prediction the Model is to produce. “classification” - Predict one out of multiple target values is picked for each row.

> “regression” - Predict a value based on its

relation to other values. This type is available only to columns that contain semantically numeric values, i.e. integers or floating point number, even if stored as e.g. strings.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### target_column()

The column name of the target column that the model is to predict.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### transformations()

Each transformation will apply transform function to given input column. And the result will be used for training. When creating transformation for BigQuery Struct column, the column should be flattened using “.” as the delimiter.

  * **Type**

MutableSequence[[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation)]




#### optimization_objective()

Objective function the model is optimizing towards. The training process creates a model that maximizes/minimizes the value of the objective function over the validation set.

The supported optimization objectives depend on the prediction type. If the field is not set, a default objective function is used.

classification (binary):

> “maximize-au-roc” (default) - Maximize the

area under the receiver operating characteristic (ROC) curve. “minimize-log-loss” - Minimize log loss.

> “maximize-au-prc” - Maximize the area under

the precision-recall curve. “maximize-precision-at-recall” - Maximize precision for a specified recall value. “maximize-recall-at-precision” - Maximize recall for a specified precision value.

classification (multi-class):

> “minimize-log-loss” (default) - Minimize log

loss.

regression:

> “minimize-rmse” (default) - Minimize

root-mean-squared error (RMSE). “minimize-mae”

  * Minimize mean-absolute error (MAE). “minimize-rmsle” - Minimize root-mean-squared log error (RMSLE).

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### train_budget_milli_node_hours()

Required. The train budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour.

The training cost of the model will not exceed this budget. The final cost will be attempted to be close to the budget, though may end up being (even) noticeably smaller - at the backend’s discretion. This especially may happen when further model training ceases to provide any improvements.

If the budget is set to a value known to be insufficient to train a model for the given dataset, the training won’t be attempted and will error.

The train budget must be between 1,000 and 72,000 milli node hours, inclusive.

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### disable_early_stopping()

Use the entire training budget. This disables the early stopping feature. By default, the early stopping feature is enabled, which means that AutoML Tables might stop training before the entire training budget has been used.

  * **Type**

[bool](https://docs.python.org/3/builtins/functions.html#bool)




#### weight_column_name()

Column name that should be used as the weight column. Higher values in this column give more importance to the row during model training. The column must have numeric values between 0 and 10000 inclusively; 0 means the row is ignored for training. If weight column field is not set, then all rows are assumed to have equal weight of 1.

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### export_evaluated_data_items_config()

Configuration for exporting test set predictions to a BigQuery table. If this configuration is absent, then the export is not performed.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.ExportEvaluatedDataItemsConfig](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.ExportEvaluatedDataItemsConfig)




#### additional_experiments()

Additional experiment flags for the Tables training pipeline.

  * **Type**

MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]




#### _class_ Transformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

This message has [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

#### auto()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.AutoTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.AutoTransformation)




#### numeric()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.NumericTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.NumericTransformation)




#### categorical()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.CategoricalTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.CategoricalTransformation)




#### timestamp()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.TimestampTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.TimestampTransformation)




#### text()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.TextTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.TextTransformation)




#### repeated_numeric()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.NumericArrayTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.NumericArrayTransformation)




#### repeated_categorical()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.CategoricalArrayTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.CategoricalArrayTransformation)




#### repeated_text()

This field is a member of [oneof](https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields) `transformation_detail`.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.TextArrayTransformation](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.TextArrayTransformation)




#### _class_ AutoTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Training pipeline will infer the proper transformation based on the statistic of dataset.

#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### _class_ CategoricalArrayTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Treats the column as categorical array and performs following transformation functions.

  * For each element in the array, convert the category name to a dictionary lookup index and generate an embedding for each index. Combine the embedding of all elements into a single embedding using the mean.

  * Empty arrays treated as an embedding of zeroes.




#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### _class_ CategoricalTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Training pipeline will perform following transformation functions.

  * The categorical string as is–no change to case, punctuation, spelling, tense, and so on.

  * Convert the category name to a dictionary lookup index and generate an embedding for each index.

  * Categories that appear less than 5 times in the training dataset are treated as the “unknown” category. The “unknown” category gets its own special lookup index and resulting embedding.




#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### _class_ NumericArrayTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Treats the column as numerical array and performs following transformation functions.

  * All transformations for Numerical types applied to the average of the all elements.

  * The average of empty arrays is treated as zero.




#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### invalid_values_allowed()

If invalid values is allowed, the training pipeline will create a boolean feature that indicated whether the value is valid. Otherwise, the training pipeline will discard the input row from trainining data.

  * **Type**

[bool](https://docs.python.org/3/builtins/functions.html#bool)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### invalid_values_allowed(_: [bool](<https://docs.python.org/3/builtins/functions.html#bool>_ )

#### _class_ NumericTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Training pipeline will perform following transformation functions.

  * The value converted to float32.

  * The z_score of the value.

  * log(value+1) when the value is greater than or equal to 0. Otherwise, this transformation is not applied and the value is considered a missing value.

  * z_score of log(value+1) when the value is greater than or equal to

  * Otherwise, this transformation is not applied and the value is considered a missing value.

  * A boolean value that indicates whether the value is valid.




#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### invalid_values_allowed()

If invalid values is allowed, the training pipeline will create a boolean feature that indicated whether the value is valid. Otherwise, the training pipeline will discard the input row from trainining data.

  * **Type**

[bool](https://docs.python.org/3/builtins/functions.html#bool)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### invalid_values_allowed(_: [bool](<https://docs.python.org/3/builtins/functions.html#bool>_ )

#### _class_ TextArrayTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Treats the column as text array and performs following transformation functions.

  * Concatenate all text values in the array into a single text value using a space (” “) as a delimiter, and then treat the result as a single text value. Apply the transformations for Text columns.

  * Empty arrays treated as an empty text.




#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### _class_ TextTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Training pipeline will perform following transformation functions.

  * The text as is–no change to case, punctuation, spelling, tense, and so on.

  * Tokenize text to words. Convert each words to a dictionary lookup index and generate an embedding for each index. Combine the embedding of all elements into a single embedding using the mean.

  * Tokenization is based on unicode script boundaries.

  * Missing values get their own lookup index and resulting embedding.

  * Stop-words receive no special treatment and are not removed.




#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### _class_ TimestampTransformation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Training pipeline will perform following transformation functions.

  * Apply the transformation functions for Numerical columns.

  * Determine the year, month, day,and weekday. Treat each value from the

  * timestamp as a Categorical column.

  * Invalid numerical values (for example, values that fall outside of a typical timestamp range, or are extreme values) receive no special treatment and are not removed.




#### column_name()

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### time_format()

The format in which that time field is expressed. The time_format must either be one of:

  * `unix-seconds`

  * `unix-milliseconds`

  * `unix-microseconds`

  * `unix-nanoseconds` (for respectively number of seconds, milliseconds, microseconds and nanoseconds since start of the Unix epoch); or be written in `strftime` syntax. If time_format is not set, then the default format is RFC 3339 `date-time` format, where `time-offset` = `"Z"` (e.g. 1985-04-12T23:20:50.52Z)

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### invalid_values_allowed()

If invalid values is allowed, the training pipeline will create a boolean feature that indicated whether the value is valid. Otherwise, the training pipeline will discard the input row from trainining data.

  * **Type**

[bool](https://docs.python.org/3/builtins/functions.html#bool)




#### column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### invalid_values_allowed(_: [bool](<https://docs.python.org/3/builtins/functions.html#bool>_ )

#### time_format(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### auto(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_tables.AutoMlTablesInputs.Transformation.AutoTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.AutoTransformation_ )

#### categorical(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_tables.AutoMlTablesInputs.Transformation.CategoricalTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.CategoricalTransformation_ )

#### numeric(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_tables.AutoMlTablesInputs.Transformation.NumericTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.NumericTransformation_ )

#### repeated_categorical(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_tables.AutoMlTablesInputs.Transformation.CategoricalArrayTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.CategoricalArrayTransformation_ )

#### repeated_numeric(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_tables.AutoMlTablesInputs.Transformation.NumericArrayTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.NumericArrayTransformation_ )

#### repeated_text(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_tables.AutoMlTablesInputs.Transformation.TextArrayTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.TextArrayTransformation_ )

#### text(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_tables.AutoMlTablesInputs.Transformation.TextTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.TextTransformation_ )

#### timestamp(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_tables.AutoMlTablesInputs.Transformation.TimestampTransformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation.TimestampTransformation_ )

#### additional_experiments(_: MutableSequence[[str](https://docs.python.org/3/builtins/stdtypes.html#str)_ )

#### disable_early_stopping(_: [bool](<https://docs.python.org/3/builtins/functions.html#bool>_ )

#### export_evaluated_data_items_config(_: gcastd_export_evaluated_data_items_config.ExportEvaluatedDataItemsConfi_ )

#### optimization_objective(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### optimization_objective_precision_value(_: [float](<https://docs.python.org/3/builtins/functions.html#float>_ )

#### optimization_objective_recall_value(_: [float](<https://docs.python.org/3/builtins/functions.html#float>_ )

#### prediction_type(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### target_column(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### train_budget_milli_node_hours(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

#### transformations(_: MutableSequence[[Transformation](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesInputs.Transformation)_ )

#### weight_column_name(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTablesMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Model metadata specific to AutoML Tables.

#### train_cost_milli_node_hours()

Output only. The actual training cost of the model, expressed in milli node hours, i.e. 1,000 value in this field means 1 node hour. Guaranteed to not exceed the train budget.

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### train_cost_milli_node_hours(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextClassification(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

A TrainingJob that trains and uploads an AutoML Text Classification Model.

#### inputs()

The input parameters of this TrainingJob.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextClassificationInputs](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextClassificationInputs)




#### inputs(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_text_classification.AutoMlTextClassificationInputs](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextClassificationInputs_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextClassificationInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

#### multi_label()

  * **Type**

[bool](https://docs.python.org/3/builtins/functions.html#bool)




#### multi_label(_: [bool](<https://docs.python.org/3/builtins/functions.html#bool>_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextExtraction(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

A TrainingJob that trains and uploads an AutoML Text Extraction Model.

#### inputs()

The input parameters of this TrainingJob.

  * **Type**

google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextExtractionInputs




#### inputs(_: google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_text_extraction.AutoMlTextExtractionInput_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextExtractionInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextSentiment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

A TrainingJob that trains and uploads an AutoML Text Sentiment Model.

#### inputs()

The input parameters of this TrainingJob.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextSentimentInputs](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextSentimentInputs)




#### inputs(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_text_sentiment.AutoMlTextSentimentInputs](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextSentimentInputs_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlTextSentimentInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

#### sentiment_max()

A sentiment is expressed as an integer ordinal, where higher value means a more positive sentiment. The range of sentiments that will be used is between 0 and sentimentMax (inclusive on both ends), and all the values in the range must be represented in the dataset before a model can be created. Only the Annotations with this sentimentMax will be used for training. sentimentMax value must be between 1 and 10 (inclusive).

  * **Type**

[int](https://docs.python.org/3/builtins/functions.html#int)




#### sentiment_max(_: [int](<https://docs.python.org/3/builtins/functions.html#int>_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoActionRecognition(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

A TrainingJob that trains and uploads an AutoML Video Action Recognition Model.

#### inputs()

The input parameters of this TrainingJob.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoActionRecognitionInputs](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoActionRecognitionInputs)




#### inputs(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_video_action_recognition.AutoMlVideoActionRecognitionInputs](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoActionRecognitionInputs_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoActionRecognitionInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

#### model_type()

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoActionRecognitionInputs.ModelType](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoActionRecognitionInputs.ModelType)




#### _class_ ModelType(value)

Bases: [`proto.enums.Enum`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.enums.Enum)

Values:
    
    
    MODEL_TYPE_UNSPECIFIED (0):
    
        Should not be set.
    
    CLOUD (1):
    
        A model best tailored to be used within
        Google Cloud, and which c annot be exported.
        Default.
    
    MOBILE_VERSATILE_1 (2):
    
        A model that, in addition to being available
        within Google Cloud, can also be exported (see
        ModelService.ExportModel) as a TensorFlow or
        TensorFlow Lite model and used on a mobile or
        edge device afterwards.
    
    MOBILE_JETSON_VERSATILE_1 (3):
    
        A model that, in addition to being available
        within Google Cloud, can also be exported (see
        ModelService.ExportModel) to a Jetson device
        afterwards.
    
    MOBILE_CORAL_VERSATILE_1 (4):
    
        A model that, in addition to being available
        within Google Cloud, can also be exported (see
        ModelService.ExportModel) as a TensorFlow or
        TensorFlow Lite model and used on a Coral device
        afterwards.
    

#### CLOUD(_=_ )

#### MOBILE_CORAL_VERSATILE_1(_=_ )

#### MOBILE_JETSON_VERSATILE_1(_=_ )

#### MOBILE_VERSATILE_1(_=_ )

#### MODEL_TYPE_UNSPECIFIED(_=_ )

#### model_type(_: [ModelType](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoActionRecognitionInputs.ModelType_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoClassification(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

A TrainingJob that trains and uploads an AutoML Video Classification Model.

#### inputs()

The input parameters of this TrainingJob.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoClassificationInputs](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoClassificationInputs)




#### inputs(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_video_classification.AutoMlVideoClassificationInputs](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoClassificationInputs_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoClassificationInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

#### model_type()

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoClassificationInputs.ModelType](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoClassificationInputs.ModelType)




#### _class_ ModelType(value)

Bases: [`proto.enums.Enum`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.enums.Enum)

Values:
    
    
    MODEL_TYPE_UNSPECIFIED (0):
    
        Should not be set.
    
    CLOUD (1):
    
        A model best tailored to be used within
        Google Cloud, and which cannot be exported.
        Default.
    
    MOBILE_VERSATILE_1 (2):
    
        A model that, in addition to being available
        within Google Cloud, can also be exported (see
        ModelService.ExportModel) as a TensorFlow or
        TensorFlow Lite model and used on a mobile or
        edge device afterwards.
    
    MOBILE_JETSON_VERSATILE_1 (3):
    
        A model that, in addition to being available
        within Google Cloud, can also be exported (see
        ModelService.ExportModel) to a Jetson device
        afterwards.
    

#### CLOUD(_=_ )

#### MOBILE_JETSON_VERSATILE_1(_=_ )

#### MOBILE_VERSATILE_1(_=_ )

#### MODEL_TYPE_UNSPECIFIED(_=_ )

#### model_type(_: [ModelType](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoClassificationInputs.ModelType_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoObjectTracking(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

A TrainingJob that trains and uploads an AutoML Video ObjectTracking Model.

#### inputs()

The input parameters of this TrainingJob.

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoObjectTrackingInputs](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoObjectTrackingInputs)




#### inputs(_: [google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.automl_video_object_tracking.AutoMlVideoObjectTrackingInputs](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoObjectTrackingInputs_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoObjectTrackingInputs(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

#### model_type()

  * **Type**

[google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoObjectTrackingInputs.ModelType](https://docs.cloud.google.com/python/docs/reference/aiplatform/definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoObjectTrackingInputs.ModelType)




#### _class_ ModelType(value)

Bases: [`proto.enums.Enum`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.enums.Enum)

Values:
    
    
    MODEL_TYPE_UNSPECIFIED (0):
    
        Should not be set.
    
    CLOUD (1):
    
        A model best tailored to be used within
        Google Cloud, and which c annot be exported.
        Default.
    
    MOBILE_VERSATILE_1 (2):
    
        A model that, in addition to being available
        within Google Cloud, can also be exported (see
        ModelService.ExportModel) as a TensorFlow or
        TensorFlow Lite model and used on a mobile or
        edge device afterwards.
    
    MOBILE_CORAL_VERSATILE_1 (3):
    
        A versatile model that is meant to be
        exported (see ModelService.ExportModel) and used
        on a Google Coral device.
    
    MOBILE_CORAL_LOW_LATENCY_1 (4):
    
        A model that trades off quality for low
        latency, to be exported (see
        ModelService.ExportModel) and used on a Google
        Coral device.
    
    MOBILE_JETSON_VERSATILE_1 (5):
    
        A versatile model that is meant to be
        exported (see ModelService.ExportModel) and used
        on an NVIDIA Jetson device.
    
    MOBILE_JETSON_LOW_LATENCY_1 (6):
    
        A model that trades off quality for low
        latency, to be exported (see
        ModelService.ExportModel) and used on an NVIDIA
        Jetson device.
    

#### CLOUD(_=_ )

#### MOBILE_CORAL_LOW_LATENCY_1(_=_ )

#### MOBILE_CORAL_VERSATILE_1(_=_ )

#### MOBILE_JETSON_LOW_LATENCY_1(_=_ )

#### MOBILE_JETSON_VERSATILE_1(_=_ )

#### MOBILE_VERSATILE_1(_=_ )

#### MODEL_TYPE_UNSPECIFIED(_=_ )

#### model_type(_: [ModelType](../definition_v1beta1/types_.md#google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.AutoMlVideoObjectTrackingInputs.ModelType_ )

### _class_ google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1.types.ExportEvaluatedDataItemsConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bases: [`proto.message.Message`](https://proto-plus-python.readthedocs.io/en/latest/reference/message.html#proto.message.Message)

Configuration for exporting test set predictions to a BigQuery table.

#### destination_bigquery_uri()

URI of desired destination BigQuery table. Expected format: bq://<project_id>:<dataset_id>:

If not specified, then results are exported to the following auto-created BigQuery table: <project_id>:export_evaluated_examples_<model_name>_<yyyy_MM_dd’T’HH_mm_ss_SSS’Z’>.evaluated_examples

  * **Type**

[str](https://docs.python.org/3/builtins/stdtypes.html#str)




#### override_existing_table()

If true and an export destination is specified, then the contents of the destination are overwritten. Otherwise, if the export destination already exists, then the export operation fails.

  * **Type**

[bool](https://docs.python.org/3/builtins/functions.html#bool)




#### destination_bigquery_uri(_: [str](<https://docs.python.org/3/builtins/stdtypes.html#str>_ )

#### override_existing_table(_: [bool](<https://docs.python.org/3/builtins/functions.html#bool>_ )

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
