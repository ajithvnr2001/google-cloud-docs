---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-evaluation-get-rouge-score/
title: Evaluate a model response against a reference (ground truth) using the ROUGE metric \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:12.108157+00:00
---

# Evaluate a model response against a reference (ground truth) using the ROUGE metric  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-evaluation-get-rouge-score/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Evaluate a model response against a reference (ground truth) using the ROUGE metric Stay organized with collections  Save and categorize content based on your preferences. 

This code sample demonstrates how to use Vertex AI to compute ROUGE metrics for evaluating text summarization models. It shows how to define an evaluation task and calculate ROUGE scores for multiple generated summaries against a reference summary.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Gen AI evaluation service API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/evaluation)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	aiplatform "cloud.google.com/go/aiplatform/apiv1beta1"
    	aiplatformpb "cloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb"
    	"google.golang.org/api/option"
    )
    
    // getROUGEScore evaluates a model response against a reference (ground truth) using the ROUGE metric
    func getROUGEScore(w io.Writer, projectID, location string) error {
    	// location = "us-central1"
    	ctx := context.Background()
    	apiEndpoint := fmt.Sprintf("%s-aiplatform.googleapis.com:443", location)
    	client, err := aiplatform.[NewEvaluationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1beta1.html#cloud_google_com_go_aiplatform_apiv1beta1_EvaluationClient_NewEvaluationClient)(ctx, option.WithEndpoint(apiEndpoint))
    
    	if err != nil {
    		return fmt.Errorf("unable to create aiplatform client: %w", err)
    	}
    	defer client.Close()
    
    	modelResponse := `
    The Great Barrier Reef, the world's largest coral reef system located in Australia,
    is a vast and diverse ecosystem. However, it faces serious threats from climate change,
    ocean acidification, and coral bleaching, endangering its rich marine life.
    `
    	reference := `
    The Great Barrier Reef, the world's largest coral reef system, is
    located off the coast of Queensland, Australia. It's a vast
    ecosystem spanning over 2,300 kilometers with thousands of reefs
    and islands. While it harbors an incredible diversity of marine
    life, including endangered species, it faces serious threats from
    climate change, ocean acidification, and coral bleaching.
    `
    	req := aiplatformpb.EvaluateInstancesRequest{
    		Location: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		MetricInputs: &aiplatformpb.EvaluateInstancesRequest_RougeInput{
    			RougeInput: &aiplatformpb.RougeInput{
    				// Check the API reference for the list of supported ROUGE metric types:
    				// https://cloud.google.com/vertex-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1#rougespec
    				MetricSpec: &aiplatformpb.RougeSpec{
    					RougeType: "rouge1",
    				},
    				Instances: []*aiplatformpb.RougeInstance{
    					{
    						Prediction: &modelResponse,
    						Reference:  &reference,
    					},
    				},
    			},
    		},
    	}
    
    	resp, err := client.EvaluateInstances(ctx, &req)
    	if err != nil {
    		return fmt.Errorf("evaluateInstances failed: %v", err)
    	}
    
    	fmt.Fprintln(w, "evaluation results:")
    	fmt.Fprintln(w, resp.GetRougeResults().GetRougeMetricValues())
    	// Example response:
    	// [score:0.6597938]
    
    	return nil
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import pandas as pd
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai.preview.evaluation import EvalTask
    
    # TODO(developer): Update & uncomment line below
    # PROJECT_ID = "your-project-id"
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(project=PROJECT_ID, location="us-central1")
    
    reference_summarization = """
    The Great Barrier Reef, the world's largest coral reef system, is
    located off the coast of Queensland, Australia. It's a vast
    ecosystem spanning over 2,300 kilometers with thousands of reefs
    and islands. While it harbors an incredible diversity of marine
    life, including endangered species, it faces serious threats from
    climate change, ocean acidification, and coral bleaching."""
    
    # Compare pre-generated model responses against the reference (ground truth).
    eval_dataset = pd.DataFrame(
        {
            "response": [
                """The Great Barrier Reef, the world's largest coral reef system located
            in Australia, is a vast and diverse ecosystem. However, it faces serious
            threats from climate change, ocean acidification, and coral bleaching,
            endangering its rich marine life.""",
                """The Great Barrier Reef, a vast coral reef system off the coast of
            Queensland, Australia, is the world's largest. It's a complex ecosystem
            supporting diverse marine life, including endangered species. However,
            climate change, ocean acidification, and coral bleaching are serious
            threats to its survival.""",
                """The Great Barrier Reef, the world's largest coral reef system off the
            coast of Australia, is a vast and diverse ecosystem with thousands of
            reefs and islands. It is home to a multitude of marine life, including
            endangered species, but faces serious threats from climate change, ocean
            acidification, and coral bleaching.""",
            ],
            "reference": [reference_summarization] * 3,
        }
    )
    eval_task = EvalTask(
        dataset=eval_dataset,
        metrics=[
            "rouge_1",
            "rouge_2",
            "rouge_l",
            "rouge_l_sum",
        ],
    )
    result = eval_task.[evaluate](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.evals.Evals.html#vertexai__genai_evals_Evals_evaluate)()
    
    print("Summary Metrics:\n")
    for key, value in [result](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.CheckQueryJobResultDict.html#vertexai__genai_types_CheckQueryJobResultDict_result).summary_metrics.items():
        print(f"{key}: \t{value}")
    
    print("\n\nMetrics Table:\n")
    print([result](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.CheckQueryJobResultDict.html#vertexai__genai_types_CheckQueryJobResultDict_result).metrics_table)
    # Example response:
    #
    # Summary Metrics:
    #
    # row_count:      3
    # rouge_1/mean:   0.7191161666666667
    # rouge_1/std:    0.06765143922270488
    # rouge_2/mean:   0.5441118566666666
    # ...
    # Metrics Table:
    #
    #                                        response                         reference  ...  rouge_l/score  rouge_l_sum/score
    # 0  The Great Barrier Reef, the world's ...  \n    The Great Barrier Reef, the ...  ...       0.577320           0.639175
    # 1  The Great Barrier Reef, a vast coral...  \n    The Great Barrier Reef, the ...  ...       0.552381           0.666667
    # 2  The Great Barrier Reef, the world's ...  \n    The Great Barrier Reef, the ...  ...       0.774775           0.774775

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
