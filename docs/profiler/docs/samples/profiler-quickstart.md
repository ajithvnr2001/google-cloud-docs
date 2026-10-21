---
url: https://docs.cloud.google.com/profiler/docs/samples/profiler-quickstart/
title: Go quickstart \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:07:32.936885+00:00
---

# Go quickstart  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/samples/profiler-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Samples ](https://docs.cloud.google.com/profiler/docs/samples)



#  Go quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Sample profiler_quickstart simulates a CPU-intensive workload for Cloud Profiler in Go.

## Code sample

### Go

For more information, see the [Profiler Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/profiler). 

To authenticate to Profiler, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample profiler_quickstart simulates a CPU-intensive workload for profiler.
    package main
    
    import (
    	"log"
    	"runtime"
    
    	"cloud.google.com/go/profiler"
    )
    
    func busyloop() {
    	for {
    		load()
    		// Make sure to yield so that the profiler thread
    		// gets some CPU time even on single core machines
    		// where GOMAXPROCS is 1. Not needed in real programs
    		// as typically the preemption happens naturally.
    		runtime.Gosched()
    	}
    }
    
    func load() {
    	for i := 0; i < (1 << 20); i++ {
    	}
    }
    
    func main() {
    	err := profiler.[Start](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/profiler/latest/index.html#cloud_google_com_go_profiler_Start)(profiler.[Config](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/profiler/latest/index.html#cloud_google_com_go_profiler_Config){
    		Service:              "hello-profiler",
    		NoHeapProfiling:      true,
    		NoAllocProfiling:     true,
    		NoGoroutineProfiling: true,
    		DebugLogging:         true,
    		// ProjectID must be set if not running on GCP.
    		// ProjectID: "my-project",
    	})
    	if err != nil {
    		log.Fatalf("failed to start the profiler: %v", err)
    	}
    	busyloop()
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudprofiler). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
