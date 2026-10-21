---
url: https://docs.cloud.google.com/run/docs/tutorials/resources/diagram-as-a-service.dot.txt
title: https://docs.cloud.google.com/run/docs/tutorials/resources/diagram-as-a-service.dot.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-15T09:04:57.958921+00:00
---

# https://docs.cloud.google.com/run/docs/tutorials/resources/diagram-as-a-service.dot.txt

> Source: https://docs.cloud.google.com/run/docs/tutorials/resources/diagram-as-a-service.dot.txt


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
