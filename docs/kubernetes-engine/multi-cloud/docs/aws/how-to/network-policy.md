---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/network-policy/
title: Configure a network policy \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:43.893986+00:00
---

# Configure a network policy  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/network-policy/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Configure a network policy Stay organized with collections  Save and categorize content based on your preferences. 

This page demonstrates how to use cluster network policies to control whether a Pod can receive incoming (or Ingress) network traffic, and whether it can send outgoing (or Egress) traffic.

Network policies allow you to limit connections between Pod objects, so you can reduce exposure to attack.

Network policies act as a firewall on layer 3 or layer 4 of the [OSI model](http://wikipedia.org/wiki/OSI_model). They do not offer additional features such as authorization or encryption.

## Restricting incoming traffic to Pod objects

A [`NetworkPolicy` object](https://kubernetes.io/docs/concepts/services-networking/network-policies/) lets you configure network access policies for a Pod. `NetworkPolicy` objects contain the following information:

  * Pod objects the policy applies to. You define Pod objects and workloads with [labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

  * Type of traffic the network policy affects: Ingress for incoming traffic, Egress for outgoing traffic, or both.

  * For Ingress policies, which Pod objects can connect to the specified Pod objects.

  * For Egress policies, the Pod objects to which the specified Pod objects can connect.




### Example incoming traffic restriction

This section demonstrates the creation of an incoming traffic restriction on a sample application. Modify this example to suit your own application environment.

  1. Run a web server application with the label `app=hello` and expose it internally in the cluster:
         
         kubectl run hello-web --labels app=hello \
             --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0 \
             --port 8080 --expose
         

  2. Configure a `NetworkPolicy` to allow traffic to the `hello-web` Pod from only the `app=foo` Pod objects. GKE on AWS blocks incoming traffic from Pod objects that do not have this label, as well as external traffic, and traffic from Pod objects in a different Namespace.

The following manifest selects Pod objects with the label `app=hello` and specifies an Ingress policy to allow traffic only from Pod objects with the label `app=foo`:
         
         kind: NetworkPolicy
         apiVersion: networking.k8s.io/v1
         metadata:
           name: hello-allow-from-foo
         spec:
           policyTypes:
           - Ingress
           podSelector:
             matchLabels:
               app: hello
           ingress:
           - from:
             - podSelector:
                 matchLabels:
                   app: foo

  3. Apply this policy to the cluster:
         
         kubectl apply -f hello-allow-from-foo.yaml
         




### Verify the Ingress policy

  1. Run a temporary Pod with the label `app=foo`. To verify that incoming traffic is allowed, make a request to the `hello-web:8080` endpoint:
         
         kubectl run -l app=foo --image=alpine --restart=Never --rm -i -t foo-app \
             -- wget -qO- --timeout=2 http://hello-web:8080
         

If traffic from Pod `app=foo` to the `app=hello` Pod objects is enabled, the output looks like the following:
         
         Hello, world!
         Version: 1.0.0
         Hostname: hello-web-2258067535-vbx6z
         

  2. Run a temporary Pod with a different label (`app=other`) and make the same request to observe that the traffic is not allowed:
         
         kubectl run -l app=other --image=alpine --restart=Never --rm -i -t other-app \
             -- wget -qO- --timeout=2 http://hello-web:8080
         

The output confirms the connection doesn't receive a response:
         
         wget: download timed out
         




## Restrict outgoing traffic from Pod objects

You can restrict outgoing traffic just as you would incoming traffic.

However, to query internal hostnames such as `hello-web` or external hostnames such as `www.example.com`, you must create an Egress policy that allows DNS traffic on port 53 using TCP and UDP protocols.

To enable Egress network policies, deploy a `NetworkPolicy` controlling outbound traffic from Pod objects with the label `app=foo` while allowing traffic only to Pod objects with the label `app=hello`, as well as the DNS traffic.

The following manifest specifies a `NetworkPolicy` controlling Egress traffic from Pod objects with label `app=foo` with two allowed destinations:

  1. Pod objects in the same Namespace with the label `app=hello`
  2. Internal or external endpoints on port 53 (UDP and TCP)


    
    
    kind: NetworkPolicy
    apiVersion: networking.k8s.io/v1
    metadata:
      name: foo-allow-to-hello
    spec:
      policyTypes:
      - Egress
      podSelector:
        matchLabels:
          app: foo
      egress:
      - to:
        - podSelector:
            matchLabels:
              app: hello
      - ports:
        - port: 53
          protocol: TCP
        - port: 53
          protocol: UDP

Apply this policy to the cluster:
    
    
    kubectl apply -f foo-allow-to-hello.yaml
    

### Validate the Egress policy

  1. Deploy a new web application called `hello-web-2` and expose it internally in the cluster:
         
         kubectl run hello-web-2 --labels app=hello-2 \
           --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0 --port 8080 --expose
         

  2. Run a temporary Pod with the label `app=foo` and validate that the Pod can establish connections to `hello-web:8080`:
         
         kubectl run -l app=foo --image=alpine --rm -i -t --restart=Never foo-app \
           -- wget -qO- --timeout=2 http://hello-web:8080
         

The Pod responds to the request:
         
         Hello, world!
         Version: 1.0.0
         Hostname: hello-web-2258067535-vbx6z
         

  3. Validate that the Pod can't establish connections to `hello-web-2:8080`:
         
         kubectl run -l app=foo --image=alpine --rm -i -t --restart=Never foo-app \
             -- wget -qO- --timeout=2 http://hello-web-2:8080
         

The output confirms the connection doesn't receive a response:
         
         wget: download timed out
         

  4. Validate that the Pod can't establish connections to external websites such as `www.example.com`.
         
         kubectl run -l app=foo --image=alpine --rm -i -t --restart=Never foo-app \
             -- wget -qO- --timeout=2 http://www.example.com
         

The output confirms the connection doesn't receive a response:
         
         wget: download timed out
         




## Clean up

To remove the resources you created in this tutorial, run these commands:
    
    
    kubectl delete pods --labels app=hello-2
    kubectl delete pods --labels app=hello
    kubectl delete -f foo-allow-to-hello.yaml
    kubectl delete -f hello-allow-from-foo.yaml
    

## What's next

  * [Kubernetes Network Policies documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
  * Use [network policy logging](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/network-policy-logging) to record when connections to Pod objects are allowed or denied by your cluster's [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
