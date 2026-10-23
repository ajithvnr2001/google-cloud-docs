---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-grpc-request-auth/
title: Send gRPC requests with authentication \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:34.812975+00:00
---

# Send gRPC requests with authentication  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-grpc-request-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Send gRPC requests with authentication Stay organized with collections  Save and categorize content based on your preferences. 

Sends a request with an authorization header using a gRPC connection.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Using gRPC](https://docs.cloud.google.com/run/docs/triggering/grpc)



## Code sample

### Go

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"time"
    
    	"google.golang.org/api/idtoken"
    	"google.golang.org/grpc"
    	grpcMetadata "google.golang.org/grpc/metadata"
    
    	pb "github.com/GoogleCloudPlatform/golang-samples/run/grpc-ping/pkg/api/v1"
    )
    
    // pingRequestWithAuth mints a new Identity Token for each request.
    // This token has a 1 hour expiry and should be reused.
    // audience must be the auto-assigned URL of a Cloud Run service or HTTP Cloud Function without port number.
    func pingRequestWithAuth(conn *grpc.ClientConn, p *pb.Request, audience string) (*pb.Response, error) {
    	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    	defer cancel()
    
    	// Create an identity token.
    	// With a global TokenSource tokens would be reused and auto-refreshed at need.
    	// A given TokenSource is specific to the audience.
    	tokenSource, err := idtoken.NewTokenSource(ctx, audience)
    	if err != nil {
    		return nil, fmt.Errorf("idtoken.NewTokenSource: %w", err)
    	}
    	token, err := tokenSource.Token()
    	if err != nil {
    		return nil, fmt.Errorf("TokenSource.Token: %w", err)
    	}
    
    	// Add token to gRPC Request.
    	ctx = grpcMetadata.AppendToOutgoingContext(ctx, "authorization", "Bearer "+token.AccessToken)
    
    	// Send the request.
    	client := pb.NewPingServiceClient(conn)
    	return client.Send(ctx, p)
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
