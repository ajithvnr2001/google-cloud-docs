---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-create-evaluation-task/
title: Evaluate text generation models using Vertex AI Gen AI evaluation service \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:55.206355+00:00
---

# Evaluate text generation models using Vertex AI Gen AI evaluation service  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-create-evaluation-task/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Evaluate text generation models using Vertex AI Gen AI evaluation service Stay organized with collections  Save and categorize content based on your preferences. 

Use the Vertex AI Gen AI evaluation service to evaluate generation models for Natural Language Processing (NLP) tasks like summarization, translation, and question answering. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Gen AI evaluation service API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/evaluation)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	context_pkg "context"
    	"fmt"
    	"io"
    
    	aiplatform "cloud.google.com/go/aiplatform/apiv1beta1"
    	aiplatformpb "cloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb"
    	"google.golang.org/api/option"
    )
    
    // evaluateModelResponse evaluates the output of an LLM for groundedness, i.e., how well
    // the model response connects with verifiable sources of information
    func evaluateModelResponse(w io.Writer, projectID, location string) error {
    	// location = "us-central1"
    	ctx := context_pkg.Background()
    	apiEndpoint := fmt.Sprintf("%s-aiplatform.googleapis.com:443", location)
    	client, err := aiplatform.[NewEvaluationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1beta1.html#cloud_google_com_go_aiplatform_apiv1beta1_EvaluationClient_NewEvaluationClient)(ctx, option.WithEndpoint(apiEndpoint))
    
    	if err != nil {
    		return fmt.Errorf("unable to create aiplatform client: %w", err)
    	}
    	defer client.Close()
    
    	// evaluate the pre-generated model response against the reference (ground truth)
    	responseToEvaluate := `
    The city is undertaking a major project to revamp its public transportation system.
    This initiative is designed to improve efficiency, reduce carbon emissions, and promote
    eco-friendly commuting. The city expects that this investment will enhance accessibility
    and usher in a new era of sustainable urban transportation.
    `
    	reference := `
    As part of a comprehensive initiative to tackle urban congestion and foster
    sustainable urban living, a major city has revealed ambitious plans for an
    extensive overhaul of its public transportation system. The project aims not
    only to improve the efficiency and reliability of public transit but also to
    reduce the city\'s carbon footprint and promote eco-friendly commuting options.
    City officials anticipate that this strategic investment will enhance
    accessibility for residents and visitors alike, ushering in a new era of
    efficient, environmentally conscious urban transportation.
    `
    	req := aiplatformpb.EvaluateInstancesRequest{
    		Location: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		// Check the API reference for a full list of supported metric inputs:
    		// https://cloud.google.com/vertex-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1#evaluateinstancesrequest
    		MetricInputs: &aiplatformpb.EvaluateInstancesRequest_GroundednessInput{
    			GroundednessInput: &aiplatformpb.GroundednessInput{
    				MetricSpec: &aiplatformpb.GroundednessSpec{},
    				Instance: &aiplatformpb.GroundednessInstance{
    					Context:    &reference,
    					Prediction: &responseToEvaluate,
    				},
    			},
    		},
    	}
    
    	resp, err := client.EvaluateInstances(ctx, &req)
    	if err != nil {
    		return fmt.Errorf("evaluateInstances failed: %v", err)
    	}
    
    	results := resp.GetGroundednessResult()
    	fmt.Fprintf(w, "score: %.2f\n", results.GetScore())
    	fmt.Fprintf(w, "confidence: %.2f\n", results.GetConfidence())
    	fmt.Fprintf(w, "explanation:\n%s\n", results.GetExplanation())
    	// Example response:
    	// score: 1.00
    	// confidence: 1.00
    	// explanation:
    	// STEP 1: All aspects of the response are found in the context.
    	// The response accurately summarizes the city's plan to overhaul its public transportation system, highlighting the goals of ...
    	// STEP 2: According to the rubric, the response is scored 1 because all aspects of the response are attributable to the context.
    
    	return nil
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import pandas as pd
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai.preview.evaluation import EvalTask, MetricPromptTemplateExamples
    
    # TODO(developer): Update and un-comment below line
    # PROJECT_ID = "your-project-id"
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(project=PROJECT_ID, location="us-central1")
    
    eval_dataset = pd.DataFrame(
        {
            "instruction": [
                "Summarize the text in one sentence.",
                "Summarize the text such that a five-year-old can understand.",
            ],
            "context": [
                """As part of a comprehensive initiative to tackle urban congestion and foster
                sustainable urban living, a major city has revealed ambitious plans for an
                extensive overhaul of its public transportation system. The project aims not
                only to improve the efficiency and reliability of public transit but also to
                reduce the city\'s carbon footprint and promote eco-friendly commuting options.
                City officials anticipate that this strategic investment will enhance
                accessibility for residents and visitors alike, ushering in a new era of
                efficient, environmentally conscious urban transportation.""",
                """A team of archaeologists has unearthed ancient artifacts shedding light on a
                previously unknown civilization. The findings challenge existing historical
                narratives and provide valuable insights into human history.""",
            ],
            "response": [
                "A major city is revamping its public transportation system to fight congestion, reduce emissions, and make getting around greener and easier.",
                "Some people who dig for old things found some very special tools and objects that tell us about people who lived a long, long time ago! What they found is like a new puzzle piece that helps us understand how people used to live.",
            ],
        }
    )
    
    eval_task = EvalTask(
        dataset=eval_dataset,
        metrics=[
            MetricPromptTemplateExamples.Pointwise.SUMMARIZATION_QUALITY,
            MetricPromptTemplateExamples.Pointwise.GROUNDEDNESS,
            MetricPromptTemplateExamples.Pointwise.VERBOSITY,
            MetricPromptTemplateExamples.Pointwise.INSTRUCTION_FOLLOWING,
        ],
    )
    
    prompt_template = (
        "Instruction: {instruction}. Article: {context}. Summary: {response}"
    )
    result = eval_task.[evaluate](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.evals.Evals.html#vertexai__genai_evals_Evals_evaluate)(prompt_template=prompt_template)
    
    print("Summary Metrics:\n")
    
    for key, value in [result](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.CheckQueryJobResultDict.html#vertexai__genai_types_CheckQueryJobResultDict_result).summary_metrics.items():
        print(f"{key}: \t{value}")
    
    print("\n\nMetrics Table:\n")
    print([result](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.CheckQueryJobResultDict.html#vertexai__genai_types_CheckQueryJobResultDict_result).metrics_table)
    # Example response:
    # Summary Metrics:
    # row_count:      2
    # summarization_quality/mean:     3.5
    # summarization_quality/std:      2.1213203435596424
    # ...
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
