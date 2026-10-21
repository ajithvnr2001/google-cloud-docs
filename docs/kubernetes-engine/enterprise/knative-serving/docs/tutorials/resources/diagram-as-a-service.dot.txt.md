---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tutorials/resources/diagram-as-a-service.dot.txt
title: diagram as a service.dot
method: httpx-raw-text
fetched_at: 2026-10-17T08:52:06.516784+00:00
---

# diagram as a service.dot

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tutorials/resources/diagram-as-a-service.dot.txt

digraph daas {
  rankdir="LR"

  A [ color="red" label="User" ]
  B [ color="green" label="Web Service" ]
  C [ color="blue" label="Graphviz Dot CLI" ]

  A -> B [ label="http request" ]
  B -> C [ label="system call" ]
  C -> B [ label="results" ]
  B -> A [ label="http response" ]
}