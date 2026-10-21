---
url: https://docs.cloud.google.com/run/docs/triggering/grpc/
title: Using gRPC \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:39:47.885331+00:00
---

# Using gRPC  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/triggering/grpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Using gRPC Stay organized with collections  Save and categorize content based on your preferences. 

This page shows Cloud Run-specific details for developers who want to use [gRPC](https://grpc.io/) to connect a Cloud Run service with other services, for example, to provide simple, high performance communication between internal microservices. You can use [all gRPC types](https://grpc.io/docs/what-is-grpc/core-concepts#rpc-life-cycle), streaming or unary, with Cloud Run.

Possible use cases include:

  * Communication between internal microservices.
  * High loads of data (gRPC uses [protocol buffers](https://developers.google.com/protocol-buffers), which are up to seven times faster than REST calls).
  * Only a simple service definition is needed, you don't want to write a full client library.
  * Use streaming gRPCs in your gRPC server to build more responsive applications and APIs.



To integrate your service with gRPC:

  * Configure your service to use HTTP/2 if you are using streaming gRPC. HTTP/2 is the transport method for gRPC streaming.
  * Define the request messages and responses in a proto file and compile them.
  * Create a gRPC server to handle requests and return responses: it should listen to the `PORT` environment variable.
  * Create a client that sends requests and handles responses from the gRPC server.
  * Optionally, add authentication.
  * Build and deploy your service.



## Configuring your service to use HTTP/2

Google recommends [configuring your service to use HTTP/2](https://docs.cloud.google.com/run/docs/configuring/http2) if you use gRPC with Cloud Run. Although some simple gRPC features work without using HTTP/2, many gRPC features, such as streaming and metadata, require HTTP/2.

## Defining and compiling messages in a proto file

There are no extra or Cloud Run-specific things to add to your proto definitions. Just as with any other use of gRPC, you use [gRPC protocol buffers](https://grpc.io/docs/guides/#working-with-protocol-buffers) for service definitions and data serialization.

## Creating a gRPC client

There are no extra or Cloud Run specific things to add to a client that uses gRPC: follow the gRPC docs on using service definitions in [client code](https://grpc.io/docs/guides/concepts/#using-the-api), and the sample clients provided in the language-specific [gRPC tutorials](https://grpc.io/docs/languages).

## Autoscaling and load balancing

Cloud Run uses Google-managed load balancers that keep separate connections between clients and your Cloud Run instances. With gRPC, autoscaling behaves as follows:

  * gRPC connections from clients end at the edge load balancer. Adjusting `KeepAlive` settings only affects the connection to the load balancer, not the Cloud Run instances. The client doesn't recognize when an instance drops.
  * During scale-in, the load balancer closes connections by sending GOAWAY messages to the backend instances as they shut down.
  * During scale-out, the load balancer creates new connections to the backend instances. All these operations are transparent to clients.
  * During autoscaling, many instances can start up and multiplex into a single connection between the client and the proxy load balancer.
  * Concurrency is determined by the [maximum concurrent requests per instance](https://docs.cloud.google.com/run/docs/about-concurrency) for messages. In streaming, each stream is counted once against the maximum concurrent requests.



## Listening for gRPC requests in a Cloud Run service

The only special requirement for a gRPC server running in Cloud Run is to listen at the port specified by the `PORT` environment variable as shown in the following code:

###  Go 
    
    
    func main() {
    	log.Printf("grpc-ping: starting server...")
    
    	port := os.Getenv("PORT")
    	if port == "" {
    		port = "8080"
    		log.Printf("Defaulting to port %s", port)
    	}
    
    	listener, err := net.Listen("tcp", ":"+port)
    	if err != nil {
    		log.Fatalf("net.Listen: %v", err)
    	}
    
    	grpcServer := grpc.NewServer()
    	pb.RegisterPingServiceServer(grpcServer, &pingService{})
    	if err = grpcServer.Serve(listener); err != nil {
    		log.Fatal(err)
    	}
    }
    

## Opening a gRPC connection to a service

To open a gRPC connection to a service so you can send gRPC messages, you need to specify the host domain, which is the URL of the Cloud Run service or the custom domain [mapped](https://docs.cloud.google.com/run/docs/mapping-custom-domains) to that service, along with the port 443, which is the port expected to be used by gRPC.

###  Go 
    
    
    import (
    	"crypto/tls"
    	"crypto/x509"
    
    	"google.golang.org/grpc"
    	"google.golang.org/grpc/credentials"
    )
    
    // NewConn creates a new gRPC connection.
    // host should be of the form domain:port, e.g., example.com:443
    func NewConn(host string, insecure bool) (*grpc.ClientConn, error) {
    	var opts []grpc.DialOption
    	if host != "" {
    		opts = append(opts, grpc.WithAuthority(host))
    	}
    
    	if insecure {
    		opts = append(opts, grpc.WithInsecure())
    	} else {
    		// Note: On the Windows platform, use of x509.SystemCertPool() requires
    		// Go version 1.18 or higher.
    		systemRoots, err := x509.SystemCertPool()
    		if err != nil {
    			return nil, err
    		}
    		cred := credentials.NewTLS(&tls.Config{
    			RootCAs: systemRoots,
    		})
    		opts = append(opts, grpc.WithTransportCredentials(cred))
    	}
    
    	return grpc.Dial(host, opts...)
    }
    

## Sending gRPC requests without authentication

The following sample shows how to send a request without authentication, using a gRPC connection configured as mentioned previously.

###  Go 
    
    
    import (
    	"context"
    	"time"
    
    	pb "github.com/GoogleCloudPlatform/golang-samples/run/grpc-ping/pkg/api/v1"
    	"google.golang.org/grpc"
    )
    
    // pingRequest sends a new gRPC ping request to the server configured in the connection.
    func pingRequest(conn *grpc.ClientConn, p *pb.Request) (*pb.Response, error) {
    	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    	defer cancel()
    
    	client := pb.NewPingServiceClient(conn)
    	return client.Send(ctx, p)
    }
    

## Sending gRPC requests with authentication

The following sample shows how to use authentication between services, if the calling service has invoker permission to the receiving service. Notice that this code creates an authorization header that has the proper identity token: this is required. The required permissions and the authorization header are described in detail in [service to service authentication](https://docs.cloud.google.com/run/docs/authenticating/service-to-service).

###  Go 
    
    
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
    

## Sample code for gRPC streaming

For sample code, refer to the `RouteGuide` implementation in the [gRPC](https://grpc.io/) Basics tutorial for the language of your choice. When using Go, for example, refer to [Implementing RouteGuide](https://grpc.io/docs/languages/go/basics/#implementing-routeguide).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
