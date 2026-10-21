---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/vertex_ai_text_embeddings/
title: Generate text embeddings by using the Vertex AI API \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:48.481522+00:00
---

# Generate text embeddings by using the Vertex AI API  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/vertex_ai_text_embeddings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Generate text embeddings by using the Vertex AI API Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/data_preprocessing/vertex_ai_text_embeddings.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/data_preprocessing/vertex_ai_text_embeddings.ipynb) Text embeddings are a way to represent text as numerical vectors. This process lets computers understand and process text data, which is essential for many natural language processing (NLP) tasks. The following NLP tasks use embeddings:

  * **Semantic search:** Find documents or passages that are relevant to a query when the query doesn't use the exact same words as the documents.
  * **Text classification:** Categorize text data into different classes, such as spam and not spam, or positive sentiment and negative sentiment.
  * **Machine translation:** Translate text from one language to another and preserve the meaning.
  * **Text summarization:** Create shorter summaries of text.

This notebook uses the Vertex AI text-embeddings API to generate text embeddings that use Google’s large generative artificial intelligence (AI) models. To generate text embeddings by using the Vertex AI text-embeddings API, use `MLTransform` with the `VertexAITextEmbeddings` class to specify the model configuration. For more information, see [Get text embeddings](https://cloud.google.com/vertex-ai/docs/generative-ai/embeddings/get-text-embeddings) in the Vertex AI documentation.  For more information about using `MLTransform`, see [Preprocess data with MLTransform](https://beam.apache.org/documentation/ml/preprocess-data/) in the Apache Beam documentation.

## Requirements

To use the Vertex AI text-embeddings API, complete the following prerequisites:

  * Install the `google-cloud-aiplatform` Python package.
  * Do one of the following tasks: 
    * Configure credentials for your Google Cloud project. For more information, see [Google Auth Library for Python](https://googleapis.dev/python/google-auth/latest/reference/google.auth.html#module-google.auth).
    * Store the path to a service account JSON file by using the [GOOGLE_APPLICATION_CREDENTIALS](https://cloud.google.com/docs/authentication/application-default-credentials#GAC) environment variable.

To use your Google Cloud account, authenticate this notebook.
    
    
    from google.colab import auth
    auth.authenticate_user()
    
    # Replace <PROJECT_ID> with a valid Google Cloud project ID.
    project = '<PROJECT_ID>' # @param {type:'string'}
    

## Install dependencies

Install Apache Beam and the dependencies required for the Vertex AI text-embeddings API.
    
    
     pip install apache_beam[interactive,gcp]>=2.53.0 --quiet
    
    
    import tempfile
    import apache_beam as beam
    from apache_beam.ml.transforms.base import MLTransform
    from apache_beam.ml.transforms.embeddings.vertex_ai import VertexAITextEmbeddings
    

## Transform the data

`MLTransform` is a `PTransform` that you can use for data preparation, including generating text embeddings.

### Use MLTransform in write mode

In `write` mode, `MLTransform` saves the transforms and their attributes to an artifact location. Then, when you run `MLTransform` in `read` mode, these transforms are used. This process ensures that you're applying the same preprocessing steps when you train your model and when you serve the model in production or test its accuracy.

### Get the data

`MLTransform` processes dictionaries that include column names and their associated text data. To generate embeddings for specific columns, specify these column names in the `columns` argument of `VertexAITextEmbeddings`. This transform uses the the Vertex AI text-embeddings API for online predictions to generate an embeddings vector for each sentence.
    
    
    artifact_location = tempfile.mkdtemp(prefix='vertex_ai')
    
    # Use the latest text embedding model from the Vertex AI text-embeddings API documentation.
    # https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-embeddings
    text_embedding_model_name = 'textembedding-gecko@latest'
    
    # Generate text embeddings on the sentences.
    content = [
        {
            'x' : 'I would like embeddings for this text'
        },
        {
            'x' : 'Hello world'
        },
        {
            'x': 'The Dog is running in the park.'
        }
      ]
    
    # helper function that returns a dict containing only first
    # ten elements of generated embeddings
    def truncate_embeddings(d):
      for key in d.keys():
        d[key] = d[key][:10]
      return d
    
    
    
    embedding_transform = VertexAITextEmbeddings(
            model_name=text_embedding_model_name, columns=['x'], project=project)
    
    with beam.Pipeline() as pipeline:
      data_pcoll = (
          pipeline
          | "CreateData" >> beam.Create(content))
      transformed_pcoll = (
          data_pcoll
          | "MLTransform" >> MLTransform(write_artifact_location=artifact_location).with_transform(embedding_transform))
    
      # Show only the first ten elements of the embeddings to prevent clutter in the output.
      transformed_pcoll | beam.Map(truncate_embeddings) | 'LogOutput' >> beam.Map(print)
    
      transformed_pcoll | "PrintEmbeddingShape" >> beam.Map(lambda x: print(f"Embedding shape: {len(x['x'])}"))
    
    
    
    {'x': [0.041293490678071976, -0.010302993468940258, -0.048611514270305634, -0.01360565796494484, 0.06441926211118698, 0.022573700174689293, 0.016446372494101524, -0.033894773572683334, 0.004581860266625881, 0.060710687190294266]}
    Embedding shape: 10
    {'x': [0.05889148637652397, -0.0046180677600204945, -0.06738516688346863, -0.012708292342722416, 0.06461101770401001, 0.025648491457104683, 0.023468563333153725, -0.039828114211559296, -0.009968819096684456, 0.050098177045583725]}
    Embedding shape: 10
    {'x': [0.04683901369571686, -0.013076924718916416, -0.082594133913517, -0.01227626483887434, 0.00417641457170248, -0.024504298344254494, 0.04282262548804283, -0.0009824123699218035, -0.02860993705689907, 0.01609829254448414]}
    Embedding shape: 10
    

### Use MLTransform in read mode

In `read` mode, `MLTransform` uses the artifacts saved during `write` mode. In this example, the transform and its attributes are loaded from the saved artifacts. You don't need to specify artifacts again during `read` mode. In this way, `MLTransform` provides consistent preprocessing steps for training and inference workloads.
    
    
    test_content = [
        {
            'x': 'This is a test sentence'
        },
        {
            'x': 'The park is full of dogs'
        },
    ]
    
    with beam.Pipeline() as pipeline:
      data_pcoll = (
          pipeline
          | "CreateData" >> beam.Create(test_content))
      transformed_pcoll = (
          data_pcoll
          | "MLTransform" >> MLTransform(read_artifact_location=artifact_location))
    
      transformed_pcoll | beam.Map(truncate_embeddings) | 'LogOutput' >> beam.Map(print)
    
    
    
    {'x': [0.04782044142484665, -0.010078949853777885, -0.05793016776442528, -0.026060665026307106, 0.05756739526987076, 0.02292264811694622, 0.014818413183093071, -0.03718176111578941, -0.005486017093062401, 0.04709304869174957]}
    {'x': [0.042911216616630554, -0.007554919924587011, -0.08996245265007019, -0.02607591263949871, 0.0008614308317191899, -0.023671219125390053, 0.03999944031238556, -0.02983051724731922, -0.015057179145514965, 0.022963201627135277]}
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
