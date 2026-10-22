---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/expired-certs/
title: Renew expired cluster certificates manually \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:11.352819+00:00
---

# Renew expired cluster certificates manually  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/expired-certs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Renew expired cluster certificates manually Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to manually renew expired certificates for your Google Distributed Cloud. Transport Layer Security (TLS) certificates are used by the control plane components of Google Distributed Cloud. When these certificates expire, your ability to manage workloads and cluster lifecycles is blocked until the certificates can be renewed. For more information about the impact of expired certificates, see [Certificate expiration](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/failure-mode-analysis#certificate_expiration).

This page is for Admins and architects and Operators who manage the lifecycle of the underlying tech infrastructure, and respond to alerts and pages when service level objectives (SLOs) aren't met or applications fail. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

By default, TLS certificates, including etcd certificates, have a 1-year expiration period. Google Distributed Cloud renews these certificates during cluster upgrades and when you [Rotate certificate authorities](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/ca-rotation). These certificates don't update periodically on their own. We recommend that you upgrade your clusters regularly to keep them secure, supported, and to prevent TLS certificates from expiring.

## Errors caused by certificate expiration

If the TLS certificates on your cluster expire, the core controllers can't establish TLS connections with the Kubernetes API server. This lack of connectivity causes the following errors:

  * **Unable to connect to the server: x509**

When you use `kubectl` to get your cluster nodes, the response includes an error that your certificates have expired, similar to the following example output:
        
        **Unable to connect to the server: x509** : certificate has expired or is not yet valid
        

  * **could not connect: x509** or **rejected connection**

Expired certificates block access to the etcd cluster, as peers can't communicate with each other. The etcd logs might contain error entries like the following:
        
        W | rafthttp: health check for peer 6221a1d241bb2d0a **could not connect: x509** : certificate
        has expired or is not yet valid
        I | embed: **rejected connection** from "10.200.0.4:46108" (error "remote error: tls: bad
        certificate", ServerName "")
        




## Check certificate expiration times

To check certificate expiration times, perform the following steps on each control plane node:

  1. Sign in to one of the control plane node machines and run the following command:
         
         sudo kubeadm certs check-expiration
         

The command output lists the certificates created by `kubeadm` for the control plane components and their expiry, as shown in the following example output:
         
         CERTIFICATE                EXPIRES                  RESIDUAL TIME   CERTIFICATE AUTHORITY   EXTERNALLY MANAGED
         admin.conf                 Nov 28, 2021 19:09 UTC   53m                                     no
         apiserver                  Nov 28, 2021 19:09 UTC   53m             ca                      no
         apiserver-etcd-client      Nov 28, 2021 19:09 UTC   53m             etcd-ca                 no
         apiserver-kubelet-client   Nov 28, 2021 19:09 UTC   53m             ca                      no
         controller-manager.conf    Nov 28, 2021 19:09 UTC   53m                                     no
         etcd-healthcheck-client    Nov 28, 2021 19:09 UTC   53m             etcd-ca                 no
         etcd-peer                  Nov 28, 2021 19:09 UTC   53m             etcd-ca                 no
         etcd-server                Nov 28, 2021 19:09 UTC   53m             etcd-ca                 no
         front-proxy-client         Nov 28, 2021 19:09 UTC   53m             front-proxy-ca          no
         scheduler.conf             Nov 28, 2021 19:09 UTC   53m                                     no
         
         CERTIFICATE AUTHORITY   EXPIRES                  RESIDUAL TIME   EXTERNALLY MANAGED
         ca                      Nov 26, 2031 18:06 UTC   9y              no
         etcd-ca                 Nov 26, 2031 18:06 UTC   9y              no
         front-proxy-ca          Nov 26, 2031 18:06 UTC   9y              no
         

  2. Run the following command to check the expiration times for `kubelet` certificates:
         
         sudo openssl x509 -in /var/lib/kubelet/pki/kubelet-client-current.pem -text | grep Validity -A2
         sudo openssl x509 -in /var/lib/kubelet/pki/kubelet-server-current.pem -text | grep Validity -A2
         

The response for each command looks like the following example output:
         
         Validity
             Not Before: Sep 17 22:27:53 2021 GMT
             Not After : Sep 17 22:33:16 2022 GMT
         

If all control plane nodes have been bootstrapped at the same time, then the certificate expiry times are within minutes of each other. This timing relationship applies across all control plane nodes. You can verify expiry times by running the preceding commands on each control plane node.

  3. Run the following command on the admin workstation to check the expiration time of the client certificate in the kubeconfig file of the cluster:
         
         grep 'client-certificate-data' KUBECONFIG_PATH | \
             awk '{print $2}' | base64 -d | openssl x509 -text | grep Validity -A2
         

The response looks like this sample output:
         
         Validity
             Not Before: Sep 17 22:27:53 2021 GMT
             Not After : Sep 17 22:33:16 2022 GMT
         

  4. Run the following command to look up the certificate expiration for the cluster kubeconfig in the admin cluster:
         
         kubectl get secret/CLUSTER_NAME-kubeconfig \
             -n CLUSTER_NAMESPACE \
             --kubeconfig ADMIN_KUBECONFIG \
             -o jsonpath='{.data.value}' | base64 --decode | grep client-certificate-data | \
             awk '{print $2}' | base64 -d | openssl x509 -text | grep Validity -A2
         

Replace the following:

     * `ADMIN_KUBECONFIG`: the path of the admin cluster kubeconfig file.

     * `CLUSTER_NAME`: the name of the cluster that you're renewing certificates for.

     * `CLUSTER_NAMESPACE`: the namespace of the cluster that you're renewing certificates for.

The response looks like this sample output:
    
    Validity
        Not Before: Sep 17 22:27:53 2021 GMT
        Not After : Sep 17 22:33:16 2022 GMT
    

The kubeconfig certificate in the admin cluster and the certificate in the kubeconfig file on the admin workstation are the same. Therefore, the output for this command and the command from the previous step must match.




## Renew certificates manually

To manually renew TLS certificates for a cluster, use the instructions in the following sections.

**Key Point:** The following instructions renew both expired and non-expired certificates. In either case, the expiration period for the renewed TLS certificates on your cluster is reset to one year. We strongly recommend that you renew cluster certificates before they expire to avoid significant cluster downtime. The recommended method for renewing certificates before they expire is to [upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) your clusters regularly.

### Renew certificates on each control plane node

Perform the following steps on each control plane node of the affected cluster:

**Important:** Renew certificates on only one node at a time. Perform all steps before starting on a new control plane node.

  1. Back up the `/etc/kubernetes` folder.

  2. Run the following `kubeadm` command to renew all the certificates. The command renews the certificates using the existing Certificate Authorities (CAs) on the machine:
         
         sudo kubeadm certs renew all
         

The command output is similar to the following example:
         
         certificate embedded in the kubeconfig file for the admin to use and for kubeadm itself renewed
         certificate for serving the Kubernetes API renewed
         certificate the apiserver uses to access etcd renewed
         certificate for the API server to connect to kubelet renewed
         certificate embedded in the kubeconfig file for the controller manager to use renewed
         certificate for liveness probes to healthcheck etcd renewed
         certificate for etcd nodes to communicate with each other renewed
         certificate for serving etcd renewed
         certificate for the front proxy client renewed
         certificate embedded in the kubeconfig file for the scheduler manager to use renewed
         

  3. Verify that the certificates have a new expiry time by running the following command:
         
         sudo kubeadm certs check-expiration
         

  4. Not all control plane components support dynamic certificate reload. To pick up the renewed certificates, the following steps restart the following containers: `kube-apiserver`, `kube-scheduler`, and `kube-controller-manager`.

Repeat the following steps for **each** of the four containers:

**Note:** If your certificates are expired, we recommend that you perform the following step for the `kube-apiserver` container first. Then, stop the `kube-scheduler` and `kube-controller-manager` containers.
     1. Find the container ID for each container:
            
            sudo crictl ps | grep CONTAINER_NAME
            

Replace `CONTAINER_NAME` with the name of the following containers: `kube-apiserver`, `kube-scheduler`, or `kube-controller-manager`.

The response is similar to the following output:
            
            c331ade490cb6       28df10594cd92      26 hours ago       Running          kube-apiserver ...
            

The container ID is the value in the first column.

     2. Stop each container:
            
            sudo crictl stop CONTAINER_ID
            

Replace `CONTAINER_ID` with the container ID from the preceding step.

When the stopped container exits, kubelet creates a new container in its place and deletes the stopped one. If you encounter an error, such as `context deadline exceeded` (error code `DeadlineExceeded`), rerun the command.




### Verify that connectivity is restored

The kubeadm certs should now be renewed on all control plane nodes. If you're renewing expired certificates, perform the following step:

  * To verify the connection with the Kubernetes API server, run the following `kubectl` command on any control plane node:
        
        kubectl get nodes --kubeconfig /etc/kubernetes/admin.conf
        




The response should return the list of nodes for the cluster. If your certificates are properly renewed, no TLS or certificate errors are returned.

### Update the kubeconfig secret in the cluster

The following steps use the renewed certificates from the `admin.conf` file to update the kubeconfig secret for your cluster. However, the contents of the updated `admin.conf` file can't be used as-is. You must make a copy of the `admin.conf` file with some needed edits first.

To update the new kubeconfig to the secret, perform the following steps on a control plane node:

  1. Use `sed` to replace `kubernetes` in the `admin.conf` file with the name of your cluster and write the changes to a new file, `kubeconfig_secret.conf`:
         
         sed "s/kubernetes/CLUSTER_NAME/g" \
             /etc/kubernetes/admin.conf > /etc/kubernetes/kubeconfig_secret.conf
         

  2. Use `diff` to confirm that the `kubeconfig_secret.conf` file has been updated:
         
         diff /etc/kubernetes/admin.conf /etc/kubernetes/kubeconfig_secret.conf
         

The response shows all of the places where the `kubeconfig_secret.conf` file is different from the updated `admin.conf` file. For example, if you performed the preceding step for a cluster named `demo-cluster`, the output would look similar to the following:
         
         6c6
         <   name: kubernetes
         ---
         >   name: demo-cluster
         9,12c9,12
         <     cluster: kubernetes
         <     user: kubernetes-admin
         <   name: kubernetes-admin@kubernetes
         < current-context: kubernetes-admin@kubernetes
         ---
         >     cluster: demo-cluster
         >     user: demo-cluster-admin
         >   name: demo-cluster-admin@demo-cluster
         > current-context: demo-cluster-admin@demo-cluster
         16c16
         < - name: kubernetes-admin
         ---
         > - name: demo-cluster-admin
         

  3. Run the following commands to update the kubeconfig secret in your cluster:
         
         CLUSTER_KUBECONFIG_BASE64=$(base64 /etc/kubernetes/kubeconfig_secret.conf -w 0)
         
         kubectl get secret/CLUSTER_NAME-kubeconfig \
             -n CLUSTER_NAMESPACE \
             --kubeconfig /etc/kubernetes/admin.conf -o json | jq \
             --arg conf "${CLUSTER_KUBECONFIG_BASE64}" '.data."value" |= $conf' | kubectl apply \
             --kubeconfig /etc/kubernetes/admin.conf -f -
         




### Replace the cluster kubeconfig file

To replace the kubeconfig file for your cluster with one that has the renewed certificates, use the following steps:

  1. Copy the `admin.conf` file from one of the cluster control plane nodes to the admin workstation.

As noted in prior sections, the `admin.conf` file is found in the `etc/kubernetes` directory on the cluster control plane nodes.

  2. To create the new kubeconfig file, run the following `kubectl` command on the admin workstation:
         
         kubectl --kubeconfig ADMIN_CONF_PATH get secret/CLUSTER_NAME-kubeconfig  \
             -n "CLUSTER_NAMESPACE" -o jsonpath='{.data.value}'  | \
             base64 --decode > new_kubeconfig.conf
         

Replace the following:

     * `ADMIN_CONF_PATH`: the path of the `admin.conf` file that has been copied to the admin workstation from a control plane node.

     * `CLUSTER_NAME`: the name of the cluster that you're renewing certificates for.

     * `CLUSTER_NAMESPACE`: the namespace of the cluster that you're renewing certificates for.

The `new_kubeconfig.conf` file contains the updated certificate data.

  3. Verify that the new kubeconfig works by running any `kubectl` command, using the new credentials:
         
         kubectl get nodes --kubeconfig new_kubeconfig.conf
         

  4. Replace the contents of the old kubeconfig file saved in the cluster directory on the admin workstation with the contents of the new kubeconfig file `new-kubeconfig.conf`.

By default, the path to the cluster configuration file is `bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig`.




### Verify kubelet certificates and restart `etcd-defrag`

To finish the process of renewing cluster certificates manually, perform the following steps for each control plane node:

  1. Sign in to the control plane node and verify the kubelet client and serving certificate expiry time by running the following commands:

Kubelet certificates are rotated automatically as long as the control plane is reachable. The period for automatic renewal of kubelet certificates is shorter than the expiration period for control plane component certificates. Therefore, it's likely that kubelet certificates have been renewed before:
         
         sudo openssl x509 -in /var/lib/kubelet/pki/kubelet-client-current.pem -text | grep Validity -A2
         sudo openssl x509 -in /var/lib/kubelet/pki/kubelet-server-current.pem -text | grep Validity -A2
         

The output of either command looks something like the following example:
         
         Validity
             Not Before: Nov 28 18:04:57 2022 GMT
             Not After : Nov 28 19:04:57 2023 GMT
         

  2. Use the following command to restart the `etcd-defrag` container:

The `etcd-defrag` container uses the `apiserver-etcd` client certificate to talk to etcd and must be restarted to pick up the updated certificates.
         
         kubectl rollout restart daemonset etcd-defrag -n kube-system --kubeconfig KUBECONFIG_PATH
         




After you complete these manual steps to renew cluster certificates, verify that all Pods are running properly and that no TLS errors are reported for control plane containers.

## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
