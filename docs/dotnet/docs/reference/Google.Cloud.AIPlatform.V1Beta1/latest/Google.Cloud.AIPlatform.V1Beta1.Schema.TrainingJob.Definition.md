---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition
title: Vertex AI v1beta1 API - Namespace Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:28.890166+00:00
---

# Vertex AI v1beta1 API - Namespace Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Namespace Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 

## Classes 

### [AutoMlForecasting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecasting)

A TrainingJob that trains and uploads an AutoML Forecasting Model.

### [AutoMlForecastingInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs)

### [AutoMlForecastingInputs.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types)

Container for nested types declared in the AutoMlForecastingInputs message type.

### [AutoMlForecastingInputs.Types.Granularity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types.Granularity)

A duration of time expressed in time granularity units.

### [AutoMlForecastingInputs.Types.Transformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types.Transformation)

### [AutoMlForecastingInputs.Types.Transformation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types.Transformation.Types)

Container for nested types declared in the Transformation message type.

### [AutoMlForecastingInputs.Types.Transformation.Types.AutoTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types.Transformation.Types.AutoTransformation)

Training pipeline will infer the proper transformation based on the statistic of dataset.

### [AutoMlForecastingInputs.Types.Transformation.Types.CategoricalTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types.Transformation.Types.CategoricalTransformation)

Training pipeline will perform following transformation functions.

  * The categorical string as is--no change to case, punctuation, spelling, tense, and so on.

  * Convert the category name to a dictionary lookup index and generate an embedding for each index.

  * Categories that appear less than 5 times in the training dataset are treated as the "unknown" category. The "unknown" category gets its own special lookup index and resulting embedding.




### [AutoMlForecastingInputs.Types.Transformation.Types.NumericTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types.Transformation.Types.NumericTransformation)

Training pipeline will perform following transformation functions.

  * The value converted to float32.

  * The z_score of the value.

  * log(value+1) when the value is greater than or equal to 0. Otherwise, this transformation is not applied and the value is considered a missing value.

  * z_score of log(value+1) when the value is greater than or equal to 0. Otherwise, this transformation is not applied and the value is considered a missing value.

  * A boolean value that indicates whether the value is valid.




### [AutoMlForecastingInputs.Types.Transformation.Types.TextTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types.Transformation.Types.TextTransformation)

Training pipeline will perform following transformation functions.

  * The text as is--no change to case, punctuation, spelling, tense, and so on.

  * Convert the category name to a dictionary lookup index and generate an embedding for each index.




### [AutoMlForecastingInputs.Types.Transformation.Types.TimestampTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types.Transformation.Types.TimestampTransformation)

Training pipeline will perform following transformation functions.

  * Apply the transformation functions for Numerical columns.

  * Determine the year, month, day,and weekday. Treat each value from the timestamp as a Categorical column.

  * Invalid numerical values (for example, values that fall outside of a typical timestamp range, or are extreme values) receive no special treatment and are not removed.




### [AutoMlForecastingMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingMetadata)

Model metadata specific to AutoML Forecasting.

### [AutoMlImageClassification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageClassification)

A TrainingJob that trains and uploads an AutoML Image Classification Model.

### [AutoMlImageClassificationInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageClassificationInputs)

### [AutoMlImageClassificationInputs.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageClassificationInputs.Types)

Container for nested types declared in the AutoMlImageClassificationInputs message type.

### [AutoMlImageClassificationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageClassificationMetadata)

### [AutoMlImageClassificationMetadata.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageClassificationMetadata.Types)

Container for nested types declared in the AutoMlImageClassificationMetadata message type.

### [AutoMlImageObjectDetection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetection)

A TrainingJob that trains and uploads an AutoML Image Object Detection Model.

### [AutoMlImageObjectDetectionInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs)

### [AutoMlImageObjectDetectionInputs.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs.Types)

Container for nested types declared in the AutoMlImageObjectDetectionInputs message type.

### [AutoMlImageObjectDetectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionMetadata)

### [AutoMlImageObjectDetectionMetadata.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionMetadata.Types)

Container for nested types declared in the AutoMlImageObjectDetectionMetadata message type.

### [AutoMlImageSegmentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageSegmentation)

A TrainingJob that trains and uploads an AutoML Image Segmentation Model.

### [AutoMlImageSegmentationInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageSegmentationInputs)

### [AutoMlImageSegmentationInputs.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageSegmentationInputs.Types)

Container for nested types declared in the AutoMlImageSegmentationInputs message type.

### [AutoMlImageSegmentationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageSegmentationMetadata)

### [AutoMlImageSegmentationMetadata.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageSegmentationMetadata.Types)

Container for nested types declared in the AutoMlImageSegmentationMetadata message type.

### [AutoMlTables](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTables)

A TrainingJob that trains and uploads an AutoML Tables Model.

### [AutoMlTablesInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs)

### [AutoMlTablesInputs.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types)

Container for nested types declared in the AutoMlTablesInputs message type.

### [AutoMlTablesInputs.Types.Transformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation)

### [AutoMlTablesInputs.Types.Transformation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types)

Container for nested types declared in the Transformation message type.

### [AutoMlTablesInputs.Types.Transformation.Types.AutoTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.AutoTransformation)

Training pipeline will infer the proper transformation based on the statistic of dataset.

### [AutoMlTablesInputs.Types.Transformation.Types.CategoricalArrayTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.CategoricalArrayTransformation)

Treats the column as categorical array and performs following transformation functions.

  * For each element in the array, convert the category name to a dictionary lookup index and generate an embedding for each index. Combine the embedding of all elements into a single embedding using the mean.
  * Empty arrays treated as an embedding of zeroes.



### [AutoMlTablesInputs.Types.Transformation.Types.CategoricalTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.CategoricalTransformation)

Training pipeline will perform following transformation functions.

  * The categorical string as is--no change to case, punctuation, spelling, tense, and so on.
  * Convert the category name to a dictionary lookup index and generate an embedding for each index.
  * Categories that appear less than 5 times in the training dataset are treated as the "unknown" category. The "unknown" category gets its own special lookup index and resulting embedding.



### [AutoMlTablesInputs.Types.Transformation.Types.NumericArrayTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.NumericArrayTransformation)

Treats the column as numerical array and performs following transformation functions.

  * All transformations for Numerical types applied to the average of the all elements.
  * The average of empty arrays is treated as zero.



### [AutoMlTablesInputs.Types.Transformation.Types.NumericTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.NumericTransformation)

Training pipeline will perform following transformation functions.

  * The value converted to float32.
  * The z_score of the value.
  * log(value+1) when the value is greater than or equal to 0. Otherwise, this transformation is not applied and the value is considered a missing value.
  * z_score of log(value+1) when the value is greater than or equal to 0. Otherwise, this transformation is not applied and the value is considered a missing value.
  * A boolean value that indicates whether the value is valid.



### [AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.TextArrayTransformation)

Treats the column as text array and performs following transformation functions.

  * Concatenate all text values in the array into a single text value using a space (" ") as a delimiter, and then treat the result as a single text value. Apply the transformations for Text columns.
  * Empty arrays treated as an empty text.



### [AutoMlTablesInputs.Types.Transformation.Types.TextTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.TextTransformation)

Training pipeline will perform following transformation functions.

  * The text as is--no change to case, punctuation, spelling, tense, and so on.
  * Tokenize text to words. Convert each words to a dictionary lookup index and generate an embedding for each index. Combine the embedding of all elements into a single embedding using the mean.
  * Tokenization is based on unicode script boundaries.
  * Missing values get their own lookup index and resulting embedding.
  * Stop-words receive no special treatment and are not removed.



### [AutoMlTablesInputs.Types.Transformation.Types.TimestampTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.Types.TimestampTransformation)

Training pipeline will perform following transformation functions.

  * Apply the transformation functions for Numerical columns.
  * Determine the year, month, day,and weekday. Treat each value from the
  * timestamp as a Categorical column.
  * Invalid numerical values (for example, values that fall outside of a typical timestamp range, or are extreme values) receive no special treatment and are not removed.



### [AutoMlTablesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesMetadata)

Model metadata specific to AutoML Tables.

### [AutoMlTextClassification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTextClassification)

A TrainingJob that trains and uploads an AutoML Text Classification Model.

### [AutoMlTextClassificationInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTextClassificationInputs)

### [AutoMlTextExtraction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTextExtraction)

A TrainingJob that trains and uploads an AutoML Text Extraction Model.

### [AutoMlTextExtractionInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTextExtractionInputs)

### [AutoMlTextSentiment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTextSentiment)

A TrainingJob that trains and uploads an AutoML Text Sentiment Model.

### [AutoMlTextSentimentInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTextSentimentInputs)

### [AutoMlVideoActionRecognition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlVideoActionRecognition)

A TrainingJob that trains and uploads an AutoML Video Action Recognition Model.

### [AutoMlVideoActionRecognitionInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlVideoActionRecognitionInputs)

### [AutoMlVideoActionRecognitionInputs.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlVideoActionRecognitionInputs.Types)

Container for nested types declared in the AutoMlVideoActionRecognitionInputs message type.

### [AutoMlVideoClassification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlVideoClassification)

A TrainingJob that trains and uploads an AutoML Video Classification Model.

### [AutoMlVideoClassificationInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlVideoClassificationInputs)

### [AutoMlVideoClassificationInputs.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlVideoClassificationInputs.Types)

Container for nested types declared in the AutoMlVideoClassificationInputs message type.

### [AutoMlVideoObjectTracking](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlVideoObjectTracking)

A TrainingJob that trains and uploads an AutoML Video ObjectTracking Model.

### [AutoMlVideoObjectTrackingInputs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlVideoObjectTrackingInputs)

### [AutoMlVideoObjectTrackingInputs.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlVideoObjectTrackingInputs.Types)

Container for nested types declared in the AutoMlVideoObjectTrackingInputs message type.

### [ExportEvaluatedDataItemsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.ExportEvaluatedDataItemsConfig)

Configuration for exporting test set predictions to a BigQuery table.

## Enums 

### [AutoMlForecastingInputs.Types.Transformation.TransformationDetailOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlForecastingInputs.Types.Transformation.TransformationDetailOneofCase)

Enum of possible cases for the "transformation_detail" oneof.

### [AutoMlImageClassificationInputs.Types.ModelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageClassificationInputs.Types.ModelType)

### [AutoMlImageClassificationMetadata.Types.SuccessfulStopReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageClassificationMetadata.Types.SuccessfulStopReason)

### [AutoMlImageObjectDetectionInputs.Types.ModelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs.Types.ModelType)

### [AutoMlImageObjectDetectionMetadata.Types.SuccessfulStopReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionMetadata.Types.SuccessfulStopReason)

### [AutoMlImageSegmentationInputs.Types.ModelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageSegmentationInputs.Types.ModelType)

### [AutoMlImageSegmentationMetadata.Types.SuccessfulStopReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageSegmentationMetadata.Types.SuccessfulStopReason)

### [AutoMlTablesInputs.AdditionalOptimizationObjectiveConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.AdditionalOptimizationObjectiveConfigOneofCase)

Enum of possible cases for the "additional_optimization_objective_config" oneof.

### [AutoMlTablesInputs.Types.Transformation.TransformationDetailOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlTablesInputs.Types.Transformation.TransformationDetailOneofCase)

Enum of possible cases for the "transformation_detail" oneof.

### [AutoMlVideoActionRecognitionInputs.Types.ModelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlVideoActionRecognitionInputs.Types.ModelType)

### [AutoMlVideoClassificationInputs.Types.ModelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlVideoClassificationInputs.Types.ModelType)

### [AutoMlVideoObjectTrackingInputs.Types.ModelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlVideoObjectTrackingInputs.Types.ModelType)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
