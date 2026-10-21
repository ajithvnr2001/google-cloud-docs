---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/medlm/medlm-prompts/
title: Create MedLM prompts \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:01:04.804835+00:00
---

# Create MedLM prompts  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/medlm/medlm-prompts/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Create MedLM prompts Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** MedLM is deprecated. Access to MedLM will no longer be available on or after September 29, 2025. 

The available MedLM models, MedLM-medium and MedLM-large, are foundation models for medical question answering and summarization. You can access the models using the Vertex AI MedLM API. This page gives you an overview of the available MedLM models, the APIs you use to interact with the models, and ways to customize their behaviors.

## Before you begin

  * See [MedLM models overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/medlm/overview) for information including customer responsibilities, regulatory information, and [Responsible AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/responsible-ai) best practices.
  * See the MedLM model card for model details, such as MedLM's intended use, data overview, and safety information. Click the following link to download a PDF version of the MedLM model card:

[Download the MedLM model card](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/medlm/MedLM-model-card.pdf)




## Prompt design

To interact with the MedLM models, you send natural language instructions, also called prompts, that tell the model what you want it to generate. However, LLMs can sometimes behave in unpredictable ways. Prompt design is an iterative process of trial and error that takes time and practice to become proficient in. To learn about general prompt design strategies, see [Introduction to prompt design](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/introduction-prompt-design). For task-specific prompt design guidance for text, see [Overview of prompting strategies](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies).

## Use cases

  * **Summarization** : Create a shorter version of a document that incorporates pertinent information from the original text. For example, you might want to summarize a medical note describing an outpatient visit, and to extract relevant information for specific data points.
  * **Question answering** : Provide answers to questions in text. For example, you might want to ask a general medical question to generate answers from the knowledge base.



## Supported models

  * `medlm-medium`
  * `medlm-large`



## Get started

The following samples show how to get started with the MedLM API using the following interfaces:

  * The Vertex AI REST API
  * Vertex AI SDK for Python
  * Vertex AI Studio



### REST

**Caution:** The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased information and should be reviewed. All summaries or answers should be considered draft and not final.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * `MEDLM_MODEL`: The MedLM model, either `medlm-medium` or `medlm-large`.



HTTP method and URL: 
    
    
    POST https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict

Request JSON body: 
    
    
    {
      "instances": [
        {
          "content": "Question: What causes you to get ringworm?"
        }
      ],
      "parameters": {
        "temperature": 0,
        "maxOutputTokens": 256,
        "topK": 40,
        "topP": 0.95
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "instances": [
        {
          "content": "Question: What causes you to get ringworm?"
        }
      ],
      "parameters": {
        "temperature": 0,
        "maxOutputTokens": 256,
        "topK": 40,
        "topP": 0.95
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "instances": [
        {
          "content": "Question: What causes you to get ringworm?"
        }
      ],
      "parameters": {
        "temperature": 0,
        "maxOutputTokens": 256,
        "topK": 40,
        "topP": 0.95
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict" | Select-Object -Expand Content

### Python (Colaboratory)

Run the following Python code in [Colaboratory](https://colab.research.google.com/).
    
    
    !pip install google-cloud-aiplatform
    
    # The following restarts the runtime.
    import IPython
    
    app = IPython.Application.instance()
    # Note that this will result in a pop-up telling you that the session has
    # crashed for an unknown reason. This can be safely ignored and you can continue
    # with the following cells after getting this message.
    app.kernel.do_shutdown(True)

Run the following code in your Colaboratory notebook. Enter your Google Cloud project ID where indicated. To find your project ID, see [Locate the project ID](https://support.google.com/googleapi/answer/7014113).
    
    
    from google.colab import auth as google_auth
    import vertexai
    from vertexai.preview.language_models import TextGenerationModel
    
    google_auth.authenticate_user()
    
    # TODO: Replace with project ID from Cloud Console
    # (https://support.google.com/googleapi/answer/7014113)
    PROJECT_ID = 'my-project'
    
    # MedLM models are only available in us-central1.
    vertexai.init(project=PROJECT_ID, location='us-central1')
    
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 256,
        "temperature": 0.0,
        "top_k": 40,
        "top_p": 0.80,
    }
    
    model_instance = TextGenerationModel.from_pretrained("medlm-medium")
    response = model_instance.predict(
        "Question: What causes you to get ringworm?",
        **parameters
    )
    
    print(f"Response from Model: {response.text}")

### Vertex AI Studio

Use Vertex AI Studio to design, test, and customize your prompts sent to the MedLM API. Before using Vertex AI Studio for MedLM, see [Send text prompts to Gemini using Vertex AI Studio](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart) for prerequisites.

To test a MedLM prompt using Vertex AI Studio in the Google Cloud console, do following:

  1. In the Vertex AI section of the Google Cloud console, go to the Vertex AI Studio page. 

[Go to Vertex AI Studio](https://console.cloud.google.com/vertex-ai/generative/language)

  2. Click **Get started**.
  3. Click **Create prompt**.
  4. In the **Model** menu, select `MedLM-Medium` or `MedLM-Large`.
  5. In the **Prompt** field, enter your prompt.
  6. (Optional) You can adjust the **Temperature** and **Token limit** values to experiment with how they affect the response. We recommend using the default values. If you're unsure about which values to use, use the default values.
  7. Click **Submit** to generate a response.
  8. (Optional) To save a prompt, click **Save**.
  9. (Optional) To view the Python code or a `curl` command for your prompt, click **Get code**.



## Question answering prompts

The following sections contain question answering prompt samples. Each sample prompt includes the recommended model and parameter values.

### Long-form question answering

The following samples show how the MedLM API answers a long-form medical question formulated as a query.

### REST

**Caution:** The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased information and should be reviewed. All summaries or answers should be considered draft and not final.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * `MEDLM_MODEL`: The MedLM model, either `medlm-medium` or `medlm-large`.



HTTP method and URL: 
    
    
    POST https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict

Request JSON body: 
    
    
    {
      "instances": [
        {
          "content": "Question: What causes you to get ringworm?"
        }
      ],
      "parameters": {
        "temperature": 0,
        "maxOutputTokens": 256,
        "topK": 40,
        "topP": 0.95
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "instances": [
        {
          "content": "Question: What causes you to get ringworm?"
        }
      ],
      "parameters": {
        "temperature": 0,
        "maxOutputTokens": 256,
        "topK": 40,
        "topP": 0.95
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "instances": [
        {
          "content": "Question: What causes you to get ringworm?"
        }
      ],
      "parameters": {
        "temperature": 0,
        "maxOutputTokens": 256,
        "topK": 40,
        "topP": 0.95
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict" | Select-Object -Expand Content

**Caution:** The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased information and should be reviewed. All summaries or answers should be considered draft and not final.

### Multiple choice question answering

The following samples show how the MedLM API answers a multiple choice medical question. The prompt is the following:
    
    
    Instructions: This text contains multiple-choice questions about medical knowledge. Solve each question step-by-step, starting by summarizing the available information. Select a single option from the four choices provided as the final answer.
    
    Question 1: Which medication causes the maximum increase in prolactin level?
    (A) Risperidone
    (B) Clozapine
    (C) Olanzapine
    (D) Aripiprazole
    
    Explanation: To solve this question, let's refer to authoritative sources. Clozapine generally does not elevate prolactin levels. Atypicals like olanzapine and aripiprazole cause little to no elevation. Risperidone, on the other hand, is known to result in a sustained elevated prolactin level. Therefore, risperidone is likely to cause the maximum increase in prolactin level.
    
    Answer: (A)
    
    Question 2: What is the recommended age for routine screening mammography?
    (A) 20 years
    (B) 30 years
    (C) 40 years
    (D) 50 years
    
    Explanation: The age of routine screening may vary depending on the country. In the United States, according to the American Cancer Society, it is recommended to start routine screening mammography at 40 years of age. In Europe, it is typically closer to 50 years. For a patient based in the US, the best answer is 40 years.
    
    Answer: (C)
    
    Question 3: A 65-year-old male experiences severe back pain and paralysis in his left lower limb. Imaging studies show compression of nerve elements at the intervertebral foramen between vertebrae L5 and S1. Which structure is most likely causing this compression?
    (A) Anulus fibrosus
    (B) Nucleus pulposus
    (C) Posterior longitudinal ligament
    (D) Anterior longitudinal ligament
    
    Explanation: This man's symptoms and imaging findings are consistent with a herniated intervertebral disk. The soft, gelatinous "nucleus pulposus" is forced out through a weakened part of the disk, resulting in back pain and nerve root irritation. In this case, the impingement is resulting in paralysis, which should be considered a medical emergency. Overall, the structure that is causing the compression and symptoms is the nucleus pulposus.
    
    Answer: (B)
    
    Question 4: Which cells in the lungs are also known as APUD cells?
    (A) Dendritic cells
    (B) Type I pneumocytes
    (C) Type II pneumocytes
    (D) Neuroendocrine cells
    
    Explanation: Neuroendocrine cells, also known as Kultschitsky-type cells, Feyrter cells, and APUD cells, are found in the basal layer of the surface epithelium and in the bronchial glands.
    
    Answer: (D)
    
    Question 5: Which microorganism indicates remote contamination of water?
    (A) Streptococci
    (B) Staphylococci
    (C) Clostridium perfringens
    (D) Vibrio
    
    Explanation: The presence of Clostridium perfringens in water indicates remote contamination because it is a spore-forming bacterium that can survive in the environment for extended periods of time.
    
    Answer: (C)
    

### REST

**Caution:** The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased information and should be reviewed. All summaries or answers should be considered draft and not final.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * `MEDLM_MODEL`: The MedLM model, either `medlm-medium` or `medlm-large`.



HTTP method and URL: 
    
    
    POST https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict

Request JSON body: 
    
    
    {
      "instances": [
        {
          "content": "Instructions: The following are multiple choice questions about medical knowledge. Solve them in a step-by-step fashion, starting by summarizing the available information. Output a single option from the four options as the final answer. \n \nQuestion: Maximum increase in prolactin level is caused by: \n(A) Risperidone (B) Clozapine (C) Olanzapine (D) Aripiprazole \nExplanation: Let's solve this step-by-step, referring to authoritative sources as needed. Clozapine generally does not raise prolactin levels. Atypicals such as olanzapine and aripiprazole cause small if no elevation. Risperidone is known to result in a sustained elevated prolactin level. Therefore risperidone is likely to cause the maximum increase in prolactin level. \nAnswer: (A) \n \nQuestion: What is the age of routine screening mammography? \n(A) 20 years (B) 30 years (C) 40 years (D) 50 years \nExplanation: Let's solve this step-by-step, referring to authoritative sources as needed. The age of routine screening depends on the country you are interested in and varies widely. For the US, it is 40 years of age according to the American Cancer Society. In Europe, it is typically closer to 50 years. For a patient based in the US, the best answer is 40 years. \nAnswer: (C) \n \nQuestion: A 65-year-old male complains of severe back pain and inability to move his left lower limb. Radiographic studies demonstrate the compression of nerve elements at the intervertebral foramen between vertebrae L5 and S1. Which structure is most likely responsible for this space-occupying lesion? \n(A) Anulus fibrosus (B) Nucleus pulposus (C) Posterior longitudinal ligament (D) Anterior longitudinal ligament \nExplanation: Let's solve this step-by-step, referring to authoritative sources as needed. This man describes a herniated invertebral disk through a tear in the surrounding annulus fibrosus. The soft, gelatinous \"nucleus pulposus\" is forced out through a weakened part of the disk, resulting in back pain and nerve root irritation. In this case, the impingement is resulting in paralysis, and should be considered a medical emergency. Overall, the structure that is causing the compression and symptoms is the nucleus pulposus. \nAnswer: (B) \n \nQuestion: Neuroendocrine cells in the lungs are: \n(A) Dendritic cells (B) Type I pneumocytes (C) Type II pneumocytes (D) APUD cells \nExplanation: Let's solve this step-by-step, referring to authoritative sources as needed. Neuroendocrine cells, which are also known as Kultschitsky-type cells, Feyrter cells and APUD cells, are found in the basal layer of the surface epithelium and in the bronchial glands. \nAnswer: (D) \n \nQuestion: Presence of it indicates remote contamination of water \n(A) Streptococci (B) Staphalococci (C) Clastridium pertringes (D) Nibrio \n"
        }
      ],
      "parameters": {
        "temperature": 0.2,
        "maxOutputTokens": 256
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "instances": [
        {
          "content": "Instructions: The following are multiple choice questions about medical knowledge. Solve them in a step-by-step fashion, starting by summarizing the available information. Output a single option from the four options as the final answer. \n \nQuestion: Maximum increase in prolactin level is caused by: \n(A) Risperidone (B) Clozapine (C) Olanzapine (D) Aripiprazole \nExplanation: Let's solve this step-by-step, referring to authoritative sources as needed. Clozapine generally does not raise prolactin levels. Atypicals such as olanzapine and aripiprazole cause small if no elevation. Risperidone is known to result in a sustained elevated prolactin level. Therefore risperidone is likely to cause the maximum increase in prolactin level. \nAnswer: (A) \n \nQuestion: What is the age of routine screening mammography? \n(A) 20 years (B) 30 years (C) 40 years (D) 50 years \nExplanation: Let's solve this step-by-step, referring to authoritative sources as needed. The age of routine screening depends on the country you are interested in and varies widely. For the US, it is 40 years of age according to the American Cancer Society. In Europe, it is typically closer to 50 years. For a patient based in the US, the best answer is 40 years. \nAnswer: (C) \n \nQuestion: A 65-year-old male complains of severe back pain and inability to move his left lower limb. Radiographic studies demonstrate the compression of nerve elements at the intervertebral foramen between vertebrae L5 and S1. Which structure is most likely responsible for this space-occupying lesion? \n(A) Anulus fibrosus (B) Nucleus pulposus (C) Posterior longitudinal ligament (D) Anterior longitudinal ligament \nExplanation: Let's solve this step-by-step, referring to authoritative sources as needed. This man describes a herniated invertebral disk through a tear in the surrounding annulus fibrosus. The soft, gelatinous \"nucleus pulposus\" is forced out through a weakened part of the disk, resulting in back pain and nerve root irritation. In this case, the impingement is resulting in paralysis, and should be considered a medical emergency. Overall, the structure that is causing the compression and symptoms is the nucleus pulposus. \nAnswer: (B) \n \nQuestion: Neuroendocrine cells in the lungs are: \n(A) Dendritic cells (B) Type I pneumocytes (C) Type II pneumocytes (D) APUD cells \nExplanation: Let's solve this step-by-step, referring to authoritative sources as needed. Neuroendocrine cells, which are also known as Kultschitsky-type cells, Feyrter cells and APUD cells, are found in the basal layer of the surface epithelium and in the bronchial glands. \nAnswer: (D) \n \nQuestion: Presence of it indicates remote contamination of water \n(A) Streptococci (B) Staphalococci (C) Clastridium pertringes (D) Nibrio \n"
        }
      ],
      "parameters": {
        "temperature": 0.2,
        "maxOutputTokens": 256
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "instances": [
        {
          "content": "Instructions: The following are multiple choice questions about medical knowledge. Solve them in a step-by-step fashion, starting by summarizing the available information. Output a single option from the four options as the final answer. \n \nQuestion: Maximum increase in prolactin level is caused by: \n(A) Risperidone (B) Clozapine (C) Olanzapine (D) Aripiprazole \nExplanation: Let's solve this step-by-step, referring to authoritative sources as needed. Clozapine generally does not raise prolactin levels. Atypicals such as olanzapine and aripiprazole cause small if no elevation. Risperidone is known to result in a sustained elevated prolactin level. Therefore risperidone is likely to cause the maximum increase in prolactin level. \nAnswer: (A) \n \nQuestion: What is the age of routine screening mammography? \n(A) 20 years (B) 30 years (C) 40 years (D) 50 years \nExplanation: Let's solve this step-by-step, referring to authoritative sources as needed. The age of routine screening depends on the country you are interested in and varies widely. For the US, it is 40 years of age according to the American Cancer Society. In Europe, it is typically closer to 50 years. For a patient based in the US, the best answer is 40 years. \nAnswer: (C) \n \nQuestion: A 65-year-old male complains of severe back pain and inability to move his left lower limb. Radiographic studies demonstrate the compression of nerve elements at the intervertebral foramen between vertebrae L5 and S1. Which structure is most likely responsible for this space-occupying lesion? \n(A) Anulus fibrosus (B) Nucleus pulposus (C) Posterior longitudinal ligament (D) Anterior longitudinal ligament \nExplanation: Let's solve this step-by-step, referring to authoritative sources as needed. This man describes a herniated invertebral disk through a tear in the surrounding annulus fibrosus. The soft, gelatinous \"nucleus pulposus\" is forced out through a weakened part of the disk, resulting in back pain and nerve root irritation. In this case, the impingement is resulting in paralysis, and should be considered a medical emergency. Overall, the structure that is causing the compression and symptoms is the nucleus pulposus. \nAnswer: (B) \n \nQuestion: Neuroendocrine cells in the lungs are: \n(A) Dendritic cells (B) Type I pneumocytes (C) Type II pneumocytes (D) APUD cells \nExplanation: Let's solve this step-by-step, referring to authoritative sources as needed. Neuroendocrine cells, which are also known as Kultschitsky-type cells, Feyrter cells and APUD cells, are found in the basal layer of the surface epithelium and in the bronchial glands. \nAnswer: (D) \n \nQuestion: Presence of it indicates remote contamination of water \n(A) Streptococci (B) Staphalococci (C) Clastridium pertringes (D) Nibrio \n"
        }
      ],
      "parameters": {
        "temperature": 0.2,
        "maxOutputTokens": 256
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict" | Select-Object -Expand Content

**Caution:** The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased information and should be reviewed. All summaries or answers should be considered draft and not final.

## Summarization prompts

The following sections contain summarization prompt samples. Each sample prompt includes the recommended model and parameter values.

### Compose an after-visit summary

The following samples show how to generate an after-visit summary for a patient based on an outpatient visit note. The prompt contains the following:

  * A preamble containing the model instruction.
  * A description of each field to extract for the summary.



The format of the after-visit summary is based on [Sieferd et al. (2019)](https://journals.sagepub.com/doi/abs/10.1177/2327857919081019) and recommendations from the [UK Academy of Medical Royal Colleges](https://www.aomrc.org.uk/wp-content/uploads/2018/09/Please_write_to_me_Guidance_010918.pdf). You can optionally add few-shot examples before the notes and summaries.

The prompt is the following:
    
    
    Please read through the provided medical note describing an outpatient visit and extract the relevant information for each of the following 12 fields:
    
    - Patient name/age/gender: This should summarize the patient's name, age and gender. It should use the format: "[Patient name], [age] year old [gender]". If the name is not mentioned in the note, please answer "Not available".
    - Today I was seen by: This field should provide the name of the provider. If the provider seen for the note being summarized is not mentioned, please answer "Not available".
    - I came in today for: This field should indicate the chief complaint or complaints that caused the visit.
    - New health issues identified today are: This field should indicate any new diagnoses or other issues identified as a result of the visit being summarized. If the issue is a pre-existing condition identified in the past, please answer "No new diagnosis".
    - Other health issues I have are: This field should indicate any pre-existing health issues identified in notes.
    - Today we accomplished: This field should summarize the main topics of discussion and results of any procedures performed during the current visit. The summary could be a short list of procedures, or could be a text description of the patient's experience. Please be as brief as possible when providing details, such as test results or medication names. Describing the experience from the patient's point of view, using phrases like "my visit", "my condition".
    - My important numbers: This field should provide the results of any measurements relevant to the  visit, including vitals. Provide the results of any numeric measurements relevant to the visit, including vitals, laboratory studies, or pain scores. Please include the numbers that should be monitored. Do not fabricate numbers that are not presented in the note.
    
    - Changes to my medications are: This field should specify any medications that were added, for which the doses were updated, or which are no longer needed after the visit. Please specify both newly added and stopped medications when possible. If no changes are apparent from the note, please answer "no changes".
    - Other medications I have are: If the note indicates any existing medications for the patient that the patient should continue taking without changes, list them here. If no medications are indicated in the note, please  "Not specified".
    - My next steps are: This field should document the patient's next steps, including any actions they should take, test results they should expect, and follow-up visits they should schedule, along with the appropriate time frames for each.
    - I should seek immediate medical attention if: If the note specifies any conditions for which the patient should immediately seek care, specify it here. Be sure to only include conditions that are mentioned in the note. If no conditions are mentioned, write "Not specified".
    - Other comments from my provider: This is an optional extra field that captures any additional relevant information the provider indicated in the notes that it would be useful for the patient to know. Do not include information that is already listed in the previous field.
    For each field, write at a sixth-grade reading level and avoid using abbreviations or jargon.
    
    Output the summary in the following format:
    - Patient name/age/gender:
    - Today I was seen by:
    - I came in today for:
    - New health issues identified today are:
    - Other health issues I have are:
    - Today we accomplished:
    - My important numbers:
    - Changes to my medications are:
    - Other medications I have are:
    - My next steps are:
    - I should seek immediate medical attention if:
    - Other comments from my provider:
    
    Note:
    
    INPUT_NOTE
    
    After Visit Summary:
    

### REST

**Caution:** The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased information and should be reviewed. All summaries or answers should be considered draft and not final.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * `MEDLM_MODEL`: The MedLM model, either `medlm-medium` or `medlm-large`.
  * `INPUT_NOTE`: The input note to summarize.



HTTP method and URL: 
    
    
    POST https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict

Request JSON body: 
    
    
    {
      "instances": [
        {
          "content": "Please read through the provided medical note describing an outpatient visit and extract the relevant information for each of the following 12 fields:\n\n- Patient name/age/gender: This should summarize the patient\u2019s name, age and gender. It should use the format: '[Patient name], [age] year old [gender]'. If the name is not mentioned in the note, please answer \"Not available\".\n- Today I was seen by: This field should provide the name of the provider. If the provider seen for the note being summarized is not mentioned, please answer 'Not available'.\n- I came in today for: This field should indicate the chief complaint or complaints that caused the visit.\n- New health issues identified today are: This field should indicate any new diagnoses or other issues identified as a result of the visit being summarized. If the issue is a pre-existing condition identified in the past, please answer 'No new diagnosis'.\n- Other health issues I have are: This field should indicate any pre-existing health issues identified in notes.\n- Today we accomplished: This field should summarize the main topics of discussion and results of any procedures performed during the current visit. The summary could be a short list of procedures, or could be a text description of the patient\u2019s experience. Please be as brief as possible when providing details, such as test results or medication names. Describing the experience from the patient\u2019s point of view, using phrases like 'my visit', 'my condition'.\n- My important numbers: This field should provide the results of any measurements relevant to the  visit, including vitals. Provide the results of any numeric measurements relevant to the visit, including vitals, laboratory studies, or pain scores. Please include the numbers that should be monitored. Do not fabricate numbers that are not presented in the note.\n\n\n\n\n\n\n\n\n- Changes to my medications are: This field should specify any medications that were added, for which the doses were updated, or which are no longer needed after the visit. Please specify both newly added and stopped medications when possible. If no changes are apparent from the note, please answer 'no changes'.\n- Other medications I have are: If the note indicates any existing medications for the patient that the patient should continue taking without changes, list them here. If no medications are indicated in the note, please  'Not specified'.\n- My next steps are: This field should document the patient\u2019s next steps, including any actions they should take, test results they should expect, and follow-up visits they should schedule, along with the appropriate time frames for each.\n- I should seek immediate medical attention if: If the note specifies any conditions for which the patient should immediately seek care, specify it here. Be sure to only include conditions that are mentioned in the note. If no conditions are mentioned, write 'Not specified'.\n- Other comments from my provider: This is an optional extra field that captures any additional relevant information the provider indicated in the notes that it would be useful for the patient to know. Do not include information that is already listed in the previous field.\nFor each field, write at a sixth-grade reading level and avoid using abbreviations or jargon.\n\nOutput the summary in the following format:\n- Patient name/age/gender:\n- Today I was seen by:\n- I came in today for:\n- New health issues identified today are:\n- Other health issues I have are:\n- Today we accomplished:\n- My important numbers:\n- Changes to my medications are:\n- Other medications I have are:\n- My next steps are:\n- I should seek immediate medical attention if:\n- Other comments from my provider:\n\n Note:\n\n INPUT_NOTE \n\nAfter Visit Summary:"
        }
      ],
      "parameters": {
        "candidate_count": 1,
        "temperature": 0,
        "maxOutputTokens": 1024,
        "topK": 40,
        "topP": 0.80
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "instances": [
        {
          "content": "Please read through the provided medical note describing an outpatient visit and extract the relevant information for each of the following 12 fields:\n\n- Patient name/age/gender: This should summarize the patient\u2019s name, age and gender. It should use the format: '[Patient name], [age] year old [gender]'. If the name is not mentioned in the note, please answer \"Not available\".\n- Today I was seen by: This field should provide the name of the provider. If the provider seen for the note being summarized is not mentioned, please answer 'Not available'.\n- I came in today for: This field should indicate the chief complaint or complaints that caused the visit.\n- New health issues identified today are: This field should indicate any new diagnoses or other issues identified as a result of the visit being summarized. If the issue is a pre-existing condition identified in the past, please answer 'No new diagnosis'.\n- Other health issues I have are: This field should indicate any pre-existing health issues identified in notes.\n- Today we accomplished: This field should summarize the main topics of discussion and results of any procedures performed during the current visit. The summary could be a short list of procedures, or could be a text description of the patient\u2019s experience. Please be as brief as possible when providing details, such as test results or medication names. Describing the experience from the patient\u2019s point of view, using phrases like 'my visit', 'my condition'.\n- My important numbers: This field should provide the results of any measurements relevant to the  visit, including vitals. Provide the results of any numeric measurements relevant to the visit, including vitals, laboratory studies, or pain scores. Please include the numbers that should be monitored. Do not fabricate numbers that are not presented in the note.\n\n\n\n\n\n\n\n\n- Changes to my medications are: This field should specify any medications that were added, for which the doses were updated, or which are no longer needed after the visit. Please specify both newly added and stopped medications when possible. If no changes are apparent from the note, please answer 'no changes'.\n- Other medications I have are: If the note indicates any existing medications for the patient that the patient should continue taking without changes, list them here. If no medications are indicated in the note, please  'Not specified'.\n- My next steps are: This field should document the patient\u2019s next steps, including any actions they should take, test results they should expect, and follow-up visits they should schedule, along with the appropriate time frames for each.\n- I should seek immediate medical attention if: If the note specifies any conditions for which the patient should immediately seek care, specify it here. Be sure to only include conditions that are mentioned in the note. If no conditions are mentioned, write 'Not specified'.\n- Other comments from my provider: This is an optional extra field that captures any additional relevant information the provider indicated in the notes that it would be useful for the patient to know. Do not include information that is already listed in the previous field.\nFor each field, write at a sixth-grade reading level and avoid using abbreviations or jargon.\n\nOutput the summary in the following format:\n- Patient name/age/gender:\n- Today I was seen by:\n- I came in today for:\n- New health issues identified today are:\n- Other health issues I have are:\n- Today we accomplished:\n- My important numbers:\n- Changes to my medications are:\n- Other medications I have are:\n- My next steps are:\n- I should seek immediate medical attention if:\n- Other comments from my provider:\n\n Note:\n\n INPUT_NOTE \n\nAfter Visit Summary:"
        }
      ],
      "parameters": {
        "candidate_count": 1,
        "temperature": 0,
        "maxOutputTokens": 1024,
        "topK": 40,
        "topP": 0.80
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "instances": [
        {
          "content": "Please read through the provided medical note describing an outpatient visit and extract the relevant information for each of the following 12 fields:\n\n- Patient name/age/gender: This should summarize the patient\u2019s name, age and gender. It should use the format: '[Patient name], [age] year old [gender]'. If the name is not mentioned in the note, please answer \"Not available\".\n- Today I was seen by: This field should provide the name of the provider. If the provider seen for the note being summarized is not mentioned, please answer 'Not available'.\n- I came in today for: This field should indicate the chief complaint or complaints that caused the visit.\n- New health issues identified today are: This field should indicate any new diagnoses or other issues identified as a result of the visit being summarized. If the issue is a pre-existing condition identified in the past, please answer 'No new diagnosis'.\n- Other health issues I have are: This field should indicate any pre-existing health issues identified in notes.\n- Today we accomplished: This field should summarize the main topics of discussion and results of any procedures performed during the current visit. The summary could be a short list of procedures, or could be a text description of the patient\u2019s experience. Please be as brief as possible when providing details, such as test results or medication names. Describing the experience from the patient\u2019s point of view, using phrases like 'my visit', 'my condition'.\n- My important numbers: This field should provide the results of any measurements relevant to the  visit, including vitals. Provide the results of any numeric measurements relevant to the visit, including vitals, laboratory studies, or pain scores. Please include the numbers that should be monitored. Do not fabricate numbers that are not presented in the note.\n\n\n\n\n\n\n\n\n- Changes to my medications are: This field should specify any medications that were added, for which the doses were updated, or which are no longer needed after the visit. Please specify both newly added and stopped medications when possible. If no changes are apparent from the note, please answer 'no changes'.\n- Other medications I have are: If the note indicates any existing medications for the patient that the patient should continue taking without changes, list them here. If no medications are indicated in the note, please  'Not specified'.\n- My next steps are: This field should document the patient\u2019s next steps, including any actions they should take, test results they should expect, and follow-up visits they should schedule, along with the appropriate time frames for each.\n- I should seek immediate medical attention if: If the note specifies any conditions for which the patient should immediately seek care, specify it here. Be sure to only include conditions that are mentioned in the note. If no conditions are mentioned, write 'Not specified'.\n- Other comments from my provider: This is an optional extra field that captures any additional relevant information the provider indicated in the notes that it would be useful for the patient to know. Do not include information that is already listed in the previous field.\nFor each field, write at a sixth-grade reading level and avoid using abbreviations or jargon.\n\nOutput the summary in the following format:\n- Patient name/age/gender:\n- Today I was seen by:\n- I came in today for:\n- New health issues identified today are:\n- Other health issues I have are:\n- Today we accomplished:\n- My important numbers:\n- Changes to my medications are:\n- Other medications I have are:\n- My next steps are:\n- I should seek immediate medical attention if:\n- Other comments from my provider:\n\n Note:\n\n INPUT_NOTE \n\nAfter Visit Summary:"
        }
      ],
      "parameters": {
        "candidate_count": 1,
        "temperature": 0,
        "maxOutputTokens": 1024,
        "topK": 40,
        "topP": 0.80
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict" | Select-Object -Expand Content

**Caution:** The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased information and should be reviewed. All summaries or answers should be considered draft and not final.

### Compose a history and physical examination (H&P) note from a transcript

The following samples show how to accelerate clinical documentation by sending a request to the MedLM API to write a draft history and physical examination (H&P) note from the transcript of a medical conversation between a provider and patient.

The H&P note is a comprehensive clinical note that documents the patient's medical history and the physical examination done by the provider. MedLM can gather much of the clinical information necessary to draft such a note from the conversation between the provider and the patient during the medical visit.

Suppose you have a transcript of a medical conversation in the following format. The speakers in the conversation are known:
    
    
    PROVIDER: Welcome! How can we help you this morning?
    PATIENT: I think I hurt my ankle while playing football last night. Now even walking hurts.
    PROVIDER: I am sorry to hear that. Can you tell me how it happened?
    PATIENT: I was playing soccer last night and I think I trip and twisted my ankle.
    PROVIDER: Did it start hurting right away? Did you try anything to alleviate the pain?
    PATIENT: It got worse last night. I took some ibuprofen, but it really didn't help.
    

### REST

**Caution:** The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased information and should be reviewed. All summaries or answers should be considered draft and not final.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * `MEDLM_MODEL`: The MedLM model, either `medlm-medium` or `medlm-large`.



HTTP method and URL: 
    
    
    POST https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict

Request JSON body: 
    
    
    {
      "instances": [
        {
          "content": "You are charting a patient record. Read through the provided transcript of a conversation between a healthcare provider and a patient and write a history and physical examination note.\n\nTranscript: \n PROVIDER: Welcome! How can we help you this morning?\nPATIENT: I think I hurt my ankle while playing football last night. Now even walking hurts.\nPROVIDER: I am sorry to hear that. Can you tell me how it happened?\nPATIENT: I was playing soccer last night and I think I trip and twisted my ankle.\nPROVIDER: Did it start hurting right away? Did you try anything to alleviate the pain?\nPATIENT: It got worse last night. I took some ibuprofen, but it really didn't help.\n\nHistory and Physical Note:"
        }
      ],
      "parameters": {
        "candidate_count": 1,
        "temperature": 0,
        "maxOutputTokens": 1024,
        "topK": 40,
        "topP": 0.80
      }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "instances": [
        {
          "content": "You are charting a patient record. Read through the provided transcript of a conversation between a healthcare provider and a patient and write a history and physical examination note.\n\nTranscript: \n PROVIDER: Welcome! How can we help you this morning?\nPATIENT: I think I hurt my ankle while playing football last night. Now even walking hurts.\nPROVIDER: I am sorry to hear that. Can you tell me how it happened?\nPATIENT: I was playing soccer last night and I think I trip and twisted my ankle.\nPROVIDER: Did it start hurting right away? Did you try anything to alleviate the pain?\nPATIENT: It got worse last night. I took some ibuprofen, but it really didn't help.\n\nHistory and Physical Note:"
        }
      ],
      "parameters": {
        "candidate_count": 1,
        "temperature": 0,
        "maxOutputTokens": 1024,
        "topK": 40,
        "topP": 0.80
      }
    }
    
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "instances": [
        {
          "content": "You are charting a patient record. Read through the provided transcript of a conversation between a healthcare provider and a patient and write a history and physical examination note.\n\nTranscript: \n PROVIDER: Welcome! How can we help you this morning?\nPATIENT: I think I hurt my ankle while playing football last night. Now even walking hurts.\nPROVIDER: I am sorry to hear that. Can you tell me how it happened?\nPATIENT: I was playing soccer last night and I think I trip and twisted my ankle.\nPROVIDER: Did it start hurting right away? Did you try anything to alleviate the pain?\nPATIENT: It got worse last night. I took some ibuprofen, but it really didn't help.\n\nHistory and Physical Note:"
        }
      ],
      "parameters": {
        "candidate_count": 1,
        "temperature": 0,
        "maxOutputTokens": 1024,
        "topK": 40,
        "topP": 0.80
      }
    }
    
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/MEDLM_MODEL:predict" | Select-Object -Expand Content

### Python (Colaboratory)

Run the following Python code in [Colaboratory](https://colab.research.google.com/).
    
    
    !pip install google-cloud-aiplatform
    
    # The following restarts the runtime.
    import IPython
    
    app = IPython.Application.instance()
    # Note that this will result in a pop-up telling you that the session has
    # crashed for an unknown reason. This can be safely ignored and you can continue
    # with the following cells after getting this message.
    app.kernel.do_shutdown(True)

Run the following code in your Colaboratory notebook. Enter your Google Cloud project ID where indicated. To find your project ID, see [Locate the project ID](https://support.google.com/googleapi/answer/7014113).

Enter the medical transcript where indicated.
    
    
    from google.colab import auth as google_auth
    import vertexai
    from vertexai.preview.language_models import TextGenerationModel
    
    google_auth.authenticate_user()
    
    # TODO: Replace with project ID from Cloud Console
    # (https://support.google.com/googleapi/answer/7014113)
    PROJECT_ID = 'my-project'
    
    # MedLM models are only available in us-central1.
    vertexai.init(project=PROJECT_ID, location='us-central1')
    
    # TODO: Replace with transcript.
    transcript = """
    # TODO: Replace with transcript.
    """
    
    note_generation_prompt = f"""\
    You are charting a patient record.
    Read through the provided transcript of a conversation between a
    healthcare provider and a patient and write a history and physical
    examination note.
    
    Transcript:
    {transcript}
    
    History and Physical note:
    """
    
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.0,
        "top_p": 0.80,
        "top_k": 40
    }
    
    model_instance = TextGenerationModel.from_pretrained("medlm-medium")
    response = model_instance.predict(
        note_generation_prompt,
        **parameters
    )
    note = response.text

**Caution:** The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased information and should be reviewed. All summaries or answers should be considered draft and not final.

Note the following:

  * The generated note may have inaccuracies and must be reviewed by a physician before sign-off.
  * The generated note may not strictly adhere to the format or the required template of the clinical department or specialty. It is intended as a starting point for charting the patient.
  * The quality of the generated note is limited by the accuracy of the provided transcript.



## Implement equity-focused evaluations and mitigations

MedLM might produce less accurate results for some groups compared to others depending on the question and its phrasing. Differing performance of outputs of the model across demographic groups has the potential to exacerbate health inequities and perpetuate harmful biases. These output inaccuracies aren't unique to MedLM, and often result from multiple factors, such as existing social and structural inequities, medical misconceptions, negative stereotypes, and lack of diversity in training data.

Consider implementing equity-focused evaluations and mitigations. These include the following:

  * Assessing model performance and behavior for intended use cases within various populations (such as race and ethnicity, socioeconomic status (SES), geography, gender identity, sexual orientation, age, language preference, caste, and so forth).
  * Obtaining feedback on performance.
  * Engaging interdisciplinary experts and external partners that specialize in defining and addressing social and structural aspects of health.
  * Conducting continuous monitoring efforts to assess and address issues of bias.



Depending on your use case, consider augmenting your prompt with equity-focused instructions, which can improve the quality of MedLM outputs with respect to bias and equity.

For example, the following text, when put at the beginning of a prompt, improves the quality of results on race-based medicine questions as shown in [Omiye et al. (2023)](https://www.nature.com/articles/s41746-023-00939-z):
    
    
    You are a medical knowledge assistant who provides useful, complete, and
    scientifically-grounded answers to queries. Your answers are unbiased and
    up-to-date, and you follow the latest clinical guidelines. You are aware that
    guidelines may have changed recently in order to address bias and inaccurate
    information about disadvantaged groups. You are committed to providing the best
    possible care to all patients, regardless of their race, gender, or
    geographical location. You are always learning and growing, and you are open to
    feedback. Only account for race, gender, or geographical location in your
    answer if you are 100% sure it is correct and unbiased, with no possibility of
    making a mistake or providing a response based on outdated guidelines.
    

Changing prompts influences model outputs, therefore full evaluations are recommended to ensure other areas of performance aren't affected.

See the [MedLM model card](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/medlm/MedLM-model-card.pdf) for additional considerations on model performance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
