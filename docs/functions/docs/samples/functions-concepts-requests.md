---
url: https://docs.cloud.google.com/functions/docs/samples/functions-concepts-requests/
title: Send HTTP requests \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:18.021602+00:00
---

# Send HTTP requests  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-concepts-requests/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Send HTTP requests Stay organized with collections  Save and categorize content based on your preferences. 

Shows how to make an HTTP request from a Cloud Function.

## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.Functions.Framework;
    using Google.Cloud.Functions.Hosting;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.AspNetCore.Http;
    using [Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Microsoft.Extensions.DependencyInjection.html);
    using System.Net.Http;
    using System.Threading.Tasks;
    
    namespace SendHttpRequest;
    
    // Dependency injection configuration, executed during server startup.
    public class Startup : FunctionsStartup
    {
        public override void ConfigureServices(WebHostBuilderContext context, IServiceCollection services)
        {
            // Make an HttpClient available to our function via dependency injection.
            // There are many options here; see
            // https://docs.microsoft.com/en-us/aspnet/core/fundamentals/http-requests
            // for more details.
            services.AddHttpClient<IHttpFunction, Function>();
        }
    }
    
    // Function, decorated with the FunctionsStartup attribute to specify the startup class
    // for dependency injection.
    [FunctionsStartup(typeof(Startup))]
    public class Function : IHttpFunction
    {
        private readonly HttpClient _httpClient;
    
        public Function(HttpClient httpClient) =>
            _httpClient = httpClient;
    
        public async Task HandleAsync(HttpContext context)
        {
            string url = "http://example.com";
            using (HttpResponseMessage clientResponse = await _httpClient.GetAsync(url, context.RequestAborted))
            {
                await context.Response.WriteAsync(
                    $"Received code '{(int) clientResponse.StatusCode}' from URL '{url}'.",
                    context.RequestAborted);
            }
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package http provides a set of HTTP Cloud Functions samples.
    package http
    
    import (
    	"fmt"
    	"net/http"
    	"time"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    var urlString = "https://example.com"
    
    // client is used to make HTTP requests with a 10 second timeout.
    // http.Clients should be reused instead of created as needed.
    var client = &http.Client{
    	Timeout: 10 * time.Second,
    }
    
    func init() {
    	functions.HTTP("MakeRequest", MakeRequest)
    }
    
    // MakeRequest is an example of making an HTTP request. MakeRequest uses a
    // single http.Client for all requests to take advantage of connection
    // pooling and caching. See https://godoc.org/net/http#Client.
    func MakeRequest(w http.ResponseWriter, r *http.Request) {
    	resp, err := client.Get(urlString)
    	if err != nil {
    		http.Error(w, "Error making request", http.StatusInternalServerError)
    		return
    	}
    	if resp.StatusCode != http.StatusOK {
    		msg := fmt.Sprintf("Bad StatusCode: %d", resp.StatusCode)
    		http.Error(w, msg, http.StatusInternalServerError)
    		return
    	}
    	fmt.Fprintf(w, "ok")
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.IOException;
    import java.io.PrintWriter;
    import java.net.URI;
    import java.net.http.HttpClient;
    import java.net.http.HttpResponse.BodyHandlers;
    import java.time.Duration;
    
    public class SendHttpRequest implements HttpFunction {
    
      // Create a client with some reasonable defaults. This client can be reused for multiple requests.
      // (java.net.httpClient also pools connections automatically by default.)
      private static HttpClient client =
          HttpClient.newBuilder().connectTimeout(Duration.ofSeconds(10)).build();
    
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException, InterruptedException {
        // Create a GET sendHttpRequest to "http://example.com"
        String url = "http://example.com";
        var getRequest = java.net.http.HttpRequest.newBuilder().uri(URI.create(url)).GET().build();
    
        // Send the sendHttpRequest using the client
        var getResponse = client.send(getRequest, BodyHandlers.ofString());
    
        // Write the results to the output:
        var writer = new PrintWriter(response.getWriter());
        writer.printf("Received code '%s' from url '%s'.", getResponse.statusCode(), url);
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const fetch = require('node-fetch');
    const functions = require('@google-cloud/functions-framework');
    
    /**
     * HTTP Cloud Function that makes an HTTP request
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('makeRequest', async (req, res) => {
      const url = 'https://example.com'; // URL to send the request to
      const externalRes = await fetch(url);
      res.sendStatus(externalRes.ok ? 200 : 500);
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Psr\Http\Message\ServerRequestInterface;
    use Psr\Http\Message\ResponseInterface;
    use GuzzleHttp\Client;
    use GuzzleHttp\Psr7\Response;
    
    function makeRequest(ServerRequestInterface $request): ResponseInterface
    {
        // This sample uses the GuzzleHTTP client
        // See its documentation for usage information
        // https://docs.guzzlephp.org/en/stable/
    
        // Specify the URL to send requests to
        $client = new Client([
            'base_uri' => 'https://example.com',
        ]);
    
        // Send the request
        $url_response = $client->get('/');
    
        $function_response = new Response(
            $url_response->getStatusCode(),
            [], // headers
            ''  // body
        );
    
        return $function_response;
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    
    @functions_framework.http
    def make_request(request):
        """
        HTTP Cloud Function that makes another HTTP request.
        Args:
            request (flask.Request): The request object.
            <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
        """
        import requests
    
        # The URL to send the request to
        url = "http://example.com"
    
        # Process the request
        response = requests.get(url)
        response.raise_for_status()
        return "Success!"
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    require "net/http"
    
    FunctionsFramework.http "concepts_requests" do |_request|
      url = "example.com"
      response = Net::HTTP.get_response url, "/"
      "Received code: #{response.code} from url: #{url}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
