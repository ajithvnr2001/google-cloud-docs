---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-grpc-conn/
title: Open a gRPC connection to a service \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:10.793570+00:00
---

# Open a gRPC connection to a service  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-grpc-conn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Open a gRPC connection to a service Stay organized with collections  Save and categorize content based on your preferences. 

Function to create a new gRPC connection.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Invoking with gRPC](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/triggering/grpc)
  * [Using gRPC](https://docs.cloud.google.com/run/docs/triggering/grpc)



## Code sample

### Go

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
