---
url: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/reachability/
title: Measuring reachability \u00a0|\u00a0 Network Intelligence Center - Connectivity Tests \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:16.517349+00:00
---

# Measuring reachability  |  Network Intelligence Center - Connectivity Tests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/reachability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)



Send feedback 

#  Measuring reachability Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how Connectivity Tests measures reachability. It also explains how configuration analysis and live data plane analysis work.

## What is reachability?

A resource is _reachable_ from another endpoint if network configurations such as firewalls and routes allow traffic to get from one to the other. For example, if the network configuration should allow VM1 to send packets to VM2, then VM2 is said to be _reachable_ from VM1.

Note the following aspects about how Connectivity Tests measures reachability:

  * Connectivity Tests measures reachability from a particular source to a particular destination. The fact that VM1 can reach VM2 does not necessarily mean that VM3 can reach VM2.
  * Connectivity Tests measures unidirectional reachability. The fact that VM1 can open a connection to VM2 does not mean that VM2 can open a connection with VM1. Firewall rules might allow traffic in one direction, but not the other.
  * Connectivity Tests measures reachability for a particular protocol and destination port. The fact that VM1 can reach VM2 on `tcp:443` does not mean it can reach it on `tcp:80`.
  * Connectivity Tests only tests Google Cloud VPC network configurations that might affect packet delivery from the source to the destination. It does not check to see whether a valid server is running on the destination, whether operating system firewall rules might block the traffic, or if security software blocks a packet carrying a virus payload.



The concept of [Reachability](https://wikipedia.org/wiki/Reachability) originated in [graph theory](https://wikipedia.org/wiki/Graph_theory). Conceptually, the entire reachability graph of a network contains all of the endpoints as nodes, and directional edges that indicate reachability from source nodes to destination nodes.

_Reachability analysis_ is a more generic term that describes a body of analysis that can be conducted to determine network reachability. One of the use cases from a reachability analysis is a connectivity test. _Connectivity_ , in this case, refers to the state of network connections.

For every step along the network forwarding path, a reachability analysis tests and provides results for the underlying network configuration. For example, Connectivity Tests analyzes the Google Cloud firewall rules and routes that are applied to a simulated test packet.

## How Connectivity Tests works

Connectivity Tests includes two main components: a configuration analysis and live data plane analysis. This section describes how these two types of analyses work.

### How configuration analysis works

This section describes how Connectivity Tests and its components work.

Connectivity Tests performs a [reachability analysis](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#analyze-configurations) that evaluates the Google Cloud resources in your testing path against an ideal configuration model. It is augmented by the live data plane analysis feature, which sends packets to verify the state of the data plane and provide baseline information for supported configurations. For details about how live data plane analysis works, see How live data plane analysis works.

As a network administrator, you have control over many configurations that could impact the analysis result, although some exceptions apply. For example, you don't have control over VPC networks that host Google-managed services such as Cloud SQL instances. Additionally, because of permissions restrictions, you might not have control over hierarchical firewall policy rules that affect your network.

When you run a Connectivity Test, you input a specific set of parameters and receive formatted results in the form of a _network trace_ , or query. A Connectivity Test generates more than one trace if a test has multiple possible paths in the network (for example, when the destination endpoint is a Google Cloud load balancer with multiple backends).

  * A _match_ means that Connectivity Tests finds a Google Cloud configuration that allows the simulated packet to continue through the testing path.
  * _No match_ means that Connectivity Tests can't find a match. Thus, the configuration doesn't exist.
  * A _denied match_ means that Connectivity Tests finds a Google Cloud configuration where the simulated test packet must be dropped.



#### Connectivity Tests components

A Connectivity Test is the top-level component that contains all other testing sub-components needed for the configuration analysis. These components include the following:

  * Source and destination endpoints
  * Reachability details for the test and its traces, including an overall reachability result determined by the configuration analysis
  * One or more traces that each contain one or more steps
  * A state for each step



Each test has a unique name and each step has a state and `Info` metadata associated with it. For example, if a step checks a route, `RouteInfo` metadata is included in that step.

The following diagram shows a test from one Compute Engine VM instance to another. For descriptions of the test components, see the sections that follow.

[ ![State machine for a VM-to-VM trace.](https://docs.cloud.google.com/static/network-intelligence-center/docs/connectivity-tests/images/vm-2-vm-tracing-state-machine.svg)](https://docs.cloud.google.com/static/network-intelligence-center/docs/connectivity-tests/images/vm-2-vm-tracing-state-machine.svg) State machine for a VM-to-VM trace

#### Source and destination endpoints

The Connectivity Tests configuration analysis supports a 5-tuple packet header without the source port. This is because the source port is not used for validating resources in Google Cloud network configurations. Thus, you don't need to provide it when running tests.

The packet header contains the following components:

  * A network protocol
  * A source endpoint, consisting of one of the following: 
    * A VM instance name
    * A source IP address
    * A source App Engine service
    * A Cloud Run function (1st gen) environment
    * A Cloud Run service
    * A Cloud Run job
    * A Cloud SQL instance name
    * A cluster name for a GKE control plane
  * A destination endpoint, consisting of one of the following and a port number: 
    * A VM instance name
    * A destination IP address
    * A Cloud SQL instance name
    * A cluster name for a GKE control plane
    * A Private Service Connect endpoint

**Note:** You cannot select an [external server](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#terminology) as a Cloud SQL instance endpoint.

You can also specify a Google Cloud or non-Google Cloud network type or a combination of a network type and IP address or VM instance name to uniquely identify a network location.

The following networking protocols are supported for VM, IP address, and Google-managed services:

  * TCP
  * UDP
  * ICMP
  * ESP
  * AH
  * SCTP
  * IPIP



The following networking protocols are supported by Serverless VPC Access connectors:

  * TCP
  * UDP



Destination ports for the TCP or UDP protocols are supported. If you don't specify a port, the default setting is port `80`.

#### Traces, steps, and states

The configuration analysis contains one or more traces. Each trace represents one unique, simulated packet forwarding path in a test.

  * Each trace contains multiple ordered _steps_.
  * Each step contains a _state_ related to the Google Cloud configuration that Connectivity Tests checks for that step.
  * States are categorized into non-final and final states.



##### Non-final states

Non-final states represent a configuration check for each Google Cloud resource in the testing path, such as a VM instance, endpoint, firewall rule, route, or Google Cloud load balancer.

There are four non-final states:

  * Initial
  * Config checking
  * Forwarding
  * Transition



For more information, see [Configuration analysis states](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables#other_states).

##### Final state

Each trace must end with a final state, which is the last step in the trace.

There are four possible final states:

  * `Drop`
  * `Abort`
  * `Forward`
  * `Deliver`



Each state has a reason associated with it. For more information, see the [details for each final state](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables#final-state).

##### Overall reachability result

The configuration analysis also provides an overall reachability result that can take one of four values: `Reachable`, `Unreachable`, `Ambiguous`, or `Undetermined`.

Knowing the overall reachability result can be helpful for setting up monitoring or automation.

For more information, see [Overall reachability result](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables#reachability-result).

#### Spoof checking

Connectivity Tests performs a spoof check when a simulated packet to or from a VM instance uses an IP address not owned by that instance. IP addresses owned by a VM include all VM internal IP addresses and secondary IP addresses.

If the address is an address that appears to originate from external traffic, also called a foreign address, then the IP address fails the spoof check.

#### Metadata

Each state can have metadata associated with it in the form of an `Info` field. For example, `InstanceInfo` contains details for a VM instance, including the name and IP address.

The configuration analysis provides metadata for [the test itself](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables#result_metadata) and metadata for [each step in a test](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables#resource-metadata).

### How live data plane analysis works

The probing mechanism for live data plane analysis does not involve the guest OS and is fully transparent to the user. Probes are injected on behalf of the source endpoint to the network and are dropped just before being delivered to the destination endpoint. Probes are excluded from regular network billing, telemetry metrics, and flow logs.

## What's next

  * [Roles and permissions](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/access-control)

  * [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)

  * [Use Connectivity Tests for different connectivity use cases](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/common-use-cases)

  * [Detect invalid or inconsistent configurations](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/detecting-configs)

  * [Identify and fix ICMP issues](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/tutorials/tutorial-troubleshooting-workflow) (tutorial)

  * [Troubleshoot Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/troubleshooting)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
