---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-safety-with-txt/
title: Generate text with safety settings \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:29:58.457614+00:00
---

# Generate text with safety settings  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-safety-with-txt/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Generate text with safety settings Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to use the Gemini model with safety settings to generate text.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Safety and content filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"google.golang.org/genai"
    )
    
    // generateTextWithSafety shows how to apply safety settings to a text generation request.
    func generateTextWithSafety(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := genai.NewClient(ctx, &genai.ClientConfig{
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create genai client: %w", err)
    	}
    
    	systemInstruction := &genai.Content{
    		Parts: []*genai.Part{
    			{Text: "Be as mean as possible."},
    		},
    		Role: genai.RoleUser,
    	}
    
    	prompt := "Write a list of 5 disrespectful things that I might say to the universe after stubbing my toe in the dark."
    
    	safetySettings := []*genai.SafetySetting{
    		{Category: genai.HarmCategoryDangerousContent, Threshold: genai.HarmBlockThresholdBlockLowAndAbove},
    		{Category: genai.HarmCategoryHarassment, Threshold: genai.HarmBlockThresholdBlockLowAndAbove},
    		{Category: genai.HarmCategoryHateSpeech, Threshold: genai.HarmBlockThresholdBlockLowAndAbove},
    		{Category: genai.HarmCategorySexuallyExplicit, Threshold: genai.HarmBlockThresholdBlockLowAndAbove},
    	}
    
    	config := &genai.GenerateContentConfig{
    		SystemInstruction: systemInstruction,
    		SafetySettings:    safetySettings,
    	}
    	modelName := "gemini-2.5-flash"
    	resp, err := client.Models.GenerateContent(ctx, modelName,
    		[]*genai.Content{{Parts: []*genai.Part{{Text: prompt}}, Role: genai.RoleUser}},
    		config,
    	)
    	if err != nil {
    		return fmt.Errorf("failed to generate content: %w", err)
    	}
    
    	fmt.Fprintln(w, resp.Text())
    
    	if len(resp.Candidates) > 0 {
    		fmt.Fprintln(w, "Finish Reason:", resp.Candidates[0].FinishReason)
    
    		for _, rating := range resp.Candidates[0].SafetyRatings {
    			fmt.Fprintf(w, "\nCategory: %v\nIs Blocked: %v\nProbability: %v\nProbability Score: %v\nSeverity: %v\nSeverity Score: %v\n",
    				rating.Category,
    				rating.Blocked,
    				rating.Probability,
    				rating.ProbabilityScore,
    				rating.Severity,
    				rating.SeverityScore,
    			)
    		}
    	}
    
    	// Example response:
    	// Category: HARM_CATEGORY_HATE_SPEECH
    	// Is Blocked: false
    	// Probability: NEGLIGIBLE
    	// Probability Score: 8.996795e-06
    	// Severity: HARM_SEVERITY_NEGLIGIBLE
    	// Severity Score: 0.04771039
    	//
    	// Category: HARM_CATEGORY_DANGEROUS_CONTENT
    	// Is Blocked: false
    	// Probability: NEGLIGIBLE
    	// Probability Score: 2.2431707e-06
    	// Severity: HARM_SEVERITY_NEGLIGIBLE
    	// Severity Score: 0
    	//
    	// Category: HARM_CATEGORY_HARASSMENT
    	// Is Blocked: false
    	// Probability: NEGLIGIBLE
    	// Probability Score: 0.00026123362
    	// Severity: HARM_SEVERITY_NEGLIGIBLE
    	// Severity Score: 0.022358216
    	//
    	// Category: HARM_CATEGORY_SEXUALLY_EXPLICIT
    	// Is Blocked: false
    	// Probability: NEGLIGIBLE
    	// Probability Score: 6.1352006e-07
    	// Severity: HARM_SEVERITY_NEGLIGIBLE
    	// Severity Score: 0.020111412
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.genai.Client;
    import com.google.genai.types.Candidate;
    import com.google.genai.types.Content;
    import com.google.genai.types.GenerateContentConfig;
    import com.google.genai.types.GenerateContentResponse;
    import com.google.genai.types.HarmBlockThreshold;
    import com.google.genai.types.HarmCategory;
    import com.google.genai.types.HttpOptions;
    import com.google.genai.types.Part;
    import com.google.genai.types.SafetySetting;
    import java.util.List;
    import java.util.stream.Collectors;
    
    public class SafetyWithTxt {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String modelId = "gemini-2.5-flash";
        generateContent(modelId);
      }
    
      // Shows how to generate content with safety settings.
      public static GenerateContentResponse generateContent(String modelId) {
        // Client Initialization. Once created, it can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("global")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1").build())
                .build()) {
    
          String systemInstruction = "Be as mean as possible.";
    
          String prompt =
              "Write a list of 5 disrespectful things that I might say"
                  + " to the universe after stubbing my toe in the dark.";
    
          // Set safety settings.
          List<HarmCategory.Known> categoriesToBlock =
              List.of(
                  HarmCategory.Known.HARM_CATEGORY_DANGEROUS_CONTENT,
                  HarmCategory.Known.HARM_CATEGORY_HARASSMENT,
                  HarmCategory.Known.HARM_CATEGORY_HATE_SPEECH,
                  HarmCategory.Known.HARM_CATEGORY_SEXUALLY_EXPLICIT);
    
          List<SafetySetting> safetySettings =
              categoriesToBlock.stream()
                  .map(
                      category ->
                          SafetySetting.builder()
                              .category(category)
                              .threshold(HarmBlockThreshold.Known.BLOCK_LOW_AND_ABOVE)
                              .build())
                      .collect(Collectors.toList());
    
          GenerateContentResponse response =
              client.models.generateContent(
                  modelId,
                  prompt,
                  GenerateContentConfig.builder()
                      .systemInstruction(Content.fromParts(Part.fromText(systemInstruction)))
                      .safetySettings(safetySettings)
                      .build());
    
          // Get response candidate.
          Candidate candidate =
              response
                  .candidates()
                  .flatMap(candidates -> candidates.stream().findFirst())
                  .orElseThrow(
                      () -> new IllegalStateException("No response candidate generated by the model."));
    
          // Finish Reason will be `SAFETY` if it is blocked.
          System.out.println(candidate.finishReason());
          // Example response:
          // Optional[SAFETY]
    
          // For details on all the fields in the response.
          candidate
              .safetyRatings()
              .ifPresent(
                  safetyRatings ->
                      safetyRatings.forEach(
                          safetyRating -> {
                            System.out.println("\nCategory: " + safetyRating.category());
                            System.out.println("Is Blocked: " + safetyRating.blocked());
                            System.out.println("Probability: " + safetyRating.probability());
                            System.out.println("Probability Score: " + safetyRating.probabilityScore());
                            System.out.println("Severity: " + safetyRating.severity());
                            System.out.println("Severity Score: " + safetyRating.severityScore());
                          }));
          // Example response:
          // Category: Optional[HARM_CATEGORY_HATE_SPEECH]
          // Is Blocked: Optional.empty
          // Probability: Optional[NEGLIGIBLE]
          // Probability Score: Optional[1.9967922E-5]
          // Severity: Optional[HARM_SEVERITY_NEGLIGIBLE]
          // Severity Score: Optional[0.05732864]
          //
          // Category: Optional[HARM_CATEGORY_DANGEROUS_CONTENT]
          // Is Blocked: Optional.empty
          // Probability: Optional[NEGLIGIBLE]
          // Probability Score: Optional[2.9124324E-6]
          // Severity: Optional[HARM_SEVERITY_NEGLIGIBLE]
          // Severity Score: Optional[0.04544826]
          //
          // Category: Optional[HARM_CATEGORY_HARASSMENT]
          // Is Blocked: Optional[true]
          // Probability: Optional[MEDIUM]
          // Probability Score: Optional[0.4593908]
          // Severity: Optional[HARM_SEVERITY_MEDIUM]
          // Severity Score: Optional[0.22082388]
          //
          // Category: Optional[HARM_CATEGORY_SEXUALLY_EXPLICIT]
          // Is Blocked: Optional.empty
          // Probability: Optional[NEGLIGIBLE]
          // Probability Score: Optional[6.453211E-8]
          // Severity: Optional[HARM_SEVERITY_NEGLIGIBLE]
          // Severity Score: Optional[0.023201048]
          return response;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {GoogleGenAI} = require('@google/genai');
    
    const GOOGLE_CLOUD_PROJECT = process.env.GOOGLE_CLOUD_PROJECT;
    const GOOGLE_CLOUD_LOCATION = process.env.GOOGLE_CLOUD_LOCATION || 'global';
    
    async function generateWithSafetySettings(
      projectId = GOOGLE_CLOUD_PROJECT,
      location = GOOGLE_CLOUD_LOCATION
    ) {
      const client = new GoogleGenAI({
        vertexai: true,
        project: projectId,
        location: location,
      });
    
      const systemInstruction = 'Be as mean as possible.';
    
      const prompt =
        'Write a list of 5 disrespectful things that I might say to the universe after stubbing my toe in the dark.';
    
      const safetySettings = [
        {
          category: 'HARM_CATEGORY_DANGEROUS_CONTENT',
          threshold: 'BLOCK_LOW_AND_ABOVE',
        },
        {
          category: 'HARM_CATEGORY_HARASSMENT',
          threshold: 'BLOCK_LOW_AND_ABOVE',
        },
        {
          category: 'HARM_CATEGORY_HATE_SPEECH',
          threshold: 'BLOCK_LOW_AND_ABOVE',
        },
        {
          category: 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
          threshold: 'BLOCK_LOW_AND_ABOVE',
        },
      ];
    
      const response = await client.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: prompt,
        config: {
          systemInstruction: systemInstruction,
          safetySettings: safetySettings,
        },
      });
    
      // console.log(response.text);
      // console.log(response.candidates[0].finishMessage);
      //
      // for (const each of response.candidates[0].safetyRatings) {
      //   console.log('\nCategory:', String(each.category));
      //   console.log('Is Blocked:', each.blocked);
      //   console.log('Probability:', each.probability);
      //   console.log('Probability Score:', each.probabilityScore);
      //   console.log('Severity:', each.severity);
      //   console.log('Severity Score:', each.severityScore);
      // }
    
      // Example response:
      //
      //     Category:  HarmCategory.HARM_CATEGORY_HATE_SPEECH
      //     Is Blocked: False
      //     Probability:  HarmProbability.NEGLIGIBLE
      //     Probability Score:  2.547714e-05
      //     Severity: HarmSeverity.HARM_SEVERITY_NEGLIGIBLE
      //     Severity Score: None
      //
      //     Category:  HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT
      //     Is Blocked: False
      //     Probability:  HarmProbability.NEGLIGIBLE
      //     Probability Score:  3.6103818e-06
      //     Severity: HarmSeverity.HARM_SEVERITY_NEGLIGIBLE
      //     Severity Score: None
      //
      //     Category:  HarmCategory.HARM_CATEGORY_HARASSMENT
      //     Is Blocked: True
      //     Probability:  HarmProbability.MEDIUM
      //     Probability Score:  0.71599233
      //     Severity: HarmSeverity.HARM_SEVERITY_MEDIUM
      //     Severity Score: 0.30782545
      //
      //     Category:  HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT
      //     Is Blocked: False
      //     Probability:  HarmProbability.NEGLIGIBLE
      //     Probability Score:  1.5624657e-05
      //     Severity: HarmSeverity.HARM_SEVERITY_NEGLIGIBLE
      //     Severity Score: None
    
      return response;
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai.types import (
        GenerateContentConfig,
        HarmBlockThreshold,
        HarmCategory,
        HttpOptions,
        SafetySetting,
    )
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    
    system_instruction = "Be as mean as possible."
    
    prompt = """
        Write a list of 5 disrespectful things that I might say to the universe after stubbing my toe in the dark.
    """
    
    safety_settings = [
        SafetySetting(
            category=HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
        SafetySetting(
            category=HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
        SafetySetting(
            category=HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
        SafetySetting(
            category=HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
    ]
    
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=GenerateContentConfig(
            system_instruction=system_instruction,
            safety_settings=safety_settings,
        ),
    )
    
    # Response will be `None` if it is blocked.
    print(response.text)
    # Example response:
    #     None
    
    # Finish Reason will be `SAFETY` if it is blocked.
    print(response.candidates[0].finish_reason)
    # Example response:
    #     FinishReason.SAFETY
    
    # For details on all the fields in the response
    for each in response.candidates[0].safety_ratings:
        print('\nCategory: ', str(each.category))
        print('Is Blocked:', True if each.blocked else False)
        print('Probability: ', each.probability)
        print('Probability Score: ', each.probability_score)
        print('Severity:', each.severity)
        print('Severity Score:', each.severity_score)
    # Example response:
    #
    #     Category:  HarmCategory.HARM_CATEGORY_HATE_SPEECH
    #     Is Blocked: False
    #     Probability:  HarmProbability.NEGLIGIBLE
    #     Probability Score:  2.547714e-05
    #     Severity: HarmSeverity.HARM_SEVERITY_NEGLIGIBLE
    #     Severity Score: None
    #
    #     Category:  HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT
    #     Is Blocked: False
    #     Probability:  HarmProbability.NEGLIGIBLE
    #     Probability Score:  3.6103818e-06
    #     Severity: HarmSeverity.HARM_SEVERITY_NEGLIGIBLE
    #     Severity Score: None
    #
    #     Category:  HarmCategory.HARM_CATEGORY_HARASSMENT
    #     Is Blocked: True
    #     Probability:  HarmProbability.MEDIUM
    #     Probability Score:  0.71599233
    #     Severity: HarmSeverity.HARM_SEVERITY_MEDIUM
    #     Severity Score: 0.30782545
    #
    #     Category:  HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT
    #     Is Blocked: False
    #     Probability:  HarmProbability.NEGLIGIBLE
    #     Probability Score:  1.5624657e-05
    #     Severity: HarmSeverity.HARM_SEVERITY_NEGLIGIBLE
    #     Severity Score: None

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
