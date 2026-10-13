---
url: https://docs.cloud.google.com/java/docs/reference/grpc-gcp/latest/com.google.cloud.grpc.GcpChannelPrimer
title: Interface GcpChannelPrimer (1.17.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:48.412896+00:00
---

# Interface GcpChannelPrimer (1.17.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/grpc-gcp/latest/com.google.cloud.grpc.GcpChannelPrimer

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GcpChannelPrimer (1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.13.0  1.12.0  1.11.0 
    
    
    public interface GcpChannelPrimer

Primes delegate channels built by dynamic scale-up before they are published to the pool. The initial pool and non-dynamic growth are not primed.

## Methods 

### prime(ManagedChannel channel)
    
    
    public abstract ListenableFuture<Void> prime(ManagedChannel channel)

Issues a cheap, read-only end-to-end RPC on `channel` so its transport, TLS session, and server-side connection are established before the channel serves live traffic. Scale-up batches invoke this method concurrently across channels and publish each channel as soon as its own future succeeds. For example, a Cloud Spanner implementation can execute `SELECT 1`. Return a failed future to reject the attempt; the pool retries up to the configured attempt count and closes the channel when they are exhausted.

Implementations must observe the following:

  * **Return promptly and do the work inside the future.** Do not block in this method (no blocking stub, `ResultSet.next()`, `Future.get()`, or waiting on other threads). The configured prime timeout bounds each attempt as a whole: a future still pending at the timeout is cancelled and the attempt retried, while a call that is still blocked inside this method at the timeout fails the channel with no retry, because nothing can stop it. Such a call keeps occupying its primer thread and a scale-up slot until it returns. 
  * **Set an explicit, short deadline on the RPC** , for example ` stub.withDeadlineAfter(5, SECONDS)`. Do not rely on the default deadline: many Google Cloud APIs default to very long ones, such as one hour for Cloud Spanner's ` ExecuteStreamingSql`, so an unresponsive backend would leave the call lingering on the server long after the pool has given up on it. 
  * **Propagate cancellation to the gRPC call.** The pool calls ` future.cancel(true)` on the returned future when the attempt times out or the pool shuts down. Cancelling the future must cancel the underlying io.grpc.ClientCall or io.grpc.Context.CancellableContext so the stream and its server-side resources are released promptly. 
  * **Expect the channel to be shut down under a running call.** The pool may call ` shutdownNow()` on `channel` while this method is still running: when the call is still blocked at the timeout, or when the pool shuts down. A channel-shutdown status from an RPC on `channel` is then expected and is not a backend outage. 
  * **Tolerate concurrent calls for one channel.** A retry may overlap work from a cancelled future if that work does not promptly honor cancellation, so the implementation must be safe for multiple invocations on the same channel at once. 
  * **Keep the RPC trivial and side-effect free.** It should be strictly read-only and need minimal server work, such as `SELECT 1` or a lightweight ping. 



**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.ManagedChannel`  
the newly built, not yet published delegate channel to prime  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` | a future that succeeds when the priming RPC succeeds, or fails to reject the attempt  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
