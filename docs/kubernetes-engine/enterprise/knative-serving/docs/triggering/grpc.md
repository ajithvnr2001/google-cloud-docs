---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/triggering/grpc/
title: Invoking with gRPC \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:26.772333+00:00
---

# Invoking with gRPC  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/triggering/grpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Invoking with gRPC Stay organized with collections  Save and categorize content based on your preferences. 

This page shows Knative serving-specific details for developers who want to use [gRPC](https://grpc.io/) to connect a Knative serving service with other services, for example, to provide simple, high performance communication between internal microservices. Knative serving supports both unary and streaming gRPC calls.

### gRPC Unary

In a unary RPC call, the client sends a single request to the server and gets a single response back, similar to a normal function call: 
    
    
    rpc SayHello(HelloRequest) returns (HelloResponse);

OK

### gRPC Streaming

The following streaming options are available with gRPC. Server streaming RPCs where the client sends a request to the server and gets a stream to read containing a sequence of messages. The client reads the returned stream until there are no more messages. 
    
    
    rpc LotsOfReplies(HelloRequest) returns (stream HelloResponse);

Client streaming RPCs where the client writes a sequence of messages and sends them to the server in a stream. After the client finishes writing messages, it waits for the server to return its response. 
    
    
    rpc LotsOfGreetings(stream HelloRequest) returns (HelloResponse);

Bidirectional streaming RPCs where client and server send messages in two read-write streams that operate independently. 
    
    
    rpc BidiHello(stream HelloRequest) returns (stream HelloResponse);

OK

Possible use cases include:

  * Communication between internal microservices.
  * High loads of data (gRPC uses [protocol buffers](https://developers.google.com/protocol-buffers), which are up to seven times faster than REST calls).
  * Only a simple service definition is needed, you don't want to write a full client library.



To integrate your service with gRPC,

  * Define the request messages and responses in a proto file and compile them.
  * Create a gRPC server to handle requests and return responses: it should listen to the `PORT` environment variable.
  * Create a client that sends requests and handles responses from the gRPC server.
  * Optionally, add authentication.
  * Build and deploy your service.



## Defining and compiling messages in a proto file

There are no extra or Knative serving specific things to add to your proto definitions. Just as with any other use of gRPC, you use [gRPC protocol buffers](https://grpc.io/docs/guides/#working-with-protocol-buffers) for service definitions and data serialization.

## Creating a gRPC client

There are no extra or Knative serving specific things to add to a client that uses gRPC: follow the gRPC docs on using service definitions in [client code](https://grpc.io/docs/guides/concepts/#using-the-api), and the sample clients provided in the language-specific [gRPC tutorials](https://grpc.io/docs/languages).

## Listening for gRPC requests in a Knative serving service

The only special requirement for a gRPC server running in Knative serving is to listen at the port specified by the `PORT` environment variable as shown in the code:

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

To open a gRPC connection to a service so you can send gRPC messages, you need to specify the host domain, which is the URL of the Knative serving service or the custom domain [mapped](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains) to that service, along with the port 443, which is the port expected to be used by gRPC.

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
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
