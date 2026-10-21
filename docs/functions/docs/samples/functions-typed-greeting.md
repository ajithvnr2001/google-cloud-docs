---
url: https://docs.cloud.google.com/functions/docs/samples/functions-typed-greeting/
title: Cloud Functions: Greeting Function \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:33.149638+00:00
---

# Cloud Functions: Greeting Function  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-typed-greeting/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Cloud Functions: Greeting Function Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to create a Cloud Function that accepts a first name and last name as input, and returns a personalized greeting message.

## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.Functions.Framework;
    using System.Text.Json.Serialization;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace Greeting;
    
    public class Function : ITypedFunction<GreetingRequest, GreetingResponse>
    {
        public Task<GreetingResponse> HandleAsync(GreetingRequest request, CancellationToken cancellationToken) =>
            Task.FromResult(new GreetingResponse
            {
                Message = $"Hello {request.FirstName} {request.LastName}!",
            });
    }
    
    public class GreetingRequest
    {
        [JsonPropertyName("first_name")]
        public string FirstName { get; set; }
    
        [JsonPropertyName("last_name")]
        public string LastName { get; set; }
    }
    
    public class GreetingResponse
    {
        [JsonPropertyName("message")]
        public string Message { get; set; }
    }
    

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package greeting provides a set of Cloud Functions samples.
    package greeting
    
    import (
    	"fmt"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    func init() {
    	functions.Typed("Greeting", greeting)
    }
    
    // greeting is a Typed Cloud Function.
    func greeting(request *GreetingRequest) (*GreetingResponse, error) {
    	return &GreetingResponse{
    		Message: fmt.Sprintf("Hello %v %v!", request.FirstName, request.LastName),
    	}, nil
    }
    
    type GreetingRequest struct {
    	FirstName string `json:"first_name"`
    	LastName  string `json:"last_name"`
    }
    
    type GreetingResponse struct {
    	Message string `json:"message"`
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.TypedFunction;
    import com.google.gson.annotations.SerializedName;
    
    public class Greeting implements TypedFunction<GreetingRequest, GreetingResponse> {
      @Override
      public GreetingResponse apply(GreetingRequest request) throws Exception {
        GreetingResponse response = new GreetingResponse();
        response.message = String.format("Hello %s %s!", request.firstName, request.lastName);
        return response;
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    functions.typed('greeting', req => {
      return {
        message: `Hello ${req.first_name} ${req.last_name}!`,
      };
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\CloudFunctions\FunctionsFramework;
    
    class GreetingRequest
    {
        /** @var string */
        public $first_name;
    
        /** @var string */
        public $last_name;
    
        public function __construct(string $first_name = '', string $last_name = '')
        {
            $this->first_name = $first_name;
            $this->last_name = $last_name;
        }
    
        public function serializeToJsonString(): string
        {
            return json_encode([
                'first_name' => $this->first_name,
                'last_name' => $this->last_name,
            ]);
        }
    
        public function mergeFromJsonString(string $body): void
        {
            $obj = json_decode($body);
            $this->first_name = $obj['first_name'];
            $this->last_name = $obj['last_name'];
        }
    }
    
    class GreetingResponse
    {
        /** @var string */
        public $message;
    
        public function __construct(string $message = '')
        {
            $this->message = $message;
        }
    
        public function serializeToJsonString(): string
        {
            return json_encode([
                'message' => $message,
            ]);
        }
    
        public function mergeFromJsonString(string $body): void
        {
            $obj = json_decode($body);
            $this->message = $obj['message'];
        }
    };
    
    function greeting(GreetingRequest $req): GreetingResponse
    {
        return new GreetingResponse("Hello $req->first_name $req->last_name!");
    };
    
    FunctionsFramework::typed('greeting', 'greeting');
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from dataclasses import dataclass
    
    import functions_framework
    
    
    @dataclass
    class GreetingRequest:
        first_name: str
        last_name: str
    
        # Required to deserialize the request
        @staticmethod
        def from_dict(req: dict) -> "GreetingRequest":
            return GreetingRequest(
                first_name=req["first_name"],
                last_name=req["last_name"],
            )
    
    
    @dataclass
    class GreetingResponse:
        message: str
    
        # Required to serialize the response
        def to_dict(self) -> dict:
            return {
                "message": self.message,
            }
    
    
    @functions_framework.typed
    def greeting(req: GreetingRequest):
        return GreetingResponse(message=f"Hello {req.first_name} {req.last_name}!")
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    FunctionsFramework.typed "greeting" do |req|
      {
        message: "Hello #{req['first_name']} #{req['last_name']}!"
      }
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
