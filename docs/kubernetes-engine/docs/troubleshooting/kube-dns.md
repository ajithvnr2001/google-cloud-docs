---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/kube-dns/
title: Troubleshoot kube-dns in GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:21.338167+00:00
---

# Troubleshoot kube-dns in GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/kube-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot kube-dns in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

If you use kube-dns for service discovery, you might experience connection errors such as `dial tcp: i/o timeout` or `no such host`. Such errors often indicate problems with the kube-dns Pods in the `kube-system` namespace, such as incorrect configurations, resource limitations, or network connectivity issues affecting these Pods.

Use this page to diagnose and resolve common issues specific to the kube-dns deployment, helping to ensure reliable DNS resolution for your workloads.

This information is important for Platform admins and operators, who are responsible for maintaining core cluster components like kube-dns, and for Application developers, whose applications depend on it to connect with other services within the cluster. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Identify the source of DNS issues in kube-dns

The following sections help you diagnose why kube-dns is having difficulty resolving queries.

### Check if kube-dns Pods are running

Kube-dns Pods are critical for name resolution within the cluster. If they're not running you're likely to experience issues with DNS resolution.

To verify that the kube-dns Pods are running without any recent restarts, view the status of these Pods:
    
    
    kubectl get pods -l k8s-app=kube-dns -n kube-system
    

The output is similar to the following:
    
    
    NAME                   READY          STATUS          RESTARTS       AGE
    kube-dns-POD_ID_1      5/5            Running         0              16d
    kube-dns-POD_ID_2      0/5            Terminating     0              16d
    

In this output, `POD_ID_1` and `POD_ID_2` represent unique identifiers that are automatically appended to the kube-dns Pods.

If your output shows that any of your kube-dns Pods don't have a status of `Running`, work though the following steps:

  1. Use the Admin Activity audit logs to investigate if there's been any recent changes such as cluster or node pool version upgrades, or changes to the kube-dns ConfigMap. To learn more about audit logs, see [GKE audit logging information](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging). If you find changes, revert them and view the status of the Pods again.

  2. If you don't find any relevant recent changes, investigate if you're experiencing an OOM error on the node that the kube-dns Pod runs on. If you see an error similar to the following in your Cloud Logging log messages, then these Pods are experiencing an OOM error:
         
         Warning: OOMKilling Memory cgroup out of memory
         

This message indicates that Kubernetes terminated a process due to excessive resource consumption. Kubernetes schedules Pods based on resource requests, but lets Pods consume up to their resource limits. If limits are higher than the requests or there are no limits, the Pod's resource usage can exceed the resources of the system.

To resolve this error, you can either delete the problematic workloads, or set memory or CPU limits. To learn more about setting limits, see [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers) in the Kubernetes documentation. For more information about OOM events, see [Troubleshoot OOM events](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/oom-events).

  3. If you don't find any OOM error messages, restart the kube-dns Deployment:
         
         kubectl rollout restart deployment/kube-dns --namespace=kube-system
         

After you've restarted the Deployment, check if your kube-dns Pods are running.




If these steps don't work, or all of your kube-dns Pods have a status of `Running`, but you're still having DNS issues, check that the `/etc/resolv.conf` file is configured correctly.

### Check that `/etc/resolv.conf` is configured correctly

Review the `/etc/resolv.conf` file of the Pods experiencing DNS issues and make sure that the entries it contains are correct:

  1. View the `/etc/resolv.conf` file of the Pod:
         
         kubectl exec -it POD_NAME -- cat /etc/resolv.conf
         

Replace POD_NAME with the name of the Pod that's experiencing DNS issues. If there are multiple Pods that are experiencing issues, repeat the steps in this section for each Pod.

If the Pod binary doesn't support the `kubectl exec` command, this command might fail. If this happens, [create a simple Pod to use as a test environment](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/#create-a-simple-Pod-to-use-as-a-test-environment). This procedure lets you run a test Pod in the same namespace as your problematic Pod.

  2. Verify that the name server IP address in `/etc/resolv.conf` file is correct:

     * Pods that are using a host network should use the values in the node's `/etc/resolv.conf` file. The name server IP address should be `169.254.169.254`.
     * For Pods that aren't using a host network, the kube-dns Service IP address should be the same as the name server IP address. To compare the IP addresses, complete the following steps:

       1. Get the IP address of the kube-dns Service:
              
              kubectl get svc kube-dns -n kube-system
              

The output is similar to the following:
              
              NAME       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)         AGE
              kube-dns   ClusterIP   192.0.2.10   <none>        53/UDP,53/TCP   64d
              

       2. Make note of the value in the Cluster IP column. In this example, it's `192.0.2.10`.

       3. Compare the kube-dns Service IP address with the IP address from the `/etc/resolv.conf` file:
              
              # cat /etc/resolv.conf
              
              search default.svc.cluster.local svc.cluster.local cluster.local c.PROJECT_NAME google.internal
              **nameserver 192.0.2.10**
              options ndots:5
              

In this example, the two values match, so an incorrect name server IP address isn't the cause of your problem.

However, if the IP addresses don't match, that means that a [`dnsConfig`](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-dns-config) field is configured in the manifest of the application Pod.

If the value in the `dnsConfig.nameservers` field is correct, investigate your DNS server and make sure it's functioning correctly.

If you don't want to use the custom name server, remove the field and perform a rolling restart of the Pod:
              
              kubectl rollout restart deployment POD_NAME
              

Replace `POD_NAME` with the name of your Pod.

  3. Verify the `search` and `ndots` entries in `/etc/resolv.conf`. Make sure there are no spelling errors, stale configurations and the failing request points to existing service in the correct namespace.




### Perform a DNS lookup

After you've confirmed that `/etc/resolv.conf` is configured correctly and the DNS record is correct, use the dig command-line tool to perform DNS lookups from the Pod that's reporting DNS errors:

  1. Directly query a Pod by opening a shell inside of it:
         
         kubectl exec -it POD_NAME -n NAMESPACE_NAME -- SHELL_NAME
         

Replace the following:

     * `POD_NAME`: the name of Pod that's reporting DNS errors.
     * `NAMESPACE_NAME`: the namespace that the Pod belongs to.
     * `SHELL_NAME`: The name of the shell that you want to open. For example, `sh` or `/bin/bash`.

This command might fail if your Pod doesn't permit the `kubectl exec` command or if the Pod doesn't have the dig binary. If this happens, create a test Pod with an image that has dig installed:
    
    kubectl run "test-$RANDOM" ti --restart=Never --image=thockin/dnsutils - bash
    

  2. Check if the Pod can correctly resolve the internal DNS Service of the cluster:
         
         dig kubernetes
         

Because the `/etc/resolv.conf` file is pointing to the kube-dns Service IP address, when you run this command the DNS server is the kube-dns Service.

You should see a successful DNS response with the IP address of the Kubernetes API Service (often something like `10.96.0.1`). If you see `SERVFAIL` or no response, this usually indicates that the kube-dns Pod is unable to resolve the internal service names.

  3. Check if the kube-dns Service can resolve an external domain name:
         
         dig example.com
         

  4. If you're experiencing difficulties with a particular kube-dns Pod responding to DNS queries, check if that Pod can resolve an external domain name:
         
         dig example.com @KUBE_DNS_POD_IP
         

Replace `KUBE_DNS_POD_IP` with the IP address of the kube-dns Pod. If you don't know the value of this IP address, run the following command:
         
         kubectl get pods -n kube-system -l k8s-app=kube-dns -o wide
         

The IP address is in the `IP` column.

If the resolution of the command is successful, then you see `status: NOERROR` and details of the A record as shown in the following example:
         
         ; <<>> DiG 9.16.27 <<>> example.com
          ;; global options: +cmd
          ;; Got answer:
          ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 31256
          ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
         
          ;; OPT PSEUDOSECTION:
          ; EDNS: version: 0, flags:; udp: 512
          ;; QUESTION SECTION:
          ;example.com.                   IN      A
         
          ;; ANSWER SECTION:
          example.com.            30      IN      A       93.184.215.14
         
          ;; Query time: 6 msec
          ;; SERVER: 10.76.0.10#53(10.76.0.10)
          ;; WHEN: Tue Oct 15 16:45:26 UTC 2024
          ;; MSG SIZE  rcvd: 56
         

  5. Exit the shell:
         
         exit
         




If any of these commands fail, perform a rolling restart of the kube-dns Deployment:
    
    
    kubectl rollout restart deployment/kube-dns --namespace=kube-system
    

After you've completed the restart, re-try the dig commands and see if they now succeed. If they still fail, proceed to take a packet capture.

### Take a packet capture

Take a packet capture to verify if the DNS queries are being received and answered appropriately by the kube-dns Pods:

  1. Using SSH, connect to the node running the kube-dns Pod. For example:

     1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

     2. Locate the node that you want to connect to. If you don't know the name of the node on your kube-dns Pod, run the following command:
            
            kubectl get pods -n kube-system -l k8s-app=kube-dns -o wide
            

The name of the node is listed in the **Node** column.

     3. In the **Connect** column, click **SSH**.

  2. In the terminal, start [toolbox](https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox); a pre-installed debugging tool:
         
         toolbox
         

  3. At the root prompt, install the `tcpdump` package:
         
         apt update -y && apt install -y tcpdump
         

  4. Using `tcpdump`, take a packet capture of your DNS traffic:
         
         tcpdump -i eth0 port 53" -w FILE_LOCATION
         

Replace `FILE_LOCATION` with a path to where you want to save the capture.

  5. Review the packet capture. Check if there are packets with destination IP addresses that match the kube-dns Service IP address. This helps ensure that the DNS requests are reaching the right destination for resolution. Failure to see DNS traffic landing on the correct Pods, might indicate presence of a network policy that's blocking the requests.




### Check for a network policy

Restrictive network policies can sometimes disrupt DNS traffic. To verify if a network policy exists in the kube-system namespace, run the following command:
    
    
    kubectl get networkpolicy -n kube-system
    

If you find a network policy, review it and ensure the policy allows necessary DNS communication. For example, if you have a network policy which blocks all egress traffic, the policy would also block DNS requests.

If the output is `No resources found in kube-system namespace` then you don't have any network policies and you can rule this out as the cause of your issue. Investigating logs can help you find more points of failure.

### Enable temporary DNS query logging

To help you identify issues such incorrect DNS responses, temporarily enable debug logging of DNS queries. To enable queries, create a Pod based on an existing kube-dns Pod. Any changes to the kube-dns Deployment are automatically reverted.

Enabling temporary DNS query logging is a resource intensive procedure, so we recommend that you delete the Pod you create as soon as you collect a suitable sample of logs.

To enable temporary DNS query logging, complete the following steps:

  1. Retrieve a kube-dns Pod and store it in variable named `POD`:
         
         POD=$(kubectl -n kube-system get pods --selector=k8s-app=kube-dns -o jsonpath="{.items[0].metadata.name}")
         

  2. Create a Pod named `kube-dns-debug`. This Pod is a copy of the Pod stored in the `POD` variable, but with dnsmasq logging enabled. This command doesn't modify the original kube-dns Pod:
         
         kubectl apply -f <(kubectl get pod -n kube-system ${POD} -o json | jq -e '
         
         (
         
         (.spec.containers[] | select(.name == "dnsmasq") | .args) += ["--log-queries"]
         
         )
         
         | (.metadata.name = "kube-dns-debug")
         
         | (del(.metadata.labels."pod-template-hash"))
         
         ')
         

  3. Inspect the logs:
         
         kubectl logs -f --tail 100 -c dnsmasq -n kube-system kube-dns-debug
         

You can also see the queries in Cloud Logging.

  4. After you finish viewing DNS query logs, delete the `kube-dns-debug` Pod:
         
         kubectl -n kube-system delete pod kube-dns-debug
         




### Investigate the kube-dns Pod

Review how kube-dns Pods receive and resolve DNS queries with Cloud Logging.

To view log entries related to the kube-dns Pod, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the query pane, enter the following filter to view events related to the kube-dns container:
         
         resource.type="k8s_container"
         resource.labels.namespace_name="kube-system"
         resource.labels.pod_name:"kube-dns"
         resource.labels.cluster_name="CLUSTER_NAME"
         resource.labels.location="CLUSTER_LOCATION"
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster that the kube-dns Pod belongs to.
     * `CLUSTER_LOCATION`: the location of your cluster.
  3. Click **Run query**.

  4. Review the output. The following example output shows one possible error that you might see:
         
         {
            "timestamp": "2024-10-10T15:32:16.789Z",
            "severity": "ERROR",
            "resource": {
               "type": "k8s_container",
               "labels": {
               "namespace_name": "kube-system",
               "pod_name": "kube-dns",
               "cluster_name": "CLUSTER_NAME",
               "location": "CLUSTER_LOCATION"
               }
            },
            "message": "Failed to resolve 'example.com': Timeout."
         },
         

In this example, kube-dns couldn't resolve `example.com` in a reasonable time. This type of error can be caused by multiple issues. For example, the upstream server might be incorrectly configured in the kube-dns ConfigMap, or there might be high network traffic.




If you don't have Cloud Logging enabled, view the Kubernetes logs instead:
    
    
    Pod=$(kubectl get Pods -n kube-system -l k8s-app=kube-dns -o name | head -n1)
    kubectl logs -n kube-system $Pod -c dnsmasq
    kubectl logs -n kube-system $Pod -c kubedns
    kubectl logs -n kube-system $Pod -c sidecar
    

### Investigate recent changes in the kube-dns ConfigMap

If you suddenly encounter DNS resolution failures in your cluster, one cause is an incorrect configuration change made to the kube-dns ConfigMap. In particular, configuration changes to the stub domains and upstream servers definitions can cause issues.

To check for updates to the stub domain settings, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the query pane, enter the following query:
         
         resource.labels.cluster_name="clouddns"
         resource.type="k8s_container"
         resource.labels.namespace_name="kube-system"
         labels.k8s-pod/k8s-app="kube-dns" jsonPayload.message=~"Updated stubDomains to"
         

  3. Click **Run query**.

  4. Review the output. If there have been any updates, the output is similar to the following:
         
         Updated stubDomains to map[example.com: [8.8.8.8 8.8.4.4 1.1.3.3 1.0.8.111]]
         

If you see an update, expand the result to learn more about the changes. Verify that any stub domains and their corresponding upstream DNS servers are correctly defined. Incorrect entries here can lead to resolution failures for those domains.




To check for changes to the upstream server, complete the following steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the query pane, enter the following query:
         
         resource.labels.cluster_name="clouddns"
         resource.type="k8s_container" resource.labels.namespace_name="kube-system"
         labels.k8s-pod/k8s-app="kube-dns" jsonPayload.message=~"Updated upstreamNameservers to"
         

  3. Click **Run query**.

  4. Review the output. If there have been any changes, the output is similar to the following:
         
         Updated upstreamNameservers to [8.8.8.8]
         

Expand the result to learn more about the changes. Verify that the list of upstream DNS servers is accurate and that these servers are reachable from your cluster. If these servers are unavailable or misconfigured, general DNS resolution might fail.




If you've checked for changes to the stub domains and upstream servers, but didn't find any results, check for all changes with the following filter:
    
    
    resource.type="k8s_cluster"
    protoPayload.resourceName:"namespaces/kube-system/configmaps/kube-dns"
    protoPayload.methodName=~"io.k8s.core.v1.configmaps."
    

Review any listed changes to see if they've caused the error.

### Contact Cloud Customer Care

If you've worked through the preceding sections, but still can't diagnose the cause of your issue, [contact Cloud Customer Care](https://docs.cloud.google.com/support/docs/customer-care-procedures#manage_a_support_case).

## Resolve common issues

If you've experienced a specific error or issue, use the advice in the following sections.

### Issue: Intermittent DNS timeouts

If you notice intermittent DNS resolution timeouts that occur when there's an increase in DNS traffic or when business hours start, try the following solutions to optimize your DNS performance:

  * Check the number of kube-dns Pods running on the cluster and compare it to the total number of GKE nodes. If there aren't enough resources, consider [scaling up](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache#scaling_up_kube-dns) the kube-dns Pods.

  * To improve average DNS lookup time, enable [NodeLocal DNS Cache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache#enable).

  * DNS resolution to external names can overload the kube-dns Pod. To reduce the number of queries, adjust the `ndots` setting in the `/etc/resolv.conf` file. `ndots` represents the number of dots that must appear in a domain name to resolve a query before the initial absolute query.

The following example is the `/etc/resolv.conf` file of an application Pod:
        
        search default.svc.cluster.local svc.cluster.local cluster.local c.PROJECT_ID.internal google.internal
        nameserver 10.52.16.10
        options ndots:5
        

In this example, kube-dns looks for five dots in the domain that's queried. If the Pod makes a DNS resolution call for `example.com`, then your logs look similar to the following example:
        
        "A IN example.com.default.svc.cluster.local." NXDOMAIN
        "A IN example.com.svc.cluster.local." NXDOMAIN
        "A IN example.com.cluster.local." NXDOMAIN
        "A IN example.com.google.internal." NXDOMAIN
        "A IN example.com.c.PROJECT_ID.internal." NXDOMAIN
        "A IN example.com." NOERROR
        

To resolve this issue, either change the value of ndots to `1` to look only for a single dot or append a dot (`.`) at the end of the domain that you query or use. For example:
        
        dig example.com.
        




### Issue: DNS queries fail intermittently from some nodes

If you notice DNS queries failing intermittently from some nodes, you might see the following symptoms:

  * When you run dig commands to the kube-dns Service IP address or Pod IP address, the DNS queries fail intermittently with timeouts.
  * Running dig commands from a Pod on the same node as the kube-dns Pod fails.



To resolve this issue, complete the following steps:

  1. Perform a [Connectivity Test](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests). Set the problematic Pod or node as the source, and destination as the IP address of the kube-dns Pod. This lets you check if you have the required firewall rules in place to allow this traffic.
  2. If the test is not successful, and traffic is being blocked by a firewall rule, use Cloud Logging to list any manual changes made to the firewall rules. Look for changes that block a specific kind of traffic:

     1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

     2. In the query pane, enter the following query:
            
            logName="projects/project-name/logs/cloudaudit.googleapis.com/activity"
            resource.type="gce_firewall_rule"
            

     3. Click **Run query**. Use the output of the query to determine if any changes have been made. If you notice any errors, correct them and reapply the firewall rule.

Make sure you don't make changes to any [automated firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#cluster-fws).

  3. If there haven't been any changes to the firewall rules, check the node pool version and make sure it's compatible with the control plane and other working node pools. If any of the cluster's node pools are more than two minor versions older than the control plane, this might be causing issues. For more information about this incompatibility, see [Node version not compatible with control plane version](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/upgrades#node-version-incompatible).

  4. To determine if the requests are being sent to the correct kube-dns service IP, capture network traffic on the problematic node and filter for port 53 (DNS traffic). Capture traffic on the kube-dns Pods themselves to see if the requests are reaching the intended Pods and if they're being successfully resolved.




## What's next

  * For general information about diagnosing Kubernetes DNS issues, see [Debugging DNS Resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
