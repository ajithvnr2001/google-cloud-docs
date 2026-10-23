---
url: https://docs.cloud.google.com/load-balancing/docs/backend-service-load-testing/
title: Guidelines for load testing backend services with Application Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:39.682975+00:00
---

# Guidelines for load testing backend services with Application Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/backend-service-load-testing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Guidelines for load testing backend services with Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

While integrating a backend service with Application Load Balancer, it's important to measure the performance of a backend service on its own, in the absence of a load balancer. Load testing under controlled conditions helps you assess capacity-planning trade-offs between different dimensions of performance, such as throughput and latency. Because careful capacity planning could still underestimate actual demand, we recommend that you use load tests to proactively determine how the availability of a service is affected when the system is overloaded.

### Load testing goals

A typical load test measures the externally visible behavior of the backend service under different dimensions of load. Some of the most relevant dimensions of this testing are as follows:

  * **Request throughput:** The number of requests served per second.
  * **Request concurrency:** The number of requests processed concurrently.
  * **Connection throughput:** The number of connections initiated by clients per second. Most services that use Transport Layer Security (TLS) have some network transport and TLS negotiation overhead associated with each connection that is independent of request processing.
  * **Connection concurrency:** The number of client connections processed concurrently.

**Note:** This number might be lower than the request concurrency because HTTPS clients often reuse connections for multiple requests. Note that connections consume system resources (such as RAM and file handles) even when they are not serving requests.
  * **Request latency:** The total elapsed time between the beginning of the request and the end of the response.

  * **Error rate:** How often requests cause errors, such as HTTP 5xx errors and prematurely closed connections.




To assess the health of the server under load, a load test procedure might also collect the following internal service metrics:

  * **Use of system resources:** System resources, such as CPU, RAM, and file handles (sockets), are typically expressed in percentage.

The importance of these metrics differs based on how the service is implemented. Applications experience reduced performance, shed load, or crash when they exhaust their resources. Therefore, it becomes essential to determine the availability of resources when a host is under heavy load.

  * **Use of other bounded resources:** Non-system resources that could be depleted under load, such as at the application layer.

Some examples of such resources include the following:

    * A bounded pool of worker threads or processes.
    * For an application server using threads, it's common to limit the number of worker threads operating concurrently. Thread pool size limits are useful for preventing memory and CPU exhaustion, but default settings are often very conservative. Limits that are too low might prevent adequate use of system resources.
    * Some servers use process pools, instead of thread pools. For example, an Apache server when set up with the [Prefork Multi-Processing Model](https://httpd.apache.org/docs/2.4/mod/prefork.html), assigns one process to each client connection. So, the size limit of the pool determines the upper bound on connection concurrency.
    * A service deployed as a frontend to another service that has a backend connection pool of bounded size.



## Capacity planning versus overload testing

Load-testing tools help you measure different scaling dimensions individually. For capacity planning, determine the load threshold for the acceptable performance in multiple dimensions. For example, instead of measuring the absolute limit of a service request throughout, consider measuring the following:

  * The request rate at which the service can serve with 99th-percentile latency that is less than a specified number of milliseconds. The number is specified by the SLO of the service.
  * The maximum request rate that doesn't cause system resource utilization to exceed optimal levels. Note that the optimal utilization varies by application and could be significantly less than 100%. For example, at 80% peak memory utilization, the application might be able to handle minor load spikes better than if the peak utilization were at 99%.



While it's important to use load test results to form capacity planning decisions, it's equally important to understand how a service behaves when load exceeds capacity. Some server behaviors that are often evaluated using overload tests are as follows:

  * Load-shedding: When a service receives excessive incoming requests or connections, it could respond by slowing down all requests, or by rejecting some requests to maintain acceptable performance for the remaining ones. We recommend the latter approach to prevent client timeouts before receiving a response and to reduce the risk of memory exhaustion by lowering request concurrency on the server.

  * Resilience against resource exhaustion: A service generally avoids crashing from resource exhaustion because it's difficult for pending requests to make further progress if the service has crashed. If a backend service has many instances, the robustness of individual instances is vital for overall availability of the service. While an instance restarts from a crash, other instances might experience more load, potentially causing cascade failure.




## General testing guidelines

While defining your test cases, consider the following guidelines.

**Note:** The guidelines listed in this section are not applicable to every service, and the list is not exhaustive. For more information, see the [best benchmarking practices](https://www.envoyproxy.io/docs/envoy/latest/faq/performance/how_to_benchmark_envoy) page maintained by the Envoy project. The page contains many suggestions that are relevant to load testing of any HTTPS service.

### Create small-scale tests

Create small-scale tests to measure the performance limits of the server. With excessive server capacity, there's a risk that a test won't reveal the performance limits of the service itself, but might uncover bottlenecks in other systems, such as the client hosts or the network layer.

For best results, consider a test case that uses a single virtual machine (VM) instance or a Google Kubernetes Engine (GKE) Pod to independently test the service. To achieve full load on the server, if necessary, you can use multiple VMs, but remember they can complicate the collection of performance data.

### Choose open-loop load patterns

Most load generators use the closed-loop pattern to limit the number of concurrent requests and delay new requests until the previous ones are complete. We don't recommend this approach because production clients of the service might not exhibit such throttling behavior.

In contrast, the open-loop pattern enables load generators to simulate the production load by sending requests at a steady rate, independent of the rate at which server responses arrive.

## Run tests using recommended load generators

We recommend the following load generators for the load testing of the backend service:

### Nighthawk

[Nighthawk](https://github.com/envoyproxy/nighthawk) is an open-source tool developed in coordination with the Envoy project. You can use it to generate client load, [visualize benchmarks](https://github.com/envoyproxy/nighthawk/blob/main/README.md#visualizing-the-output-of-a-benchmark), and measure server performance for most load-testing scenarios of HTTPS services.

#### Test HTTP/1

To test HTTP/1, use the following command:
    
    
    nighthawk_client URI \
        --duration DURATION \
        --open-loop \
        --no-default-failure-predicates \
        --protocol http1 \
        --request-body-size REQ_BODY_SIZE \
        --concurrency CONCURRENCY \
        --rps RPS \
        --connections CONNECTIONS
    

Replace the following:

  * `URI`: the URI to benchmark
  * `DURATION`: total test run time in seconds
  * `REQ_BODY_SIZE`: size of the POST payload in each request
  * `CONCURRENCY`: the total number of concurrent event loops

This number should match the core count of the client VM

  * `RPS`: the target rate of requests per second, per event loop

  * `CONNECTIONS`: the number of concurrent connections, per event loop


**Note:** The `no-default-failure-predicates` flag is new. Use the latest Nighthawk build to test it.

See the following example:
    
    
    nighthawk_client http://10.20.30.40:80 \
        --duration 600 --open-loop --no-default-failure-predicates \
        --protocol http1 --request-body-size 5000 \
        --concurrency 16 --rps 500 --connections 200
    

The output of each test run provides a histogram of response latencies. In the [example from the Nighthawk documentation](https://github.com/envoyproxy/nighthawk#a-sample-benchmark-run) , notice that the 99th-percentile latency is approximately 135 microseconds.
    
    
    Initiation to completion
        samples: 9992
        mean:    0s 000ms 113us
        pstdev:  0s 000ms 061us
    
        Percentile  Count       Latency
        0           1           0s 000ms 077us
        0.5         4996        0s 000ms 115us
        0.75        7495        0s 000ms 118us
        0.8         7998        0s 000ms 118us
        0.9         8993        0s 000ms 121us
        0.95        9493        0s 000ms 124us
        0.990625    9899        0s 000ms 135us
        0.999023    9983        0s 000ms 588us
        1           9992        0s 004ms 090us
    

#### Test HTTP/2

To test HTTP/2, use the following command:
    
    
    nighthawk_client URI \
        --duration DURATION \
        --open-loop \
        --no-default-failure-predicates \
        --protocol http2 \
        --request-body-size REQ_BODY_SIZE \
        --concurrency CONCURRENCY \
        --rps RPS \
        --max-active-requests MAX_ACTIVE_REQUESTS \
        --max-concurrent-streams MAX_CONCURRENT_STREAMS
    

Replace the following:

  * `URI`: the URI to benchmark
  * `DURATION`: total test run time in seconds
  * `REQ_BODY_SIZE`: size of the POST payload in each request
  * `CONCURRENCY`: the total number of concurrent event loops

This number should match the core count of the client VM

  * `RPS`: the target rate of requests per second for each event loop

  * `MAX_ACTIVE_REQUESTS`: the maximum number of concurrent active requests for each event loop

  * `MAX_CONCURRENT_STREAMS`: the maximum number of concurrent streams allowed on each HTTP/2 connection




See the following example:
    
    
    nighthawk_client http://10.20.30.40:80 \
        --duration 600 --open-loop --no-default-failure-predicates \
        --protocol http2 --request-body-size 5000 \
        --concurrency 16 --rps 500 \
        --max-active-requests 200 --max-concurrent-streams 1
    

### ab (Apache benchmark tool)

[`ab`](https://httpd.apache.org/docs/2.4/programs/ab.html) is a less flexible alternative to Nighthawk, but it's available as a package on almost every Linux distribution. `ab` is only recommended for quick and simple tests.

To install `ab`, use the following command:

  * On Debian and Ubuntu, run `sudo apt-get install apache2-utils`.
  * On RedHat-based distributions, run `sudo yum install httpd-utils`.



After you've installed `ab`, use the following command to run it:
    
    
    ab -c CONCURRENCY \
        -n NUM_REQUESTS \
        -t TIMELIMIT \
        -p POST_FILE URI
    

Replace the following:

  * `CONCURRENCY`: number of concurrent requests to perform
  * `NUM_REQUESTS`: number of requests to perform
  * `TIMELIMIT`: maximum number of seconds to spend on requests
  * `POST_FILE`: local file containing the HTTP POST payload
  * `URI`: the URI to benchmark



See the following example:
    
    
    ab -c 200 -n 1000000 -t 600 -p body http://10.20.30.40:80
    

The command in the preceding example sends requests with a concurrency of 200 (closed-loop pattern), and stops after either 1,000,000 (one million) requests or 600 seconds of elapsed time. The command also includes the contents of the file `body` as an HTTP POST payload.

The `ab` command produces response latency histograms similar to those as Nighthawk, but its resolution is limited to milliseconds, instead of microseconds:
    
    
    Percentage of the requests served within a certain time (ms)
        50%     7
        66%     7
        75%     7
        80%     7
        90%    92
        95%   121
        98%   123
        99%   127
        100%  156 (longest request)
    

## What's next

  * [Capacity management with load balancing](https://docs.cloud.google.com/load-balancing/docs/tutorials/capacity-management-with-load-balancing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
