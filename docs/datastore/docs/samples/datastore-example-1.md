---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-example-1/
title: Datastore Example 1 \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:12.020010+00:00
---

# Datastore Example 1  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-example-1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Datastore Example 1 Stay organized with collections  Save and categorize content based on your preferences. 

Datastore Example showing setup

## Code sample

### Go

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func TestWithdrawLowBal(t *testing.T) {
    	ctx, done, err := aetest.NewContext()
    	if err != nil {
    		t.Fatal(err)
    	}
    	defer done()
    	key := datastore.NewKey(ctx, "BankAccount", "", 1, nil)
    	if _, err := datastore.Put(ctx, key, &BankAccount{100}); err != nil {
    		t.Fatal(err)
    	}
    
    	err = withdraw(ctx, "myid", 128, 0)
    	if err == nil || err.Error() != "insufficient funds" {
    		t.Errorf("Error: %v; want insufficient funds error", err)
    	}
    
    	b := BankAccount{}
    	if err := datastore.Get(ctx, key, &b); err != nil {
    		t.Fatal(err)
    	}
    	if bal, want := b.Balance, 100; bal != want {
    		t.Errorf("Balance %d, want %d", bal, want)
    	}
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
