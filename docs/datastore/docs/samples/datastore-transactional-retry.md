---
url: https://docs.cloud.google.com/datastore/docs/samples/datastore-transactional-retry/
title: Retry \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:21:29.464417+00:00
---

# Retry  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/samples/datastore-transactional-retry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Samples ](https://docs.cloud.google.com/datastore/docs/samples)



#  Retry Stay organized with collections  Save and categorize content based on your preferences. 

Retry a transaction.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Datastore Transactions](https://docs.cloud.google.com/datastore/docs/concepts/cloud-datastore-transactions)
  * [Transactions](https://docs.cloud.google.com/datastore/docs/concepts/transactions)



## Code sample

### C#

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /// <summary>
    /// Retry the action when a Grpc.Core.RpcException is thrown.
    /// </summary>
    private T RetryRpc<T>(Func<T> action)
    {
        List<Grpc.Core.RpcException> exceptions = null;
        var delayMs = _retryDelayMs;
        for (int tryCount = 0; tryCount < _retryCount; ++tryCount)
        {
            try
            {
                return action();
            }
            catch (Grpc.Core.RpcException e)
            {
                if (exceptions == null)
                    exceptions = new List<Grpc.Core.RpcException>();
                exceptions.Add(e);
            }
            System.Threading.Thread.Sleep(delayMs);
            delayMs *= 2;  // Exponential back-off.
        }
        throw new AggregateException(exceptions);
    }
    
    private void RetryRpc(Action action)
    {
        RetryRpc(() => { action(); return 0; });
    }
    
    [Fact]
    public void TestTransactionalRetry()
    {
        int tryCount = 0;
        var keys = UpsertBalances();
        RetryRpc(() =>
        {
            using (var transaction = _db.BeginTransaction())
            {
                TransferFunds(keys[0], keys[1], 10, transaction);
                // Insert a conflicting transaction on the first try.
                if (tryCount++ == 0)
                    TransferFunds(keys[1], keys[0], 5);
                transaction.Commit();
            }
        });
        Assert.Equal(2, tryCount);
    }

### Go

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Go API reference documentation](https://cloud.google.com/go/docs/reference/cloud.google.com/go/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    type BankAccount struct {
    	Balance int
    }
    
    const amount = 50
    _, err := client.RunInTransaction(ctx, func(tx *datastore.Transaction) error {
    	keys := []*datastore.Key{to, from}
    	accs := make([]BankAccount, 2)
    	if err := tx.GetMulti(keys, accs); err != nil {
    		return err
    	}
    	accs[0].Balance += amount
    	accs[1].Balance -= amount
    	_, err := tx.PutMulti(keys, accs)
    	return err
    })

### Java

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datastore/latest/history). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    int retries = 5;
    while (true) {
      try {
        transferFunds(fromKey, toKey, 10);
        break;
      } catch (DatastoreException e) {
        if (retries == 0) {
          throw e;
        }
        --retries;
      }
    }
    // Retry handling can also be configured and automatically applied using google-cloud-java.

### PHP

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $retries = 5;
    for ($i = 0; $i < $retries; $i++) {
        try {
            require_once __DIR__ . '/transfer_funds.php';
            transfer_funds($fromKeyId, $toKeyId, 10, $namespaceId);
        } catch (\Google\Cloud\Core\Exception\ConflictException $e) {
            // if $i >= $retries, the failure is final
            continue;
        }
        // Succeeded!
        break;
    }

### Python

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Python API reference documentation](https://cloud.google.com/python/docs/reference/datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
    
    # For help authenticating your client, visit
    # https://cloud.google.com/docs/authentication/getting-started
    client = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html)()
    
    import google.cloud.exceptions
    
    for _ in range(5):
        try:
            transfer_funds(client, account1.key, account2.key, 50)
            break
        except google.cloud.exceptions.Conflict:
            continue
    else:
        print("Transaction failed.")

### Ruby

To learn how to install and use the client library for Datastore mode, see [Datastore mode client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries). For more information, see the [Datastore mode Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest). 

To authenticate to Datastore mode, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    (1..5).each do |i|
      begin
        return transfer_funds from_key, to_key, amount
      rescue Google::Cloud::Error => e
        raise e if i == 5
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datastore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
