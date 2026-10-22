---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues/
title: Google Distributed Cloud (software only) for VMware known issues \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:20.657354+00:00
---

# Google Distributed Cloud (software only) for VMware known issues  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Google Distributed Cloud (software only) for VMware known issues Stay organized with collections  Save and categorize content based on your preferences. 

This page lists all known issues for Google Distributed Cloud on VMware. This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure, and respond to alerts and pages when service level objectives (SLOs) aren't met or applications fail. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

If you're part of the Google Developer Program, save this page to receive notifications when a release note related to this page is published. To learn more, see [Saved Pages](https://developers.google.com/profile/help/saved-pages).

To filter the known issues by a product version or category, select your desired filters from the following drop-down menus.

Select your Google Distributed Cloud version: 1.361.351.341.331.321.311.301.291.281.161.151.141.131.12

Select your problem category: Advanced clusterConfigurationInstallationUpgradesUpdatesOperationLogging and monitoringNetworkingSecurityStorageOperating systemVMwareIdentityMigrationOther

Or, search for you issue:

Category | Identified version(s) | Issue and workaround  
---|---|---  
Installation, Networking | All versions | 

### Admin workstation creation with `gkeadm` fails when port 22 is blocked from the jump server

When you run `./gkeadm create admin-workstation` from a jump server in an environment with strict firewall rules, the command fails after deploying the admin workstation VM in vSphere, or you can't connect to the admin workstation using `ssh`. This issue occurs when a firewall blocks TCP port `22` (SSH) between the jump server and the admin workstation IP address. During creation, `gkeadm` uses SCP over SSH (port `22`) to copy `credential.yaml`, cluster configuration files, and service account keys from the jump server to the newly created admin workstation VM. The [Firewall rules for remaining components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules#firewall_rules_for_remaining_components) table lists the port `443` requirement from the jump server to the vCenter Server API and ESXi hosts, but omits the port `22` requirement from the jump server to the admin workstation. **Diagnosis:**

  1. Check the `./gkeadm create admin-workstation` output for SSH or SCP connection timeouts while copying configuration files (`credential.yaml`, `admin-cluster.yaml`, or `user-cluster.yaml`) to the admin workstation VM.
  2. From the jump server, verify whether TCP port `22` is reachable on the admin workstation IP address: 
         
         nc -zv ADMIN_WORKSTATION_IP 22
                 

Or test the SSH connection with verbose logging enabled:
         
         ssh -vvv -i SSH_KEY_PATH ubuntu@ADMIN_WORKSTATION_IP
                 

If the firewall blocks port `22`, the connection times out (`Connection timed out`) or fails to establish a TCP handshake on port `22`.

**Workaround:**

  1. Configure your firewall to allow outbound SSH traffic from the jump server to the admin workstation IP address: 
     * **From:** Jump server to deploy the admin workstation
     * **Source port:** Ephemeral port range (check `/proc/sys/net/ipv4/ip_local_port_range`)
     * **To:** Admin workstation IP address
     * **Port:** `22`
     * **Protocol:** `TCP/ssh`
  2. After you apply the firewall rule, verify connectivity on port `22` from the jump server, and then re-run the admin workstation creation command: 
         
         ./gkeadm create admin-workstation
                 


Replace the following:

  * `ADMIN_WORKSTATION_IP`: the IP address of the admin workstation VM.
  * `SSH_KEY_PATH`: the path to the SSH private key for the admin workstation (typically `~/.ssh/gke-admin-workstation`).

  
Upgrades, Networking, Migration | 1.30, 1.31, 1.32, 1.33, 1.34, 1.35, 1.36 | 

### Intermittent connection timeouts after upgrading or scaling a cluster migrated from Calico to Dataplane V2

When you upgrade or scale an admin cluster or user cluster that you previously migrated from Calico (Dataplane V1) to Dataplane V2 (`enableDataplaneV2: true`), workloads on the cluster might experience either of the following symptoms:

  * **Intermittent outbound TCP connection timeouts:** Outbound connections from Pods to external endpoints intermittently time out.
  * **Inbound connection timeouts on Services:** Traffic to `LoadBalancer` or `NodePort` Services configured with `externalTrafficPolicy: Cluster` (such as NGINX or Istio ingress controllers) fails with `Connection timed out` errors.

After you migrate a cluster from Calico to Dataplane V2, the `calico-node` and `calico-route-daemon` DaemonSets remain dormant in the `kube-system` namespace so that you can roll back to Calico if needed. If you don't remove the `features.onprem.cluster.gke.io/dpv2-migration` annotation after completing the migration, `calico-node` can briefly schedule on new Dataplane V2 nodes during subsequent cluster upgrades or node scaling, set the host `FORWARD` chain policy to `DROP`, and leave behind `cali-*` `iptables` rules that conflict with Dataplane V2 routing. Clusters that were created with Dataplane V2 enabled are not affected. **Diagnosis:**

  1. Check whether the dormant `calico-node` and `calico-route-daemon` DaemonSets are still present on the cluster: 
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG -n kube-system get daemonset calico-node calico-route-daemon
                 

  2. Check whether any Dataplane V2 nodes have leftover `cali-*` `iptables` rules by running the following commands against an `anetd` Pod on the node: 
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG -n kube-system exec ANETD_POD_NAME -c cilium-agent -- iptables-save | grep cali-
         kubectl --kubeconfig CLUSTER_KUBECONFIG -n kube-system exec ANETD_POD_NAME -c cilium-agent -- iptables -t nat -vnL POSTROUTING
                 

If the output shows `cali-*` rules (such as `cali-POSTROUTING` listed ahead of `CILIUM_POST_nat`), that node is affected by this issue.

**Workaround:** Follow the steps for your cluster's stage: **Before upgrading or scaling (one-time cleanup after Dataplane V2 migration):** **Caution:** Only remove this annotation after the migration to Dataplane V2 is complete on all nodes. Removing it on a cluster that is still using Calico or is in the middle of migrating evicts Calico from existing nodes and disrupts Pod networking. Don't manually delete the DaemonSets using `kubectl delete daemonset`, because the cluster controller recreates manually deleted DaemonSets during updates and upgrades unless you remove the `features.onprem.cluster.gke.io/dpv2-migration` annotation. 

  1. Verify that the Dataplane V2 migration is complete and that all nodes in the cluster have the `networking.gke.io/cni-type: cilium` label: 
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG get nodes -L networking.gke.io/cni-type
                 

  2. After you confirm that Dataplane V2 is running on all nodes and you no longer need to roll back to Calico, remove the `features.onprem.cluster.gke.io/dpv2-migration` annotation from the `OnPremUserCluster` custom resource (and from `OnPremAdminCluster` if your admin cluster was migrated from Calico during the upgrade from version 1.29 to 1.30) so the controller permanently deletes `calico-node` and `calico-route-daemon`: 
         
         # For a user cluster:
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG annotate onpremusercluster USER_CLUSTER_NAME \
           -n USER_CLUSTER_NAME-gke-onprem-mgmt \
           features.onprem.cluster.gke.io/dpv2-migration-
         
         # For an admin cluster:
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG annotate onpremadmincluster ADMIN_CLUSTER_NAME \
           -n kube-system \
           features.onprem.cluster.gke.io/dpv2-migration-
                 

  3. Verify that the `calico-node` and `calico-route-daemon` DaemonSets are deleted (both return `NotFound`): 
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG -n kube-system get daemonset calico-node calico-route-daemon
                 


**After upgrading or scaling (if nodes already have leftover`cali-*` `iptables` rules):**

  1. Complete the preceding **Before upgrading or scaling** steps to remove the `features.onprem.cluster.gke.io/dpv2-migration` annotation on the affected user cluster or admin cluster so the controller permanently deletes `calico-node` and `calico-route-daemon`.
  2. **Restart or recreate the affected nodes (recommended):** Restart or recreate the affected nodes so they initialize with a clean network configuration and flush any residual Calico files and kernel state under Dataplane V2.
  3. **Optional immediate mitigation in place:** If you can't restart or recreate the affected nodes immediately, run the following command to remove the leftover `cali-*` jump rules from the host `iptables` chains and reset the host `FORWARD` chain default policy from `DROP` to `ACCEPT` across all `anetd` Pods, and then restart or recreate the nodes during your next maintenance window: 
         
         for pod in $(kubectl --kubeconfig CLUSTER_KUBECONFIG get pods -n kube-system -l k8s-app=cilium -o jsonpath='{.items[*].metadata.name}'); do
           kubectl --kubeconfig CLUSTER_KUBECONFIG exec -n kube-system "$pod" -c cilium-agent -- sh -c '
             for c in POSTROUTING PREROUTING OUTPUT; do iptables -t nat -S $c | grep cali- | sed "s/^-A/-D/" | xargs -r -L 1 iptables -t nat; done
             iptables -P FORWARD ACCEPT
             for c in FORWARD INPUT OUTPUT; do iptables -S $c | grep cali- | sed "s/^-A/-D/" | xargs -r -L 1 iptables; done
           '
         done
                 


Replace the following:

  * `CLUSTER_KUBECONFIG`: the path to the `kubeconfig` file for the affected admin or user cluster.
  * `ANETD_POD_NAME`: the name of an `anetd` Pod running on the node you are inspecting.
  * `ADMIN_CLUSTER_KUBECONFIG`: the path to the admin cluster `kubeconfig` file.
  * `USER_CLUSTER_NAME`: the name of the user cluster.
  * `ADMIN_CLUSTER_NAME`: the name of the admin cluster (you can find this by running `kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get onpremadmincluster -n kube-system`).

  
Installation, Networking, Advanced cluster | 1.31, 1.32, 1.33, 1.34, 1.35, 1.36 | 

### Cluster creation fails preflight validation when the control plane VIP is in a different subnet with manual load balancing

When you create an HA admin cluster or a Controlplane V2 user cluster that has advanced cluster enabled and uses manual control plane load balancing, preflight validation fails if the control plane VIP (`loadBalancer.vips.controlPlaneVIP`) is in a different subnet from the control plane nodes. The failure occurs when you run `gkectl check-config`, `gkectl create admin`, or `gkectl create cluster`. A cluster uses manual control plane load balancing in any of the following cases:

  * In version 1.32 and later, the cluster configuration file sets `adminMaster.controlPlaneLoadBalancer.mode: "manual"` (admin cluster) or `masterNode.controlPlaneLoadBalancer.mode: "manual"` (user cluster).
  * In version 1.32 and later, the cluster uses topology domains, which means that the `infraConfigFilePath` field is set in the admin cluster configuration file. With topology domains, `"manual"` is the default control plane load balancer mode, so this issue applies even if you don't set the mode explicitly.
  * In version 1.31, the cluster configuration file sets `loadBalancer.kind: "ManualLB"`. The `controlPlaneLoadBalancer` section isn't available in version 1.31, so the control plane load balancer follows `loadBalancer.kind`.

Preflight validation requires the control plane VIP to be in the control plane node subnet regardless of the control plane load balancer mode. This requirement applies only to the bundled control plane load balancer, which runs `keepalived` and `haproxy` on the control plane nodes. In manual mode, your external load balancer serves the control plane VIP, so a VIP outside the node subnet is valid. In version 1.32 and later, `loadBalancer.kind: "ManualLB"` doesn't set the control plane load balancer mode. If the cluster doesn't use topology domains, the control plane load balancer defaults to `"bundled"` unless you set `controlPlaneLoadBalancer.mode: "manual"`. In bundled mode, the control plane VIP must be in the control plane node subnet, and this issue doesn't apply. **Diagnosis:**

  1. Check the `gkectl` output for errors similar to the following: 
         
         [FAILURE] CIDR, VIP and static IP (availability and overlapping): control plane VIP needs to be in the same cluster subnet: ip "CONTROL_PLANE_VIP" not in subnet "NODE_SUBNET"
         [FAILURE] Config: Validator Config failed after retries: timed out waiting for the condition, last failed result: failed LoadBalancer validation for user cluster: control plane VIP needs to be in the same cluster subnet: ip "CONTROL_PLANE_VIP" not in subnet "NODE_SUBNET"
                 

For an admin cluster, the second message says `failed LoadBalancer validation for admin cluster` instead of `failed LoadBalancer validation for user cluster`.
  2. In version 1.32 and later, verify in your cluster configuration file that `adminMaster.controlPlaneLoadBalancer.mode` or `masterNode.controlPlaneLoadBalancer.mode` is set to `"manual"`, or that the cluster uses topology domains. In version 1.31, verify that `loadBalancer.kind` is set to `"ManualLB"`.
  3. Confirm that no other checks in the `Network Configuration` or `Config Check` validation categories report `[FAILURE]`.

**Workaround:** If the control plane VIP subnet errors are the only preflight failures, create the cluster with the `--skip-validation-load-balancer` and `--skip-validation-net-config` flags. **Caution:** These flags skip all load balancer and network configuration preflight checks, not only the control plane VIP subnet check. Use them only after you confirm that the control plane VIP subnet errors are the only failures. 

  * For an admin cluster: 
        
        gkectl create admin --config ADMIN_CLUSTER_CONFIG --skip-validation-load-balancer --skip-validation-net-config
                

  * For a user cluster: 
        
        gkectl create cluster --config USER_CLUSTER_CONFIG --kubeconfig ADMIN_KUBECONFIG --skip-validation-load-balancer --skip-validation-net-config
                


Replace the following:

  * `ADMIN_CLUSTER_CONFIG`: the path to your admin cluster configuration file.
  * `USER_CLUSTER_CONFIG`: the path to your user cluster configuration file.
  * `ADMIN_KUBECONFIG`: the path to your admin cluster `kubeconfig` file.

  
Upgrades, Updates, Advanced cluster, Security | 1.33, 1.34 | 

### Control plane nodes fail to join during an update or upgrade to an advanced cluster after CA rotation

When you update or upgrade an admin cluster or user cluster to an [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters) (`enableAdvancedCluster: true` or `enableAdvancedClusters: true`) in version 1.33 or 1.34, the operation fails if you previously rotated the cluster's certificate authorities (CAs) using `gkectl update credentials certificate-authorities rotate`. After a CA rotation completes, the active CA certificates and keys are stored in version-suffixed secrets (such as `cluster-ca-cert-2`, `etcd-ca-cert-2`, and `front-proxy-ca-cert-2`). During the migration to an advanced cluster, `gkectl` looks up the unversioned secrets (`cluster-ca-cert`, `etcd-ca-cert`, and `front-proxy-ca-cert`) instead of checking the `ca-rotation-stage` ConfigMap for the active CA version:

  * **If the unversioned`cluster-ca-cert` secret does not exist** (common on user clusters): `gkectl` fails during cluster preparation with `failed to get user cluster ca secret from admin client: secrets "cluster-ca-cert" not found`.
  * **If the unversioned secrets still exist with pre-rotation CA material** (common on admin clusters): `gkectl` seeds the bootstrap cluster with the outdated CA and pins the outdated public key hash into the `kubeadm` join configuration, causing control plane nodes to fail to join (`none of the public keys ... are pinned`). If `gkectl` also updates your local workstation `kubeconfig` file with the outdated CA, running `kubectl` commands with that `kubeconfig` fails with `crypto/rsa: verification error`.

A permanent fix is available in version 1.34.1000 and later. **Diagnosis:**

  1. Check for either of the following error messages: 
     * In the `gkectl upgrade` or `gkectl update` output during cluster preparation: 
           
           Failed to create kubeadm objects in user cluster: failed to get user cluster ca secret from admin client: secrets "cluster-ca-cert" not found
                       

     * In the `machine-init` pod logs in the bootstrap cluster if the upgrade is stuck joining a control plane node: 
           
           kubectl --kubeconfig BOOTSTRAP_KUBECONFIG -n kube-system get pods | grep machine-init
           kubectl --kubeconfig BOOTSTRAP_KUBECONFIG -n kube-system logs MACHINE_INIT_POD_NAME -c ansible-runner
                       

Look for the following error message:
           
           error execution phase control-plane-prepare/certs: couldn't validate the identity of the API Server: cluster CA found in cluster-info ConfigMap is invalid: none of the public keys "<sha256-hash>" are pinned
                       

  2. Check the `ca-rotation-stage` ConfigMap on the admin cluster to verify that the active CA version (`CA_VERSION`) is greater than `1` (such as `2`) and that CA rotation is complete: 
         
         kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE get configmap ca-rotation-stage -o jsonpath='{.data.data}'; echo
                 

Confirm that every version number in the output is the same version (greater than `1`, such as `2`) and that `caBundle` contains only that single version (`[2]`):
         
         {"controlPlane":{"caBundle":[2],"csrCA":2,"certCA":2,...},"dataPlane":{"caBundle":[2],"csrCA":2}}
                 

**Caution:** If version `1` or multiple versions appear in `caBundle` (for example, `[1]` or `[1,2]`), CA rotation has either not been performed or is still in progress. Don't proceed with the workaround until the CA rotation completes. 
  3. Check whether the unversioned `cluster-ca-cert` secret is missing (`NotFound`) or reports a different serial number than `cluster-ca-cert-CA_VERSION`: 
         
         kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE get secret cluster-ca-cert -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -noout -serial -dates
         kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE get secret cluster-ca-cert-CA_VERSION -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -noout -serial -dates
                 

If `cluster-ca-cert` is not found or reports an older serial number (such as `serial=00`) than `cluster-ca-cert-CA_VERSION`, your cluster is affected by this issue.

**Workaround:** Follow the instructions for your cluster's scenario: **Scenario 1: Clusters that have not been upgraded yet (or failed during cluster preparation with`secrets "cluster-ca-cert" not found`)** **Note:** You only need to synchronize `cluster-ca-cert`, `etcd-ca-cert`, and `front-proxy-ca-cert`. Don't copy `peer-etcd-ca-cert-CA_VERSION` (the advanced cluster derives etcd peer trust from `etcd-ca-cert`) or any version-suffixed leaf certificate secrets (such as `admin-cert-CA_VERSION` or `apiserver-cert-CA_VERSION`); the advanced cluster re-issues all leaf certificates automatically from the three synchronized CAs. 

  1. Back up the existing CA secrets and the `ca-rotation-stage` ConfigMap before making any changes: 
         
         export WORKDIR=~/ca-backup && mkdir -p "${WORKDIR}"
         kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE get secret \
           cluster-ca-cert cluster-ca-cert-CA_VERSION \
           etcd-ca-cert etcd-ca-cert-CA_VERSION \
           front-proxy-ca-cert front-proxy-ca-cert-CA_VERSION \
           --ignore-not-found -o yaml > "${WORKDIR}/backup-ca-secrets.yaml"
         kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE get configmap ca-rotation-stage \
           -o yaml > "${WORKDIR}/backup-ca-rotation-stage.yaml"
                 

  2. Synchronize `cluster-ca-cert`, `etcd-ca-cert`, and `front-proxy-ca-cert` from their active `-CA_VERSION` counterparts (this command patches `.data` in place if the secret exists so its immutable `type` and metadata are preserved, or creates an `Opaque` secret if it is missing): 
         
         for base in cluster-ca-cert etcd-ca-cert front-proxy-ca-cert; do
           src="${base}-CA_VERSION"
           crt=$(kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE get secret "${src}" -o jsonpath='{.data.tls\.crt}')
           key=$(kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE get secret "${src}" -o jsonpath='{.data.tls\.key}')
           if [ -z "${crt}" ] || [ -z "${key}" ]; then echo "Error: ${src} missing tls.crt or tls.key"; break; fi
           if kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE get secret "${base}" >/dev/null 2>&1; then
             kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE patch secret "${base}" --type merge \
               -p "{\"metadata\":{\"annotations\":{\"gke-on-prem.googleapis.com/synced-from\":\"${src}\"}},\"data\":{\"tls.crt\":\"${crt}\",\"tls.key\":\"${key}\"}}"
           else
             cat <<EOF | kubectl --kubeconfig ADMIN_KUBECONFIG apply -f -
         apiVersion: v1
         kind: Secret
         metadata:
           name: ${base}
           namespace: CLUSTER_NAMESPACE
           annotations:
             gke-on-prem.googleapis.com/synced-from: ${src}
         type: Opaque
         data:
           tls.crt: ${crt}
           tls.key: ${key}
         EOF
           fi
         done
                 

  3. Verify that each unversioned secret now has the same `tls.crt` and `tls.key` data and reports the same certificate serial number as its `-CA_VERSION` counterpart: 
         
         for base in cluster-ca-cert etcd-ca-cert front-proxy-ca-cert; do
           src="${base}-CA_VERSION"
           for field in 'tls\.crt' 'tls\.key'; do
             a=$(kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE get secret "${base}" -o jsonpath="{.data.${field}}")
             b=$(kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE get secret "${src}" -o jsonpath="{.data.${field}}")
             if [ "${a}" = "${b}" ] && [ -n "${a}" ]; then
               echo "OK: ${base} (${field}) matches ${src}"
             else
               echo "ERROR: ${base} (${field}) differs from ${src}"
             fi
           done
           printf '%-28s ' "${base}"
           kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE get secret "${base}" \
             -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -noout -serial
           printf '%-28s ' "${src}"
           kubectl --kubeconfig ADMIN_KUBECONFIG -n CLUSTER_NAMESPACE get secret "${src}" \
             -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -noout -serial
         done
                 

  4. Run the cluster upgrade or update command as planned: 
         
         # For an admin cluster:
         gkectl upgrade admin --kubeconfig ADMIN_KUBECONFIG --config CLUSTER_CONFIG
         # For a user cluster:
         gkectl upgrade cluster --kubeconfig ADMIN_KUBECONFIG --config CLUSTER_CONFIG
                 


**Scenario 2: Clusters that are stuck upgrading (control plane node fails to join with`none of the public keys ... are pinned`)**

  1. Complete **Steps 1 through 3** in **Scenario 1** to back up and synchronize `cluster-ca-cert`, `etcd-ca-cert`, and `front-proxy-ca-cert` with their active `-CA_VERSION` counterparts on the admin cluster.
  2. Re-run the cluster upgrade or update command with `--reuse-bootstrap-cluster=false` to recreate the bootstrap cluster using the synchronized CA secrets: 
         
         # For an admin cluster:
         gkectl upgrade admin --kubeconfig ADMIN_KUBECONFIG --config CLUSTER_CONFIG --reuse-bootstrap-cluster=false
         # For a user cluster:
         gkectl upgrade cluster --kubeconfig ADMIN_KUBECONFIG --config CLUSTER_CONFIG --reuse-bootstrap-cluster=false
                 

If `gkectl` reuses the existing bootstrap cluster, delete the bootstrap cluster manually by running `kind delete cluster --name bmctl-control-plane`, and then re-run the command.
  3. Once the new bootstrap cluster starts reconciling the control plane node, verify that the bootstrap cluster holds the active CA and that the rendered `kubeadmconfig` secret pins the matching CA hash: 
         
         kubectl --kubeconfig BOOTSTRAP_KUBECONFIG -n kube-system get secret CLUSTER_NAME-ca \
           -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -noout -serial
         kubectl --kubeconfig BOOTSTRAP_KUBECONFIG -n kube-system get secret NODE_IP-kubeadmconfig-yaml \
           -o jsonpath='{.data.kubeadmconfig\.yaml}' | base64 -d | grep -A3 caCertHashes
                 

If the rendered `kubeadmconfig` secret still pins the outdated CA hash, remove `caCertHashes` from the `KubeadmConfig` resource and delete the rendered secret so the bootstrap controller regenerates it:
         
         kubectl --kubeconfig BOOTSTRAP_KUBECONFIG -n kube-system patch kubeadmconfig NODE_IP --type json \
           -p '[{"op":"remove","path":"/spec/joinConfiguration/discovery/bootstrapToken/caCertHashes"}]'
         kubectl --kubeconfig BOOTSTRAP_KUBECONFIG -n kube-system delete secret NODE_IP-kubeadmconfig-yaml --ignore-not-found=true
                 


**Note:** Leave the synchronized unversioned CA secrets in place after the upgrade completes. Reverting them can reintroduce this issue during subsequent `gkectl update` or `gkectl upgrade` operations until you upgrade to a version that includes the permanent fix. Replace the following:

  * `BOOTSTRAP_KUBECONFIG`: the path to the bootstrap cluster `kubeconfig` file (typically `~/.kube/kind-config-gkectl`).
  * `MACHINE_INIT_POD_NAME`: the name of the `bm-system-machine-init` pod for the failing control plane node.
  * `ADMIN_KUBECONFIG`: the path to a working admin cluster `kubeconfig` file.
  * `CLUSTER_NAMESPACE`: `kube-system` for an admin cluster, or the user cluster namespace (such as `USER_CLUSTER_NAME`) on the admin cluster.
  * `CA_VERSION`: the active CA version number from the `ca-rotation-stage` ConfigMap (such as `2`).
  * `CLUSTER_CONFIG`: the path to your admin or user cluster configuration file.
  * `CLUSTER_NAME`: the name of the cluster being upgraded.
  * `NODE_IP`: the IP address of the control plane node being joined.

  
Upgrades, Storage | 1.33, 1.34 | 

### User cluster upgrade stalls due to immutable StorageClass parameters

During a user cluster upgrade to version 1.33 or 1.34, the upgrade process might stall indefinitely in the `UPGRADING` or `RECONCILING` state. This issue occurs if you use the legacy in-tree provisioner (`kubernetes.io/vsphere-volume`) to create the default `standard` StorageClass. The system tries to update StorageClass to the vSphere CSI provisioner, but StorageClass parameters are immutable, so the Kubernetes API rejects the update. **Diagnosis:** To find out if this issue impacts you, check the `component-provisioner-user` job logs in the admin cluster's `kube-system` namespace:
    
    
    kubectl --kubeconfig ADMIN_KUBECONFIG -n kube-system logs -l baremetal.cluster.gke.io/componentprovisioner.profile=user,baremetal.cluster.gke.io/componentprovisioner.targetcluster=USER_CLUSTER_NAME --tail=100
        

If the logs contain the following error, this issue impacts you:
    
    
    Error executing the component provisioner: failed to apply manifests: failed to update resource standard: StorageClass.storage.k8s.io "standard" is invalid: parameters: Forbidden: updates to parameters are forbidden.
        

**Workaround:**

  1. Delete the legacy `standard` StorageClass on the target user cluster: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete storageclass standard --ignore-not-found=true
                 

**Note:** Deleting the `StorageClass` object does not impact existing PersistentVolumes (PVs), PersistentVolumeClaims (PVCs), or active disk attachments. 
  2. In the admin cluster, delete the failed provisioner job to force an immediate retry: 
         
         kubectl --kubeconfig ADMIN_KUBECONFIG -n kube-system delete job -l baremetal.cluster.gke.io/componentprovisioner.profile=user,baremetal.cluster.gke.io/componentprovisioner.targetcluster=USER_CLUSTER_NAME --ignore-not-found=true
                 

  3. Verify that the new provisioner pod completes successfully (status `Completed`): 
         
         kubectl --kubeconfig ADMIN_KUBECONFIG -n kube-system get pods -l baremetal.cluster.gke.io/componentprovisioner.profile=user,baremetal.cluster.gke.io/componentprovisioner.targetcluster=USER_CLUSTER_NAME -w
                 

  4. Resume the cluster upgrade: 
         
         gkectl upgrade cluster --config USER_CLUSTER_CONFIG --kubeconfig ADMIN_KUBECONFIG
                 

Replace the following: 
     * `ADMIN_KUBECONFIG`: The path to your admin cluster kubeconfig file.
     * `USER_CLUSTER_CONFIG`: The path to your user cluster configuration file.
     * `USER_CLUSTER_KUBECONFIG`: The path to your user cluster kubeconfig file.
     * `USER_CLUSTER_NAME`: The name of the user cluster being upgraded.

  
Installation | All versions | 

### Admin cluster creation fails on vSAN datastores

Admin cluster creation might fail or time out if the target datastore is a vSAN datastore. This occurs because the installation process cannot programmatically create the required top-level `anthos/` directory on vSAN datastores. **Symptoms:**  
The cluster installation fails immediately with an invalid fault, or times out after an hour. You might observe an error message similar to the following in the create operation logs: 
    
    
    "error"="failed to create VM via actuator: failed to create VM via rpc request:
    failed to create data disk: failed to get resolved data disk path:
    failed to convert full path "\"ds:///vmfs/volumes/vsan:<datastore-uuid>/anthos/<cluster-name>/kube-system/<vm-name>-data.vmdk\":"
    ServerFaultCode: A general system error occurred: Invalid fault"

  
**Workaround:** Before running the cluster creation command, manually create the required directory:

  1. Log in to the vSphere Client using the exact same vCenter service account specified in your `admin-cluster.yaml` configuration file.
  2. Open the vCenter Datastore Browser for the target vSAN datastore.
  3. Create a folder named `anthos` at the root level of the datastore.
  4. Run the `gkectl create admin` command again.

  
Upgrades, Networking | 1.28, 1.29, 1.30, 1.31, 1.32 | 

### User cluster workloads become unreachable through Seesaw load balancer during admin cluster upgrade

When you upgrade an admin cluster in an environment configured with the Seesaw load balancer, incoming network traffic to applications and services running in your user clusters might experience a transient outage (typically lasting 3 to 5 minutes) during the control plane restart. This issue occurs because the node health check endpoint (port 10256) reports worker nodes as unhealthy while the admin cluster's control plane is restarting. Consequently, the Seesaw load balancer temporarily stops routing external and cross-cluster traffic to user cluster `LoadBalancer` services until the control plane finishes restarting. **Symptoms**: During an admin cluster upgrade, you might observe the following:

  * Incoming client requests or cross-cluster connections to user cluster `LoadBalancer` services fail, time out, or return connection refused errors.
  * Workload traffic drops for 3 to 5 minutes while the admin control plane is upgrading, even if your user clusters are configured for high availability (HA).
  * Seesaw load balancer logs show health check failures for backend worker nodes during the control plane restart window.
  * In rare cases, if a worker node reboots during this period, it might get stuck in a `NotReady` state with `kubelet` logs reporting connection failures to the control plane VIP: 
        
        Readiness probe failed... dial tcp <VIP>:443: connect: connection refused


**Workaround and resolution**: A permanent fix is available in the following patch versions and later: 1.30.1100-gke.X, 1.31.700-gke.X, and 1.32.300-gke.X. To avoid or address this disruption:

  * If you are planning an upgrade (recommended): Upgrade your user clusters to a fixed patch version (such as 1.30.1100+ or 1.31.700+) before you upgrade your admin cluster. Because the health checking component resides on the user cluster nodes, updating the user clusters first prevents Seesaw from dropping traffic during the subsequent admin cluster upgrade.
  * If your user clusters cannot be upgraded first: Schedule your admin cluster upgrade during a planned maintenance window when a 3-to-5-minute interruption to user cluster `LoadBalancer` traffic is acceptable.
  * If the upgrade is currently running: The traffic disruption is transient and will self-resolve automatically after the admin cluster control plane finishes restarting. No manual load balancer intervention is required.
  * If a worker node remains in a `NotReady` state after upgrade: Restart the networking pod on the affected node: 
    1. Find the CNI pod running on the affected node: 
           
           kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get pods -n kube-system -o wide | grep NODE_NAME

Replace ADMIN_CLUSTER_KUBECONFIG with your admin cluster kubeconfig path and NODE_NAME with the name of the node. 
    2. Delete the pod to force Kubernetes to recreate it: 
           
           kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG delete pod CNI_POD_NAME -n kube-system

Replace CNI_POD_NAME with the name of the pod from the previous step. 

  
Upgrades, Advanced cluster, Security | 1.32.0-1.32.1200, 1.33.0-1.33.1000, 1.34.0-1.34.700, 1.35.0-1.35.300 | 

### Etcd secret decryption fails after retrying an admin cluster or user cluster upgrade to Advanced Cluster

When upgrading an admin cluster or user cluster to Advanced Cluster, if the initial upgrade attempt fails and the upgrade is retried (such as re-running with an existing bootstrap cluster), the encryption keys in the `generated-key-kms-plugin-config` secret might be stripped. This causes a random encryption key to be generated upon reconciliation, preventing the control plane from decrypting existing Kubernetes secrets in etcd. **Symptoms:**  
You might observe the following symptoms after retrying or re-running a cluster upgrade: 

  * Control plane components (such as `kube-apiserver` or machine initialization jobs) fail to start or remain in an error state.
  * Logs for the control plane or `machine-init` jobs contain decryption errors similar to the following: 
        
        failed to decrypt: cipher: message authentication failed

or: 
        
        could not find a JWS signature in machine-init job

  * For a user cluster upgrade, the `generated-key-kms-plugin-config` secret in the user cluster namespace on the admin cluster contains a newly generated encryption key that does not match the keys stored in the `user-master-component-options` secret.
  * For an admin cluster upgrade, the `generated-key-kms-plugin-config` secret in the `kube-system` namespace contains a newly generated encryption key that does not match the keys stored in the `admin-master-component-options` secret.

**Workaround:** To recover the cluster and restore secret decryption, restore the original encryption keys from the component options secret into the `generated-key-kms-plugin-config` secret: **For a user cluster:**

  1. In the admin cluster, retrieve the valid encryption keys from the `user-master-component-options` secret in the user cluster namespace (USER_CLUSTER_NAMESPACE): 
         
         kubectl --kubeconfig ADMIN_KUBECONFIG -n USER_CLUSTER_NAMESPACE get secret user-master-component-options -o yaml

Locate the original base64-encoded encryption key string inside the `StandaloneMasterLinuxSecret.GeneratedKeys` section of the decoded payload.
  2. Update the `generated-key-kms-plugin-config` secret in the user cluster namespace (USER_CLUSTER_NAMESPACE) on the admin cluster so that its data matches the original key string from step 1: 
         
         kubectl --kubeconfig ADMIN_KUBECONFIG -n USER_CLUSTER_NAMESPACE create secret generic generated-key-kms-plugin-config --from-literal=<KEY_VERSION>=<ORIGINAL_KEY_STRING> --dry-run=client -o yaml | kubectl --kubeconfig ADMIN_KUBECONFIG apply -f -

Replace `<KEY_VERSION>` with the version ID of your key (for example, `1`) and `<ORIGINAL_KEY_STRING>` with the key string retrieved in step 1.
  3. Restart or delete any failing control plane pods or machine jobs so they mount the restored encryption key and successfully decrypt etcd secrets.

**For an admin cluster:**

  1. In the admin cluster (or bootstrap cluster during upgrade), retrieve the valid encryption keys from the `admin-master-component-options` secret in the `kube-system` namespace: 
         
         kubectl --kubeconfig ADMIN_OR_BOOTSTRAP_KUBECONFIG -n kube-system get secret admin-master-component-options -o yaml

Locate the original base64-encoded encryption key string inside the `StandaloneMasterLinuxSecret.GeneratedKeys` section of the decoded payload.
  2. Update the `generated-key-kms-plugin-config` secret in the `kube-system` namespace so that its data matches the original key string from step 1: 
         
         kubectl --kubeconfig ADMIN_OR_BOOTSTRAP_KUBECONFIG -n kube-system create secret generic generated-key-kms-plugin-config --from-literal=<KEY_VERSION>=<ORIGINAL_KEY_STRING> --dry-run=client -o yaml | kubectl --kubeconfig ADMIN_OR_BOOTSTRAP_KUBECONFIG apply -f -

Replace `<KEY_VERSION>` with the version ID of your key (for example, `1`) and `<ORIGINAL_KEY_STRING>` with the key string retrieved in step 1.
  3. Restart or delete any failing control plane pods or machine jobs so they mount the restored encryption key and successfully decrypt etcd secrets.

  
Upgrades, Updates, Advanced cluster | 1.32, 1.33, 1.34 | 

### User cluster upgrade to Advanced Cluster stalls if [advanced networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#advancednetworking-field) is enabled due to Anthos Network Gateway (ANG) immutable selector error

When upgrading a user cluster with [advanced networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#advancednetworking-field) feature enabled to the Advanced Cluster, the reconciliation process may fail or stall because the label selectors for Anthos Network Gateway (ANG) components have changed. Because Kubernetes does not allow modifications to the `spec.selector` field of existing resources, the upgrade cannot proceed. **Symptoms:**  
You may observe the following symptoms: 

  * The user cluster remains in a `Reconciling` or `ERROR` state indefinitely.
  * Logs for the `cluster-profile-deployer` or `lifecycle-controllers-deployer` contain errors similar to the following: 
        
        "msg"="replace run failed" "error"="error when replacing \"/tmp/...\": Deployment.apps \"ang-controller-manager\" is invalid: spec.selector: ... field is immutable"


**Workaround:** **Caution:** Deleting the ANG resources will temporarily interrupt network traffic managed by the gateway until the resources are recreated. Replace USER_CLUSTER_KUBECONFIG with the kubeconfig path of the user cluster. **If you are in the middle of upgrade:** Manually delete the affected ANG resources from the user cluster. The cluster's controllers will automatically recreate them with the correct label selectors, allowing the upgrade to complete: 

  1. Delete the ANG Controller Manager and Autoscaler Deployments: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG -n kube-system delete deployment ang-controller-manager ang-controller-manager-autoscaler

  2. Delete the ANG DaemonSet: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG -n kube-system delete daemonset ang-node


**If you have not upgraded yet:** Perform the following script for re-applying the ANG components with the correct labels.
    
    
    #!/bin/bash
    # fix-ang-selectors.sh
    # Workaround: Get, Update Labels, Delete, and Re-apply ANG resources.
    
    RESOURCES=("daemonset/ang-node" "deployment/ang-controller-manager" "deployment/ang-controller-manager-autoscaler")
    
    for RES in "${RESOURCES[@]}"; do
        NAME=$(echo $RES | cut -d'/' -f2)
        FILE="${NAME}.yaml"
    
        echo "Processing $RES..."
    
        # 1. Get the resource
        kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get $RES -n kube-system -o yaml > $FILE
    
        # 2. Update the labels (using sed for automation)
        # Adds the version label to the selector and template labels
        sed -i 's/^\([[:space:]]*\)component.networking.gke.io: ang/\0\n\1version.ang.networking.gke.io: 1.1.0-gke.0/' $FILE
        # Strip unnecessary fields
        sed -i '/resourceVersion:\|uid:\|creationTimestamp:\|managedFields:/d' $FILE
        sed -i '/^status:/,/^[^ ]/ { /^status:/d; /^  /d; }' $FILE
    
        # 3. Delete the resource
        kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete $RES -n kube-system --ignore-not-found
    
        # 4. Re-apply the resource
        kubectl --kubeconfig USER_CLUSTER_KUBECONFIG apply -f $FILE
    done  
  
Security, Upgrades, Updates, Advanced cluster | 1.32.0-1.32.1200, 1.33.0-1.33.800, 1.34.0-1.34.500, 1.35.0-1.35.100 | 

### Always-on secrets encryption enablement or disablement fails or gets stuck in a loop in Advanced Cluster

When enabling or disabling always-on secrets encryption (using `mode: GeneratedKey`) as a Day 2 operation on an existing Advanced cluster, the cluster update or upgrade process may fail or stall indefinitely during the reconciliation phase. **Symptoms (Enablement):**  
You may observe one or more of the following symptoms when enabling secrets encryption: 

  * The `gkectl update admin` command hangs indefinitely.
  * In the bootstrap cluster, `ansible-runner` pods fail to start with a volume setup failure. Checking the pod logs or events shows a `FailedMount` warning or a `Forbidden` error from Node Restriction similar to the following: 
        
        MountVolume.SetUp failed for volume "etcd-encryption-volume" : secret "etcd-encryption-key-yyyy" not found (or Forbidden: ... Node Restriction ...)

  * If you attempt to retry the update after a failure, it fails immediately during the pivot phase with an admission webhook error: 
        
        admission webhook "vcluster.kb.io" denied the request: Cluster.baremetal.cluster.gke.io "gke-admin-yyyy" is invalid: annotations[baremetal.cluster.gke.io/etcd-secrets-encryption-key-versions]: Invalid value: "": etcd key version is not allowed to change during changing etcd secret encryption mode

  * The upgrade remains stuck, and `bm-system-update-control-plane-config` jobs are repeatedly created, successfully run on the nodes, and immediately deleted and recreated in a loop. On the control plane nodes, the `kube-scheduler` static pods continuously terminate and restart (receiving `SIGTERM` every 30-40 seconds).

**Symptoms (Disablement):**  
You may observe one or more of the following symptoms when disabling secrets encryption: 

  * The cluster upgrade or configuration update process hangs.
  * You see the control plane configuration update job (typically named starting with `bm-system-update-control-plane-config-`) continuously deleting and recreating itself in an infinite loop without completing.
  * A control plane node might experience volume mount failures on the host because Kubelet fails to mount old encryption keys or secrets, making the API server unhealthy.

**Workarounds:** To bypass these issues and allow the secrets encryption enablement or disablement update to complete successfully, apply the temporary mitigations described below depending on which cluster you are updating. **For Admin Cluster updates:**  
Apply the mitigations in the bootstrap cluster on your admin workstation while the update is stuck or retrying:

  1. Locate the temporary bootstrap cluster kubeconfig:  

         
         /home/ubuntu/.kube/kind-config-gkectl

  2. Save the following manifest as `bypass-node-restriction.yaml` to grant the bootstrap control plane node's identity permission to read secrets. This bypasses the Node Restriction error: 
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           name: bootstrap-secret-reader
           namespace: kube-system
         rules:
         - apiGroups: [""]
           resources: ["secrets"]
           verbs: ["get", "list"]
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: bootstrap-node-secret-reader
           namespace: kube-system
         subjects:
         - kind: Group
           name: system:nodes
           apiGroup: rbac.authorization.k8s.io
         roleRef:
           kind: Role
           name: bootstrap-secret-reader
           apiGroup: rbac.authorization.k8s.io

  3. Apply the manifest to the bootstrap cluster: 
         
         kubectl --kubeconfig=/home/ubuntu/.kube/kind-config-gkectl apply -f bypass-node-restriction.yaml

  4. Delete the validating webhook configuration: 
         
         kubectl --kubeconfig=/home/ubuntu/.kube/kind-config-gkectl delete validatingwebhookconfiguration lcm-validating-webhook-configuration

  5. List the control plane machine names: 
         
         kubectl --kubeconfig=/home/ubuntu/.kube/kind-config-gkectl get baremetalmachine -n kube-system

  6. Patch all listed control plane machines: 
         
         kubectl --kubeconfig=/home/ubuntu/.kube/kind-config-gkectl annotate baremetalmachine -n kube-system BMM_NAME_1 "baremetal.cluster.gke.io/etcd-secrets-encryption=1" --overwrite
         kubectl --kubeconfig=/home/ubuntu/.kube/kind-config-gkectl annotate baremetalmachine -n kube-system BMM_NAME_2 "baremetal.cluster.gke.io/etcd-secrets-encryption=1" --overwrite
         kubectl --kubeconfig=/home/ubuntu/.kube/kind-config-gkectl annotate baremetalmachine -n kube-system BMM_NAME_3 "baremetal.cluster.gke.io/etcd-secrets-encryption=1" --overwrite

Replace BMM_NAME_1, BMM_NAME_2, and BMM_NAME_3 with the bare metal machine names.

**For User Cluster updates:**  
Apply the mitigations directly in the admin cluster while the user cluster update is stuck or retrying:

  1. Save the following manifest as `bypass-node-restriction-user.yaml` to grant the admin cluster control plane nodes' identities permission to read secrets in the user cluster namespace. This bypasses the Node Restriction error: 
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           name: user-secret-reader
           namespace: USER_CLUSTER_NAMESPACE
         rules:
         - apiGroups: [""]
           resources: ["secrets"]
           verbs: ["get", "list"]
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: user-node-secret-reader
           namespace: USER_CLUSTER_NAMESPACE
         subjects:
         - kind: Group
           name: system:nodes
           apiGroup: rbac.authorization.k8s.io
         roleRef:
           kind: Role
           name: user-secret-reader
           apiGroup: rbac.authorization.k8s.io

Replace USER_CLUSTER_NAMESPACE with the name of the user cluster namespace.
  2. Apply the manifest to the admin cluster: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG apply -f bypass-node-restriction-user.yaml

Replace ADMIN_KUBECONFIG with the path to your admin cluster kubeconfig.
  3. List the user cluster control plane machine names: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG get baremetalmachine -n USER_CLUSTER_NAMESPACE

  4. Patch all listed control plane machines: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG annotate baremetalmachine -n USER_CLUSTER_NAMESPACEBMM_NAME_1 "baremetal.cluster.gke.io/etcd-secrets-encryption=1" --overwrite
         kubectl --kubeconfig=ADMIN_KUBECONFIG annotate baremetalmachine -n USER_CLUSTER_NAMESPACEBMM_NAME_2 "baremetal.cluster.gke.io/etcd-secrets-encryption=1" --overwrite
         kubectl --kubeconfig=ADMIN_KUBECONFIG annotate baremetalmachine -n USER_CLUSTER_NAMESPACEBMM_NAME_3 "baremetal.cluster.gke.io/etcd-secrets-encryption=1" --overwrite


**To unblock Always-on secrets encryption disablement:** Apply the temporary mitigations directly while the update is stuck or retrying. If you are updating a user cluster, apply the steps in the admin cluster. If you are updating the admin cluster, apply the steps in the **bootstrap cluster** on your admin workstation:

  1. Identify the BareMetalMachine resource that is stuck in the update loop
         
         kubectl get baremetalmachines -n USER_CLUSTER_NAMESPACE --kubeconfig ADMIN_KUBECONFIG>

  2. Manually update the status of the affected BareMetalMachine to clear the stale encryption key versions. Edit the BareMetalMachine resource status:
         
         kubectl edit baremetalmachine MACHINE_IP_ADDRESS -n USER_CLUSTER_NAMESPACE --kubeconfig ADMIN_KUBECONFIG --subresource=status

Replace MACHINE_IP_ADDRESS with the IP address of the bare metal machine.
  3. Locate the `status.etcdEncryptionKeyVersions` field and set it to an empty string (`""`):
         
         status:
           etcdEncryptionKeyVersions: ""

  4. Save your changes. The controller manager will recognize the decryption phase as complete, safely terminate the recreate loop, and automatically proceed to upgrade and roll over the remaining control plane nodes.

  
Installation, Upgrade, Advanced cluster | 1.33.0-1.33.800, 1.34.0-1.34.400, 1.35.0 | 

### User cluster installation or upgrade stalls if vSphere resource metrics are disabled

Installations or upgrade of advanced user clusters can stall indefinitely if you explicitly disable vSphere resource metrics in the configuration file. **Symptoms:**  
The installation or upgrade process hangs during the cluster provisioning phase (failing to reach `NodePoolsReady`). If you check the user cluster pods, you might see that `vsphere-csi-controller` pods remain in a `ContainerCreating` state, and `vsphere-csi-node` pods enter a `CrashLoopBackOff`.  **Verification:**  


  1. Review your `user-cluster.yaml` file and check if you have explicitly disabled metrics: 
         
         stackdriver:
           disableVsphereResourceMetrics: true

  2. Check the logs or events for the failed CSI pods. You will see a `FailedMount` warning similar to the following: 
         
         Warning FailedMount ... MountVolume.SetUp failed for volume "vsphere-cert" : configmap "vsphere-ca-
         certificate-1a2b3c4d" not found


**Workaround:**

  * To prevent this issue, set `stackdriver.disableVsphereResourceMetrics` to `false` (or remove it, as it defaults to `false`) in your user cluster configuration file before you start the installation or upgrade.
  * If the upgrade stalls, set this field to `false` and run `gkectl update cluster`.

  
Installation, Advanced cluster | 1.32, 1.33.0-1.33.800, 1.34.0-1.34.400 | 

### Advanced user cluster recreation stuck in PROVISIONING state due to missing service account

When you recreate a advanced user cluster using a name that was previously used, the recreation process might stall in the `PROVISIONING` state. This happens because stale resources from the previous cluster deletion can interfere with the recreation process. Specifically, a leftover `ClusterRoleBinding` from the old cluster prevents the system from automatically creating the required `k8s-health-check` `ServiceAccount` in the user cluster's namespace on the admin cluster. You might see an error message similar to the following in the cluster operator logs:
    
    
    pods "bm-system-kubernetes-check-..." is forbidden: error looking up service account USER_CLUSTER_NAMESPACE/k8s-health-check: serviceaccount "k8s-health-check" not found

**Workaround:** To resolve this issue, manually create the missing `ServiceAccount` in the user cluster's namespace on the admin cluster. For example, if your user cluster is named `my-user-cluster`, the namespace in the admin cluster is typically also `my-user-cluster`. Run the following command:
    
    
    kubectl --kubeconfig ADMIN_KUBECONFIG -n USER_CLUSTER_NAMESPACE create serviceaccount k8s-health-check

Replace `ADMIN_KUBECONFIG` with the path to your admin cluster kubeconfig file, and `USER_CLUSTER_NAMESPACE` with your actual user cluster namespace.  
Upgrades, Advanced cluster | 1.32.0-1.32.1000, 1.33.0-1.33.600, 1.34.0-1.34.200 | 

### Rerunning `gkectl upgrade admin` deletes the bootstrap cluster upgrade to the advanced clusters

If an operation fails during upgrade from a non-advanced cluster to an advanced cluster, and you rerun the `gkectl upgrade admin` command using an older binary, the operation might delete the bootstrap cluster. If the bootstrap cluster is deleted, the upgrade state is lost and the upgrade can't resume.  **Prevention:** You can avoid this issue by using the latest `gkectl` binary for your target minor version before attempting or retrying the upgrade. The following binaries (and beyond) include fixes to automatically reuse the bootstrap cluster and safely handle retries:

  * 1.32.1000-gke.57+
  * 1.33.700-gke.71+
  * 1.34.300-gke.50+

**Verification:** If the upgrade process fails or stalls, verify whether the bootstrap cluster still exists. Run the following command on the admin workstation: 
    
    
    docker ps -a -q --filter "label=io.x-k8s.kind.role=control-plane"

If the command returns a container ID, the bootstrap cluster is still active. **Do not delete it.** You can resume the upgrade using a fixed binary. If the command returns no output, the bootstrap cluster has been deleted. Follow the recovery steps below. **Recovery:** Follow these steps to recover and complete the upgrade:

  1. Download the latest `gkectl` binary for your target minor version (which contains the fix for handling existing machines). For example, if an upgrade to version 1.33.0 failed, download version 1.33.700-gke.71 or later.
  2. Resume the upgrade by running the update command with the `--force` flag to bypass the checks and recover the state: 
         
         gkectl update admin --force --skip-version-validation

  3. Once the bootstrap cluster is brought up, run the following command: 
         
         kubectl --kubeconfig .kube/kind-config-gkectl -n kube-system set env deployment/anthos-cluster-operator-VERSION SERVER_SIDE_PIVOT=true -c operator


  
Upgrades, Advanced cluster | 1.33.0-1.33.600, 1.34.0-1.34.200 | 

### Admission webhook error during cluster upgrade with `noProxy`

When you attempt to upgrade a cluster, the process stalls with the following error:
    
    
    Reconciliation failed: failed to create or update operator Cluster: failed to create or update operator Cluster :
    admission webhook "vcluster.kb.io" denied the request:
    Cluster.baremetal.cluster.gke.io "" is invalid:
    spec: Forbidden: Fields should not be changed during upgrade.
    (A in old)
    (B in new)
    ...
    A: },
    B: ,"noProxy":[""]},
    ...

An incorrect conversion bug causes an empty `noProxy` field (either `nil` or `""`) which the admission webhook detects as a configuration change.  
**Workaround:**

  1. Temporarily bypass the `UPDATE` check in the validating webhook before or during the upgrade: 
         
         kubectl patch --kubeconfig ADMIN_CLUSTER_KUBECONFIG validatingwebhookconfiguration lcm-validating-webhook-configuration -p '
         webhooks:
         - name: vcluster.kb.io
           rules:
           - apiGroups:
             - baremetal.cluster.gke.io
             apiVersions:
             - v1
             operations:
             - CREATE
             - DELETE
             resources:
             - clusters
         '

  2. Upgrade the cluster.
  3. Re-enable the webhook: 
         
         kubectl patch --kubeconfig ADMIN_CLUSTER_KUBECONFIG validatingwebhookconfiguration lcm-validating-webhook-configuration -p '
         webhooks:
         - name: vcluster.kb.io
           rules:
           - apiGroups:
             - baremetal.cluster.gke.io
             apiVersions:
             - v1
             operations:
             - CREATE
             - UPDATE
             - DELETE
             resources:
             - clusters
         '


  
Networking, Configuration | 1.34.0–1.34.300, 1.33.0-1.33.700, 1.32.0-1.32.1100 and earlier | 

### `gkectl check-config` fails with bundled ingress disabled in the user cluster configuration file 

If you disable bundled ingress for a new user cluster in the configuration file (see [Disable bundled ingress for a new cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/disable-bundled-ingress#disable_bundled_ingress_for_a_new_cluster)) and you run `gkectl check-config` to validate the user cluster configuration, the command can fail when the system performs preflight checks and tests VM creation. The failure happens because `cloud-init` generates an invalid network configuration command (for example, it might generate a command like `ip addr add /32 dev ens192`, which isn't valid). **Workaround:** Use the `--fast` flag with `gkectl check-config` to skip the slow preflight checks and run the fast validators and bypass the test VM creation failure without modifying your configuration file.  
Storage, Legacy Feature Migration | 1.29+ | 

### Control plane v2 migration fails across vSphere clusters

Control Plane v2 (CPv2) migration fails when user clusters are configured across different vSphere ESXi clusters, resulting in the control plane's specified datastore being inaccessible during preflight validation. The `masterNode.vsphere.datastore` field within the user cluster configuration is immutable, preventing direct modification. You see the following: `ControlPlane Datastore: datastore "***" is not accessible for cluster "***"`. **Workaround:** To proceed with the CPv2 migration, do the following: 

  1. In the user cluster configuration file, comment out the `masterNode.vsphere.datastore` field.
  2. Temporarily disable the validation webhook that enforces configuration immutability. The controller might re-enable the webhook before the migration. Run the command periodically until migration starts. 
         
         kubectl patch --kubeconfig ADMIN_CLUSTER_KUBECONFIG validatingwebhookconfiguration onprem-user-cluster-controller -p '
         webhooks:
         - name: vonpremusercluster.onprem.cluster.gke.io
           rules:
           - apiGroups:
             - onprem.cluster.gke.io
             apiVersions:
             - v1alpha1
             operations:
             - CREATE
             resources:
             - onpremuserclusters
         '

  3. Perform the Control Plane v2 migration.
  4. After the migration completes successfully, re-enable the validation webhook: 
         
         kubectl patch --kubeconfig ADMIN_CLUSTER_KUBECONFIG validatingwebhookconfiguration onprem-user-cluster-controller -p '
         webhooks:
         - name: vonpremusercluster.onprem.cluster.gke.io
           rules:
           - apiGroups:
             - onprem.cluster.gke.io
             apiVersions:
             - v1alpha1
             operations:
             - CREATE
             - UPDATE
             resources:
             - onpremuserclusters
         '


  
Networking, Upgrades and updates | 1.30 and later | 

### Istiod pod fails to reach readiness during upgrades

The bundled Ingress feature in Google Distributed Cloud uses `istiod`. This feature doesn't use custom resource definitions defined by Istio. However, because the code used is open source, the pods are sensitive to Istio installations that you might have for your own use cases. If there are no Istio custom resource definitions present in the clusters, Istiod declares itself as ready without waiting for custom resource definitions. However, if there are `v1beta` custom resource definitions in the cluster, Istiod waits for `v1` custom resource definitions before declaring readiness. As a result, the Istiod pod might fail to reach readiness, causing cluster upgrades to fail. **Verification:** To confirm whether your cluster is affected, check the Istiod pod status in the `gke-system` namespace:
    
    
    kubectl get pods -n gke-system -l app=istiod

If the pod status is `Running` but the readiness check fails (for example, `0/1` ready), your cluster is likely affected.   
**Workaround:** To resolve this issue, use one of the following workarounds:

  * Manually deploy the Istio `v1` custom resource definitions to your cluster. You can get the custom resource definitions from github. For example, <https://github.com/istio/api/blob/v1.25.2/kubernetes/customresourcedefinitions.gen.yaml>. Your version might vary.
  * Disable the bundled-ingress feature if you aren't using it. This workaround only works if you haven't started the cluster upgrade.

  
Upgrades, Advanced cluster | 1.32.0-1.32.1000, 1.33.0-1.33.600, 1.34.0-1.34.300 | 

### Cluster upgrade fails due to inconsistent fleet membership state

When you attempt to upgrade a cluster, the process can stall because of a fleet membership issue. **Symptom:** When you use the `gkectl upgrade` command, you receive an error similar to the following:
    
    
    failed registering cluster: failed to apply Hub Membership: Membership
    API request failed: rpc error: code = InvalidArgument desc = InvalidFieldError
    for field endpoint.on_prem_cluster.admin_cluster: field cannot be updated

**Workaround:** Manually unregister the cluster from the fleet using the following command. The system then automatically registers the cluster in the fleet.
    
    
    gcloud container fleet memberships unregister MEMBERSHIP_NAME \
      --project=PROJECT_ID \
      --context=CLUSTER_NAME \
      --kubeconfig=KUBECONFIG

Replace the following: 

  * MEMBERSHIP_NAME: The name used to uniquely represent the cluster in its fleet.
  * PROJECT_ID: The project ID of the Google Cloud project for your cluster.
  * CLUSTER_NAME: The name of your cluster you are unregistering.
  * KUBECONFIG: The path of your kubeconfig file.

  
Upgrades, Advanced cluster | 1.32.0-1.32.900, 1.33.0-1.33.500, 1.34.0-1.34.200 | 

### Node pool label `cloud.google.com/gke-nodepool` adds an unexpected `-np` suffix on workload `Node` after upgrading to Advanced Cluster

When you upgrade to an Advanced Cluster, the value of the `cloud.google.com/gke-nodepool` label on the `Node` updates with a `-np` suffix. Workloads that rely on this label for pod scheduling, such as those using node selectors or affinity rules, might fail to schedule or be rescheduled incorrectly. **Symptom:** To verify if your cluster is affected, check the labels on your nodes. Run the following command to check the labels on your nodes. If the `cloud.google.com/gke-nodepool` label has an unexpected `-np` suffix, your cluster is affected:
    
    
    kubectl --kubeconfig USER_KUBECONFIG get nodes --show-labels

**Workaround:** Manually overwrite the `cloud.google.com/gke-nodepool` label in the node pool before or after the upgrade: 

  1. Set this label in the [ node pool labels](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#labels-field) field: 
         
         nodePools:
         - name: NODE_POOL_NAME
           labels:
             ...
             "cloud.google.com/gke-nodepool": "NODE_POOL_NAME"

  2. Update the cluster by `gkectl update cluster`.

  
Upgrades, Advanced cluster | 1.32.0-1.32.900, 1.33.0-1.33.500, 1.34.0-1.34.200 | 

### Upgrading admin or user clusters fails if `stackdriver.enableVPC` is set to true

Upgrades to Advanced Clusters will fail if `stackdriver.enableVPC` is enabled. You will see `gkectl upgrade` exit with error: 
    
    
    Failed to generate diff: failed to get desired onprem admin cluster from
    seed config with dry-run webhooks: failed to apply validating webhook to
    OnPremAdminCluster: stackdriver.enableVPC: Invalid value: true: stackdriver
    VPC cannot be enabled when AdvancedCluster is enabled

This is because `stackdriver.enableVPC` field is already deprecated and we don't need to configure this field any more if DNS is set as suggested in the [Set up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#procedure-overview) **Workaround:** Disable the `stackdriver.enableVPC` field by `gkectl update admin/cluster --force`.   
Installation, Upgrades, Advanced cluster | 1.32.0-1.32.900, 1.33.0-1.33.500, 1.34.0-1.34.200 | 

### Creating or upgrading admin or user clusters fails if proxy configuration contains spaces

Creating or upgrading admin or user clusters might fail if the `proxy` or `noProxy` fields in your cluster configuration contain extraneous whitespaces, such as leading or trailing spaces or spaces between `noProxy` values. If there is a space in the configuration (for example, `noProxy: "noproxy-1.com, noproxy-2.com"`), the control plane load balancer initialization job fails, which halts the entire cluster creation or upgrade process. **Symptoms**

  * The cluster creation or upgrade process hangs or fails.
  * Check the logs of the control plane load balancer initialization pod (typically named starting with `bm-system-cplb-init-`) to see if a fatal error relates to command-line flags.

**Validate the root cause** If your cluster creation or upgrade fails, you can validate if this space-character issue is the root cause by inspecting the control plane load balancer initialization logs in the bootstrap (`kind`) cluster:

  1. Set the target of your `kubectl` to the temporary bootstrap cluster's kubeconfig file.
  2. Find the failing control plane load balancer initialization pod in the `kube-system` namespace: 
         
         kubectl get pods -n kube-system --kubeconfig .kube/kind-config-gkectl | grep cplb-init

  3. Check the logs for the specific pod: 
         
         kubectl logs CPLB_INIT_POD_NAME -n kube-system --kubeconfig .kube/kind-config-gkectl

  4. The proxy configuration contains spaces issue is the root cause if you see a fatal error in the output that looks similar to: 
         
         Agent pid <PID>
         Identity added: /etc/ssh-key/id_rsa (/etc/ssh-key/id_rsa)
         FYYYY YY:YY:YY.YYYYYY YY main.go:YYY] command line flag machine-address

This failure occurs because the space in the proxy string breaks the internal command-line argument parsing for the `machine-address` flag.

**Workaround:** **Before you start creation or upgrade** Before you start the cluster creation or upgrade, update your local `admin-cluster.yaml` configuration file to remove any spaces in the `proxy` and `noProxy` sections. Ensure the `noProxy` list is strictly comma-separated without spaces. **Example of incorrect configuration:**
    
    
    proxy:
      url: "http://proxy.example.com "
      noProxy: "noproxy-1.com, noproxy-2.com "

**Corrected configuration:**
    
    
    proxy:
      url: "http://proxy.example.com"
      noProxy: "noproxy-1.com,noproxy-2.com"

Save the file and proceed with your `gkectl` creation or upgrade command. **After you start the creation or upgrade** If the operation fails or gets stuck, manually edit the `OnPremAdminCluster` custom resource in the temporary bootstrap (`kind`) cluster to remove the extraneous spaces.

  1. Connect to the bootstrap `kind` cluster by pointing your `KUBECONFIG` to the temporary bootstrap cluster's kubeconfig file (e.g., `.kube/kind-config-gkectl`).
  2. Edit the `OnPremAdminCluster` resource: 
         
         kubectl edit onpremadmincluster ADMIN_CLUSTER_NAME -n kube-system --kubeconfig .kube/kind-config-gkectl

  3. Locate the `proxy` section in the custom resource specification and remove any spaces from the `url` and `noProxy` fields.
  4. Save your changes and exit the editor.
  5. The reconciliation loop automatically picks up the updated configuration, fixes the command-line arguments for the Ansible job, and attempts to resume the creation or upgrade process.

**Note:** Update your local `admin-cluster.yaml` configuration file so that future operations succeed.  
Upgrades, Advanced cluster | 1.32.0-1.32.900, 1.33.0-1.33.500, 1.34.0-1.34.200 | 

### `gkectl upgrade admin` fails on retry with "AlreadyExists" errors in the bootstrap cluster

If you run the `gkectl upgrade admin` command a second time and the operation fails, the bootstrap cluster might be trying to recreate resources that already exist. **How to verify:** Check the `gkectl` logs for the following error messages:

  * `failed to create credential namespace in bootstrap cluster: namespaces "anthos-creds" already exists`
  * `failed to create stackdriver service account secret in bootstrap cluster: secrets "google-cloud-credentials" already exists`

**Workaround:** Delete the conflicting resources from the temporary kind bootstrap cluster before you retry the upgrade. The `kubeconfig` for the kind bootstrap cluster is located at `.kube/kind-config-gkectl`.

  1. If needed, back up your configurations or states.
  2. Delete the `anthos-creds` namespace and the `google-cloud-credentials` secret using the kind cluster's `kubeconfig`: 
         
         # Delete the credential namespace
         KUBECONFIG=.kube/kind-config-gkectl kubectl delete namespace anthos-creds --ignore-not-found
         
         # Delete the stackdriver service account secret
         KUBECONFIG=.kube/kind-config-gkectl kubectl delete secret google-cloud-credentials -n kube-system --ignore-not-found

  3. Retry the `gkectl upgrade admin` command.

  
Upgrades, Advanced cluster | 1.32.0-1.32.800, 1.33.0-1.33.400, 1.34.0 | 

### User cluster upgrade to Advanced Cluster stalls at worker node pool upgrade

Worker node upgrades might stall during user cluster [upgrading to Advanced Cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster) even after you successfully update the control plane.  You will see `gkectl upgrade` output stuck with an error message similar to: 
    
    
    Cluster is not ready yet: ready condition is not true: CreateOrUpdateNodePools:
    Creating or updating node pools, unready node pools: [NODE_POOL_NAME...]...

The `kube-system/anthos-cluster-operator` logs might also report a reconciler error similar to this: 
    
    
    msg"="Reconciler error"
    "error"="failed to create or update NodePoolClaim:
    failed to create or update NodePoolClaim [NODE_POOL_NAME...]:
    admission webhook \"vnodepoolclaim.kb.io\" denied the request:
    NodePoolClaim.baremetal.cluster.gke.io \"[NODE_POOL_NAME...]\" is invalid: spec:
    Forbidden: Fields should be immutable.

This occurs if the `OnPremNodePool` specification contains labels that trigger an immutable field validation error in the `vnodepoolclaim.kb.io` admission webhook. **Workaround:** **Option 1** To unblock the upgrade, manually create `NodePoolConfig` resources in the admin cluster for each affected node pool:
    
    
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: NodePoolConfig
    metadata:
      name: NODE_POOL_NAME-np
      namespace: USER_CLUSTER_NAME
    spec:
      updateStrategy:
        nodeRecreationUpdate:
          maxSurge: 1
          maxUnavailable: 0

**Option 2** Alternatively, you can temporarily disable the `UPDATE` rule for `nodepoolclaims` in the `lcm-validating-webhook-configuration` on the admin cluster to allow the upgrade to proceed:
    
    
    kubectl patch --kubeconfig ADMIN_KUBECONFIG validatingwebhookconfiguration lcm-validating-webhook-configuration -p '
    webhooks:
    - name: vnodepoolclaim.kb.io
      rules:
      - apiGroups:
        - baremetal.cluster.gke.io
        apiVersions:
        - v1
        operations:
        - CREATE
        resources:
        - nodepoolclaims
    '

Restore the webhook once the upgrade is finished:
    
    
    kubectl patch --kubeconfig ADMIN_KUBECONFIG validatingwebhookconfiguration lcm-validating-webhook-configuration -p '
    webhooks:
    - name: vnodepoolclaim.kb.io
      rules:
      - apiGroups:
        - baremetal.cluster.gke.io
        apiVersions:
        - v1
        operations:
        - CREATE
        - UPDATE
        resources:
        - nodepoolclaims
    '  
  
VMware, Logging and monitoring | 1.34 and earlier versions | 

### Anthos on VMware: vCenter vpxd becomes unresponsive due to `vmodl.fault.ManagedObjectNotFound` errors

The vCenter vpxd service becomes unresponsive due to a flood of `vmodl.fault.ManagedObjectNotFound` errors. This occurs when Anthos on VMware components, particularly the `vsphere-metrics-exporter` pod, continuously send API requests to vCenter using stale `ContainerView` objects after a vSphere session is re-established. You can see errors in vCenter vpxd logs that originate from a component attempting to use a `ContainerView` object that has already been deleted or not completely created from a previous vSphere session. A complete fix for this behavior is planned for an upcoming Anthos on VMware release. **Workaround:** To temporarily restore vCenter vpxd responsiveness, restart the `vsphere-metrics-exporter` pod in the Anthos on VMware admin and user cluster.  
Upgrades, Advanced cluster | 1.32 to 1.33 | 

### Anthos on VMware Advanced Cluster Upgrade Stuck with "cannot assign NodeRef to Machine" Error

An Anthos on VMware Advanced Cluster upgrade can become stuck during control plane node registration. Nodes don't register because node objects are stale, providerIDs are mismatched, or kubelet initialization fails. The stale node object containing an old `providerID` causes an error message that looks similar to the following: `{"log":""msg"="Reconciliation for Machine asked to requeue" "error"="cannot assign NodeRef to Machine \"[MACHINE_IP_ADDRESS]\" in namespace \"[NAMESPACE]\", no matching Node: requeue in 10s" "cluster"="[CLUSTER_NAME]" "logger"="controllers.Machine" "machine"="[MACHINE_IP_ADDRESS]" "namespace"="[NAMESPACE]"", "logtag":"F", "pid":"1", "source_file":"machine_controller.go", "source_line":"234"}`` **Workaround:** For control plane nodes that display an error stating `cannot assign NodeRef to Machine` errors:

  1. On the affected control plane VM, verify the `providerID` used by kubelet:
         
         ps aux | grep kubelet | grep provider-id
                 

  2. If the `providerID` is incorrect or the node object is stale, delete the stale node object.
  3. To restart the kubelet process on the affected VM, do the following:
         
         systemctl restart kubelet
                 

  4. If the node registers but lacks the "control-plane" role, manually add the necessary label:
         
         kubectl label node NODE_NAME node-role.kubernetes.io/control-plane=""
                 

  5. If the upgrade is still stuck after about 15 minutes, contact the support team for potential control plane node recovery.

  
Upgrades, Networking | 1.30 to 1.31 | 

### Upgrade Fails with CNI Pods Stuck in `Init:CreateContainerConfigError`

During an upgrade from version 1.30 to 1.31, `anetd` CNI pods on newly created control plane nodes can become stuck in `Init:CreateContainerConfigError`. The specific error message is `services have not yet been read at least once, cannot construct envvars`. This transient state occurs because a Kubernetes 1.31 kubelet attempts to retrieve service information from a Kubernetes 1.30 API server. The 1.30 API server lacks support for required field selectors, such as `spec.clusterIP`. This incompatibility occurs during the control plane rolling upgrade when both 1.30 and 1.31 nodes are present. The CNI Pod stall can last from a few seconds in low-workload environments to over 15 minutes in higher-load, non-production environments. The KMS plugin and secrets encryption aren't related to this issue. **Workaround** : The issue is transient and resolves after all control plane nodes successfully complete the upgrade to version 1.31. Allow the upgrade process to proceed naturally, because the pods become healthy once all nodes are running the target version.  
Other | 1.13+ | 

### Google Cloud console displays admin cluster after admin cluster is deleted

After you delete an admin cluster, Google Cloud console continues to display the cluster in the **Kubernetes Engine** > **Clusters** section. This issue is caused by orphaned GKE On-Prem API resources. **Workaround:** Unenroll the admin cluster from the GKE On-Prem API by running the `gcloud container vmware admin-clusters unenroll` command with the `--ignore-errors` flag:
    
    
    gcloud container vmware admin-clusters unenroll ADMIN_CLUSTER_NAME \
        --project=PROJECT_ID \
        --location=REGION \
        --ignore-errors

If Google Cloud console still displays the admin cluster, run the following command to delete the hub membership:
    
    
    gcloud container hub memberships delete ADMIN_CLUSTER_NAME \
        --project=PROJECT_ID \
        --location=REGION

Replace the following:

  * `ADMIN_CLUSTER_NAME`: the name of the admin cluster that you want to unenroll from the GKE On-Prem API.
  * `PROJECT_ID`: the fleet host project ID.
  * `REGION`: the Google Cloud region you specified when you created the cluster.

  
Upgrades, Advanced cluster | 1.32 to 1.33 | 

### User cluster upgrade to advanced cluster fails if you upgrade control plane and node pools separately

When you upgrade a user cluster from version 1.32 to 1.33, the upgrade automatically converts the cluster to an [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters). The [automatic upgrade to an advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#automatic_upgrade_to_advanced_clusters_in_133) doesn't allow version skew between the control plane and node pools. If you attempt to upgrade the control plane and the node pools in separate operations, the version skew causes the `gkectl upgrade cluster` command to fail with the following error message:
    
    
    Failed to generate diff summary: failed to get desired onprem user cluster and node pools from seed config with dry-run webhooks: failed to apply mutating and validating webhooks to OnPremNodePools: failed to get OSImage getter for mutating webhook: failed to get vm template ConfigMap: VM Template 'default/vm-template-1.32.x' not found for version "1.32.x", which must have been created before the target onprem CR
    

**Workaround:** In your user cluster configuration file, set the `gkeOnPremVersion` under all node pools to the same version as the cluster's target upgrade version (1.33.x). This ensures that the operation upgrades the control plane and node pools at the same time.  
Updates, Advanced cluster | 1.32.0-1.32.600, 1.33.0-1.33.100 | 

### Failed to update non-HA user cluster to HA advanced cluster due to immutable `masterNode.replicas` field

Using `gkectl update` to update a non-high availability (non-HA) user cluster to an advanced cluster with an HA control plane fails and gives the following error message:
    
    
    Failed to generate diff summary: failed to get desired onprem user cluster and node pools from seed config with dry-run webhooks:
    failed to apply validating webhook to OnPremUserCluster:
    masterNode.replcias: Forbidden: the field must not be mutated, diff (-before, +after): int64(- 1,+ 3)
    

**Workaround:** Use the `gkectl upgrade` command to [upgrade the non-HA user cluster to an HA advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster#upgrade_1).  
Updates | 1.30, 1.31 | 

### Windows Pods remain Pending after ControlPlaneV2 migration due to invalid TLS certificate

During an Google Distributed Cloud update operation that includes a ControlPlaneV2 migration from version 1.30.x to 1.31.x, Windows Pods might fail to schedule and remain in a `Pending` state. This problem manifests as a TLS certificate validation error for the `windows-webhook` mutating admission webhook. The issue occurs because the certificate's Subject Alternative Name (SAN) incorrectly retains a value valid for the old Kubeception architecture instead of being regenerated for the new `kube-system.svc` endpoint. You might observe the following error message: `failed calling webhook "windows.webhooks.gke.io": failed to call webhook: Post "https://windows-webhook.kube-system.svc:443/pod?timeout=10s": tls: failed to verify certificate: x509`. This situation can arise from the ControlPlaneV2 migration process copying etcd content, which carries over the old certificate without proper regeneration. It is important to note that Windows node pools are a deprecated feature and will be unavailable in Google Distributed Cloud 1.33 and later versions. **Workaround:**

  1. Backup the `user-component-options` Secret in the user cluster's namespace:
         
         kubectl get secret user-component-options -n USER_CLUSTER_NAME -oyaml > backup.yaml
             

  2. Delete the `user-component-options` secret:
         
         kubectl delete secret user-component-options -n USER_CLUSTER_NAME
             

  3. Edit the `onpremusercluster` resource to trigger reconciliation by adding the `onprem.cluster.gke.io/reconcile: "true"` annotation:
         
         kubectl edit onpremusercluster USER_CLUSTER_NAME -n USER_CLUSTER_MGMT_NAMESPACE
             


Replace `USER_CLUSTER_NAME` with the name of your user cluster.  
Upgrades, Updates, Advanced cluster | 1.32.0-1.32.500, 1.33.0 | 

### Upgrading/Updating to an advanced cluster fails if [stackdriver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-section) is not configured

When upgrading/updating a non-advanced cluster to an advanced cluster, the process might stop responding if [stackdriver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-section) isn't enabled.  **Workaround:**

  * If the cluster isn't upgraded yet, you need to follow steps to enable `stackdriver`: 
    1. Add the [stackdriver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-section) section to your cluster configuration file. 
    2. Run [`gkectl update`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general) to enable `stackdriver`. 
  * If an upgrade is already in progress, use the following steps: 
    1. Edit the `user-cluster-creds` Secret in the `USER_CLUSTER_NAME-gke-onprem-mgmt` namespace with the following command: 
           
           kubectl --kubeconfig ADMIN_KUBECONFIG \
             patch secret user-cluster-creds \
             -n USER_CLUSTER_NAME-gke-onprem-mgmt \
             --type merge -p "{\"data\":{\"stackdriver-service-account-key\":\"$(cat STACKDRIVER_SERVICE_ACCOUNT_KEY_FILE | base64 | tr -d '\n')\"}}"

    2. Update the `OnPremUserCluster` custom resource with stackdriver field, you should use the same project with same project location and service account key as cloudauditlogging if you have enabled the feature. 
           
           kubectl --kubeconfig ADMIN_KUBECONFIG \
               patch onpremusercluster USER_CLUSTER_NAME \
               -n USER_CLUSTER_NAME-gke-onprem-mgmt --type merge -p '
               spec:
                 stackdriver:
                   clusterLocation: PROJECT_LOCATION
                   providerID: PROJECT_ID
                   serviceAccountKey:
                     kubernetesSecret:
                       keyName: stackdriver-service-account-key
                       name: user-cluster-creds
           '

    3. Add the [stackdriver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-section) section to your cluster configuration file for consistency. 

  
Upgrades | 1.29, 1.30, 1.31, 1.32+ | 

### Pods unable to connect to Kubernetes API Server with Dataplane V2 and restrictive Network Policies

In clusters using Control Plane V2 (CPv2) architecture (default in version 1.29 and later) and Dataplane V2, Pods might fail to connect to the Kubernetes API server (`kubernetes.default.svc.cluster.local`). This issue is often triggered by the presence of Network Policies, especially those with default deny egress rules. Symptoms include the following: 

  * TCP connection attempts to the API server's cluster IP address or node IP addresses result in a `Connection reset by peer` message.
  * TLS handshake failures when connecting to the API server.
  * Running the `cilium monitor -t drop` command on the affected node can show packets destined for the control plane node IP addresses and API server port (typically 6443) being dropped.

**Cause** This issue arises from an interaction between Dataplane V2 (based on Cilium) and Kubernetes Network Policies in the CPv2 architecture, where control plane components run on nodes within the user cluster. The default Cilium configuration does not correctly interpret ipBlock rules in Network Policies that are intended to allow traffic to the Node IPs of the control plane members. This issue is related to an upstream Cilium issue ([cilium#20550](https://github.com/cilium/cilium/issues/20550)).  **Workaround:** For versions 1.29, 1.30, and 1.31, avoid using restrictive egress Network Policies that might block traffic to the control plane nodes. If you need a default deny policy, you might need to add a broad allow rule for all egress traffic, for example, by not specifying any to rules in the egress section, effectively allowing all egress. This solution is less secure and might not be suitable for all environments. For all other versions, enable a Cilium configuration to correctly match node IPs in Network Policy ipBlock fields. To match node IPs in Network Policy `ipBlock` fields, do the following:

  1. Edit the `cilium-config` ConfigMap: 
         
         kubectl edit configmap -n kube-system cilium-config

  2. Add or modify the data section to include `policy-cidr-match-mode: nodes`: 
         
         data:
               policy-cidr-match-mode: nodes

  3. To apply the configuration change, restart the anetd DaemonSet: 
         
         kubectl rollout restart ds anetd -n kube-system

  4. Ensure you have a Network Policy that explicitly allows egress traffic from your Pods to the control plane node IPs on the API server port. Identify the IP addresses of your user cluster control plane nodes by running `kubectl get svc kubernetes`. The output is similar to the following: 
         
         apiVersion: networking.k8s.io/v1
             kind: NetworkPolicy
             metadata:
               name: allow-egress-to-kube-apiserver
               namespace: NAMESPACE_NAME
             spec:
               podSelector: {}
               policyTypes:
               - Egress
               egress:
               - to:
                 - ipBlock:
                     cidr: CP_NODE_IP_1/32
                 - ipBlock:
                     cidr: CP_NODE_IP_2/32
                 ports:
                 - protocol: TCP
                   port: 6443 # Kubernetes API Server port on the node
         
             


  
Installation | 1.30.200-gke.101 | 

### The `gke-connect` agent Pod stuck in `Pending` state during user cluster creation

During user cluster creation, the `gke-connect` agent Pod might become stuck in a `Pending` state, preventing the cluster from being fully created. This issue occurs because the `gke-connect` agent Pod attempts to schedule before worker nodes are available, leading to a deadlock. This issue arises when the initial user cluster creation fails due to preflight validation errors, and a subsequent attempt to create the cluster is made without first deleting the partially created resources. On the subsequent cluster creation attempt, the `gke-connect` agent Pod is stuck due to untolerated taints on control-plane nodes, as indicated by an error similar to the following:
    
    
        0/3 nodes are available: 3 node(s) had untolerated taint {node-role.kubernetes.io/control-plane: }`.
        

**Workaround:** If user cluster creation fails due to preflight validation errors, delete the partially created cluster resources before attempting to create the cluster again with corrected configurations. This ensures that the creation workflow proceeds correctly, including the creation of node pools before the `gke-connect` agent Pod is deployed.  
Update | 1.16 and earlier versions, 1.28.0-1.28.1100, 1.29.0-1.29.700, 1.30.0-1.30.200 | 

### Secrets still encrypted after disabling always-on secrets encryption

After disabling [always-on secrets encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption) with `gkectl update cluster`, the secrets are still stored in `etcd` with encryption. This issue applies to kubeception user clusters only. If your cluster uses Controlplane V2, you aren't affected by this issue. To check whether the secrets are still encrypted, run the following command, which retrieves the `default/private-registry-creds` secret stored in `etcd`:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        exec -it -n USER_CLUSTER_NAME kube-etcd-0 -c kube-etcd -- \
        /bin/sh -ec "export ETCDCTL_API=3; etcdctl \
        --endpoints=https://127.0.0.1:2379 \
        --cacert=/etcd.local.config/certificates/etcdCA.crt \
        --cert=/etcd.local.config/certificates/etcd.crt \
        --key=/etcd.local.config/certificates/etcd.key \
        get /registry/secrets/default/private-registry-creds" | hexdump -C
    

If the secret is stored with encryption, the output looks like the following:
    
    
    00000000  2f 72 65 67 69 73 74 72  79 2f 73 65 63 72 65 74  |/registry/secret|
    00000010  73 2f 64 65 66 61 75 6c  74 2f 70 72 69 76 61 74  |s/default/privat|
    00000020  65 2d 72 65 67 69 73 74  72 79 2d 63 72 65 64 73  |e-registry-creds|
    00000030  0d 0a 6b 38 73 3a 65 6e  63 3a 6b 6d 73 3a 76 31  |..k8s:enc:kms:v1|
    00000040  3a 67 65 6e 65 72 61 74  65 64 2d 6b 65 79 2d 6b  |:generated-key-k|
    00000050  6d 73 2d 70 6c 75 67 69  6e 2d 31 3a 00 89 65 79  |ms-plugin-1:..ey|
    00000060  4a 68 62 47 63 69 4f 69  4a 6b 61 58 49 69 4c 43  |JhbGciOiJkaXIiLC|
    ...

If the secret isn't stored with encryption, the output looks like the following:
    
    
    00000000  2f 72 65 67 69 73 74 72  79 2f 73 65 63 72 65 74  |/registry/secret|
    00000010  73 2f 64 65 66 61 75 6c  74 2f 70 72 69 76 61 74  |s/default/privat|
    00000020  65 2d 72 65 67 69 73 74  72 79 2d 63 72 65 64 73  |e-registry-creds|
    00000030  0d 0a 6b 38 73 00 0d 0a  0c 0d 0a 02 76 31 12 06  |..k8s.......v1..|
    00000040  53 65 63 72 65 74 12 83  47 0d 0a b0 2d 0d 0a 16  |Secret..G...-...|
    00000050  70 72 69 76 61 74 65 2d  72 65 67 69 73 74 72 79  |private-registry|
    00000060  2d 63 72 65 64 73 12 00  1a 07 64 65 66 61 75 6c  |-creds....defaul|
    ...

**Workaround:**

  1. Do a rolling update on a specific DaemonSet, as follows: 
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
               rollout restart statefulsets kube-apiserver \
               -n USER_CLUSTER_NAME
             

  2. Get the manifests of all the secrets in the user cluster, in YAML format: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
               get secrets -A -o yaml > SECRETS_MANIFEST.yaml
             

  3. Reapply all the secrets in the user cluster so that all secrets are stored in `etcd` as plaintext: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
               apply -f SECRETS_MANIFEST.yaml
             


  
Configuration | 1.29, 1.30, 1.31 | 

### Generated `user-cluster.yaml` file is missing the `hostgroups` field

The user cluster configuration file, `user-cluster.yaml`, generated by the `gkectl get-config` command is missing the `hostgroups` field in the `nodePools` section. The `gkectl get-config` command generates the `user-cluster.yaml` file based on the contents of the `OnPremUserCluster` custom resource. The `nodePools[i].vsphere.hostgroups` field, however, exists in the `OnPremNodePool` custom resource and isn't copied to the `user-cluster.yaml` file when you run `gkectl get-config`. **Workaround** To resolve this issue, manually add the `nodePools[i].vsphere.hostgroups` field to the `user-cluster.yaml` file. The edited file should look similar to the following example:
    
    
    apiVersion: v1
    kind: UserCluster
    ...
    nodePools:
    - name: "worker-pool-1"
      enableLoadBalancer: true
      replicas: 3**  vsphere:
        hostgroups:
        - "hostgroup-1"**
    ...

You can use the edited user cluster configuration file to update your user cluster without triggering errors and the `hostgroups` field is persisted.  
Networking | 1.29.0-1.29.1000 1.30.0-1.30.500, 1.31.0-1.31.100 | 

### Bundled ingress is not compatible with `gateway.networking.k8s.io` resources

Istiod pods of bundled ingress cannot be ready if `gateway.networking.k8s.io` resources are installed into the user cluster. The following example error message can be found in pod logs:
    
    
        failed to list *v1beta1.Gateway: gateways.gateway.networking.k8s.io is forbidden: User \"system:serviceaccount:gke-system:istiod-service-account\" cannot list resource \"gateways\" in API group \"gateway.networking.k8s.io\" at the cluster scope"
        

**Workaround:** Apply the following ClusterRole and ClusterRoleBinding to your user cluster: 
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: istiod-gateway
    rules:
    - apiGroups:
      - 'gateway.networking.k8s.io'
      resources:
      - '*'
      verbs:
      - get
      - list
      - watch
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: istiod-gateway-binding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: istiod-gateway
    subjects:
    - kind: ServiceAccount
      name: istiod-service-account
      namespace: gke-system
          
  
Installation | 1.29.0-1.29.1000 1.30.0-1.30.500, 1.31.0-1.31.100 | 

### Admin cluster control plane nodes keep rebooting after running `gkectl create admin`

If hostnames in the [`ipblocks`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-controlplaneipblock-ips-section) field contain uppercase letters, the admin cluster control plane nodes might reboot over and over. **Workaround:** Use lowercase hostnames only.  
Installation, Upgrades | 1.30.0-1.30.500, 1.31.0-1.31.100 | 

### `Runtime: out of memory` "error" after running `gkeadm create` or `upgrade`

When creating or upgrading admin workstations with `gkeadm`, commands, you might get an OOM error when verifying the downloaded OS image. For example, 
    
    
    Downloading OS image
    "gs://gke-on-prem-release/admin-appliance/1.30.400-gke.133/gke-on-prem-admin-appliance-vsphere-1.30.400-gke.133.ova"...
    
    [==================================================>] 10.7GB/10.7GB
    
    Image saved to
    /anthos/gke-on-prem-admin-appliance-vsphere-1.30.400-gke.133.ova
    
    Verifying image gke-on-prem-admin-appliance-vsphere-1.30.400-gke.133.ova...
    |
    
    runtime: out of memory
    

**Workaround:**
* Increase the OS memory size where you execute the `gkeadm` command.  
Upgrades | 1.30.0-1.30.400 | 

### Non-HA admin cluster upgrade stuck at `Creating or updating cluster control plane workloads`

When upgrading a non-HA admin cluster, the upgrade might get stuck at the `Creating or updating cluster control plane workloads`. This issue happens if in the admin master VM, `ip a | grep cali` returns a non-empty result. For example, 
    
    
    ubuntu@abf8a975479b-qual-342-0afd1d9c ~ $ ip a | grep cali
    4: cali2251589245f@if3:  mtu 1500 qdisc noqueue state UP group default
    

**Workaround:**

  1. Repair the admin master: 
         
         gkectl repair admin-master --kubeconfig=ADMIN_KUBECONFIG \
             --config=ADMIN_CONFIG_FILE \
             --skip-validation
         

  2. Select the 1.30 VM template if you see a prompt like the following example: 
         
         Please select the control plane VM template to be used for re-creating the
         admin cluster's control plane VM.
         

  3. Resume the upgrade: 
         
         gkectl upgrade admin --kubeconfig ADMIN_KUBECONFIG \
             --config ADMIN_CONFIG_FILE
         


  
Configuration | 1.31.0 | 

### Redundant `isControlPlane` field in the cluster configuration file under `network.controlPlaneIPBlock`

Cluster configuration files generated by `gkectl create-config` in 1.31.0 contain a redundant `isControlPlane` field under `network.controlPlaneIPBlock`:
    
    
        controlPlaneIPBlock:
        netmask: ""
        gateway: ""
        ips:
        - ip: ""
          hostname: ""
          **isControlPlane: false**
        - ip: ""
          hostname: ""
          **isControlPlane: false**
        - ip: ""
          hostname: ""
          **isControlPlane: false**
        

This field is not needed and can be safely removed from the configuration file.   
Migration | 1.29.0-1.29.800, 1.30.0-1.30.400, 1.31.0 | 

### Admin add-on nodes stuck at NotReady during non-HA to HA admin cluster migration

When migrating a non-HA admin cluster that uses MetalLB to HA, admin add-on nodes might get stuck at a `NotReady` status, preventing the migration from completing. This issue only affects admin clusters configured with MetalLB, where auto-repair isn't enabled. This issue is caused by a race condition during migration where MetalLB speakers are still using the old `metallb-memberlist` secret. As a result of the race condition, the old control plane VIP becomes inaccessible, which causes the migration to stall. **Workaround:**

  1. Delete the existing `metallb-memberlist` secret: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n kube-system \
             delete secret metallb-memberlist
         

  2. Restart the `metallb-controller` Deployment so it can generate the new `metallb-memberlist`: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n kube-system \
             rollout restart deployment metallb-controller
         

  3. Ensure the new `metallb-memberlist` is generated: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n kube-system \
             get secret metallb-memberlist
         

  4. Update `updateStrategy.rollingUpdate.maxUnavailable` in the `metallb-speaker` DaemonSet from `1` to `100%`. This step is required, because certain DaemonSet pods are running on the `NotReady` nodes.
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n kube-system \
             edit daemonset metallb-speaker
         

  5. Restart the `metallb-speaker` DaemonSet so it can pick up the new memberlist: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n kube-system \
             rollout restart daemonset metallb-speaker
         

After a few minutes, the admin add-on nodes become `Ready` again, and the migration can continue.
  6. If the initial `gkectl` command timed out after more than 3 hours, rerun `gkectl update` to resume the failed migration.

  
Configuration, Operation | 1.12+, 1.13+, 1.14+, 1.15+, 1.16+, 1.28+, 1.29+, 1.30+ | 

### Cluster backup for non-HA admin cluster fails due to long datastore and datadisk names

When attempting to backup a non-HA admin cluster, the backup fails due to the combined length of the datastore and datadisk names exceeding the maximum character length. The maximum character length for a datastore name is 80.  
The backup path for a non-HA admin cluster has the naming syntax "__". So if the concatenated name exceeds the maximum length, backup folder creation will fail **Workaround:** Rename the datastore or datadisk to a shorter name.  
Ensure that the combined length of the datastore and datadisk names does not exceed the maximum character length.  
Upgrades | 1.28, 1.29, 1.30 | 

### HA admin control plane node shows older version after running `gkectl repair admin-master`

After running the `gkectl repair admin-master` command, an admin control plane node might show an older version than the expected version. This issue occurs because the backed up VM template used for the HA admin control plane node repair isn't refreshed in vCenter after an upgrade, because the backup VM template wasn't cloned during machine creation if the machine name remains unchanged. **Workaround:**

  1. Find out the machine name that is using the older Kubernetes version: 
         
         kubectl get machine -o wide --kubeconfig=ADMIN_KUBECONFIG
             

  2. Remove the `onprem.cluster.gke.io/prevented-deletion` annotation: 
         
         kubectl edit machine MACHINE_NAME --kubeconfig=ADMIN_KUBECONFIG
             

Save the edit.
  3. Run the following command to delete the machine: 
         
         kubectl delete machine MACHINE_NAME --kubeconfig=ADMIN_KUBECONFIG
             

A new machine will be created with the correct version.

  
Configuration | 1.30.0 | 

### Terraform removes `vCenter` fields unexpectedly

When updating a user cluster or nodepool using Terraform, Terraform might attempt to set `vCenter` fields to empty values. This issue can occur if the cluster wasn't originally created using Terraform. **Workaround:** To prevent the unexpected update, ensure that the update is safe before running `terraform apply`, as described in the following:

  1. Run `terraform plan`
  2. In the output, check whether the `vCenter` fields are set to `nil`.
  3. If any `vCenter` field is set to an empty value, in the Terraform configuration, add `vcenter` to the `ignore_changes` list following [ the Terraform documentation](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle#ignore_changes). This prevents updates to these fields.
  4. Run `terraform plan` again and check the output to confirm the update is as expected 

  
Updates | 1.13, 1.14, 1.15, 1.16 | 

### User cluster control plane nodes always get rebooted during the first admin cluster update operation 

After the kubeception user clusters' control plane nodes are created, updated or upgraded, they will be rebooted one by one, during the first admin cluster operation when the admin cluster is created at or upgraded to one of the affected versions. For kubeception clusters with 3 control-plane nodes, this shouldn't lead to control-plane downtime and the only impact is that the admin cluster operation takes longer.   
Installation, Upgrades and updates | 1.31 | 

### Errors creating custom resources

In version 1.31 of Google Distributed Cloud, you might get errors when you try to create custom resources, such as clusters (all types) and workloads. The issue is caused by a breaking change introduced in Kubernetes 1.31 that prevents the `caBundle` field in a custom resource definition from transitioning from a valid to an invalid state. For more information about the change, see the [Kubernetes 1.31 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#api-change-3).  Prior to Kubernetes 1.31, the `caBundle` field was often set to a makeshift value of `\n`, because in earlier Kubernetes versions the API server didn't allow empty CA bundle content. Using `\n` was a reasonable workaround to avoid confusion, as the `cert-manager` typically updates the `caBundle` later. If the `caBundle` has been patched once from an invalid to a valid state, there shouldn't be issues. However, if the custom resource definition is reconciled back to `\n` (or another invalid value), you might encounter the following error:
    
    
    ...Invalid value: []byte{0x5c, 0x6e}: unable to load root certificates: unable to parse bytes as PEM block]
    

**Workaround** If you have a custom resource definition in which `caBundle` is set to an invalid value, you can safely remove the `caBundle` field entirely. This should resolve the issue.  
OS | 1.31 | 

### `cloud-init status` always returns error

When upgrading a cluster that uses the Container Optimized OS (COS) OS image to 1.31, the `cloud-init status` command fails although cloud-init finished without errors. **Workaround:** Run the following command to check the status of cloud-init:
    
    
        systemctl show -p Result cloud-final.service
        

If the output is similar to the following, then cloud-init finished successfully:
    
    
        Result=success
          
  
Upgrades | 1.28 | 

### Admin workstation preflight check fails when upgrading to 1.28 with disk size less than 100 GB

When upgrading a cluster to 1.28, the `gkectl prepare` command fails while running admin workstation preflight checks if the admin workstation disk size is less than 100 GB. In this case, the command displays an error message similar to the following:
    
    
        Workstation Hardware: Workstation hardware requirements are not satisfied
        

In 1.28, the admin workstation disk size prerequisite was increased from 50 GB to 100 GB. **Workaround:**

  1. [Roll back the admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#roll_back_an_admin_workstation_after_an_upgrade).
  2. [Update the admin workstation config file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-workstation-configuration-file#adminworkstationdiskgb) to increase the disk size to at least 100 GB.
  3. [Upgrade the admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_awstation).

  
Upgrades | 1.30 | 

### `gkectl` returns false error on netapp storageclass

The `gkectl upgrade` command returns an incorrect error about the netapp storageclass. The error message is similar to the following, 
    
    
        detected unsupported drivers:
          csi.trident.netapp.io
        

**Workaround:** Run `gkectl upgrade` with `--skip-pre-upgrade-checks` flag.  
Identity | all versions | 

### Invalid CA certificate after cluster CA rotation in `ClientConfig` prevents cluster authentication

After you rotate the certificate authority (CA) certificates on a user cluster, the `spec.certificateAuthorityData` field in the `ClientConfig` contains an invalid CA certificate, which prevents authentication to the cluster. **Workaround:** Before the next gcloud CLI authentication, manually update the `spec.certificateAuthorityData` field in the `ClientConfig` with the correct CA certificate.

  1. Copy the cluster CA certificate from the `certificate-authority-data` field in the admin cluster kubeconfig.
  2. Edit the `ClientConfig` and paste the CA certificate in the `spec.certificateAuthorityData` field. 
         
         kubectl edit clientconfig default -n kube-public --kubeconfig USER_CLUSTER_KUBECONFIG
             


  
Updates | 1.28, 1.29, 1.30 | 

### Preflight check fails when disabling bundled ingress

When you disable bundled ingress by removing the `loadBalancer.vips.ingressVIP` field in the cluster configuration file, a bug in the MetalLB preflight check causes the cluster update to fail with the "invalid user ingress vip: invalid IP" error message. **Workaround:** Ignore the error message.  
Skip the preflight check using one of the following methods:

  * Add the `--skip-validation-load-balancer` flag to the `gkectl update cluster` command.
  * Annotate the `onpremusercluster` object with `onprem.cluster.gke.io/server-side-preflight-skip: skip-validation-load-balancer`
. 
  
VMware, Upgrades | 1.16 | 

### Cluster upgrade fails due to missing anti-affinity group rule in vCenter

During a cluster upgrade, the machine objects may get stuck in the `Creating` phase and fail to link to the node objects due to a missing anti-affinity group (AAG) rule in vCenter. If you describe the problematic machine objects, you can see recurring messages like "Reconfigure DRS rule task "task-xxxx" complete"
    
    
        kubectl --kubeconfig KUBECONFIG describe machine MACHINE_OBJECT_NAME
        

**Workaround:** Disable the anti-affinity group setting for in both the [admin cluster config](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#antiaffinitygroups-enabled-field) and the [user cluster config](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#antiaffinitygroups-enabled-field) and trigger force update command to unblock cluster upgrade:
    
    
        gkectl update admin --config ADMIN_CLUSTER_CONFIG_FILE --kubeconfig ADMIN_CLUSTER_KUBECONFIG --force
        
    
    
        gkectl update cluster --config USER_CLUSTER_CONFIG_FILE --kubeconfig USER_CLUSTER_KUBECONFIG --force
          
  
Migration | 1.29, 1.30 | 

### Migrating a user cluster to Controlplane V2 fails if secrets encryption has ever been enabled

When migrating a user cluster to Controlplane V2, if [ always-on secrets encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption) has ever been enabled, the migration process fails to properly handle the secret encryption key. Because of this issue, the new Controlplane V2 cluster is unable to decrypt secrets. If the output of the following command isn't empty, then always-on secrets encryption has been enabled at some point and the cluster is affected by this issue:
    
    
        kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
          get onpremusercluster USER_CLUSTER_NAME \
          -n USER_CLUSTER_NAME-gke-onprem-mgmt \
          -o jsonpath={.spec.secretsEncryption}
        

If you have already started the migration and the migration fails, contact Google for support. Otherwise, before the migration, [ disable always-on secrets encryption and decrypt secrets](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-kubeception-controlplane-v2#disable_and_decrypt_secrets).   
Migration | 1.29.0-1.29.600, 1.30.0-1.30.100 | 

### Migrating an admin cluster from non-HA to HA fails if secrets encryption is enabled

If the admin cluster has enabled [always-on secrets encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption) at 1.14 or earlier, and upgraded all the way from old versions to the affected 1.29 and 1.30 versions, when migrating admin cluster from non-HA to HA, the migration process fails to properly handle the secret encryption key, Because of this issue, the new HA admin cluster is unable to decrypt secrets. To check if the cluster could be using the old formatted key:
    
    
        kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get secret -n kube-system admin-master-component-options -o jsonpath='{.data.data}' | base64 -d | grep -oP '"GeneratedKeys":\[.*?\]'
        

If the output shows the empty key like the following, then it like means the cluster will be affected by this issue:
    
    
        "GeneratedKeys":[{"KeyVersion":"1","Key":""}]
        

If you have already started the migration and the migration fails, contact Google for support. Otherwise, before starting the migration, [rotate the encryption key](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption#key_rotation).  
Upgrades | 1.16, 1.28, 1.29, 1.30 | 

### `credential.yaml` regenerated incorrectly during admin workstation upgrade

When upgrading the admin workstation using the `gkeadm upgrade admin-workstation` command, the `credential.yaml` file is regenerated incorrectly. The username and password fields are empty. Additionally, the `privateRegistry` key contains a typo. The same misspelling of the `privateRegistry` key is also in the `admin-cluster.yaml` file.  
Since the `credential.yaml` file is regenerated during the admin cluster upgrade process, the typo is present even if you corrected previously. **Workaround:**

  * Update the private registry key name in `credential.yaml` to match the `privateRegistry.credentials.fileRef.entry` in the `admin-cluster.yaml`.
  * Update the private registry username and password in the `credential.yaml`.

  
Upgrades | 1.16+ | 

### User cluster upgrade fails due to pre-upgrade reconcile timeout

When upgrading a user cluster, the pre-upgrade reconcile operation might take longer than the defined timeout, resulting in an upgrade failure. The error message looks like the following:
    
    
    Failed to reconcile the user cluster before upgrade: the pre-upgrade reconcile failed, error message:
    failed to wait for reconcile to complete: error: timed out waiting for the condition,
    message: Cluster reconcile hasn't finished yet, please fix that before
    rerun the upgrade.
    

The timeout for the pre-upgrade reconcile operation is 5 minutes plus 1 minute per node pool in the user cluster. **Workaround:** Ensure that the [`gkectl diagnose cluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) command passes without errors.  
Skip the pre-upgrade reconcile operation by adding the `--skip-reconcile-before-preflight` flag to the `gkectl upgrade cluster` command. For example:
    
    
    gkectl upgrade cluster --skip-reconcile-before-preflight --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
    --config USER_CLUSTER_CONFIG_FILE  
  
Updates | 1.16, 1.28.0-1.28.800, 1.29.0-1.29.400, 1.30.0  | 

### Updating DataplaneV2 ForwardMode doesn't automatically trigger anetd DaemonSet restart

When you update the user cluster [dataplaneV2.forwardMode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-1.29#dataplanev2-forwardmode-field) field using `gkectl update cluster`, the change is only updated in the ConfigMap, the `anetd` DaemonSet won't pick up the config change until restarted and your changes aren't applied. **Workaround:** When the `gkectl update cluster` command is done, you see output of `Done updating the user cluster`. After you see that message, run the following command to restart the `anetd` DaemonSet to pick up the config change:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG rollout restart daemonset anetd

Check the DaemonSet readiness after the restart:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get daemonset anetd

In the output of the preceding command, verify that the number in the `DESIRED` column matches the number in the `READY` column.  
Upgrades | 1.16 | 

### etcdctl command not found during cluster upgrade at the admin cluster backup stage

During a 1.16 to 1.28 user cluster upgrade, the admin cluster is backed up. The admin cluster backup process displays the error message "etcdctl: command not found". The user cluster upgrade succeeds, and the admin cluster remains in a healthy state. The only issue is that the metadata file on the admin cluster isn't backed up. The cause of the issue is that the `etcdctl` binary was added in 1.28, and isn't available on 1.16 nodes. The admin cluster backup involve several steps, including taking an etcd snapshot and then writing the metadata file for the admin cluster. The etcd backup still succeeds because `etcdctl` can still be triggered after an exec into the etcd Pod. But writing the metadata file fails as it still relies on the `etcdctl` binary to be installed on the node. However, the metadata file backup isn't a blocker for taking a backup, so the backup process still succeeds, as does the user cluster upgrade. **Workaround:** If want to take a backup of the metadata file, follow [Back up and restore an admin cluster with gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl) to trigger a separate admin cluster backup using the version of `gkectl` that matches the version of your admin cluster.  
Installation | 1.16-1.29 | 

### User cluster creation failure with manual load balancing

When creating a user cluster configured for manual load balancing, a `gkectl check-config` failure occurs indicating that the `ingressHTTPNodePort` value must be at least 30000, even when bundled ingress is disabled. This issue occurs regardless of whether the `ingressHTTPNodePort` and `ingressHTTPSNodePort` fields are set or left blank. **Workaround:** To work around this issue, ignore the result returned by `gkectl check-config`. To disable bundled ingress, see [Disable bundled ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/disable-bundled-ingress#disable_bundled_ingress_for_a_new_cluster).  
Updates | 1.29.0 | 

### After migrating a user cluster to Controlplane V2, the admin cluster metrics-server PDB might become incorrectly configured

The issue with the `PodDisruptionBudget` (PDB) occurs when using high availability (HA) admin clusters, and there is 0 or 1 admin cluster node without a role after the migration. To check if there are node objects without a role, run the following command:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get nodes -o wide

If there are two or more node objects without a role after the migration, then the PDB isn't misconfigured. **Symptoms:** The output of [admin cluster diagnose](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_admin_cluster) includes the following information
    
    
    Checking all poddisruptionbudgets...FAILURE
      Reason: 1 pod disruption budget error(s).
      Unhealthy Resources:
      PodDisruptionBudget metrics-server: gke-managed-metrics-server/metrics-server might be configured incorrectly: the total replicas(1) should be larger than spec.MinAvailable(1).
    

**Workaround:** Run the following command to delete the PDB:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG delete pdb metrics-server -n gke-managed-metrics-server  
  
Installation, Upgrades and updates | 1.28.0-1.28.600,1.29.0-1.29.100 | 

### Binary Authorization webook blocks CNI plugin to start causing one of nodepool failed to come up

Under rare race conditions, an incorrect installation sequence of the Binary Authorization webhook and the gke-connect pod may cause user cluster creation to stall due to a node failing to reach a ready state. In affected scenarios, user cluster creation may stall due to a node failing to reach a ready state. If this occurs, the following message will be displayed:
    
    
         Node pool is not ready: ready condition is not true: CreateOrUpdateNodePool: 2/3 replicas are ready
        

**Workaround:**

  1. Remove the Binary Authorization configuration from your config file. For setup instructions, please refer to the [Binary Authorization day 2 installation guide for GKE on VMware](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem#gke-on-vmware). 
  2. To unblock an unhealthy node during the current cluster creation process, temporarily remove the Binary Authorization webhook configuration in user cluster using the following command. 
         
         kubectl --kubeconfig USER_KUBECONFIG delete ValidatingWebhookConfiguration binauthz-validating-webhook-configuration
                 

Once the bootstrap process is complete, you can re-add the following webhook configuration. 
         
         apiVersion: admissionregistration.k8s.io/v1
         kind: ValidatingWebhookConfiguration
         metadata:
           name: binauthz-validating-webhook-configuration
         webhooks:
         - name: "binaryauthorization.googleapis.com"
           namespaceSelector:
             matchExpressions:
             - key: control-plane
               operator: DoesNotExist
           objectSelector:
             matchExpressions:
             - key: "image-policy.k8s.io/break-glass"
               operator: NotIn
               values: ["true"]
           rules:
           - apiGroups:
             - ""
             apiVersions:
             - v1
             operations:
             - CREATE
             - UPDATE
             resources:
             - pods
             - pods/ephemeralcontainers
           admissionReviewVersions:
           - "v1beta1"
           clientConfig:
             service:
               name: binauthz
               namespace: binauthz-system
               path: /binauthz
             # CA Bundle will be updated by the cert rotator.
             caBundle: Cg==
           timeoutSeconds: 10
           # Fail Open
           failurePolicy: "Ignore"
           sideEffects: None
                 


  
Upgrades | 1.16, 1.28, 1.29 | 

### CPV2 user cluster upgrade stuck due to mirrored machine with `deletionTimestamp`

During a user cluster upgrade, the upgrade operation might get stuck if the mirrored machine object in the user cluster contains a `deletionTimestamp`. The following error message is displayed if the upgrade is stuck:
    
    
        machine is still in the process of being drained and subsequently removed
        

This issue can occur if you previously attempted to repair the user control plane node by running `gkectl delete machine` against the mirrored machine in the user cluster. **Workaround:**

  1. Get the mirrored machine object and save it to a local file for backup purposes.
  2. Run the following command to delete the finalizer from the mirrored machine and wait for it to be deleted from the user cluster. 
         
         kubectl --kubeconfig ADMIN_KUBECONFIG patch machine/MACHINE_OBJECT_NAME -n USER_CLUSTER_NAME-gke-onprem-mgmt -p '{"metadata":{"finalizers":[]}}' --type=merge

  3. Follow the steps in [ Controlplane V2 user cluster control plane node](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair#controlplane_v2_user_cluster_control_plane_node) to trigger node repair on the control plane nodes, so that the correct source machine spec will be re-synced into the user cluster.
  4. Rerun the `gkectl upgrade cluster` to resume the upgrade

  
Configuration, Installation | 1.15, 1.16, 1.28, 1.29 | 

### Cluster creation failure due to control plane VIP in different subnet

For HA admin cluster or ControlPlane V2 user cluster, the control plane VIP needs to be in the same subnet as other cluster nodes. Otherwise, cluster creation fails because kubelet can't communicate with the API server using the control plane VIP. **Workaround:** Before cluster creation, ensure that the control plane VIP is configured in the same subnet as the other cluster nodes.  
Installation, Upgrades, Updates | 1.29.0 - 1.29.100 | 

### Cluster Creation/Upgrade Failure due to non-FQDN vCenter Username

Cluster creation/upgrade fails with an error in vsphere CSI pods indicating that the vCenter username is invalid. This occurs because the username used is not a fully qualified domain name. Error message in the vsphere-csi-controller pod as below:
    
    
        GetCnsconfig failed with err: username is invalid, make sure it is a fully qualified domain username
        

This issue only occurs in version 1.29 and later, as a validation was added to the vSphere CSI driver to enforce the use of fully qualified domain usernames. **Workaround:** Use a fully qualified domain name for the vCenter username in the credentials configuration file. For example, instead of using "username1", use "username1@example.com".  
Upgrades, Updates | 1.28.0 - 1.28.500 | 

### Admin cluster upgrade fails for clusters created on versions 1.10 or earlier

When upgrading an admin cluster from 1.16 to 1.28, the bootstrap of the new admin master machine might fail to generate the control-plane certificate. The issue is caused by changes in how certificates are generated for the Kubernetes API server in version 1.28 and later. The issue reproduces for clusters created on versions 1.10 and earlier that have been upgraded all the way to 1.16 and the leaf certificate was not rotated before the upgrade. To determine if the admin cluster upgrade failure is caused by this issue, do the following steps:

  1. Connect to the failed admin master machine by using SSH.
  2. Open `/var/log/startup.log` and search for an error like the following:


    
    
    Error adding extensions from section apiserver_ext
    801B3213B57F0000:error:1100007B:X509 V3 routines:v2i_AUTHORITY_KEYID:unable to get issuer keyid:../crypto/x509/v3_akid.c:177:
    801B3213B57F0000:error:11000080:X509 V3 routines:X509V3_EXT_nconf_int:error in extension:../crypto/x509/v3_conf.c:48:section=apiserver_ext, name=authorityKeyIdentifier, value=keyid>
       

**Workaround:**

  1. Connect to the admin master machine by using SSH. For details, see [Using SSH to connect to an admin cluster node](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ssh-cluster-node#admin).
  2. Make a copy `/etc/startup/pki-yaml.sh` and name it `/etc/startup/pki-yaml-copy.sh`
  3. Edit `/etc/startup/pki-yaml-copy.sh`. Find `authorityKeyIdentifier=keyidset` and change it to `authorityKeyIdentifier=keyid,issuer` in the sections for the following extensions: `apiserver_ext`, `client_ext`, `etcd_server_ext`, and `kubelet_server_ext`. For example: 
         
         [ apiserver_ext ]
               keyUsage = critical, digitalSignature, keyEncipherment
               extendedKeyUsage=serverAuth
               basicConstraints = critical,CA:false
               authorityKeyIdentifier = keyid,issuer
               subjectAltName = @apiserver_alt_names
         

  4. Save the changes to `/etc/startup/pki-yaml-copy.sh`.
  5. Using a text editor, open `/opt/bin/master.sh`, find and replace all occurrences of `/etc/startup/pki-yaml.sh` with `/etc/startup/pki-yaml-copy.sh`, then save the changes.
  6. Run `/opt/bin/master.sh` to generate the certificate and complete the machine startup.
  7. Run the `gkectl upgrade admin` again to upgrade the admin cluster.
  8. After the upgrade completes, rotate the leaf certificate for both admin and user clusters, as described in [Start the rotation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-ca-rotation#start_the_rotation).
  9. After the certificate rotation completes, make the same edits to `/etc/startup/pki-yaml-copy.sh` as you did previously, and run `/opt/bin/master.sh`.

  
Configuration | 1.29.0 | 

### Incorrect warning message for clusters with Dataplane V2 enabled

The following incorrect warning message is output when you run `gkectl` to create, update, or upgrade a cluster that already has Dataplane V2 enabled:
    
    
    WARNING: Your user cluster is currently running our original architecture with
    [DataPlaneV1(calico)]. To enable new and advanced features we strongly recommend
    to update it to the newer architecture with [DataPlaneV2] once our migration
    tool is available.
    

There's a bug in gkectl which causes it to always show this warning as long as the `dataplaneV2.forwardMode` is not being used, even if you already have set `enableDataplaneV2: true` in your cluster configuration file. **Workaround:** You can safely ignore this warning.  
Configuration | 1.28.0-1.28.400, 1.29.0 | 

### HA admin cluster installation preflight check reports wrong number of required static IPs

When you create an HA admin cluster, the preflight check displays the following incorrect error message:
    
    
    - Validation Category: Network Configuration
        - [FAILURE] CIDR, VIP and static IP (availability and overlapping): needed
        at least X+1 IP addresses for admin cluster with X nodes
    

The requirement is incorrect for 1.28 and higher HA admin clusters because they no longer have add-on nodes. Additionally, because the 3 admin cluster control plane node IPs are specified in the `network.controlPlaneIPBlock` section in the admin cluster configuration file, the IPs in IP block file are only needed for kubeception user cluster control plane nodes. **Workaround:** To skip the incorrect preflight check in a non-fixed release, add `--skip-validation-net-config` to the `gkectl` command.  
Operation | 1.29.0-1.29.100 | 

### Connect Agent loses connection to Google Cloud after non-HA to HA admin cluster migration

If you migrated [ from a non-HA admin cluster to an HA admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-admin-cluster-ha), the Connect Agent in the admin cluster loses the connection to `gkeconnect.googleapis.com` with the error "Failed to verify JWT signature". This is because during the migration, the KSA signing key is changed, thus a re-registration is needed to refresh the OIDC JWKs.  **Workaround:** To reconnect the admin cluster to Google Cloud, do the following steps to trigger a re-registration: First get the `gke-connect` deployment name:
    
    
    kubectl --kubeconfig KUBECONFIG get deployment -n gke-connect

Delete the `gke-connect` deployment:
    
    
    kubectl --kubeconfig KUBECONFIG delete deployment GKE_CONNECT_DEPLOYMENT -n gke-connect

Trigger a force reconcile for the `onprem-admin-cluster-controller` by adding a "force-reconcile" annotation to your `onpremadmincluster` CR:
    
    
    kubectl --kubeconfig KUBECONFIG patch onpremadmincluster ADMIN_CLUSTER_NAME -n kube-system --type merge -p '
    metadata:
      annotations:
        onprem.cluster.gke.io/force-reconcile: "true"
    '

The idea is that the `onprem-admin-cluster-controller` will always redeploy the `gke-connect` deployment and re-register the cluster if it finds no existing `gke-connect` deployment available. After the workaround (it may take a few minutes for the controller to finish the reconcile), you can verify that the "Failed to verify JWT signature" 400 error is gone from the `gke-connect-agent` logs:
    
    
    kubectl --kubeconfig KUBECONFIG logs GKE_CONNECT_POD_NAME -n gke-connect  
  
Installation, Operating system | 1.28.0-1.28.500, 1.29.0 | 

### Docker bridge IP uses 172.17.0.1/16 for COS cluster control plane nodes

Google Distributed Cloud specifies a dedicated subnet, `--bip=169.254.123.1/24`, for the Docker bridge IP in the Docker configuration to prevent reserving the default `172.17.0.1/16` subnet. However, in version 1.28.0-1.28.500 and 1.29.0, the Docker service wasn't restarted after Google Distributed Cloud customized the Docker configuration because of a regression in the COS OS image. As a result, Docker picks the default `172.17.0.1/16` as its bridge IP address subnet. This might cause an IP address conflict if you already have a workload running within that IP address range. **Workaround:** To work around this issue, you must restart the docker service:
    
    
    sudo systemctl restart docker

Verify that Docker picks the correct bridge IP address:
    
    
    ip a | grep docker0

This solution does not persist across VM re-creations. You must reapply this workaround whenever VMs are re-created.  
update | 1.28.0-1.28.400, 1.29.0-1.29.100 | 

### Using multiple network interfaces with standard CNI does not work

The standard CNI binaries `bridge, ipvlan, vlan, macvlan, dhcp, tuning, host-local, ptp, portmap` are not included in the OS images in the affected versions. These CNI binaries are not used by data plane v2, but can be used for additional network interfaces in the multiple network interface feature. Multiple network interface with these CNI plugins won't work. **Workaround:** Upgrade to the version with the fix if you are using this feature.  
update | 1.15, 1.16, 1.28  | 

### Netapp trident dependencies interfere with vSphere CSI driver

Installing `multipathd` on cluster nodes interferes with the vSphere CSI driver resulting in user workloads being unable to start. **Workaround:**

  * Disable `multipathd`

  
Updates | 1.15, 1.16 | 

### The admin cluster webhook might block updates

If some required configurations are empty in the admin cluster because validations were skipped, adding them might be blocked by the admin cluster webhook. For example, if the `gkeConnect` field wasn't set in an existing admin cluster, adding it with the `gkectl update admin` command might get the following error message:
    
    
    admission webhook "vonpremadmincluster.onprem.cluster.gke.io" denied the request: connect: Required value: GKE connect is required for user clusters
    

Occasionally, there might be a problem with communication between the Kubernetes API server and the webhook. When this happens, you might see the following error message: 
    
    
    failed to apply OnPremAdminCluster 'kube-system/gke-admin-btncc': Internal error occurred: failed calling webhook "monpremadmincluster.onprem.cluster.gke.io": failed to call webhook: Post "https://onprem-admin-cluster-controller.kube-system.svc:443/mutate-onprem-cluster-gke-io-v1alpha1-onpremadmincluster?timeout=10s": dial tcp 10.96.55.208:443: connect: connection refused
    

**Workaround:** If you encounter either of these errors, use one of the following workarounds, depending on your version: 

  * For 1.15 admin clusters, run `gkectl update admin` command with `--disable-admin-cluster-webhook` flag. For example: 
        
        gkectl update admin --config ADMIN_CLUSTER_CONFIG_FILE --kubeconfig ADMIN_CLUSTER_KUBECONFIG --disable-admin-cluster-webhook
                

  * For 1.16 admin clusters, run `gkectl update admin` commands with `--force` flag. For example: 
        
        gkectl update admin --config ADMIN_CLUSTER_CONFIG_FILE --kubeconfig ADMIN_CLUSTER_KUBECONFIG --force
                


  
Configuration | 1.15.0-1.15.10, 1.16.0-1.16.6, 1.28.0-1.28.200 | 

### `controlPlaneNodePort` field defaults to 30968 when `manualLB` spec is empty

If you will be using a manual load balancer (`loadBalancer.kind` is set to `"ManualLB"`), you shouldn't need to configure the `loadBalancer.manualLB` section in the configuration file for a high availability (HA) admin cluster in versions 1.16 and higher. But when this section is empty, Google Distributed Cloud assigns default values to all NodePorts including `manualLB.controlPlaneNodePort`, which causes cluster creation to fail with the following error message:
    
    
    - Validation Category: Manual LB
      - [FAILURE] NodePort configuration: manualLB.controlPlaneNodePort must
       not be set when using HA admin cluster, got: 30968

**Workaround:** Specify `manualLB.controlPlaneNodePort: 0` in you admin cluster configuration for the HA admin cluster:
    
    
    loadBalancer:
      ...
      kind: ManualLB
      manualLB:
        controlPlaneNodePort: 0
      ...  
  
Storage | 1.28.0-1.28.100 | 

### nfs-common is missing from Ubuntu OS image

`nfs-common` is missing from the Ubuntu OS image which may cause issues for customers using NFS-dependent drivers such as NetApp. If the log contains an entry like the following after upgrading to 1.28, then you are affected by this issue: 
    
    
    Warning FailedMount 63s (x8 over 2m28s) kubelet MountVolume.SetUp failed for volume "pvc-xxx-yyy-zzz" : rpc error: code = Internal desc = error mounting NFS volume 10.0.0.2:/trident_pvc_xxx-yyy-zzz on mountpoint /var/lib/kubelet/pods/aaa-bbb-ccc/volumes/kubernetes.io~csi/pvc-xxx-yyy-zzz/mount: exit status 32".
          

**Workaround:** Make sure your nodes can download packages from Canonical. Next, apply the following DaemonSet to your cluster to install `nfs-common`:
    
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: install-nfs-common
      labels:
        name: install-nfs-common
      namespace: kube-system
    spec:
      selector:
        matchLabels:
          name: install-nfs-common
      minReadySeconds: 0
      updateStrategy:
        type: RollingUpdate
        rollingUpdate:
          maxUnavailable: 100%
      template:
        metadata:
          labels:
            name: install-nfs-common
        spec:
          hostPID: true
          hostIPC: true
          hostNetwork: true
          initContainers:
          - name: install-nfs-common
            image: ubuntu
            imagePullPolicy: IfNotPresent
            securityContext:
              privileged: true
            command:
            - chroot
            - /host
            - bash
            - -c
            args:
            - |
              apt install -y nfs-common
            volumeMounts:
            - name: host
              mountPath: /host
          containers:
          - name: pause
            image: gcr.io/gke-on-prem-release/pause-amd64:3.1-gke.5
            imagePullPolicy: IfNotPresent
          volumes:
          - name: host
            hostPath:
              path: /
            
  
Storage | 1.28.0-1.28.100 | 

### Storage policy field is missing in the admin cluster configuration template

SPBM in admin clusters is supported in 1.28.0 and later versions. But the field `vCenter.storagePolicyName` is missing in the configuration file template. **Workaround:** Add the `vCenter.storagePolicyName` field in you admin cluster configuration file if you want to configure the storage policy for the admin cluster. Please refer to the [instructions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-storagepolicyname-field).  
Logging and monitoring | 1.28.0-1.28.100 | 

### Kubernetes Metadata API does not support VPC-SC

The recently added API kubernetesmetadata.googleapis.com does not support VPC-SC. This will cause metadata collecting agent to fail to reach this API under VPC-SC. Subsequently, metric metadata labels will be missing.  **Workaround:** Set in `kube-system` namespace the CR `stackdriver` set `featureGates.disableExperimentalMetadataAgent` field to `true` by running the command  `kubectl -n kube-system patch stackdriver stackdriver -p '{"spec":{"featureGates":{"disableExperimentalMetadataAgent":true}}}'`  then run  `kubectl -n kube-system patch deployment stackdriver-operator -p '{"spec":{"template":{"spec":{"containers":[{"name":"stackdriver-operator","env":[{"name":"ENABLE_LEGACY_METADATA_AGENT","value":"true"}]}]}}}}'`   
Upgrades, Updates | 1.15.0-1.15.7, 1.16.0-1.16.4, 1.28.0 | 

### The clusterapi-controller may crash when the admin cluster and any user cluster with ControlPlane V2 enabled use different vSphere credentials

When an admin cluster and any user cluster with ControlPlane V2 enabled use different vSphere credentials, e.g., after updating vSphere credentials for the admin cluster, the clusterapi-controller may fail to connect to the vCenter after restart. View the log of the clusterapi-controller running in the admin cluster's `kube-system` namespace,
    
    
    kubectl logs -f -l component=clusterapi-controllers -c vsphere-controller-manager \
        -n kube-system --kubeconfig KUBECONFIG

If the log contains an entry like the following, then you are affected by this issue: 
    
    
    E1214 00:02:54.095668       1 machine_controller.go:165] Error checking existence of machine instance for machine object gke-admin-node-77f48c4f7f-s8wj2: Failed to check if machine gke-admin-node-77f48c4f7f-s8wj2 exists: failed to find datacenter "VSPHERE_DATACENTER": datacenter 'VSPHERE_DATACENTER' not found

**Workaround:** [Update vSphere credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials#update_vsphere_credentials) so that the admin cluster and all the user clusters with Controlplane V2 enabled are using the same vSphere credentials.   
Logging and monitoring | 1.14 | 

### etcd high number of failed GRPC requests in Prometheus Alert Manager

Prometheus might report alerts similar to the following example:
    
    
    Alert Name: cluster:gke-admin-test1: Etcd cluster kube-system/kube-etcd: 100% of requests for Watch failed on etcd instance etcd-test-xx-n001.

To check if this alert is a false positive that can be ignored, complete the following steps:

  1. Check the raw `grpc_server_handled_total` metric against the `grpc_method` given in the alert message. In this example, check the `grpc_code` label for `Watch`.  
  
You can check this metric using Cloud Monitoring with the following MQL query: 
         
         fetch
             k8s_container | metric 'kubernetes.io/anthos/grpc_server_handled_total' | align rate(1m) | every 1m

  2. An alert on all codes other than `OK` can be safely ignored if the code is not one of the following: 
         
         Unknown|FailedPrecondition|ResourceExhausted|Internal|Unavailable|DataLoss|DeadlineExceeded


  
**Workaround:** To configure Prometheus to ignore these false positive alerts, review the following options:

  1. [Silence the alert](https://prometheus.io/docs/alerting/latest/alertmanager/#silences) from the Alert Manager UI.
  2. If silencing the alert isn't an option, review the following steps to suppress the false positives: 
     1. Scale down the monitoring operator to `0` replicas so that the modifications can persist.
     2. Modify the `prometheus-config` configmap, and add `grpc_method!="Watch"` to the `etcdHighNumberOfFailedGRPCRequests` alert config as shown in the following example: 
        * **Original:**
              
              rate(grpc_server_handled_total{cluster="CLUSTER_NAME",grpc_code!="OK",job=~".*etcd.*"}[5m])

        * **Modified:**
              
              rate(grpc_server_handled_total{cluster="CLUSTER_NAME",grpc_code=~"Unknown|FailedPrecondition|ResourceExhausted|Internal|Unavailable|DataLoss|DeadlineExceeded",grpc_method!="Watch",job=~".*etcd.*"}[5m])

Replace the following `CLUSTER_NAME` with the name of your cluster.
     3. Restart the Prometheus and Alertmanager Statefulset to pick up the new configuration.
  3. If the code falls into one of the problematic cases, then check etcd log and `kube-apiserver` log to debug more.

  
Networking | 1.16.0-1.16.2, 1.28.0 | 

### Egress NAT long lived connections are dropped

Egress NAT connections might be dropped after 5 to 10 minutes of a connection being established if there's no traffic. As the conntrack only matters in the inbound direction (external connections to the cluster), this issue only happens if the connection doesn't transmit any information for a while and then the destination side transmits something. If the egress NAT'd Pod always instantiates the messaging, then this issue won't be seen. This issue occurs because the anetd garbage collection inadvertently removes conntrack entries that the daemon thinks are unused. [An upstream fix](https://github.com/cilium/cilium/pull/24905) was recently integrated into anetd to correct the behavior.   
**Workaround:** There is no easy workaround, and we haven't seen issues in version 1.16 from this behavior. If you notice long lived connections dropped due to this issue, workarounds would be to use a workload on the same node as the egress IP address, or to consistently send messages on the TCP connection.  
Operation | 1.14, 1.15, 1.16 | 

### The CSR signer ignores `spec.expirationSeconds` when signing certificates

If you create a CertificateSigningRequest (CSR) with `expirationSeconds` set, the `expirationSeconds` is ignored. **Workaround:** If you're affected by this issue, you can update your user cluster by adding `disableNodeIDVerificationCSRSigning: true` in the user cluster configuration file and run the `gkectl update cluster` command to update the cluster with this configuration.  
Networking, Upgrades, Updates | 1.16.0-1.16.3 | 

### User cluster load balancer validation fails for `disable_bundled_ingress`

If you try to [disable bundled ingress for an existing cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/disable-bundled-ingress#disable_bundled_ingress_for_an_existing_cluster), the `gkectl update cluster` command fails with an error similar to the following example:
    
    
    [FAILURE] Config: ingress IP is required in user cluster spec
    

This error happens because `gkectl` checks for a load balancer ingress IP address during preflight checks. Although this check isn't required when disabling bundled ingress, the `gkectl` preflight check fails when `disableBundledIngress` is set to `true`.   
**Workaround:** Use the `--skip-validation-load-balancer` parameter when you update the cluster, as shown in the following example:
    
    
    gkectl update cluster \
      --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG  \
      --skip-validation-load-balancer

For more information, see how to [disable bundled ingress for an existing cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/disable-bundled-ingress#disable_bundled_ingress_for_an_existing_cluster).  
Upgrades, Updates | 1.13, 1.14, 1.15.0-1.15.6 | 

### Admin cluster updates fail after CA rotation

If you rotate admin cluster certificate authority (CA) certificates, subsequent attempts to run the `gkectl update admin` command fail. The error returned is similar to the following:
    
    
    failed to get last CARotationStage: configmaps "ca-rotation-stage" not found
    

  
**Workaround:** If you're affected by this issue, you can update your admin cluster by using the `--disable-update-from-checkpoint` flag with the `gkectl update admin` command:
    
    
    gkectl update admin --config ADMIN_CONFIG_file \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --disable-update-from-checkpoint

When you use the `--disable-update-from-checkpoint` flag, the update command doesn't use the checkpoint file as the source of truth during the cluster update. The checkpoint file is still updated for future use.  
Storage | 1.15.0-1.15.6, 1.16.0-1.16.2 | 

### CSI Workload preflight check fails due to Pod startup failure

During preflight checks, the CSI Workload validation check installs a Pod in the `default` namespace. The CSI Workload Pod validates that the vSphere CSI Driver is installed and can do dynamic volume provisioning. If this Pod doesn't start, the CSI Workload validation check fails. There are a few known issues that can prevent this Pod from starting: 

  * If the Pod doesn't have resources limits specified, which is the case for some clusters with admissions webhooks installed, the Pod doesn't start.
  * If Cloud Service Mesh is installed in the cluster with automatic Istio sidecar injection enabled in the `default` namespace, the CSI Workload Pod doesn't start.

If the CSI Workload Pod doesn't start, you see a timeout error like the following during preflight validations:
    
    
    - [FAILURE] CSI Workload: failure in CSIWorkload validation: failed to create writer Job to verify the write functionality using CSI: Job default/anthos-csi-workload-writer-<run-id> replicas are not in Succeeded phase: timed out waiting for the condition

To see if the failure is caused by lack of Pod resources set, run the following command to check the `anthos-csi-workload-writer-<run-id>` job status:
    
    
    kubectl describe job anthos-csi-workload-writer-<run-id>

If the resources limits aren't set properly for the CSI Workload Pod, the job status contains an error message like the following:
    
    
    CPU and memory resource limits is invalid, as it are not defined for container: volume-tester

If the CSI Workload Pod doesn't start because of Istio sidecar injection, you can temporarily disable the automatic Istio sidecar injection in the `default` namespace. Check the labels of the namespace and use the following command to delete the label that starts with `istio.io/rev`:
    
    
    kubectl label namespace default istio.io/rev-

If the Pod is misconfigured, manually verify that dynamic volume provisioning with the vSphere CSI Driver works:

  1. Create a PVC that uses the `standard-rwo` StorageClass.
  2. Create a Pod that uses the PVC.
  3. Verify that the Pod can read/write data to the volume.
  4. Remove the Pod and the PVC after you've verified proper operation.

If dynamic volume provisioning with the vSphere CSI Driver works, run `gkectl diagnose` or `gkectl upgrade` with the `--skip-validation-csi-workload` flag to skip the CSI Workload check.   
Operation | 1.16.0-1.16.2 | 

### User cluster update timeouts when admin cluster version is 1.15

When you are logged on to a [ user-managed admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation), the `gkectl update cluster` command might timeout and fail to update the user cluster. This happens if the admin cluster version is 1.15 and you run `gkectl update admin` before you run the `gkectl update cluster`. When this failure happens, you see the following error when trying to update the cluster: 
    
    
          Preflight check failed with failed to run server-side preflight checks: server-side preflight checks failed: timed out waiting for the condition
    Preflight check failed with failed to run server-side preflight checks: server-side preflight checks failed: timed out waiting for the condition
          

During the update of a 1.15 admin cluster, the `validation-controller` that triggers the preflight checks is removed from the cluster. If you then try to update the user cluster, the preflight check hangs until the timeout is reached.  **Workaround:**

  1. Run the following command to redeploy the `validation-controller`: 
         
         gkectl prepare --kubeconfig ADMIN_KUBECONFIG --bundle-path BUNDLE_PATH --upgrade-platform
               

  2. After the prepare completes, run the `gkectl update cluster` again to update the user cluster 

  
Operation | 1.16.0-1.16.2 | 

### User cluster create timeouts when admin cluster version is 1.15

When you are logged on to a [ user-managed admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation), the `gkectl create cluster` command might timeout and fail to create the user cluster. This happens if the admin cluster version is 1.15. When this failure happens, you see the following error when trying to create the cluster: 
    
    
          Preflight check failed with failed to run server-side preflight checks: server-side preflight checks failed: timed out waiting for the condition
    Preflight check failed with failed to run server-side preflight checks: server-side preflight checks failed: timed out waiting for the condition
          

Since the `validation-controller` was added in 1.16 then when using 1.15 admin cluster the `validation-controller` that is responsible to trigger the preflight checks is missing. Therefore, when trying to create user cluster the preflight checks hang till timeout is reached.  **Workaround:**

  1. Run the following command to deploy the `validation-controller`: 
         
         gkectl prepare --kubeconfig ADMIN_KUBECONFIG --bundle-path BUNDLE_PATH --upgrade-platform
               

  2. After the prepare completes, run the `gkectl create cluster` again to create the user cluster 

  
Upgrades, Updates | 1.16.0-1.16.2 | 

### Admin cluster update or upgrade fails if the projects or locations of add-on services don't match each other

When you upgrade an admin cluster from version 1.15.x to 1.16.x, or add a `connect`, `stackdriver`, `cloudAuditLogging`, or `gkeOnPremAPI` configuration when you update an admin cluster, the operation might be rejected by admin cluster webhook. One of the following error messages might be displayed: 

  * `"projects for connect, stackdriver and cloudAuditLogging must be the same when specified during cluster creation."`
  * `"locations for connect, gkeOnPremAPI, stackdriver and cloudAuditLogging must be in the same region when specified during cluster creation."`
  * `"locations for stackdriver and cloudAuditLogging must be the same when specified during cluster creation."`

An admin cluster update or upgrade requires the `onprem-admin-cluster-controller` to reconcile the admin cluster in a kind cluster. When the admin cluster state is restored in the kind cluster, the admin cluster webhook can't distinguish if the `OnPremAdminCluster` object is for an admin cluster creation, or to resume operations for an update or upgrade. Some create-only validations are invoked on updating and upgrading unexpectedly.   
**Workaround:** Add the `onprem.cluster.gke.io/skip-project-location-sameness-validation: true` annotation to the `OnPremAdminCluster` object:

  1. Edit the `onpremadminclusters` cluster resource: 
         
         kubectl edit onpremadminclusters ADMIN_CLUSTER_NAME -n kube-system –kubeconfig ADMIN_CLUSTER_KUBECONFIG

Replace the following: 
     * `ADMIN_CLUSTER_NAME`: the name of the admin cluster.
     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
  2. Add the `onprem.cluster.gke.io/skip-project-location-sameness-validation: true` annotation and save the custom resource.
  3. Depending on the type of admin clusters, complete one of the following steps: 
     * **For non-HA admin clusters with a checkpoint file:** add the parameter `disable-update-from-checkpoint` in the update command, or add the parameter `disable-upgrade-from-checkpoint` in the upgrade command. These parameters are only needed for the next time that you run the `update` or `upgrade` command: 
       * gkectl update admin --config ADMIN_CONFIG_file --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
               --disable-update-from-checkpoint

       * gkectl upgrade admin --config ADMIN_CONFIG_file --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
               --disable-upgrade-from-checkpoint

     * **For HA admin clusters or checkpoint file is disabled:** update or upgrade admin cluster as normal. No additional parameters are needed on the update or upgrade commands.

  
Operation | 1.16.0-1.16.2 | 

### User cluster deletion fails when using a user-managed admin workstation

When you are logged on to a [ user-managed admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation), the `gkectl delete cluster` command might timeout and fail to delete the user cluster. This happens if you have first run `gkectl` on the user-managed workstation to create, update, or upgrade the user cluster. When this failure happens, you see the following error when trying to delete the cluster: 
    
    
          failed to wait for user cluster management namespace "USER_CLUSTER_NAME-gke-onprem-mgmt"
          to be deleted: timed out waiting for the condition
          

During deletion, a cluster first deletes all of its objects. The deletion of the Validation objects (that were created during the create, update, or upgrade) are stuck at the deleting phase. This happens because a finalizer blocks the object's deletion, which causes cluster deletion to fail.  **Workaround:**

  1. Get the names of all the Validation objects: 
         
         kubectl  --kubeconfig ADMIN_KUBECONFIG get validations \
                    -n USER_CLUSTER_NAME-gke-onprem-mgmt
                 

  2. For each Validation object, run the following command to remove the finalizer from the Validation object: 
         
         kubectl --kubeconfig ADMIN_KUBECONFIG patch validation/VALIDATION_OBJECT_NAME \
                 -n USER_CLUSTER_NAME-gke-onprem-mgmt -p '{"metadata":{"finalizers":[]}}' --type=merge
               

After removing the finalizer from all Validation objects, the objects are removed and the user cluster delete operation completes automatically. You don't need to take additional action. 

  
Networking | 1.15, 1.16 | 

### Egress NAT gateway traffic to external server fails

If the source Pod and egress NAT gateway Pod are on two different worker nodes, traffic from the source Pod can't reach any external services. If the Pods are located on the same host, the connection to external service or application is successful. This issue is caused by vSphere dropping VXLAN packets when tunnel aggregation is enabled. There's a known issue with NSX and VMware that only sends aggregated traffic on known VXLAN ports (4789).   
**Workaround:** Change the VXLAN port used by Cilium to `4789`: 

  1. Edit the `cilium-config` ConfigMap: 
         
         kubectl edit cm -n kube-system cilium-config --kubeconfig USER_CLUSTER_KUBECONFIG

  2. Add the following to the `cilium-config` ConfigMap: 
         
         tunnel-port: 4789

  3. Restart the anetd DaemonSet: 
         
         kubectl rollout restart ds anetd -n kube-system --kubeconfig USER_CLUSTER_KUBECONFIG


This workaround reverts every time the cluster is upgraded. You must reconfigure after each upgrade. VMware must resolve their issue in vSphere for a permanent fix.  
Upgrades | 1.15.0-1.15.4 | 

### Upgrading an admin cluster with always-on secrets encryption enabled fails

The admin cluster upgrade from 1.14.x to 1.15.x with [ always-on secrets encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption) enabled fails due to a mismatch between the controller-generated encryption key with the key that persists on the admin master data disk. The output of `gkectl upgrade admin` contains the following error message: 
    
    
          E0926 14:42:21.796444   40110 console.go:93] Exit with error:
          E0926 14:42:21.796491   40110 console.go:93] Failed to upgrade the admin cluster: failed to create admin cluster: failed to wait for OnPremAdminCluster "admin-cluster-name" to become ready: failed to wait for OnPremAdminCluster "admin-cluster-name" to be ready: error: timed out waiting for the condition, message: failed to wait for OnPremAdminCluster "admin-cluster-name" to stay in ready status for duration "2m0s": OnPremAdminCluster "non-prod-admin" is not ready: ready condition is not true: CreateOrUpdateControlPlane: Creating or updating credentials for cluster control plane
          

Running `kubectl get secrets -A --kubeconfig KUBECONFIG`` fails with the following error: 
    
    
          Internal error occurred: unable to transform key "/registry/secrets/anthos-identity-service/ais-secret": rpc error: code = Internal desc = failed to decrypt: unknown jwk
          

#### Workaround

If you have a backup of the admin cluster, do the following steps to workaround the upgrade failure:

  1. [ Disable `secretsEncryption` in the admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption#disable_always-on_secrets_encryption), and update the cluster using the following command: 
         
         gkectl update admin --config ADMIN_CLUSTER_CONFIG_FILE --kubeconfig KUBECONFIG

  2. When the new admin master VM is created, SSH to the admin master VM, replace the new key on the data disk with the old one from the backup. The key is located at `/opt/data/gke-k8s-kms-plugin/generatedkeys` on the admin master. 
  3. Update the kms-plugin.yaml static Pod manifest in `/etc/kubernetes/manifests` to update the `--kek-id` to match the `kid` field in the original encryption key. 
  4. Restart the kms-plugin static Pod by moving the `/etc/kubernetes/manifests/kms-plugin.yaml` to another directory then move it back. 
  5. Resume the admin upgrade by running `gkectl upgrade admin` again. 



#### Preventing the upgrade failure

If you haven't already upgraded, we recommend that you don't upgrade to 1.15.0-1.15.4. If you must upgrade to an affected version, do the following steps **before** upgrading the admin cluster: 

  1. [ Backup the admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl). 
  2. [ Disable `secretsEncryption` in the admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption#disable_always-on_secrets_encryption), and update the cluster using the following command: 
         
         gkectl update admin --config ADMIN_CLUSTER_CONFIG_FILE --kubeconfig KUBECONFIG

  3. [Upgrade the admin cluster.](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_admin_cluster)
  4. [ Renable always-on secrets encryption](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption#enable_always-on_secrets_encryption).

  
Storage | 1.11-1.16 | 

### Disk errors and attach failures when using Changed Block Tracking (CBT)

Google Distributed Cloud does not support Changed Block Tracking (CBT) on disks. Some backup software uses the CBT feature to track disk state and perform backups, which causes the disk to be unable to connect to a VM that runs Google Distributed Cloud. For more information, see the [VMware KB article](https://kb.vmware.com/s/article/88193).   
**Workaround:** Don't back up the Google Distributed Cloud VMs, as 3rd party backup software might cause CBT to be enabled on their disks. It's not necessary to back up these VMs. Don't enable CBT on the node, as this change won't persist across updates or upgrades. If you already have disks with CBT enabled, follow the **Resolution** steps in the [VMware KB article](https://kb.vmware.com/s/article/88193)to disable CBT on the First Class Disk.  
Storage | 1.14, 1.15, 1.16 | 

### Data corruption on NFSv3 when parallel appends to a shared file are done from multiple hosts

If you use Nutanix storage arrays to provide NFSv3 shares to your hosts, you might experience data corruption or the inability for Pods to run successfully. This issue is caused by a known compatibility issue between certain versions of VMware and Nutanix versions. For more information, see the associated [VMware KB article.](https://kb.vmware.com/s/article/90106)   
**Workaround:** The VMware KB article is out of date in noting that there is no current resolution. To resolve this issue, update to the latest version of ESXi on your hosts and to the latest Nutanix version on your storage arrays.  
Operating system | 1.13.10, 1.14.6, 1.15.3 | 

### Version mismatch between the kubelet and the Kubernetes control plane

For certain Google Distributed Cloud releases, the kubelet running on the nodes uses a different version than the Kubernetes control plane. There is a mismatch because the kubelet binary preloaded on the OS image is using a different version.  The following table lists the identified version mismatches: | Google Distributed Cloud version | kubelet version | Kubernetes version  
---|---|---  
1.13.10 | v1.24.11-gke.1200 | v1.24.14-gke.2100  
1.14.6 | v1.25.8-gke.1500 | v1.25.10-gke.1200  
1.15.3 | v1.26.2-gke.1001 | v1.26.5-gke.2100  
  
**Workaround:**

No action is needed. The inconsistency is only between Kubernetes patch versions and no problems have been caused by this version skew.   
  
Upgrades, Updates | 1.15.0-1.15.4 | 

### Upgrading or updating an admin cluster with a CA version greater than 1 fails

When an admin cluster has a certificate authority (CA) version greater than 1, an update or upgrade fails due to the CA version validation in the webhook. The output of `gkectl` upgrade/update contains the following error message: 
    
    
        CAVersion must start from 1
        

**Workaround:**

  * Scale down the `auto-resize-controller` deployment in the admin cluster to disable node auto-resizing. This is necessary because a new field introduced to the admin cluster Custom Resource in 1.15 can cause a nil pointer error in the `auto-resize-controller`. 
        
        kubectl scale deployment auto-resize-controller -n kube-system --replicas=0 --kubeconfig KUBECONFIG
              

  * Run `gkectl` commands with `--disable-admin-cluster-webhook` flag.For example: 
        
        gkectl upgrade admin --config ADMIN_CLUSTER_CONFIG_FILE --kubeconfig KUBECONFIG --disable-admin-cluster-webhook
                


  
Operation | 1.13, 1.14.0-1.14.8, 1.15.0-1.15.4, 1.16.0-1.16.1 | 

### Non-HA Controlplane V2 cluster deletion stuck until timeout

When a non-HA Controlplane V2 cluster is deleted, it is stuck at node deletion until it timesout. **Workaround:** If the cluster contains a StatefulSet with critical data, contact [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) to resolve this issue. Otherwise, do the following steps: 

  * Delete all cluster VMs from vSphere. You can delete the VMs through the vSphere UI, or run the following command: 
        
        govc vm.destroy

.
  * Force delete the cluster again: 
        
        gkectl delete cluster --cluster USER_CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG --force
             


  
Storage | 1.15.0+, 1.16.0+ | 

### Constant CNS attachvolume tasks appear every minute for in-tree PVC/PV after upgrading to version 1.15+

When a cluster contains in-tree vSphere persistent volumes (for example, PVCs created with the `standard` StorageClass), you will observe com.vmware.cns.tasks.attachvolume tasks triggered every minute from vCenter.    
**Workaround:** Edit the vSphere CSI feature configMap and set list-volumes to false:
    
    
         kubectl edit configmap internal-feature-states.csi.vsphere.vmware.com -n kube-system --kubeconfig KUBECONFIG
         

Restart the vSphere CSI controller pods:
    
    
         kubectl rollout restart deployment vsphere-csi-controller -n kube-system --kubeconfig KUBECONFIG
          
  
Storage | 1.16.0 | 

### False warnings agaisnt PVCs

When a cluster contains intree vSphere persistent volumes, the commands `gkectl diagnose` and `gkectl upgrade` might raise false warnings against their persistent volume claims (PVCs) when validating the cluster storage settings. The warning message looks like the following 
    
    
        CSIPrerequisites pvc/pvc-name: PersistentVolumeClaim pvc-name bounds to an in-tree vSphere volume created before CSI migration enabled, but it doesn't have the annotation pv.kubernetes.io/migrated-to set to csi.vsphere.vmware.com after CSI migration is enabled
        

  
**Workaround:** Run the following command to check the annotations of a PVC with the above warning:
    
    
        kubectl get pvc PVC_NAME -n PVC_NAMESPACE -oyaml --kubeconfig KUBECONFIG
        

If the `annotations` field in the output contains the following, you can safely ignore the warning:
    
    
          pv.kubernetes.io/bind-completed: "yes"
          pv.kubernetes.io/bound-by-controller: "yes"
          volume.beta.kubernetes.io/storage-provisioner: csi.vsphere.vmware.com
          
  
Upgrades, Updates | 1.15.0+, 1.16.0+ | 

### Service account key rotation fails when multiple keys are expired

If your cluster is not using a private registry, and your component access service account key and Logging-monitoring (or Connect-register) service account keys are expired, when you [rotate the service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys), `gkectl update credentials` fails with an error similar to the following: 
    
    
    Error: reconciliation failed: failed to update platform: ...

**Workaround:** First, rotate the component access service account key. Although the same error message is displayed, you should be able to rotate the other keys after the component access service account key rotation.  If the update is still not successful, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) to resolve this issue.  
Upgrades | 1.16.0-1.16.5 | 

### 1.15 User master machine encounters an unexpected recreation when the user cluster controller is upgraded to 1.16

During a user cluster upgrade, after the user cluster controller is upgraded to 1.16, if you have other 1.15 user clusters managed by the same admin cluster, their user master machine might be unexpectedly recreated. There is a bug in the 1.16 user cluster controller which can trigger the 1.15 user master machine recreation. The workaround that you do depends on how you encounter this issue. **Workaround when upgrading the user cluster using the Google Cloud console:** Option 1: Use a 1.16.6+ version of GKE on VMware with the fix. Option 2: Do the following steps:

  1. Manually add the rerun annotation by the following command: 
         
         kubectl edit onpremuserclusters USER_CLUSTER_NAME -n USER_CLUSTER_NAME-gke-onprem-mgmt --kubeconfig ADMIN_KUBECONFIG

The rerun annotation is:
         
         onprem.cluster.gke.io/server-side-preflight-rerun: true

  2. Monitor the upgrade progress by checking the `status` field of the OnPremUserCluster.

**Workaround when upgrading the user cluster using your own admin workstation:** Option 1: Use a 1.16.6+ version of GKE on VMware with the fix. Option 2: Do the following steps:

  1. Add the build info file `/etc/cloud/build.info` with the following content. This causes the preflight checks to run locally on your admin workstation rather than on the server. 
         
         gke_on_prem_version: GKE_ON_PREM_VERSION

For example: 
         
         gke_on_prem_version: 1.16.0-gke.669

  2. Rerun the upgrade command.
  3. After the upgrade completes, delete the build.info file.

  
Create | 1.16.0-1.16.5, 1.28.0-1.28.100 | 

### Preflight check fails when the hostname isn't in the IP block file.

During cluster creation, if you don't specify a hostname for every IP address in the IP block file, the preflight check fails with the following error message: 
    
    
    multiple VMs found by DNS name  in xxx datacenter. Anthos Onprem doesn't support duplicate hostname in the same vCenter and you may want to rename/delete the existing VM.`
        

There is a bug in the preflight check which assumes empty hostname as duplicate. **Workaround:** Option 1: Use a version with the fix. Option 2: Bypass this preflight check by adding `--skip-validation-net-config` flag. Option 3: Specify a unique hostname for each IP address in IP block file.  
Upgrades, Updates | 1.16 | 

### Volume mount failure when upgrade/update the admin cluster if using non-HA admin cluster and control plane v1 user cluster

For a non-HA admin cluster and a control plane v1 user cluster, when you upgrade or update the admin cluster, the admin cluster master machine recreation might happen at the same time as the user cluster master machine reboot, which can surface a race condition. This causes the user cluster control plane Pods to be unable to communicate to the admin cluster control plane, which causes volume attach issues for kube-etcd and kube-apiserver on the user cluster control plane. To verify the issue, run the following commands for the impacted pod:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG --namespace USER_CLUSTER_NAME describe pod IMPACTED_POD_NAME

And you will see the events like: 
    
    
    Events:
      Type     Reason       Age                  From               Message
      ----     ------       ----                 ----               -------
      Warning  FailedMount  101s                 kubelet            Unable to attach or mount volumes: unmounted volumes=[kube-audit], unattached volumes=[], failed to process volumes=[]: timed out waiting for the condition
      Warning  FailedMount  86s (x2 over 3m28s)  kubelet            MountVolume.SetUp failed for volume "pvc-77cd0635-57c2-4392-b191-463a45c503cb" : rpc error: code = FailedPrecondition desc = volume ID: "bd313c62-d29b-4ecd-aeda-216648b0f7dc" does not appear staged to "/var/lib/kubelet/plugins/kubernetes.io/csi/csi.vsphere.vmware.com/92435c96eca83817e70ceb8ab994707257059734826fedf0c0228db6a1929024/globalmount"
    

**Workaround:**

  1. [SSH into user control plane node](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ssh-cluster-node#admin), since it is control plane v1 user cluster, the user control plane node is in admin cluster. 
  2. Restart the kubelet using the following command: 
         
         sudo systemctl restart kubelet
             

After restart, the kubelet can reconstruct stage global mount properly. 

  
Upgrades, Updates | 1.16.0 | 

### Control plane node fails to be created

During an upgrade or update of an admin cluster, a race condition might cause the vSphere cloud controller manager to unexpectedly delete a new control plane node. This causes the clusterapi-controller to be stuck waiting for the node to be created, and evenutally the upgrade/update times out. In this case, the output of the `gkectl` upgrade/update command is similar to the following:
    
    
        controlplane 'default/gke-admin-hfzdg' is not ready: condition "Ready": condition is not ready with reason "MachineInitializing", message "Wait for the control plane machine "gke-admin-hfzdg-6598459f9zb647c8-0\" to be rebooted"...
        

To identify the symptom, run the command below to get log in vSphere cloud controller manager in the admin cluster:
    
    
        kubectl get pods --kubeconfig ADMIN_KUBECONFIG -n kube-system | grep vsphere-cloud-controller-manager
        kubectl logs -f vsphere-cloud-controller-manager-POD_NAME_SUFFIX --kubeconfig ADMIN_KUBECONFIG -n kube-system
        

Here is a sample error message from the above command:
    
    
        node name: 81ff17e25ec6-qual-335-1500f723 has a different uuid. Skip deleting this node from cache.
        

**Workaround:**

  1. Reboot the failed machine to recreate the deleted node object. 
  2. [SSH into each control plane node](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ssh-cluster-node) and restart the vSphere cloud controller manager static pod: 
         
         sudo crictl ps | grep vsphere-cloud-controller-manager | awk '{print $1}'
               sudo crictl stop PREVIOUS_COMMAND_OUTPUT
               

  3. Rerun upgrade/update command. 

  
Operation | 1.16 | 

### Duplicate hostname in the same data center causes cluster upgrade or creation failures

Upgrading a 1.15 cluster or creating a 1.16 cluster with static IPs fails if there are duplicate hostnames in the same data center. This failure happens because the vSphere cloud controller manager fails to add an external IP and provider ID in the node object. This causes the cluster upgrade/create to timeout. To identify the issue, get the vSphere cloud controller manager pod logs for the cluster. The command that you use depends on the cluster type, as follows:

  * Admin cluster: 
        
        kubectl get pods --kubeconfig ADMIN_KUBECONFIG -n kube-system | grep vsphere-cloud-controller-manager
              kubectl logs -f vsphere-cloud-controller-manager-POD_NAME_SUFFIX --kubeconfig ADMIN_KUBECONFIG -n kube-system
              

  * User cluster with [`enableControlplaneV2`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field) `false`: 
        
        kubectl get pods --kubeconfig ADMIN_KUBECONFIG -n USER_CLUSTER_NAME | grep vsphere-cloud-controller-manager
              kubectl logs -f vsphere-cloud-controller-manager-POD_NAME_SUFFIX --kubeconfig ADMIN_KUBECONFIG -n USER_CLUSTER_NAME
              

  * User cluster with [`enableControlplaneV2`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field) `true`: 
        
        kubectl get pods --kubeconfig USER_KUBECONFIG -n kube-system | grep vsphere-cloud-controller-manager
              kubectl logs -f vsphere-cloud-controller-manager-POD_NAME_SUFFIX --kubeconfig USER_KUBECONFIG -n kube-system
              


Here is a sample error message:
    
    
        I1003 17:17:46.769676       1 search.go:152] Finding node admin-vm-2 in vc=vcsa-53598.e5c235a1.asia-northeast1.gve.goog and datacenter=Datacenter
        E1003 17:17:46.771717       1 datacenter.go:111] Multiple vms found VM by DNS Name. DNS Name: admin-vm-2
        

**Check if the hostname is duplicated in the data center:** You can use the following approach to check if the hostname is duplicated, and do a workaround if needed. 
    
    
              export GOVC_DATACENTER=GOVC_DATACENTER
              export GOVC_URL=GOVC_URL
              export GOVC_USERNAME=GOVC_USERNAME
              export GOVC_PASSWORD=GOVC_PASSWORD
              export GOVC_INSECURE=true
              govc find . -type m -guest.hostName HOSTNAME
              

Example commands and output: 
    
    
              export GOVC_DATACENTER=mtv-lifecycle-vc01
              export GOVC_URL=https://mtv-lifecycle-vc01.anthos/sdk
              export GOVC_USERNAME=xxx
              export GOVC_PASSWORD=yyy
              export GOVC_INSECURE=true
              govc find . -type m -guest.hostName f8c3cd333432-lifecycle-337-xxxxxxxz
              ./vm/gke-admin-node-6b7788cd76-wkt8g
              ./vm/gke-admin-node-6b7788cd76-99sg2
              ./vm/gke-admin-master-5m2jb
              

The workaround that you do depends on the operation that failed. **Workaround for upgrades:** Do the workaround for the applicable cluster type.

  * User cluster: 
    1. Update the hostname of the affected machine in user-ip-block.yaml to a unique name and trigger a forced update:  

           
           gkectl update cluster --kubeconfig ADMIN_KUBECONFIG --config NEW_USER_CLUSTER_CONFIG --force
                     

    2. Rerun `gkectl upgrade cluster`
  * Admin cluster: 
    1. Update the hostname of the affected machine in admin-ip-block.yaml to a unique name and trigger a forced update:  

           
           gkectl update admin --kubeconfig ADMIN_KUBECONFIG --config NEW_ADMIN_CLUSTER_CONFIG --force --skip-cluster-ready-check
                     

    2. If it is a non-HA admin cluster, and you find admin master vm is using duplicate hostname, you also need to:  
Get admin master machine name 
           
           kubectl get machine --kubeconfig ADMIN_KUBECONFIG -owide -A
                     

Update admin master machine object  
**Note:** The NEW_ADMIN_MASTER_HOSTNAME should be same to what you set in admin-ip-block.yaml in step 1.  

           
           kubectl patch machine ADMIN_MASTER_MACHINE_NAME --kubeconfig ADMIN_KUBECONFIG --type='json' -p '[{"op": "replace", "path": "/spec/providerSpec/value/networkSpec/address/hostname", "value":"NEW_ADMIN_MASTER_HOSTNAME"}]'
                     

Verify hostname is updated in admin master machine object:  

           
           kubectl get machine ADMIN_MASTER_MACHINE_NAME --kubeconfig ADMIN_KUBECONFIG -oyaml
                     kubectl get machine ADMIN_MASTER_MACHINE_NAME --kubeconfig ADMIN_KUBECONFIG -o jsonpath='{.spec.providerSpec.value.networkSpec.address.hostname}'
                     

    3. Rerun admin cluster upgrade with checkpoint disabled:  

           
           gkectl upgrade admin --kubeconfig ADMIN_KUBECONFIG --config ADMIN_CLUSTER_CONFIG --disable-upgrade-from-checkpoint
                     


**Workaround for installations:** Do the workaround for the applicable cluster type.

  * Admin cluster: 
    1. [Delete the admin node machine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-an-admin-cluster#deleting_admin_node_machines). 
    2. [Delete the data disk](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-an-admin-cluster#deleting_the_data_disk). 
    3. [Delete the admin cluster checkpoint file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-an-admin-cluster#deleting_the_checkpointyaml_file). 
    4. Update the hostname of the affected machine in admin-ip-block.yaml to a unique name. 
    5. Rerun `gkectl create admin`. 
  * User cluster: 
    1. [Clean up resources](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-a-user-cluster#clean_up_resources). 
    2. Update the hostname of the affected machine in user-ip-block.yaml to a unique name. 
    3. Rerun `gkectl create cluster`.

  
Operation | 1.16.0, 1.16.1, 1.16.2, 1.16.3 | 

### `$` and ``` are not supported in vSphere username or password

The following operations fail when the vSphere username or password contains `$` or ```: 

  * Upgrading a 1.15 user cluster with Controlplane V2 enabled to 1.16
  * Upgrading a 1.15 high-availability (HA) admin cluster to 1.16
  * Creating a 1.16 user cluster with Controlplane V2 enabled
  * Creating a 1.16 HA admin cluster

Use a 1.16.4+ version of Google Distributed Cloud with the fix or perform the below workaround. The workaround that you do depends on the operation that failed. **Workaround for upgrades:**

  1. Change the vCenter username or password on the vCenter side to remove the `$` and ```. 
  2. Update the vCenter username or password in your [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file). 
  3. Trigger a forced update of the cluster.
     * User cluster: 
           
           gkectl update cluster --kubeconfig ADMIN_KUBECONFIG --config USER_CLUSTER_CONFIG --force
                   

     * Admin cluster: 
           
           gkectl update admin --kubeconfig ADMIN_KUBECONFIG --config ADMIN_CLUSTER_CONFIG --force --skip-cluster-ready-check
                   


**Workaround for installations:**

  1. Change the vCenter username or password on the vCenter side to remove the `$` and ```. 
  2. Update the vCenter username or password in your [credentials configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file). 
  3. Do the workaround for the applicable cluster type.
     * Admin cluster: 
       1. [Delete the admin node machine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-an-admin-cluster#deleting_admin_node_machines). 
       2. [Delete the data disk](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-an-admin-cluster#deleting_the_data_disk). 
       3. [Delete the admin cluster checkpoint file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-an-admin-cluster#deleting_the_checkpointyaml_file). 
       4. Rerun `gkectl create admin`. 
     * User cluster: 
       1. [Clean up resources](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-a-user-cluster#clean_up_resources). 
       2. Rerun `gkectl create cluster`.

  
Storage | 1.11+, 1.12+, 1.13+, 1.14+, 1.15+, 1.16 | 

### PVC creation failure after node is recreated with the same name

After a node is deleted and then recreated with the same node name, there is a slight chance that a subsequent PersistentVolumeClaim (PVC) creation fails with an error like the following:
    
    
        The object 'vim.VirtualMachine:vm-988369' has already been deleted or has not been completely created

This is caused by race condition where vSphere CSI controller does not delete a removed machine from its cache.   
**Workaround:** Restart the vSphere CSI controller pods:
    
    
        kubectl rollout restart deployment vsphere-csi-controller -n kube-system --kubeconfig KUBECONFIG
          
  
Operation | 1.16.0 | 

### gkectl repair admin-master returns kubeconfig unmarshall error

When you run the `gkectl repair admin-master` command on an HA admin cluster, `gkectl` returns the following error message: 
    
    
      Exit with error: Failed to repair: failed to select the template: failed to get cluster name from kubeconfig, please contact Google support. failed to decode kubeconfig data: yaml: unmarshal errors:
        line 3: cannot unmarshal !!seq into map[string]*api.Cluster
        line 8: cannot unmarshal !!seq into map[string]*api.Context
      

  
**Workaround:** Add the `--admin-master-vm-template=` flag to the command and provide the VM template of the machine to repair: 
    
    
      gkectl repair admin-master --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
          --config ADMIN_CLUSTER_CONFIG_FILE \
          --admin-master-vm-template=/DATA_CENTER/vm/VM_TEMPLATE_NAME
      

To find the VM template of the machine:

  1. Go to the **Hosts and Clusters** page in the vSphere client.
  2. Click **VM Templates** and filter by the admin cluster name. You should see the three VM templates for the admin cluster.
  3. Copy the name VM template that matches the name of the machine you're repairing and use the template name in the repair command.


    
    
      gkectl repair admin-master \
          --config=/home/ubuntu/admin-cluster.yaml \
          --kubeconfig=/home/ubuntu/kubeconfig \
          --admin-master-vm-template=/atl-qual-vc07/vm/gke-admin-98g94-zx...7vx-0-tmpl  
  
Networking | 1.10.0+, 1.11.0+, 1.12.0+, 1.13.0+, 1.14.0-1.14.7, 1.15.0-1.15.3, 1.16.0 | 

### Seesaw VM broken due to disk space low

If you use Seesaw as the load balancer type for your cluster and you see that a Seesaw VM is down or keeps failing to boot, you might see the following error message in the vSphere console:
    
    
        GRUB_FORCE_PARTUUID set, initrdless boot failed. Attempting with initrd
        

This error indicates that the disk space is low on the VM because the fluent-bit running on the Seesaw VM is not configured with correct log rotation.   
**Workaround:** Locate the log files that consume most of the disk space using `du -sh -- /var/lib/docker/containers/* | sort -rh`. Clean up the log file with largest size and reboot the VM. **Note:** If the VM is completely inaccessible, attach the disk to a working VM (e.g. admin workstation), remove the file from the attached disk, then reattach the disk back to the original Seesaw VM. To prevent the issue from happening again, connect to the VM and modify the `/etc/systemd/system/docker.fluent-bit.service` file. Add `--log-opt max-size=10m --log-opt max-file=5` in the Docker command, then run `systemctl restart docker.fluent-bit.service`  
Operation | 1.13, 1.14.0-1.14.6, 1.15 | 

### Admin SSH public key error after admin cluster upgrade or update

When you try to upgrade (`gkectl upgrade admin`) or update (`gkectl update admin`) a non-High-Availability admin cluster with checkpoint enabled, the upgrade or update may fail with errors like the following: 
    
    
    Checking admin cluster certificates...FAILURE
        Reason: 20 admin cluster certificates error(s).
    Unhealthy Resources:
        AdminMaster clusterCA bundle: failed to get clusterCA bundle on admin master, command [ssh -o IdentitiesOnly=yes -i admin-ssh-key -o StrictHostKeyChecking=no -o ConnectTimeout=30 ubuntu@AdminMasterIP -- sudo cat /etc/kubernetes/pki/ca-bundle.crt] failed with error: exit status 255, stderr: Authorized uses only. All activity may be monitored and reported.
        ubuntu@AdminMasterIP: Permission denied (publickey).
    
    
    failed to ssh AdminMasterIP, failed with error: exit status 255, stderr: Authorized uses only. All activity may be monitored and reported.
        ubuntu@AdminMasterIP: Permission denied (publickey)
    
    
    error dialing ubuntu@AdminMasterIP: failed to establish an authenticated SSH connection: ssh: handshake failed: ssh: unable to authenticate, attempted methods [none publickey]...

  
**Workaround:** If you're unable to upgrade to a patch version of Google Distributed Cloud with the fix, [contact Google Support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for assistance.  
Upgrades | 1.13.0-1.13.9, 1.14.0-1.14.6, 1.15.1-1.15.2 | 

### Upgrading an admin cluster enrolled in the GKE On-Prem API could fail

When an admin cluster is enrolled in the GKE On-Prem API, upgrading the admin cluster to the affected versions could fail because the fleet membership couldn't be updated. When this failure happens, you see the following error when trying to upgrade the cluster:
    
    
        failed to register cluster: failed to apply Hub Membership: Membership API request failed: rpc error: code = InvalidArgument desc = InvalidFieldError for field endpoint.on_prem_cluster.resource_link: field cannot be updated
        

An admin cluster is enrolled in the API when you [explicitly enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster) the cluster, or when you [upgrade a user cluster using a GKE On-Prem API client](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).   
**Workaround:** Unenroll the admin cluster: 
    
    
        gcloud alpha container vmware admin-clusters unenroll ADMIN_CLUSTER_NAME --project CLUSTER_PROJECT --location=CLUSTER_LOCATION --allow-missing
        

and [ resume upgrading the admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#about_resume_admin). You might see the stale `failed to register cluster` error temporarily. After a while, it should be updated automatically.   
Upgrades, Updates | 1.13.0-1.13.9, 1.14.0-1.14.4, 1.15.0 | 

### Enrolled admin cluster's resource link annotation is not preserved

When an admin cluster is enrolled in the GKE On-Prem API, its resource link annotation is applied to the `OnPremAdminCluster` custom resource, which is not preserved during later admin cluster updates due to the wrong annotation key being used. This can cause the admin cluster to be enrolled in the GKE On-Prem API again by mistake. An admin cluster is enrolled in the API when you [explicitly enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster) the cluster, or when you [upgrade a user cluster using a GKE On-Prem API client](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).   
**Workaround:** Unenroll the admin cluster: 
    
    
        gcloud alpha container vmware admin-clusters unenroll ADMIN_CLUSTER_NAME --project CLUSTER_PROJECT --location=CLUSTER_LOCATION --allow-missing
        

and [re-enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#admin-cluster) the admin cluster again.   
Networking | 1.15.0-1.15.2 | 

### CoreDNS `orderPolicy` not recognized

`OrderPolicy` doesn't get recognized as a parameter and isn't used. Instead, Google Distributed Cloud always uses `Random`. This issue occurs because the CoreDNS template was not updated, which causes `orderPolicy` to be ignored.   
**Workaround:** Update the CoreDNS template and apply the fix. This fix persists until an upgrade.

  1. Edit the existing template: 
         
         kubectl edit cm -n kube-system coredns-template

Replace the contents of the template with the following: 
         
         coredns-template: |-
           .:53 {
             errors
             health {
               lameduck 5s
             }
             ready
             kubernetes cluster.local in-addr.arpa ip6.arpa {
               pods insecure
               fallthrough in-addr.arpa ip6.arpa
             }
         {{- if .PrivateGoogleAccess }}
             import zones/private.Corefile
         {{- end }}
         {{- if .RestrictedGoogleAccess }}
             import zones/restricted.Corefile
         {{- end }}
             prometheus :9153
             forward . {{ .UpstreamNameservers }} {
               max_concurrent 1000
               {{- if ne .OrderPolicy "" }}
               policy {{ .OrderPolicy }}
               {{- end }}
             }
             cache 30
         {{- if .DefaultDomainQueryLogging }}
             log
         {{- end }}
             loop
             reload
             loadbalance
         }{{ range $i, $stubdomain := .StubDomains }}
         {{ $stubdomain.Domain }}:53 {
           errors
         {{- if $stubdomain.QueryLogging }}
           log
         {{- end }}
           cache 30
           forward . {{ $stubdomain.Nameservers }} {
             max_concurrent 1000
             {{- if ne $.OrderPolicy "" }}
             policy {{ $.OrderPolicy }}
             {{- end }}
           }
         }
         {{- end }}


  
Upgrades, Updates | 1.10, 1.11, 1.12, 1.13.0-1.13.7, 1.14.0-1.14.3 | 

### OnPremAdminCluster status inconsistent between checkpoint and actual CR 

Certain race conditions could cause the `OnPremAdminCluster` status to be inconsistent between checkpoint and actual CR. When the issue happens, you could encounter the following error when update the admin cluster after you upgraded it:
    
    
    Exit with error:
    E0321 10:20:53.515562  961695 console.go:93] Failed to update the admin cluster: OnPremAdminCluster "gke-admin-rj8jr" is in the middle of a create/upgrade ("" -> "1.15.0-gke.123"), which must be completed before it can be updated
    Failed to update the admin cluster: OnPremAdminCluster "gke-admin-rj8jr" is in the middle of a create/upgrade ("" -> "1.15.0-gke.123"), which must be completed before it can be updated

To workaround this issue, you will need to either edit the checkpoint or disable the checkpoint for upgrade/update, please reach out to our support team to proceed with the workaround.   
Operation | 1.13.0-1.13.9, 1.14.0-1.14.5, 1.15.0-1.15.1 | 

### Reconciliation process changes admin certificates on admin clusters

Google Distributed Cloud changes the admin certificates on admin cluster control planes with every reconciliation process, such as during a cluster upgrade. This behavior increases the possibility of getting invalid certificates for your admin cluster, especially for version 1.15 clusters. If you're affected by this issue, you may encounter problems like the following:

  * Invalid certificates may cause the following commands to time out and return errors: 
    * `gkectl create admin`
    * `gkectl upgrade amdin`
    * `gkectl update admin`
These commands may return authorization errors like the following:
    
    Failed to reconcile admin cluster: unable to populate admin clients: failed to get admin controller runtime client: Unauthorized

  * The `kube-apiserver` logs for your admin cluster may contain errors like the following: 
        
        Unable to authenticate the request" err="[x509: certificate has expired or is not yet valid...


  
**Workaround:** Upgrade to a version of Google Distributed Cloud with the fix: 1.13.10+, 1.14.6+, 1.15.2+. If upgrading isn't feasible for you, contact Cloud Customer Care to resolve this issue.  
Networking, Operation | 1.10, 1.11, 1.12, 1.13, 1.14 | 

### Anthos Network Gateway components evicted or pending due to missing priority class

Network gateway Pods in `kube-system` might show a status of `Pending` or `Evicted`, as shown in the following condensed example output:
    
    
    $ kubectl -n kube-system get pods | grep ang-node
    ang-node-bjkkc     2/2     Running     0     5d2h
    ang-node-mw8cq     0/2     Evicted     0     6m5s
    ang-node-zsmq7     0/2     Pending     0     7h

These errors indicate eviction events or an inability to schedule Pods due to node resources. As Anthos Network Gateway Pods have no PriorityClass, they have the same default priority as other workloads. When nodes are resource-constrained, the network gateway Pods might be evicted. This behavior is particularly bad for the `ang-node` DaemonSet, as those Pods must be scheduled on a specific node and can't migrate.   
**Workaround:** Upgrade to 1.15 or later. As a short-term fix, you can manually assign a [PriorityClass](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass) to the Anthos Network Gateway components. The Google Distributed Cloud controller overwrites these manual changes during a reconciliation process, such as during a cluster upgrade.

  * Assign the `system-cluster-critical` PriorityClass to the `ang-controller-manager` and `autoscaler` cluster controller Deployments.
  * Assign the `system-node-critical` PriorityClass to the `ang-daemon` node DaemonSet.

  
Upgrades, Updates | 1.12, 1.13, 1.14, 1.15.0-1.15.2 | 

### admin cluster upgrade fails after registering the cluster with gcloud

After you use `gcloud` to register an admin cluster with non-empty [ `gkeConnect`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#gkeconnect-section) section, you might see the following error when trying to upgrade the cluster:
    
    
    failed to register cluster: failed to apply Hub Mem\
    bership: Membership API request failed: rpc error: code = InvalidArgument desc = InvalidFieldError for field endpoint.o\
    n_prem_cluster.admin_cluster: field cannot be updated

Delete the `gke-connect` namespace: 
    
    
    kubectl delete ns gke-connect --kubeconfig=ADMIN_KUBECONFIG

Get the admin cluster name: 
    
    
    kubectl get onpremadmincluster -n kube-system --kubeconfig=ADMIN_KUBECONFIG

Delete the fleet membership: 
    
    
    gcloud container fleet memberships delete ADMIN_CLUSTER_NAME

and [ resume upgrading the admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#about_resume_admin).   
Operation | 1.13.0-1.13.8, 1.14.0-1.14.5, 1.15.0-1.15.1 | 

### `gkectl diagnose snapshot --log-since` fails to limit the time window for `journalctl` commands running on the cluster nodes

This does not affect the functionality of taking a snapshot of the cluster, as the snapshot still includes all logs that are collected by default by running `journalctl` on the cluster nodes. Therefore, no debugging information is missed.  
Installation, Upgrades, Updates | 1.9+, 1.10+, 1.11+, 1.12+ | 

### `gkectl prepare windows` fails

`gkectl prepare windows` fails to install Docker on Google Distributed Cloud versions earlier than 1.13 because [`MicrosoftDockerProvider`](https://github.com/OneGet/MicrosoftDockerProvider) is deprecated.   
**Workaround:** The general idea to workaround this issue is to upgrade to Google Distributed Cloud 1.13 and use the 1.13 `gkectl` to create a Windows VM template and then create Windows node pools. There are two options to get to Google Distributed Cloud 1.13 from your current version as shown below. **Note:** We do have options to workaround this issue in your current version without needing to upgrade all the way to 1.13, but it will need more manual steps, please reach out to our support team if you would like to consider this option.   
**Option 1:** Blue/Green upgrade You can create a new cluster using Google Distributed Cloud 1.13+ version with windows node pools, and migrate your workloads to the new cluster, then tear down the current cluster. It's recommended to use the latest Google Distributed Cloud minor version. **Note:** This will require extra resources to provision the new cluster, but less downtime and disruption for existing workloads.   
**Option 2:** Delete Windows node pools and add them back when upgrading to Google Distributed Cloud 1.13 **Note:** For this option, the Windows workloads will not be able to run until the cluster is upgraded to 1.13 and Windows node pools are added back.

  1. Delete existing Windows node pools by removing the windows node pools config from user-cluster.yaml file, then run the command: 
         
         gkectl update cluster --kubeconfig=ADMIN_KUBECONFIG --config USER_CLUSTER_CONFIG_FILE

  2. Upgrade the Linux-only admin+user clusters to 1.12 following the [ upgrade user guide](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading) for the corresponding target minor version.
  3. (Make sure to perform this step before upgrading to 1.13) Ensure the `enableWindowsDataplaneV2: true` is configured in `OnPremUserCluster` CR, otherwise the cluster will keep using Docker for Windows node pools, which will not be compatible with the newly created 1.13 Windows VM template that not have Docker installed. If not configured or setting to false, update your cluster to set it to true in user-cluster.yaml, then run: 
         
         gkectl update cluster --kubeconfig=ADMIN_KUBECONFIG --config USER_CLUSTER_CONFIG_FILE

  4. Upgrade the Linux-only admin+user clusters to 1.13 following the [ upgrade user guide](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).
  5. Prepare Windows VM template using 1.13 gkectl: 
         
         gkectl prepare windows --base-vm-template BASE_WINDOWS_VM_TEMPLATE_NAME --bundle-path 1.13_BUNDLE_PATH --kubeconfig=ADMIN_KUBECONFIG

  6. Add back the Windows node pool configuration to user-cluster.yaml with the `OSImage` field set to the newly created Windows VM template.
  7. Update the cluster to add Windows node pools 
         
         gkectl update cluster --kubeconfig=ADMIN_KUBECONFIG --config USER_CLUSTER_CONFIG_FILE


  
Installation, Upgrades, Updates | 1.13.0-1.13.9, 1.14.0-1.14.5, 1.15.0-1.15.1 | 

### `RootDistanceMaxSec` configuration not taking effect for `ubuntu` nodes

The 5 seconds default value for `RootDistanceMaxSec` will be used on the nodes, instead of 20 seconds which should be the expected configuration. If you check the node startup log by SSH'ing into the VM, which is located at `/var/log/startup.log`, you can find the following error:
    
    
    + has_systemd_unit systemd-timesyncd
    /opt/bin/master.sh: line 635: has_systemd_unit: command not found

Using a 5 seconds `RootDistanceMaxSec` might cause the system clock to be out of sync with NTP server when the clock drift is larger than 5 seconds.   
**Workaround:** Apply the following DaemonSet to your cluster to configure `RootDistanceMaxSec`:
    
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: change-root-distance
      namespace: kube-system
    spec:
      selector:
        matchLabels:
          app: change-root-distance
      template:
        metadata:
          labels:
            app: change-root-distance
        spec:
          hostIPC: true
          hostPID: true
          tolerations:
          # Make sure pods gets scheduled on all nodes.
          - effect: NoSchedule
            operator: Exists
          - effect: NoExecute
            operator: Exists
          containers:
          - name: change-root-distance
            image: ubuntu
            command: ["chroot", "/host", "bash", "-c"]
            args:
            - |
              while true; do
                conf_file="/etc/systemd/timesyncd.conf.d/90-gke.conf"
                if [ -f $conf_file ] && $(grep -q "RootDistanceMaxSec=20" $conf_file); then
                  echo "timesyncd has the expected RootDistanceMaxSec, skip update"
                else
                  echo "updating timesyncd config to RootDistanceMaxSec=20"
                  mkdir -p /etc/systemd/timesyncd.conf.d
                  cat > $conf_file << EOF
              [Time]
              RootDistanceMaxSec=20
              EOF
                  systemctl restart systemd-timesyncd
                fi
                sleep 600
              done
            volumeMounts:
            - name: host
              mountPath: /host
            securityContext:
              privileged: true
          volumes:
          - name: host
            hostPath:
              path: /  
  
Upgrades, Updates | 1.12.0-1.12.6, 1.13.0-1.13.6, 1.14.0-1.14.2 | 

### `gkectl update admin` fails because of empty `osImageType` field

When you use version 1.13 `gkectl` to update a version 1.12 admin cluster, you might see the following error:
    
    
    Failed to update the admin cluster: updating OS image type in admin cluster
    is not supported in "1.12.x-gke.x"

When you use `gkectl update admin` for version 1.13 or 1.14 clusters, you might see the following message in the response:
    
    
    Exit with error:
    Failed to update the cluster: the update contains multiple changes. Please
    update only one feature at a time

If you check the `gkectl` log, you might see that the multiple changes include setting `osImageType` from an empty string to `ubuntu_containerd`. These update errors are due to improper backfilling of the `osImageType` field in the admin cluster config since it was introduced in version 1.9.   
**Workaround:** Upgrade to a version of Google Distributed Cloud with the fix. If upgrading isn't feasible for you, contact Cloud Customer Care to resolve this issue.  
Installation, Security | 1.13, 1.14, 1.15, 1.16 | 

### SNI doesn't work on user clusters with Controlplane V2

The ability to provide an additional serving certificate for the Kubernetes API server of a user cluster with [ `authentication.sni`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#authentication-sni-section) doesn't work when the Controlplane V2 is enabled ([ `enableControlplaneV2: true`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field)).   
**Workaround:** Until a Google Distributed Cloud patch is available with the fix, if you need to use SNI, disable Controlplane V2 (`enableControlplaneV2: false`).  
Installation | 1.0-1.11, 1.12, 1.13.0-1.13.9, 1.14.0-1.14.5, 1.15.0-1.15.1 | 

### `$` in the private registry username causes admin control plane machine startup failure

The admin control plane machine fails to start up when the private registry username contains `$`. When checking the `/var/log/startup.log` on the admin control plane machine, you see the following error: 
    
    
    ++ REGISTRY_CA_CERT=xxx
    ++ REGISTRY_SERVER=xxx
    /etc/startup/startup.conf: line 7: anthos: unbound variable

  
**Workaround:** Use a private registry username without `$`, or use a version of Google Distributed Cloud with the fix.  
Upgrades, Updates | 1.12.0-1.12.4 | 

### False-positive warnings about unsupported changes during admin cluster update

When you [ update admin clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general), you will see the following false-positive warnings in the log, and you can ignore them. 
    
    
        console.go:47] detected unsupported changes: &v1alpha1.OnPremAdminCluster{
          ...
          -         CARotation:        &v1alpha1.CARotationConfig{Generated: &v1alpha1.CARotationGenerated{CAVersion: 1}},
          +         CARotation:        nil,
          ...
        }  
  
Upgrades, Updates | 1.13.0-1.13.9, 1.14.0-1.14.5, 1.15.0-1.15.1 | 

### Update user cluster failed after KSA signing key rotation

After you [rotate KSA signing keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotate-ksa-signing-key) and subsequently [ update a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general), `gkectl update` might fail with the following error message: 
    
    
    Failed to apply OnPremUserCluster 'USER_CLUSTER_NAME-gke-onprem-mgmt/USER_CLUSTER_NAME':
    admission webhook "vonpremusercluster.onprem.cluster.gke.io" denied the request:
    requests must not decrement *v1alpha1.KSASigningKeyRotationConfig Version, old version: 2, new version: 1"

  
**Workaround:** Change the version of your KSA signing key version back to 1, but retain the latest key data: 

  1. Check the secret in admin cluster under `USER_CLUSTER_NAME` namespace, and get the name of ksa-signing-key secret: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n=USER_CLUSTER_NAME get secrets | grep ksa-signing-key

  2. Copy the ksa-signing-key secret, and name the copied secret as service-account-cert: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n=USER_CLUSTER_NAME get secret KSA-KEY-SECRET-NAME -oyaml | \
         sed 's/ name: .*/ name: service-account-cert/' | \
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n=USER_CLUSTER_NAME apply -f -

  3. Delete the previous ksa-signing-key secret: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n=USER_CLUSTER_NAME delete secret KSA-KEY-SECRET-NAME

  4. Update the `data.data` field in ksa-signing-key-rotation-stage configmap to `'{"tokenVersion":1,"privateKeyVersion":1,"publicKeyVersions":[1]}'`: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n=USER_CLUSTER_NAME \
         edit configmap ksa-signing-key-rotation-stage

  5. Disable the validation webhook to edit the version information in the OnPremUserCluster custom resource: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG patch validatingwebhookconfiguration onprem-user-cluster-controller -p '
         webhooks:
         - name: vonpremnodepool.onprem.cluster.gke.io
           rules:
           - apiGroups:
             - onprem.cluster.gke.io
             apiVersions:
             - v1alpha1
             operations:
             - CREATE
             resources:
             - onpremnodepools
         - name: vonpremusercluster.onprem.cluster.gke.io
           rules:
           - apiGroups:
             - onprem.cluster.gke.io
             apiVersions:
             - v1alpha1
             operations:
             - CREATE
             resources:
             - onpremuserclusters
         '

  6. Update the `spec.ksaSigningKeyRotation.generated.ksaSigningKeyRotation` field to `1` in your OnPremUserCluster custom resource: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n=USER_CLUSTER_NAME-gke-onprem-mgmt \
         edit onpremusercluster USER_CLUSTER_NAME

  7. Wait until the target user cluster to be ready, you can check the status by: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n=USER_CLUSTER_NAME-gke-onprem-mgmt \
         get onpremusercluster

  8. Restore the validation webhook for the user cluster: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG patch validatingwebhookconfiguration onprem-user-cluster-controller -p '
         webhooks:
         - name: vonpremnodepool.onprem.cluster.gke.io
           rules:
           - apiGroups:
             - onprem.cluster.gke.io
             apiVersions:
             - v1alpha1
             operations:
             - CREATE
             - UPDATE
             resources:
             - onpremnodepools
         - name: vonpremusercluster.onprem.cluster.gke.io
           rules:
           - apiGroups:
             - onprem.cluster.gke.io
             apiVersions:
             - v1alpha1
             operations:
             - CREATE
             - UPDATE
             resources:
             - onpremuserclusters
         '

  9. Avoid another KSA signing key rotation until the cluster is upgraded to the version with the fix.

  
Operation | 1.13.1+, 1.14, 1., 1.16 | 

### F5 BIG-IP virtual servers aren't cleaned up when Terraform deletes user clusters

When you use Terraform to delete a user cluster with a F5 BIG-IP load balancer, the F5 BIG-IP virtual servers aren't removed after the cluster deletion.   
**Workaround:** To remove the F5 resources, follow the steps to [clean up a user cluster F5 partition ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-a-user-cluster#clean_up_F5)  
Installation, Upgrades, Updates | 1.13.8, 1.14.4 | 

### kind cluster pulls container images from `docker.io`

If you create a version 1.13.8 or version 1.14.4 admin cluster, or upgrade an admin cluster to version 1.13.8 or 1.14.4, the kind cluster pulls the following container images from `docker.io`: 
* `docker.io/kindest/kindnetd`
* `docker.io/kindest/local-path-provisioner`
* `docker.io/kindest/local-path-helper`
If `docker.io` isn't accessible from your admin workstation, the admin cluster creation or upgrade fails to bring up the kind cluster. Running the following command on the admin workstation shows the corresponding containers pending with `ErrImagePull`:
    
    
    docker exec gkectl-control-plane kubectl get pods -A

The response contains entries like the following:
    
    
    ...
    kube-system         kindnet-xlhmr                             0/1
        ErrImagePull  0    3m12s
    ...
    local-path-storage  local-path-provisioner-86666ffff6-zzqtp   0/1
        Pending       0    3m12s
    ...

These container images should be preloaded in the kind cluster container image. However, kind v0.18.0 has [an issue with the preloaded container images](https://github.com/kubernetes-sigs/kind/issues/3173), which causes them to be pulled from the internet by mistake.   
**Workaround:** Run the following commands on the admin workstation, while your admin cluster is pending on creation or upgrade:
    
    
    docker exec gkectl-control-plane ctr -n k8s.io images tag docker.io/kindest/kindnetd:v20230330-48f316cd@sha256:c19d6362a6a928139820761475a38c24c0cf84d507b9ddf414a078cf627497af docker.io/kindest/kindnetd:v20230330-48f316cd
    docker exec gkectl-control-plane ctr -n k8s.io images tag docker.io/kindest/kindnetd:v20230330-48f316cd@sha256:c19d6362a6a928139820761475a38c24c0cf84d507b9ddf414a078cf627497af docker.io/kindest/kindnetd@sha256:c19d6362a6a928139820761475a38c24c0cf84d507b9ddf414a078cf627497af
    
    docker exec gkectl-control-plane ctr -n k8s.io images tag docker.io/kindest/local-path-helper:v20230330-48f316cd@sha256:135203f2441f916fb13dad1561d27f60a6f11f50ec288b01a7d2ee9947c36270 docker.io/kindest/local-path-helper:v20230330-48f316cd
    docker exec gkectl-control-plane ctr -n k8s.io images tag docker.io/kindest/local-path-helper:v20230330-48f316cd@sha256:135203f2441f916fb13dad1561d27f60a6f11f50ec288b01a7d2ee9947c36270 docker.io/kindest/local-path-helper@sha256:135203f2441f916fb13dad1561d27f60a6f11f50ec288b01a7d2ee9947c36270
    
    docker exec gkectl-control-plane ctr -n k8s.io images tag docker.io/kindest/local-path-provisioner:v0.0.23-kind.0@sha256:f2d0a02831ff3a03cf51343226670d5060623b43a4cfc4808bd0875b2c4b9501 docker.io/kindest/local-path-provisioner:v0.0.23-kind.0
    docker exec gkectl-control-plane ctr -n k8s.io images tag docker.io/kindest/local-path-provisioner:v0.0.23-kind.0@sha256:f2d0a02831ff3a03cf51343226670d5060623b43a4cfc4808bd0875b2c4b9501 docker.io/kindest/local-path-provisioner@sha256:f2d0a02831ff3a03cf51343226670d5060623b43a4cfc4808bd0875b2c4b9501  
  
Operation | 1.13.0-1.13.7, 1.14.0-1.14.4, 1.15.0 | 

### Unsuccessful failover on HA Controlplane V2 user cluster and admin cluster when the network filters out duplicate GARP requests

If your cluster VMs are connected with a switch that filters out duplicate GARP (gratuitous ARP) requests, the keepalived leader election might encounter a race condition, which causes some nodes to have incorrect ARP table entries. The affected nodes can `ping` the control plane VIP, but a TCP connection to the control plane VIP will time out.   
**Workaround:** Run the following command on each control plane node of the affected cluster: 
    
    
        iptables -I FORWARD -i ens192 --destination CONTROL_PLANE_VIP -j DROP
          
  
Upgrades, Updates | 1.13.0-1.13.7, 1.14.0-1.14.4, 1.15.0 | 

### `vsphere-csi-controller` needs be restarted after the vCenter certificate rotation 

`vsphere-csi-controller` should refresh its vCenter secret after vCenter certificate rotation. However, the current system does not properly restart the pods of `vsphere-csi-controller`, causing `vsphere-csi-controller` to crash after the rotation.   
**Workaround:** For clusters created at 1.13 and later versions, follow the instructions below to restart `vsphere-csi-controller`
    
    
    kubectl --kubeconfig=ADMIN_KUBECONFIG rollout restart deployment vsphere-csi-controller -n kube-system  
  
Installation | 1.10.3-1.10.7, 1.11, 1.12, 1.13.0-1.13.1 | 

### Admin cluster creation does not fail on [cluster registration](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#on-premises) errors

Even when [cluster registration](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console) fails during admin cluster creation, the command `gkectl create admin` does not fail on the error and might succeed. In other words, the admin cluster creation could "succeed" without being registered to a fleet.  To identify the symptom, you can look for the following error messages in the log of `gkectl create admin`, 
    
    
    Failed to register admin cluster

You can also check whether you can find the cluster among [registered clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console#view_registered_clusters) on cloud console.   
**Workaround:** For clusters created at 1.12 and later versions, follow the instructions for [re-attempting the admin cluster registration](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console#fleet_members_and_the_console) after cluster creation. For clusters created at earlier versions, 

  1. Append a fake key-value pair like "foo: bar" to your connect-register SA key file 
  2. Run [`gkectl update admin`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general) to re-register the admin cluster. 

  
Upgrades, Updates | 1.10, 1.11, 1.12, 1.13.0-1.13.1 | 

### Admin cluster re-registration might be skipped during admin cluster upgrade

During admin cluster upgrade, if upgrading user control plane nodes times out, the admin cluster will not be re-registered with the updated connect agent version.   
**Workaround:** Check whether the cluster shows among [registered clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console#view_registered_clusters). As an optional step, [Log in to the cluster after setting up authentication](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console#fleet_members_and_the_console). If the cluster is still registered, you might skip the following instructions for re-attempting the registration. For clusters upgraded to 1.12 and later versions, follow the instructions for [re-attempting the admin cluster registration](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console#fleet_members_and_the_console) after cluster creation. For clusters upgraded to earlier versions, 

  1. Append a fake key-value pair like "foo: bar" to your connect-register SA key file 
  2. Run [`gkectl update admin`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general) to re-register the admin cluster. 

  
Configuration | 1.15.0 | 

### False error message about `vCenter.dataDisk`

For a high-availability admin cluster, `gkectl prepare` shows this false error message:
    
    
    vCenter.dataDisk must be present in the AdminCluster spec

  
**Workaround:** You can safely ignore this error message.  
VMware | 1.15.0 | 

### Node pool creation fails because of redundant VM-Host affinity rules

During creation of a node pool that uses [VM-Host affinity](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-vm-host-affinity), a race condition might result in multiple [VM-Host affinity rules](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-2FB90EF5-7733-4095-8B66-F10D6C57B820.html) being created with the same name. This can cause node pool creation to fail.   
**Workaround:** Remove the old redundant rules so that node pool creation can proceed. These rules are named [USER_CLUSTER_NAME]-[HASH].  
Operation | 1.15.0 | 

### `gkectl repair admin-master` may fail due to `failed to delete the admin master node object and reboot the admin master VM `

The `gkectl repair admin-master` command may fail due to a race condition with the following error. 
    
    
    Failed to repair: failed to delete the admin master node object and reboot the admin master VM

  
**Workaround:** This command is idempotent. It can rerun safely until the command succeeds.  
Upgrades, Updates | 1.15.0 | 

### Pods remain in Failed state afer re-creation or update of a control-plane node

After you re-create or update a control-plane node, certain Pods might be left in the `Failed` state due to NodeAffinity predicate failure. These failed Pods don't affect normal cluster operations or health.    
**Workaround:** You can safely ignore the failed Pods or manually delete them.  
Security, Configuration | 1.15.0-1.15.1 | 

### OnPremUserCluster not ready because of private registry credentials

If you use [prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials) and a private registry, but you haven't configured prepared credentials for your private registry, the OnPremUserCluster might not become ready, and you might see the following error message: 
    
    
    failed to check secret reference for private registry …

  
**Workaround:** Prepare the private registry credentials for the user cluster according to the instructions in [Configure prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials).   
Upgrades, Updates | 1.15.0 | 

### `gkectl upgrade admin` fails with `StorageClass standard sets the parameter diskformat which is invalid for CSI Migration `

During `gkectl upgrade admin`, the storage preflight check for CSI Migration verifies that the StorageClasses don't have parameters that are ignored after CSI Migration. For example, if there's a StorageClass with the parameter `diskformat` then `gkectl upgrade admin` flags the StorageClass and reports a failure in the preflight validation. Admin clusters created in Google Distributed Cloud 1.10 and before have a StorageClass with `diskformat: thin` which will fail this validation however this StorageClass still works fine after CSI Migration. These failures should be interpreted as warnings instead.  For more information, check the StorageClass parameter section in [ Migrating In-Tree vSphere Volumes to vSphere Container Storage Plug-in](https://docs.vmware.com/en/VMware-vSphere-Container-Storage-Plug-in/2.0/vmware-vsphere-csp-getting-started/GUID-968D421F-D464-4E22-8127-6CB9FF54423F.html?hWord=N4IghgNiBcIMYGcCWACAtkg5gJzAFyQHsA7EAXyA#considerations-for-migration-of-intree-vsphere-volumes-0).    
**Workaround:** After confirming that your cluster has a StorageClass with parameters ignored after CSI Migration run `gkectl upgrade admin` with the flag `--skip-validation-cluster-health`.  
Storage | 1.15, 1.16 | 

### Migrated in-tree vSphere volumes using the Windows file system can't be used with vSphere CSI driver

Under certain conditions disks can be attached as readonly to Windows nodes. This results in the corresponding volume being readonly inside a Pod. This problem is more likely to occur when a new set of nodes replaces an old set of nodes (for example, cluster upgrade or node pool update). Stateful workloads that previously worked fine might be unable to write to their volumes on the new set of nodes.   
**Workaround:**

  1. Get the UID of the Pod that is unable to write to its volume: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get pod \
             POD_NAME --namespace POD_NAMESPACE \
             -o=jsonpath='{.metadata.uid}{"\n"}'

  2. Use the PersistentVolumeClaim to get the name of the PersistentVolume: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get pvc \
             PVC_NAME --namespace POD_NAMESPACE \
             -o jsonpath='{.spec.volumeName}{"\n"}'

  3. Determine the name of the node where the Pod is running: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIGget pods \
             --namespace POD_NAMESPACE \
             -o jsonpath='{.spec.nodeName}{"\n"}'

  4. Obtain powershell access to the node, either through SSH or the vSphere web interface. 
  5. Set environment variables: 
         
         PS C:\Users\administrator> pvname=PV_NAME
         PS C:\Users\administrator> podid=POD_UID

  6. Identify the disk number for the disk associated with the PersistentVolume: 
         
         PS C:\Users\administrator> disknum=(Get-Partition -Volume (Get-Volume -UniqueId ("\\?\"+(Get-Item (Get-Item
         "C:\var\lib\kubelet\pods\$podid\volumes\kubernetes.io~csi\$pvname\mount").Target).Target))).DiskNumber

  7. Verify that the disk is `readonly`: 
         
         PS C:\Users\administrator> (Get-Disk -Number $disknum).IsReadonly

The result should be `True`. 
  8. Set `readonly` to `false`. 
         
         PS C:\Users\administrator> Set-Disk -Number $disknum -IsReadonly $false
         PS C:\Users\administrator> (Get-Disk -Number $disknum).IsReadonly

  9. Delete the Pod so that it will get restarted: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete pod POD_NAME \
             --namespace POD_NAMESPACE

  10. The Pod should get scheduled to the same node. But in case the Pod gets scheduled to a new node, you might need to repeat the preceding steps on the new node. 

  
Upgrades, Updates | 1.12, 1.13.0-1.13.7, 1.14.0-1.14.4 | 

### `vsphere-csi-secret` is not updated after `gkectl update credentials vsphere --admin-cluster`

If you update the vSphere credentials for an admin cluster following [updating cluster credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-cluster-credentials), you might find `vsphere-csi-secret` under `kube-system` namespace in the admin cluster still uses the old credential.   
**Workaround:**

  1. Get the `vsphere-csi-secret` secret name: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n=kube-system get secrets | grep vsphere-csi-secret

  2. Update the data of the `vsphere-csi-secret` secret you got from the above step: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n=kube-system patch secret CSI_SECRET_NAME -p \
           "{\"data\":{\"config\":\"$( \
             kubectl --kubeconfig=ADMIN_KUBECONFIG -n=kube-system get secrets CSI_SECRET_NAME -ojsonpath='{.data.config}' \
               | base64 -d \
               | sed -e '/user/c user = \"VSPHERE_USERNAME_TO_BE_UPDATED\"' \
               | sed -e '/password/c password = \"VSPHERE_PASSWORD_TO_BE_UPDATED\"' \
               | base64 -w 0 \
             )\"}}"

  3. Restart `vsphere-csi-controller`: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n=kube-system rollout restart deployment vsphere-csi-controller

  4. You can track the rollout status with: 
         
         kubectl --kubeconfig=ADMIN_KUBECONFIG -n=kube-system rollout status deployment vsphere-csi-controller

After the deployment is successfully rolled out, the updated `vsphere-csi-secret` should be used by the controller. 

  
Upgrades, Updates | 1.10, 1.11, 1.12.0-1.12.6, 1.13.0-1.13.6, 1.14.0-1.14.2  | 

### `audit-proxy` crashloop when enabling Cloud Audit Logs with `gkectl update cluster`

`audit-proxy` might crashloop because of empty `--cluster-name`. This behavior is caused by a bug in the update logic, where the cluster name is not propagated to the audit-proxy pod / container manifest.   
**Workaround:** For a control plane v2 user cluster with `enableControlplaneV2: true`, connect to the user control plane machine using SSH, and update `/etc/kubernetes/manifests/audit-proxy.yaml` with `--cluster_name=USER_CLUSTER_NAME`. For a control plane v1 user cluster, edit the `audit-proxy` container in the `kube-apiserver` statefulset to add `--cluster_name=USER_CLUSTER_NAME`:
    
    
    kubectl edit statefulset kube-apiserver -n USER_CLUSTER_NAME --kubeconfig=ADMIN_CLUSTER_KUBECONFIG  
  
Upgrades, Updates | 1.11, 1.12, 1.13.0-1.13.5, 1.14.0-1.14.1  | 

### An additional control plane redeployment right after `gkectl upgrade cluster`

Right after `gkectl upgrade cluster`, the control plane pods might be re-deployed again. The cluster state from `gkectl list clusters` change from `RUNNING` TO `RECONCILING`. Requests to the user cluster might timeout. This behavior is because of the control plane certificate rotation happens automatically after `gkectl upgrade cluster`. This issue only happens to user clusters that do NOT use control plane v2.   
**Workaround:** Wait for the cluster state to change back to `RUNNING` again in `gkectl list clusters`, or upgrade to versions with the fix: 1.13.6+, 1.14.2+ or 1.15+.  
Upgrades, Updates | 1.12.7 | 

### Bad release 1.12.7-gke.19 has been removed

Google Distributed Cloud 1.12.7-gke.19 is a bad release and you should not use it. The artifacts have been removed from the Cloud Storage bucket.   
**Workaround:** Use the 1.12.7-gke.20 release instead.  
Upgrades, Updates | 1.12.0+, 1.13.0-1.13.7, 1.14.0-1.14.3 | 

### [`gke-connect-agent`](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent) continues to use the older image after registry credential updated

If you update the registry credential using one of the following methods:

  * `gkectl update credentials componentaccess` if not using private registry
  * `gkectl update credentials privateregistry` if using private registry

you might find `gke-connect-agent` continues to use the older image or the `gke-connect-agent` pods cannot be pulled up due to `ImagePullBackOff`. This issue will be fixed in Google Distributed Cloud releases 1.13.8, 1.14.4, and subsequent releases.   
**Workaround:** **Option 1** : Redeploy `gke-connect-agent` manually: 

  1. Delete the `gke-connect` namespace: 
         
         kubectl --kubeconfig=KUBECONFIG delete namespace gke-connect

  2. Redeploy `gke-connect-agent` with the original register service account key (no need to update the key):  For admin cluster: 
         
         gkectl update credentials register --kubeconfig=ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG_FILE --admin-cluster

For user cluster: 
         
         gkectl update credentials register --kubeconfig=ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG_FILE


**Option 2** : You can manually change the data of the image pull secret `regcred` which is used by `gke-connect-agent` deployment:
    
    
    kubectl --kubeconfig=KUBECONFIG -n=gke-connect patch secrets regcred -p "{\"data\":{\".dockerconfigjson\":\"$(kubectl --kubeconfig=KUBECONFIG -n=kube-system get secrets private-registry-creds -ojsonpath='{.data.\.dockerconfigjson}')\"}}"

**Option 3** : You can add the default image pull secret for your cluster in the `gke-connect-agent` deployment by:

  1. Copy the default secret to `gke-connect` namespace: 
         
         kubectl --kubeconfig=KUBECONFIG -n=kube-system get secret private-registry-creds -oyaml | sed 's/ namespace: .*/ namespace: gke-connect/' | kubectl --kubeconfig=KUBECONFIG -n=gke-connect apply -f -

  2. Get the `gke-connect-agent` deployment name: 
         
         kubectl --kubeconfig=KUBECONFIG -n=gke-connect get deployment | grep gke-connect-agent

  3. Add the default secret to `gke-connect-agent` deployment: 
         
         kubectl --kubeconfig=KUBECONFIG -n=gke-connect patch deployment DEPLOYMENT_NAME -p '{"spec":{"template":{"spec":{"imagePullSecrets": [{"name": "private-registry-creds"}, {"name": "regcred"}]}}}}'


  
Installation | 1.13, 1.14 | 

### Manual LB configuration check failure

When you validate the configuration before creating a cluster with Manual load balancer by running `gkectl check-config`, then the command will fail with the following error messages.
    
    
     - Validation Category: Manual LB    Running validation check for "Network
    configuration"...panic: runtime error: invalid memory address or nil pointer
    dereference

  
**Workaround:** Option 1: You can use the patch version 1.13.7 and 1.14.4 that will include the fix. Option 2: You can also run the same command to validate the configuration but skip the load balancer validation.
    
    
    gkectl check-config --skip-validation-load-balancer  
  
Operation | 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13, and 1.14 | 

### etcd watch starvation

Clusters running etcd version 3.4.13 or earlier may experience watch starvation and non-operational resource watches, which can lead to the following problems: 

  * Pod scheduling is disrupted
  * Nodes are unable to register
  * kubelet doesn't observe pod changes

These problems can make the cluster non-functional.  This issue is fixed in Google Distributed Cloud releases 1.12.7, 1.13.6, 1.14.3, and subsequent releases. These newer releases use etcd version 3.4.21. All prior versions of Google Distributed Cloud are affected by this issue.  **Workaround** If you can't upgrade immediately, you can mitigate the risk of cluster failure by reducing the number of nodes in your cluster. Remove nodes until the `etcd_network_client_grpc_sent_bytes_total` metric is less than 300 MBps.  To view this metric in Metrics Explorer:

  1. Go to the Metrics Explorer in the Google Cloud console: [Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)
  2. Select the **Configuration** tab. 
  3. Expand the **Select a metric** , enter `Kubernetes Container` in the filter bar, and then use the submenus to select the metric: 
     1. In the **Active resources** menu, select **Kubernetes Container**. 
     2. In the **Active metric categories** menu, select **Anthos**.
     3. In the **Active metrics** menu, select `etcd_network_client_grpc_sent_bytes_total`.
     4. Click Apply.

  
Upgrades, Updates | 1.10, 1.11, 1.12, 1.13, and 1.14 | 

### GKE Identity Service can cause control plane latencies

At cluster restarts or upgrades, GKE Identity Service can get overwhelmed with traffic consisting of expired JWT tokens forwarded from the `kube-apiserver` to GKE Identity Service over the authentication webhook. Although GKE Identity Service doesn't crashloop, it becomes unresponsive and ceases to serve further requests. This problem ultimately leads to higher control plane latencies. This issue is fixed in the following Google Distributed Cloud releases:

  * 1.12.6+
  * 1.13.6+
  * 1.14.2+

To determine if you're affected by this issue, perform the following steps:

  1. Check whether the GKE Identity Service endpoint can be reached externally: 
         
         curl -s -o /dev/null -w "%{http_code}" \
             -X POST https://CLUSTER_ENDPOINT/api/v1/namespaces/anthos-identity-service/services/https:ais:https/proxy/authenticate -d '{}'

Replace CLUSTER_ENDPOINT with the control plane VIP and control plane load balancer port for your cluster (for example, `172.16.20.50:443`). If you're affected by this issue, the command returns a `400` status code. If the request times out, restart the `ais` Pod and rerun the `curl` command to see if that resolves the problem. If you get a status code of `000`, the problem has been resolved and you are done. If you still get a `400` status code, the GKE Identity Service HTTP server isn't starting. In this case, continue.
  2. Check the GKE Identity Service and kube-apiserver logs: 
     1. Check the GKE Identity Service log: 
            
            kubectl logs -f -l k8s-app=ais -n anthos-identity-service \
                --kubeconfig KUBECONFIG

If the log contains an entry like the following, then you are affected by this issue:
            
            I0811 22:32:03.583448      32 authentication_plugin.cc:295] Stopping OIDC authentication for ???. Unable to verify the OIDC ID token: JWT verification failed: The JWT does not appear to be from this identity provider. To match this provider, the 'aud' claim must contain one of the following audiences:

     2. Check the `kube-apiserver` logs for your clusters: In the following commands, KUBE_APISERVER_POD is the name of the `kube-apiserver` Pod on the given cluster. Admin cluster:
            
            kubectl --kubeconfig ADMIN_KUBECONFIG logs \
                -n kube-system KUBE_APISERVER_POD kube-apiserver

User cluster:
            
            kubectl --kubeconfig ADMIN_KUBECONFIG logs \
                -n USER_CLUSTER_NAME KUBE_APISERVER_POD kube-apiserver

If the `kube-apiserver` logs contain entries like the following, then you are affected by this issue:
            
            E0811 22:30:22.656085       1 webhook.go:127] Failed to make webhook authenticator request: error trying to reach service: net/http: TLS handshake timeout
            E0811 22:30:22.656266       1 authentication.go:63] "Unable to authenticate the request" err="[invalid bearer token, error trying to reach service: net/http: TLS handshake timeout]"


**Workaround** If you can't upgrade your clusters immediately to get the fix, you can identify and restart the offending pods as a workaround:

  1. Increase the GKE Identity Service verbosity level to 9: 
         
         kubectl patch deployment ais -n anthos-identity-service --type=json \
             -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", \
             "value":"--vmodule=cloud/identity/hybrid/charon/*=9"}]' \
             --kubeconfig KUBECONFIG

  2. Check the GKE Identity Service log for the invalid token context: 
         
         kubectl logs -f -l k8s-app=ais -n anthos-identity-service \
             --kubeconfig KUBECONFIG

  3. To get the token payload associated with each invalid token context, parse each related service account secret with the following command: 
         
         kubectl -n kube-system get secret SA_SECRET \
             --kubeconfig KUBECONFIG \
             -o jsonpath='{.data.token}' | base64 --decode

  4. To decode the token and see the source pod name and namespace, copy the token to the debugger at [jwt.io](https://jwt.io/). 
  5. Restart the pods identified from the tokens.

  
Operation | 1.8, 1.9, 1.10 | 

### The memory usage increase issue of etcd-maintenance pods

The etcd maintenance pods that use `etcddefrag:gke_master_etcddefrag_20210211.00_p0` image are affected. The `etcddefrag` container opens a new connection to etcd server during each defrag cycle and the old connections are not cleaned up.   
**Workaround:** Option 1: Upgrade to the latest patch version from 1.8 to 1.11 which contain the fix. Option 2: If you are using patch version earlier than 1.9.6 and 1.10.3, you need to scale down the etcd-maintenance pod for admin and user cluster:
    
    
    kubectl scale --replicas 0 deployment/gke-master-etcd-maintenance -n USER_CLUSTER_NAME --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    kubectl scale --replicas 0 deployment/gke-master-etcd-maintenance -n kube-system --kubeconfig ADMIN_CLUSTER_KUBECONFIG  
  
Operation | 1.9, 1.10, 1.11, 1.12, 1.13 | 

### Miss the health checks of user cluster control plane pods

Both the cluster health controller and the `gkectl diagnose cluster` command perform a set of health checks including the pods health checks across namespaces. However, they start to skip the user control plane pods by mistake. If you use the control plane v2 mode, this won't affect your cluster.   
**Workaround:** This won't affect any workload or cluster management. If you want to check the control plane pods healthiness, you can run the following commands:
    
    
    kubectl get pods -owide -n USER_CLUSTER_NAME --kubeconfig ADMIN_CLUSTER_KUBECONFIG  
  
Upgrades, Updates | 1.6+, 1.7+ | 

### 1.6 and 1.7 admin cluster upgrades may be affected by the `k8s.gcr.io` -> `registry.k8s.io` redirect

Kubernetes [redirected](https://kubernetes.io/blog/2023/03/10/image-registry-redirect/) the traffic from `k8s.gcr.io` to `registry.k8s.io` on 3/20/2023. In Google Distributed Cloud 1.6.x and 1.7.x, the admin cluster upgrades use the container image `k8s.gcr.io/pause:3.2`. If you use a proxy for your admin workstation and the proxy doesn't allow `registry.k8s.io` and the container image `k8s.gcr.io/pause:3.2` is not cached locally, the admin cluster upgrades will fail when pulling the container image.   
**Workaround:** Add `registry.k8s.io` to the allowlist of the proxy for your admin workstation.  
Networking | 1.10, 1.11, 1.12.0-1.12.6, 1.13.0-1.13.6, 1.14.0-1.14.2 | 

### Seesaw validation failure on load balancer creation

`gkectl create loadbalancer` fails with the following error message:
    
    
    - Validation Category: Seesaw LB - [FAILURE] Seesaw validation: xxx cluster lb health check failed: LB"xxx.xxx.xxx.xxx" is not healthy: Get "http://xxx.xxx.xxx.xxx:xxx/healthz": dial tcpxxx.xxx.xxx.xxx:xxx: connect: no route to host

This is due to the seesaw group file already existing. And the preflight check tries to validate a non-existent seesaw load balancer. **Workaround:** Remove the existing seesaw group file for this cluster. The file name is `seesaw-for-gke-admin.yaml` for the admin cluster, and `seesaw-for-{CLUSTER_NAME}.yaml` for a user cluster.  
Networking | 1.14 | 

### Application timeouts caused by conntrack table insertion failures

Google Distributed Cloud version 1.14 is susceptible to netfilter connection tracking (conntrack) table insertion failures when using Ubuntu or COS operating system images. Insertion failures lead to random application timeouts and can occur even when the conntrack table has room for new entries. The failures are caused by changes in kernel 5.15 and higher that restrict table insertions based on chain length.  To see if you are affected by this issue, you can check the in-kernel connection tracking system statistics on each node with the following command:
    
    
    sudo conntrack -S

The response looks like this:
    
    
    cpu=0       found=0 invalid=4 insert=0 insert_failed=0 drop=0 early_drop=0 error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=1       found=0 invalid=0 insert=0 insert_failed=0 drop=0 early_drop=0 error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=2       found=0 invalid=16 insert=0 insert_failed=0 drop=0 early_drop=0 error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=3       found=0 invalid=13 insert=0 insert_failed=0 drop=0 early_drop=0 error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=4       found=0 invalid=9 insert=0 insert_failed=0 drop=0 early_drop=0 error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=5       found=0 invalid=1 insert=0 insert_failed=0 drop=0 early_drop=0 error=519 search_restart=0 clash_resolve=126 chaintoolong=0
    ...

If a `chaintoolong` value in the response is a non-zero number, you're affected by this issue. **Workaround** The short term mitigation is to increase the size of both the netfiler hash table (`nf_conntrack_buckets`) and the netfilter connection tracking table (`nf_conntrack_max`). Use the following commands on each cluster node to increase the size of the tables:
    
    
    sysctl -w net.netfilter.nf_conntrack_buckets=TABLE_SIZE
    sysctl -w net.netfilter.nf_conntrack_max=TABLE_SIZE

Replace TABLE_SIZE with new size in bytes. The default table size value is `262144`. We suggest that you set a value equal to 65,536 times the number of cores on the node. For example, if your node has eight cores, set the table size to `524288`.  
Networking | 1.13.0-1.13.2 | 

### calico-typha or anetd-operator crash loop on Windows nodes with Controlplane V2

With [ Controlplane V2 enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field), `calico-typha` or `anetd-operator` might be scheduled to Windows nodes and get into crash loop. The reason is that the two deployments tolerate all taints including Windows node taint.   
**Workaround:** Either upgrade to 1.13.3+, or run the following commands to edit the `calico-typha` or `anetd-operator` deployment:
    
    
        # If dataplane v2 is not used.
        kubectl edit deployment -n kube-system calico-typha --kubeconfig USER_CLUSTER_KUBECONFIG
        # If dataplane v2 is used.
        kubectl edit deployment -n kube-system anetd-operator --kubeconfig USER_CLUSTER_KUBECONFIG
        

Remove the following `spec.template.spec.tolerations`:
    
    
        - effect: NoSchedule
          operator: Exists
        - effect: NoExecute
          operator: Exists
        

And add the following toleration:
    
    
        - key: node-role.kubernetes.io/master
          operator: Exists
          
  
Configuration | 1.14.0-1.14.2 | 

### User cluster private registry credential file cannot be loaded

You might not be able to create a user cluster if you specify the `privateRegistry` section with credential `fileRef`. Preflight might fail with the following message: 
    
    
    [FAILURE] Docker registry access: Failed to login.
    

  
**Workaround:**

  * If you did not intend to specify the field or you want to use the same private registry credential as admin cluster, you can simply remove or comment the `privateRegistry` section in your user cluster config file.
  * If you want to use a specific private registry credential for your user cluster, you may temporarily specify the `privateRegistry` section this way: 
        
        privateRegistry:
          address: PRIVATE_REGISTRY_ADDRESS
          credentials:
            username: PRIVATE_REGISTRY_USERNAME
            password: PRIVATE_REGISTRY_PASSWORD
          caCertPath: PRIVATE_REGISTRY_CACERT_PATH

(**NOTE** : This is only a temporarily fix and these fields are already deprecated, consider using the credential file when upgrading to 1.14.3+.) 

  
Operations | 1.10+ | 

### Cloud Service Mesh and other service meshes not compatible with Dataplane v2

Dataplane V2 takes over load balancing and creates a kernel socket instead of a packet based DNAT. This means that Cloud Service Mesh cannot do packet inspection as the pod is bypassed and never uses IPTables. This manifests in kube-proxy free mode by loss of connectivity or incorrect traffic routing for services with Cloud Service Mesh as the sidecar cannot do packet inspection. This issue is present on all versions of Google Distributed Cloud 1.10, however some newer versions of 1.10 (1.10.2+) have a workaround.   
**Workaround:** Either upgrade to 1.11 for full compatibility or if running 1.10.2 or later, run:
    
    
        kubectl edit cm -n kube-system cilium-config --kubeconfig USER_CLUSTER_KUBECONFIG
        

Add `bpf-lb-sock-hostns-only: true` to the configmap and then restart the anetd daemonset:
    
    
          kubectl rollout restart ds anetd -n kube-system --kubeconfig USER_CLUSTER_KUBECONFIG
          
  
Storage | 1.12+, 1.13.3 | 

### `kube-controller-manager` might detach persistent volumes forcefully after 6 minutes

`kube-controller-manager` might timeout when detaching PV/PVCs after 6 minutes, and forcefully detach the PV/PVCs. Detailed logs from `kube-controller-manager` show events similar to the following:
    
    
    $ cat kubectl_logs_kube-controller-manager-xxxx | grep "DetachVolume started" | grep expired
    
    kubectl_logs_kube-controller-manager-gke-admin-master-4mgvr_--container_kube-controller-manager_--kubeconfig_kubeconfig_--request-timeout_30s_--namespace_kube-system_--timestamps:2023-01-05T16:29:25.883577880Z W0105 16:29:25.883446       1 reconciler.go:224] attacherDetacher.DetachVolume started for volume "pvc-8bb4780b-ba8e-45f4-a95b-19397a66ce16" (UniqueName: "kubernetes.io/csi/csi.vsphere.vmware.com^126f913b-4029-4055-91f7-beee75d5d34a") on node "sandbox-corp-ant-antho-0223092-03-u-tm04-ml5m8-7d66645cf-t5q8f"
    This volume is not safe to detach, but maxWaitForUnmountDuration 6m0s expired, force detaching
    

To verify the issue, log into the node and run the following commands:
    
    
    # See all the mounting points with disks
    lsblk -f
    
    # See some ext4 errors
    sudo dmesg -T

In the kubelet log, errors like the following are displayed:
    
    
    Error: GetDeviceMountRefs check failed for volume "pvc-8bb4780b-ba8e-45f4-a95b-19397a66ce16" (UniqueName: "kubernetes.io/csi/csi.vsphere.vmware.com^126f913b-4029-4055-91f7-beee75d5d34a") on node "sandbox-corp-ant-antho-0223092-03-u-tm04-ml5m8-7d66645cf-t5q8f" :
    the device mount path "/var/lib/kubelet/plugins/kubernetes.io/csi/pv/pvc-8bb4780b-ba8e-45f4-a95b-19397a66ce16/globalmount" is still mounted by other references [/var/lib/kubelet/plugins/kubernetes.io/csi/pv/pvc-8bb4780b-ba8e-45f4-a95b-19397a66ce16/globalmount
    

  
**Workaround:** Connect to the affected node using SSH and reboot the node.  
Upgrades, Updates | 1.12+, 1.13+, 1.14+ | 

### Cluster upgrade is stuck if 3rd party CSI driver is used

You might not be able to upgrade a cluster if you use a 3rd party CSI driver. The `gkectl cluster diagnose` command might return the following error: 
    
    
    "virtual disk "kubernetes.io/csi/csi.netapp.io^pvc-27a1625f-29e3-4e4f-9cd1-a45237cc472c" IS NOT attached to machine "cluster-pool-855f694cc-cjk5c" but IS listed in the Node.Status"
    

  
**Workaround:** Perform the upgrade using the `--skip-validation-all` option.  
Operation | 1.10+, 1.11+, 1.12+, 1.13+, 1.14+ | 

### `gkectl repair admin-master` creates the admin master VM without upgrading its vm hardware version

The admin master node created via `gkectl repair admin-master` may use a lower VM hardware version than expected. When the issue happens, you will see the error from the `gkectl diagnose cluster` report. 
    
    
    CSIPrerequisites [VM Hardware]: The current VM hardware versions are lower than vmx-15 which is unexpected. Please contact Anthos support to resolve this issue.

  
**Workaround:** Shutdown the admin master node, follow <https://kb.vmware.com/s/article/1003746> to upgrade the node to the expected version described in the error message, and then start the node.  
Operating system | 1.10+, 1.11+, 1.12+, 1.13+, 1.14+, 1.15+, 1.16+, , 1.28+, 1.29+, 1.30+, 1.31+, 1.32+  | 

### VM releases DHCP lease on shutdown/reboot unexpectedly, which may result in IP changes

In systemd v244, `systemd-networkd` has a [default behavior change](https://github.com/systemd/systemd/commit/800603524a7ab076d40450286ff7802a04289b7f?diff=unified#diff-d81a981ca75657b8fc8f6ad6871cb9f8d7705944919b67dad745680ebeec1b4e) on the `KeepConfiguration` configuration. Before this change, VMs did not send a DHCP lease release message to the DHCP server on shutdown or reboot. After this change, VMs send such a message and return the IPs to the DHCP server. As a result, the released IP may be reallocated to a different VM and/or a different IP may be assigned to the VM, resulting in IP conflict (at Kubernetes level, not vSphere level) and/or IP change on the VMs, which can break the clusters in various ways.  For example, you may see the following symptoms.

  * vCenter UI shows that no VMs use the same IP, but `kubectl get nodes -o wide` returns nodes with duplicate IPs. 
        
        NAME   STATUS    AGE  VERSION          INTERNAL-IP    EXTERNAL-IP    OS-IMAGE            KERNEL-VERSION    CONTAINER-RUNTIME
        node1  Ready     28h  v1.22.8-gke.204  10.180.85.130  10.180.85.130  Ubuntu 20.04.4 LTS  5.4.0-1049-gkeop  containerd://1.5.13
        node2  NotReady  71d  v1.22.8-gke.204  10.180.85.130  10.180.85.130  Ubuntu 20.04.4 LTS  5.4.0-1049-gkeop  containerd://1.5.13

  * New nodes fail to start due to `calico-node` error 
        
        2023-01-19T22:07:08.817410035Z 2023-01-19 22:07:08.817 [WARNING][9] startup/startup.go 1135: Calico node 'node1' is already using the IPv4 address 10.180.85.130.
        2023-01-19T22:07:08.817514332Z 2023-01-19 22:07:08.817 [INFO][9] startup/startup.go 354: Clearing out-of-date IPv4 address from this node IP="10.180.85.130/24"
        2023-01-19T22:07:08.825614667Z 2023-01-19 22:07:08.825 [WARNING][9] startup/startup.go 1347: Terminating
        2023-01-19T22:07:08.828218856Z Calico node failed to start


  
**Workaround:** Deploy the following DaemonSet on the cluster to revert the `systemd-networkd` default behavior change. The VMs that run this DaemonSet will not release the IPs to the DHCP server on shutdown/reboot. The IPs will be freed automatically by the DHCP server when the leases expire. 
    
    
          apiVersion: apps/v1
          kind: DaemonSet
          metadata:
            name: set-dhcp-on-stop
          spec:
            selector:
              matchLabels:
                name: set-dhcp-on-stop
            template:
              metadata:
                labels:
                  name: set-dhcp-on-stop
              spec:
                hostIPC: true
                hostPID: true
                hostNetwork: true
                containers:
                - name: set-dhcp-on-stop
                  image: ubuntu
                  tty: true
                  command:
                  - /bin/bash
                  - -c
                  - |
                    set -x
                    date
                    while true; do
                      export CONFIG=/host/run/systemd/network/10-netplan-ens192.network;
                      grep KeepConfiguration=dhcp-on-stop "${CONFIG}" > /dev/null
                      if (( $? != 0 )) ; then
                        echo "Setting KeepConfiguration=dhcp-on-stop"
                        sed -i '/\[Network\]/a KeepConfiguration=dhcp-on-stop' "${CONFIG}"
                        cat "${CONFIG}"
                        chroot /host systemctl restart systemd-networkd
                      else
                        echo "KeepConfiguration=dhcp-on-stop has already been set"
                      fi;
                      sleep 3600
                    done
                  volumeMounts:
                  - name: host
                    mountPath: /host
                  resources:
                    requests:
                      memory: "10Mi"
                      cpu: "5m"
                  securityContext:
                    privileged: true
                volumes:
                - name: host
                  hostPath:
                    path: /
                tolerations:
                - operator: Exists
                  effect: NoExecute
                - operator: Exists
                  effect: NoSchedule
            
  
Operation, Upgrades, Updates | 1.12.0-1.12.5, 1.13.0-1.13.5, 1.14.0-1.14.1 | 

### Component access service account key wiped out after admin cluster upgraded from 1.11.x

This issue will only affect admin clusters which are upgraded from 1.11.x, and won't affect admin clusters which are newly created after 1.12. After upgrading a 1.11.x cluster to 1.12.x, the `component-access-sa-key` field in `admin-cluster-creds` secret will be wiped out to empty. This can be checked by running the following command: 
    
    
    kubectl --kubeconfig ADMIN_KUBECONFIG -n kube-system get secret admin-cluster-creds -o yaml | grep 'component-access-sa-key'

If you find the output is empty that means the key is wiped out. After the component access service account key been deleted, installing new user clusters or upgrading existing user clusters will fail. The following lists some error messages you might encounter: 

  * Slow validation preflight failure with error message: `"Failed to create the test VMs: failed to get service account key: service account is not configured."`
  * Prepare by `gkectl prepare` failed with error message: `"Failed to prepare OS images: dialing: unexpected end of JSON input"`
  * If you are upgrading a 1.13 user cluster using the Google Cloud console or the gcloud CLI, when you run `gkectl update admin --enable-preview-user-cluster-central-upgrade` to deploy the upgrade platform controller, the command fails with the message: `"failed to download bundle to disk: dialing: unexpected end of JSON input"` (You can see this message in the `status` field in the output of `kubectl --kubeconfig  ADMIN_KUBECONFIG -n kube-system get onprembundle -oyaml`). 

  
**Workaround:** Add the component access service account key back into the secret manually by running the following command: 
    
    
    kubectl --kubeconfig ADMIN_KUBECONFIG -n kube-system get secret admin-cluster-creds -ojson | jq --arg casa "$(cat COMPONENT_ACESS_SERVICE_ACOOUNT_KEY_PATH | base64 -w 0)" '.data["component-access-sa-key"]=$casa' | kubectl --kubeconfig ADMIN_KUBECONFIG apply -f -  
  
Operation | 1.13.0+, 1.14.0+ | 

### Cluster autoscaler does not work when Controlplane V2 is enabled

For user clusters created with [Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster) enabled, node pools with [autoscaling](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-autoscaler) enabled always use their [`autoscaling.minReplicas`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-autoscaling-minreplicas-field) in the `user-cluster.yaml`. The log of the cluster-autoscaler pod shows an error similar to the following: 
    
    
      > kubectl --kubeconfig $USER_CLUSTER_KUBECONFIG -n kube-system \
      logs $CLUSTER_AUTOSCALER_POD --container_cluster-autoscaler
     TIMESTAMP  1 gkeonprem_provider.go:73] error getting onpremusercluster ready status: Expected to get a onpremusercluster with id foo-user-cluster-gke-onprem-mgmt/foo-user-cluster
     TIMESTAMP 1 static_autoscaler.go:298] Failed to get node infos for groups: Expected to get a onpremusercluster with id foo-user-cluster-gke-onprem-mgmt/foo-user-cluster
      

The cluster autoscaler pod can be found by running the following commands. 
    
    
      > kubectl --kubeconfig $USER_CLUSTER_KUBECONFIG -n kube-system \
       get pods | grep cluster-autoscaler
    cluster-autoscaler-5857c74586-txx2c                          4648017n    48076Ki    30s
      

  
**Workaround:** Disable autoscaling in all the node pools with `gkectl update cluster` until upgrading to a version with the fix  
Installation | 1.12.0-1.12.4, 1.13.0-1.13.3, 1.14.0 | 

### CIDR is not allowed in the IP block file

When users use CIDR in the IP block file, the config validation will fail with the following error: 
    
    
    - Validation Category: Config Check
        - [FAILURE] Config: AddressBlock for admin cluster spec is invalid: invalid IP:
    172.16.20.12/30
      

  
**Workaround:** Include individual IPs in the IP block file until upgrading to a version with the fix: 1.12.5, 1.13.4, 1.14.1+.  
Upgrades, Updates | 1.14.0-1.14.1 | 

### OS image type update in the admin-cluster.yaml doesn't wait for user control plane machines to be re-created

When [Updating control plane OS image type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-admin-node-image-type) in the admin-cluster.yaml, and if its corresponding user cluster was created with [`enableControlplaneV2` set to `true`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field), the user control plane machines might not finish their re-creation when the `gkectl` command finishes.   
**Workaround:** After the update is finished, keep waiting for the user control plane machines to also finish their re-creation by monitoring their node os image types using `kubectl --kubeconfig USER_KUBECONFIG get nodes -owide`. e.g. If updating from Ubuntu to COS, we should wait for all the control plane machines to completely change from Ubuntu to COS even after the update command is complete.   
Operation | 1.10, 1.11, 1.12, 1.13, 1.14.0 | 

### Pod create or delete errors due to Calico CNI service account auth token issue

An issue with Calico in Google Distributed Cloud 1.14.0 causes Pod creation and deletion to fail with the following error message in the output of `kubectl describe pods`:
    
    
      error getting ClusterInformation: connection is unauthorized: Unauthorized
      

This issue is only observed 24 hours after the cluster is created or upgraded to 1.14 using Calico. Admin clusters are always using Calico, while for user cluster there is a config field `enableDataPlaneV2` in user-cluster.yaml, if that field is set to `false`, or not specified, that means you are using Calico in user cluster. The nodes' `install-cni` container creates a kubeconfig with a token that is valid for 24 hours. This token needs to be periodically renewed by the `calico-node` Pod. The `calico-node` Pod is unable to renew the token as it doesn't have access to the directory that contains the kubeconfig file on the node.   
**Workaround:** This issue was fixed in Google Distributed Cloud version 1.14.1. Upgrade to this or a later version. If you can't upgrade right away, apply the following patch on the `calico-node` DaemonSet in your admin and user cluster:
    
    
      kubectl -n kube-system get daemonset calico-node \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG -o json \
        | jq '.spec.template.spec.containers[0].volumeMounts += [{"name":"cni-net-dir","mountPath":"/host/etc/cni/net.d"}]' \
        | kubectl apply --kubeconfig ADMIN_CLUSTER_KUBECONFIG -f -
    
      kubectl -n kube-system get daemonset calico-node \
        --kubeconfig USER_CLUSTER_KUBECONFIG -o json \
        | jq '.spec.template.spec.containers[0].volumeMounts += [{"name":"cni-net-dir","mountPath":"/host/etc/cni/net.d"}]' \
        | kubectl apply --kubeconfig USER_CLUSTER_KUBECONFIG -f -
      

Replace the following: 

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
  * `USER_CLUSTER_CONFIG_FILE`: the path of your user cluster configuration file.

  
Installation | 1.12.0-1.12.4, 1.13.0-1.13.3, 1.14.0 | 

### IP block validation fails when using CIDR

Cluster creation fails despite the user having the proper configuration. User sees creation failing due to the cluster not having enough IPs.   
**Workaround:** Split CIDR's into several smaller CIDR blocks, such as `10.0.0.0/30` becomes `10.0.0.0/31, 10.0.0.2/31`. As long as there are N+1 CIDR's, where N is the number of nodes in the cluster, this should suffice.   
Operation, Upgrades, Updates | 1.11.0 - 1.11.1, 1.10.0 - 1.10.4, 1.9.0 - 1.9.6 | 

###  Admin cluster backup does not include the always-on secrets encryption keys and configuration 

When the always-on secrets encryption feature is enabled along with cluster backup, the admin cluster backup fails to include the encryption keys and configuration required by always-on secrets encryption feature. As a result, repairing the admin master with this backup using `gkectl repair admin-master --restore-from-backup` causes the following error: 
    
    
    Validating admin master VM xxx ...
    Waiting for kube-apiserver to be accessible via LB VIP (timeout "8m0s")...  ERROR
    Failed to access kube-apiserver via LB VIP. Trying to fix the problem by rebooting the admin master
    Waiting for kube-apiserver to be accessible via LB VIP (timeout "13m0s")...  ERROR
    Failed to access kube-apiserver via LB VIP. Trying to fix the problem by rebooting the admin master
    Waiting for kube-apiserver to be accessible via LB VIP (timeout "18m0s")...  ERROR
    Failed to access kube-apiserver via LB VIP. Trying to fix the problem by rebooting the admin master

#### Workaround: 

  * Use the gkectl binary of the latest available patch version for the corresponding minor version to perform the admin cluster backup after critical cluster operations. For example, if the cluster is running a 1.10.2 version, use the 1.10.5 gkectl binary to perform a manual admin cluster backup as described in [Backup and Restore an admin cluster with gkectl.](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl#on-demand_backup)

  
Operation, Upgrades, Updates | 1.10+ | 

###  Recreating the admin master VM with a new boot disk (e.g., `gkectl repair admin-master`) will fail if the always-on secrets encryption feature is enabled using `gkectl update` command. 

If the [always-on secrets encryption feature](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/always-on-secrets-encryption) is not enabled at cluster creation, but enabled later using `gkectl update` operation then the `gkectl repair admin-master` fails to repair the admin cluster control plane node. It is recommend that always-on secrets encryption feature is enabled at cluster creation. There is no current mitigation.   
Upgrades, Updates | 1.10 | 

### Upgrading the first user cluster from 1.9 to 1.10 recreates nodes in other user clusters

Upgrading the first user cluster from 1.9 to 1.10 could recreate nodes in other user clusters under the same admin cluster. The recreation is performed in a rolling fashion. The `disk_label` was removed from `MachineTemplate.spec.template.spec.providerSpec.machineVariables`, which triggered an update on all `MachineDeployment`s unexpectedly.   
**Workaround:**

#### View workaround steps

  * Scale down the replica of `clusterapi-controllers` to 0 for all user clusters.
    
    kubectl scale --replicas=0 -n=USER_CLUSTER_NAME deployment/clusterapi-controllers --kubeconfig ADMIN_CLUSTER_KUBECONFIG

  * Upgrade each user cluster one by one.

  
Upgrades, Updates | 1.10.0 | 

### Docker restarts frequently after cluster upgrade

Upgrade user cluster to 1.10.0 might cause docker restart frequently. You can detect this issue by running `kubectl describe node NODE_NAME --kubeconfig USER_CLUSTER_KUBECONFIG` A node condition will show whether the docker restart frequently. Here is an example output:
    
    
    Normal   FrequentDockerRestart    41m (x2 over 141m)     systemd-monitor  Node condition FrequentDockerRestart is now: True, reason: FrequentDockerRestart

To understand the root cause, you need to ssh to the node that has the symptom and run commands like `sudo journalctl --utc -u docker` or `sudo journalctl -x`   
**Workaround:**

  * [Use containerd for the container runtime](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/using-containerd)
  * Upgrade the cluster to the latest version of 1.10

  
Upgrades, Updates | 1.11, 1.12 | 

### Self-deployed GMP components not preserved after upgrading to version 1.12

If you are using a Google Distributed Cloud version below 1.12, and have manually set up [Google-managed Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#config-mgd-collection) (GMP) components in the `gmp-system` namespace for your cluster, the components are not preserved when you upgrade to version 1.12.x. From version 1.12, GMP components in the `gmp-system` namespace and CRDs are [managed by `stackdriver` object](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/application-logging-monitoring), with the `enableGMPForApplications` flag set to `false` by default. If you manually deploy GMP components in the namespace prior to upgrading to 1.12, the resources will be deleted by `stackdriver`.   
**Workaround:**

  * Back up all existing [PodMonitoring](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.5.0/doc/api.md#podmonitoring) custom resources (CRs).
  * Upgrade all clusters to version 1.12, and [enable Managed Service for Prometheus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/application-logging-monitoring).
  * Redeploy PodMonitoring CRs.

  
Operation | 1.11, 1.12, 1.13.0 - 1.13.1 | 

### Missing ClusterAPI objects in cluster snapshot `system` scenario

In the `system` scenario, the cluster snapshot doesn't include any resources under the `default` namespace. However, some Kubernetes resources like Cluster API objects that are under this namespace contain useful debugging information. The cluster snapshot should include them.    
**Workaround:** You can manually run the following commands to collect the debugging information.
    
    
    export KUBECONFIG=USER_CLUSTER_KUBECONFIG
    kubectl get clusters.cluster.k8s.io -o yaml
    kubectl get controlplanes.cluster.k8s.io -o yaml
    kubectl get machineclasses.cluster.k8s.io -o yaml
    kubectl get machinedeployments.cluster.k8s.io -o yaml
    kubectl get machines.cluster.k8s.io -o yaml
    kubectl get machinesets.cluster.k8s.io -o yaml
    kubectl get services -o yaml
    kubectl describe clusters.cluster.k8s.io
    kubectl describe controlplanes.cluster.k8s.io
    kubectl describe machineclasses.cluster.k8s.io
    kubectl describe machinedeployments.cluster.k8s.io
    kubectl describe machines.cluster.k8s.io
    kubectl describe machinesets.cluster.k8s.io
    kubectl describe services

where: USER_CLUSTER_KUBECONFIG is the user cluster's kubeconfig file.  
Upgrades, Updates | 1.11.0-1.11.4, 1.12.0-1.12.3, 1.13.0-1.13.1 | 

### User cluster deletion stuck at node drain for vSAN setup

When deleting, updating or upgrading a user cluster, node drain may be stuck in the following scenarios:

  * The admin cluster has been using vSphere CSI driver on vSAN since version 1.12.x, and
  * There are no PVC/PV objects created by in-tree vSphere plugins in the admin and user cluster.

To identify the symptom, run the command below:
    
    
    kubectl logs clusterapi-controllers-POD_NAME_SUFFIX  --kubeconfig ADMIN_KUBECONFIG -n USER_CLUSTER_NAMESPACE

Here is a sample error message from the above command:
    
    
    E0920 20:27:43.086567 1 machine_controller.go:250] Error deleting machine object [MACHINE]; Failed to delete machine [MACHINE]: failed to detach disks from VM "[MACHINE]": failed to convert disk path "kubevols" to UUID path: failed to convert full path "ds:///vmfs/volumes/vsan:[UUID]/kubevols": ServerFaultCode: A general system error occurred: Invalid fault

`kubevols` is the default directory for vSphere in-tree driver. When there are no PVC/PV objects created, you may hit a bug that node drain will be stuck at finding `kubevols`, since the current implementation assumes that `kubevols` always exists.   
**Workaround:** Create the directory `kubevols` in the datastore where the node is created. This is defined in the `vCenter.datastore` field in the `user-cluster.yaml` or `admin-cluster.yaml` files.  
Configuration | 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13, 1.14 | 

### `Cluster Autoscaler ` clusterrolebinding and clusterrole are deleted after deleting a user cluster.

On user cluster deletion, the corresponding `clusterrole` and `clusterrolebinding` for cluster-autoscaler are also deleted. This affects all other user clusters on the same admin cluster with cluster autoscaler enabled. This is because the same clusterrole and clusterrolebinding are used for all cluster autoscaler pods within the same admin cluster. The symptoms are the following:

  * `cluster-autoscaler` logs
    
    kubectl logs --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n kube-system \
    cluster-autoscaler

where ADMIN_CLUSTER_KUBECONFIG is the admin cluster's kubeconfig file. Here is an example of error messages you might see: 
    
    2023-03-26T10:45:44.866600973Z W0326 10:45:44.866463       1 reflector.go:424] k8s.io/client-go/dynamic/dynamicinformer/informer.go:91: failed to list *unstructured.Unstructured: onpremuserclusters.onprem.cluster.gke.io is forbidden: User "..." cannot list resource "onpremuserclusters" in API group "onprem.cluster.gke.io" at the cluster scope
    2023-03-26T10:45:44.866646815Z E0326 10:45:44.866494       1 reflector.go:140] k8s.io/client-go/dynamic/dynamicinformer/informer.go:91: Failed to watch *unstructured.Unstructured: failed to list *unstructured.Unstructured: onpremuserclusters.onprem.cluster.gke.io is forbidden: User "..." cannot list resource "onpremuserclusters" in API group "onprem.cluster.gke.io" at the cluster scope


  
**Workaround:**

#### View workaround steps

Verify whether the clusterrole and clusterrolebinding are missing on the admin cluster 

  * kubectl get clusterrolebindings --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n kube-system | grep cluster-autoscaler

  * kubectl get clusterrole --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n kube-system | grep cluster-autoscaler


Apply the following clusterrole and clusterrolebinding to the admin cluster if they are missing. Add the service account subjects to the clusterrolebinding for each user cluster.

  * apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRole
        metadata:
          name: cluster-autoscaler
        rules:
        - apiGroups: ["cluster.k8s.io"]
          resources: ["clusters"]
          verbs: ["get", "list", "watch"]
        - apiGroups: ["cluster.k8s.io"]
          resources: ["machinesets","machinedeployments", "machinedeployments/scale","machines"]
          verbs: ["get", "list", "watch", "update", "patch"]
        - apiGroups: ["onprem.cluster.gke.io"]
          resources: ["onpremuserclusters"]
          verbs: ["get", "list", "watch"]
        - apiGroups:
          - coordination.k8s.io
          resources:
          - leases
          resourceNames: ["cluster-autoscaler"]
          verbs:
          - get
          - list
          - watch
          - create
          - update
          - patch
        - apiGroups:
          - ""
          resources:
          - nodes
          verbs: ["get", "list", "watch", "update", "patch"]
        - apiGroups:
          - ""
          resources:
          - pods
          verbs: ["get", "list", "watch"]
        - apiGroups:
          - ""
          resources:
          - pods/eviction
          verbs: ["create"]
        # read-only access to cluster state
        - apiGroups: [""]
          resources: ["services", "replicationcontrollers", "persistentvolumes", "persistentvolumeclaims"]
          verbs: ["get", "list", "watch"]
        - apiGroups: ["apps"]
          resources: ["daemonsets", "replicasets"]
          verbs: ["get", "list", "watch"]
        - apiGroups: ["apps"]
          resources: ["statefulsets"]
          verbs: ["get", "list", "watch"]
        - apiGroups: ["batch"]
          resources: ["jobs"]
          verbs: ["get", "list", "watch"]
        - apiGroups: ["policy"]
          resources: ["poddisruptionbudgets"]
          verbs: ["get", "list", "watch"]
        - apiGroups: ["storage.k8s.io"]
          resources: ["storageclasses", "csinodes"]
          verbs: ["get", "list", "watch"]
        # misc access
        - apiGroups: [""]
          resources: ["events"]
          verbs: ["create", "update", "patch"]
        - apiGroups: [""]
          resources: ["configmaps"]
          verbs: ["create"]
        - apiGroups: [""]
          resources: ["configmaps"]
          resourceNames: ["cluster-autoscaler-status"]
          verbs: ["get", "update", "patch", "delete"]

  * apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRoleBinding
        metadata:
          labels:
            k8s-app: cluster-autoscaler
          name: cluster-autoscaler
        roleRef:
          apiGroup: rbac.authorization.k8s.io
          kind: ClusterRole
          name: cluster-autoscaler
        subjects:
          - kind: ServiceAccount
          name: cluster-autoscaler
          namespace:  NAMESPACE_OF_USER_CLUSTER_1 
          - kind: ServiceAccount
          name: cluster-autoscaler
          namespace:  NAMESPACE_OF_USER_CLUSTER_2 
          ...


  
Configuration | 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13 | 

### admin cluster `cluster-health-controller` and `vsphere-metrics-exporter` do not work after deleting user cluster

On user cluster deletion, the corresponding `clusterrole` is also deleted, which results in auto repair and vsphere metrics exporter not working The symptoms are the following:

  * `cluster-health-controller` logs
    
    kubectl logs --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n kube-system \
    cluster-health-controller

where ADMIN_CLUSTER_KUBECONFIG is the admin cluster's kubeconfig file. Here is an example of error messages you might see: 
    
    error retrieving resource lock default/onprem-cluster-health-leader-election: configmaps "onprem-cluster-health-leader-election" is forbidden: User "system:serviceaccount:kube-system:cluster-health-controller" cannot get resource "configmaps" in API group "" in the namespace "default": RBAC: clusterrole.rbac.authorization.k8s.io "cluster-health-controller-role" not found

  * `vsphere-metrics-exporter` logs
    
    kubectl logs --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n kube-system \
    vsphere-metrics-exporter

where ADMIN_CLUSTER_KUBECONFIG is the admin cluster's kubeconfig file. Here is an example of error messages you might see: 
    
    vsphere-metrics-exporter/cmd/vsphere-metrics-exporter/main.go:68: Failed to watch *v1alpha1.Cluster: failed to list *v1alpha1.Cluster: clusters.cluster.k8s.io is forbidden: User "system:serviceaccount:kube-system:vsphere-metrics-exporter" cannot list resource "clusters" in API group "cluster.k8s.io" in the namespace "default"


  
**Workaround:**

#### View workaround steps

Apply the following yaml to the admin cluster

  * For vsphere-metrics-exporter
    
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: vsphere-metrics-exporter
    rules:
      - apiGroups:
          - cluster.k8s.io
        resources:
          - clusters
        verbs: [get, list, watch]
      - apiGroups:
          - ""
        resources:
          - nodes
        verbs: [get, list, watch]
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      labels:
        k8s-app: vsphere-metrics-exporter
      name: vsphere-metrics-exporter
      namespace: kube-system
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: vsphere-metrics-exporter
    subjects:
      - kind: ServiceAccount
        name: vsphere-metrics-exporter
        namespace: kube-system

  * For cluster-health-controller
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: cluster-health-controller-role
    rules:
    - apiGroups:
      - "*"
      resources:
      - "*"
      verbs:
      - "*"


  
Configuration | 1.12.1-1.12.3, 1.13.0-1.13.2 | 

### `gkectl check-config` fails at OS image validation

A known issue that could fail the `gkectl check-config` without running `gkectl prepare`. This is confusing because we suggest running the command before running `gkectl prepare` The symptom is that the `gkectl check-config` command will fail with the following error message:
    
    
    Validator result: {Status:FAILURE Reason:os images [OS_IMAGE_NAME] don't exist, please run `gkectl prepare` to upload os images. UnhealthyResources:[]}

  
**Workaround:** Option 1: run `gkectl prepare` to upload the missing OS images. Option 2: use `gkectl check-config --skip-validation-os-images` to skip the OS images validation.  
Upgrades, Updates | 1.11, 1.12, 1.13 | 

### `gkectl update admin/cluster` fails at updating anti affinity groups

A known issue that could fail the `gkectl update admin/cluster` when updating `anti affinity groups`. The symptom is that the `gkectl update` command will fail with the following error message:
    
    
    Waiting for machines to be re-deployed...  ERROR
    Exit with error:
    Failed to update the cluster: timed out waiting for the condition

  
**Workaround:**

#### View workaround steps

For the update to take effect, the machines need to be recreated `after` the failed update. **For admin cluster update, user master and admin addon nodes need to be recreated** **For user cluster update, user worker nodes need to be recreated**

#### To recreate user worker nodes

**Option 1**  
In the 1.11 version of the documentation, follow [update a node pool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/managing-node-pools#update_a_node_pool) and change the cpu or memory to trigger a rolling recreation of the nodes. **Option 2**  
Use kubectl delete to recreate the machines one at a time
    
    
    kubectl delete machines MACHINE_NAME --kubeconfig USER_KUBECONFIG

#### To recreate user master nodes

**Option 1**  
In the 1.11 version of the documentation, follow [resize control plane](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/how-to/resizing-the-control-plane-node-for-user-cluster) and change the cpu or memory to trigger a rolling recreation of the nodes. **Option 2**  
Use kubectl delete to recreate the machines one at a time
    
    
    kubectl delete machines MACHINE_NAME --kubeconfig ADMIN_KUBECONFIG

#### To recreate admin addon nodes

Use kubectl delete to recreate the machines one at a time
    
    
    kubectl delete machines MACHINE_NAME --kubeconfig ADMIN_KUBECONFIG  
  
Installation, Upgrades, Updates | 1.13.0-1.13.8, 1.14.0-1.14.4, 1.15.0 | 

### Nodes fail to register if configured hostname contains a period

Node registration fails during cluster creation, upgrade, update and node auto repair, when `ipMode.type` is `static` and the configured hostname in the [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) contains one or more periods. In this case, Certificate Signing Requests (CSR) for a node are not automatically approved. To see pending CSRs for a node, run the following command:
    
    
    kubectl get csr -A -o wide

Check the following logs for error messages:

  * View the logs in the admin cluster for the `clusterapi-controller-manager` container in the `clusterapi-controllers` Pod: 
        
        kubectl logs clusterapi-controllers-POD_NAME \
            -c clusterapi-controller-manager -n kube-system \
            --kubeconfig ADMIN_CLUSTER_KUBECONFIG

  * To view the same logs in the user cluster, run the following command: 
        
        kubectl logs clusterapi-controllers-POD_NAME \
            -c clusterapi-controller-manager -n USER_CLUSTER_NAME \
            --kubeconfig ADMIN_CLUSTER_KUBECONFIG

where: 
    * ADMIN_CLUSTER_KUBECONFIG is the admin cluster's kubeconfig file.
    * USER_CLUSTER_NAME is the name of the user cluster.
Here is an example of error messages you might see: `"msg"="failed to validate token id" "error"="failed to find machine for node node-worker-vm-1" "validate"="csr-5jpx9"`
  * View the `kubelet` logs on the problematic node: 
        
        journalctl --u kubelet

Here is an example of error messages you might see: `"Error getting node" err="node \"node-worker-vm-1\" not found"`

If you specify a domain name in the hostname field of an IP block file, any characters following the first period will be ignored. For example, if you specify the hostname as `bob-vm-1.bank.plc`, the VM hostname and node name will be set to `bob-vm-1`. When node ID verification is enabled, the CSR approver compares the node name with the hostname in the Machine spec, and fails to reconcile the name. The approver rejects the CSR, and the node fails to bootstrap.   
**Workaround:** **User cluster** Disable node ID verification by completing the following steps:

  1. Add the following fields in your user cluster configuration file: 
         
         disableNodeIDVerification: true
         disableNodeIDVerificationCSRSigning: true

  2. Save the file, and update the user cluster by running the following command: 
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG_FILE

Replace the following: 
     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.
     * `USER_CLUSTER_CONFIG_FILE`: the path of your user cluster configuration file.

**Admin cluster**

  1. Open the `OnPremAdminCluster` custom resource for editing: 
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             edit onpremadmincluster -n kube-system

  2. Add the following annotation to the custom resource: 
         
         features.onprem.cluster.gke.io/disable-node-id-verification: enabled

  3. Edit the `kube-controller-manager` manifest in the admin cluster control plane: 
     1. [SSH into the admin cluster control plane node](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ssh-cluster-node#admin).
     2. Open the `kube-controller-manager` manifest for editing: 
            
            sudo vi /etc/kubernetes/manifests/kube-controller-manager.yaml

     3. Find the list of `controllers`: 
            
            --controllers=*,bootstrapsigner,tokencleaner,-csrapproving,-csrsigning

     4. Update this section as shown below: 
            
            --controllers=*,bootstrapsigner,tokencleaner

  4. Open the Deployment Cluster API controller for editing: 
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             edit deployment clusterapi-controllers -n kube-system

  5. Change the values of `node-id-verification-enabled` and `node-id-verification-csr-signing-enabled` to `false`: 
         
         --node-id-verification-enabled=false
         --node-id-verification-csr-signing-enabled=false


  
Installation, Upgrades, Updates | 1.11.0-1.11.4 | 

### Admin control plane machine startup failure caused by private registry certificate bundle

The admin cluster creation/upgrade is stuck at the following log forever and eventually times out:
    
    
    Waiting for Machine gke-admin-master-xxxx to become ready...
    

In the 1.11 version of the documentation, the Cluster API controller log in the [ external cluster snapshot](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.11/troubleshoot-cluster-creation-upgrade#snapshot_is_created_automatically_when_admin_cluster_creation_or_upgrade_fails) includes the following log:
    
    
    Invalid value 'XXXX' specified for property startup-data
    

Here is an example file path for the Cluster API controller log:
    
    
    kubectlCommands/kubectl_logs_clusterapi-controllers-c4fbb45f-6q6g6_--container_vsphere-controller-manager_--kubeconfig_.home.ubuntu..kube.kind-config-gkectl_--request-timeout_30s_--namespace_kube-system_--timestamps
        VMware has a 64k vApp property size limit. In the identified versions,
        the data passed via vApp property is close to the limit. When the private
        registry certificate contains a certificate bundle, it may cause the final
        data to exceed the 64k limit.
          
    **Workaround:**
        Only include the required certificates in the private registry
        certificate file configured in privateRegistry.caCertPath in
        the admin cluster config file.
        Or upgrade to a version with the fix when available.
        
  
Networking | 1.10, 1.11.0-1.11.3, 1.12.0-1.12.2, 1.13.0 | 

### `NetworkGatewayNodes` marked unhealthy from concurrent status update conflict

In `networkgatewaygroups.status.nodes`, some nodes switch between `NotHealthy` and `Up`. Logs for the `ang-daemon` Pod running on that node reveal repeated errors: 
    
    
    2022-09-16T21:50:59.696Z ERROR ANGd Failed to report status {"angNode": "kube-system/my-node", "error": "updating Node CR status: sending Node CR update: Operation cannot be fulfilled on networkgatewaynodes.networking.gke.io \"my-node\": the object has been modified; please apply your changes to the latest version and try again"}
    

The `NotHealthy` status prevents the controller from assigning additional floating IPs to the node. This can result in higher burden on other nodes or a lack of redundancy for high availability. Dataplane activity is otherwise not affected. Contention on the `networkgatewaygroup` object causes some status updates to fail due to a fault in retry handling. If too many status updates fail, `ang-controller-manager` sees the node as past its heartbeat time limit and marks the node `NotHealthy`. The fault in retry handling has been fixed in later versions.   
**Workaround:** Upgrade to a fixed version, when available.  
Upgrades, Updates | 1.12.0-1.12.2, 1.13.0 | 

### Race condition blocks machine object deletion during and update or upgrade

A known issue that could cause the cluster upgrade or update to be stuck at waiting for the old machine object to be deleted. This is because the finalizer cannot be removed from the machine object. This affects any rolling update operation for node pools. The symptom is that the `gkectl` command times out with the following error message:
    
    
    E0821 18:28:02.546121   61942 console.go:87] Exit with error:
    E0821 18:28:02.546184   61942 console.go:87] error: timed out waiting for the condition, message: Node pool "pool-1" is not ready: ready condition is not true: CreateOrUpdateNodePool: 1/3 replicas are updated
    Check the status of OnPremUserCluster 'cluster-1-gke-onprem-mgmt/cluster-1' and the logs of pod 'kube-system/onprem-user-cluster-controller' for more detailed debugging information.
    

In `clusterapi-controller` Pod logs, the errors are like below:
    
    
    $ kubectl logs clusterapi-controllers-[POD_NAME_SUFFIX] -n cluster-1
        -c vsphere-controller-manager --kubeconfig [ADMIN_KUBECONFIG]
        | grep "Error removing finalizer from machine object"
    [...]
    E0821 23:19:45.114993       1 machine_controller.go:269] Error removing finalizer from machine object cluster-1-pool-7cbc496597-t5d5p; Operation cannot be fulfilled on machines.cluster.k8s.io "cluster-1-pool-7cbc496597-t5d5p": the object has been modified; please apply your changes to the latest version and try again
    

The error repeats for the same machine for several minutes for successful runs even without this issue, for most of the time it can go through quickly, but for some rare cases it can be stuck at this race condition for several hours. The issue is that the underlying VM is already deleted in vCenter, but the corresponding machine object cannot be removed, which is stuck at the finalizer removal due to very frequent updates from other controllers. This can cause the `gkectl` command to timeout, but the controller keeps reconciling the cluster so the upgrade or update process eventually completes.   
**Workaround:** We have prepared several different mitigation options for this issue, which depends on your environment and requirements.

  * Option 1: Wait for the upgrade to eventually complete by itself.  
  
Based on the analysis and reproduction in your environment, the upgrade can eventually finish by itself without any manual intervention. The caveat of this option is that it's uncertain how long it will take for the finalizer removal to go through for each machine object. It can go through immediately if lucky enough, or it could last for several hours if the machineset controller reconcile is too fast and the machine controller never gets a chance to remove the finalizer in between the reconciliations.  
  
The good thing is that this option doesn't need any action from your side, and the workloads won't be disrupted. It just needs a longer time for the upgrade to finish.
  * Option 2: Apply auto repair annotation to all the old machine objects.  
  
The machineset controller will filter out the machines that have the auto repair annotation and deletion timestamp being non zero, and won't keep issuing delete calls on those machines, this can help avoid the race condition.  
  
The downside is that the pods on the machines will be deleted directly instead of evicted, which means it won't respect the PDB configuration, this might potentially cause downtime for your workloads.  
  
The command for getting all machine names: 
        
        kubectl --kubeconfig CLUSTER_KUBECONFIG get machines

The command for applying auto repair annotation for each machine: 
        
        kubectl annotate --kubeconfig CLUSTER_KUBECONFIG \
            machine MACHINE_NAME \
            onprem.cluster.gke.io/repair-machine=true


If you encounter this issue and the upgrade or update still can't complete after a long time, [contact our support team](https://cloud.google.com/anthos/docs/support/getting-support) for mitigations.  
Installation, Upgrades, Updates | 1.10.2, 1.11, 1.12, 1.13 | 

### `gkectl` prepare OS image validation preflight failure

`gkectl prepare` command failed with:
    
    
    - Validation Category: OS Images
        - [FAILURE] Admin cluster OS images exist: os images [os_image_name] don't exist, please run `gkectl prepare` to upload os images.
    

The preflight checks of `gkectl prepare` included an incorrect validation.   
**Workaround:** Run the same command with an additional flag `--skip-validation-os-images`.  
Installation | 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13 | 

### vCenter URL with `https://` or `http://` prefix may cause cluster startup failure

Admin cluster creation failed with:
    
    
    Exit with error:
    Failed to create root cluster: unable to apply admin base bundle to external cluster: error: timed out waiting for the condition, message:
    Failed to apply external bundle components: failed to apply bundle objects from admin-vsphere-credentials-secret 1.x.y-gke.z to cluster external: Secret "vsphere-dynamic-credentials" is invalid:
    [data[https://xxx.xxx.xxx.username]: Invalid value: "https://xxx.xxx.xxx.username": a valid config key must consist of alphanumeric characters, '-', '_' or '.'
    (e.g. 'key.name', or 'KEY_NAME', or 'key-name', regex used for validation is '[-._a-zA-Z0-9]+'), data[https://xxx.xxx.xxx.password]:
    Invalid value: "https://xxx.xxx.xxx.password": a valid config key must consist of alphanumeric characters, '-', '_' or '.'
    (e.g. 'key.name', or 'KEY_NAME', or 'key-name', regex used for validation is '[-._a-zA-Z0-9]+')]
    

The URL is used as part of a Secret key, which doesn't support "/" or ":".   
**Workaround:** Remove `https://` or `http://` prefix from the `vCenter.Address` field in the admin cluster or user cluster config yaml.  
Installation, Upgrades, Updates | 1.10, 1.11, 1.12, 1.13 | 

### `gkectl prepare` panic on `util.CheckFileExists`

`gkectl prepare` can panic with the following stacktrace:
    
    
    panic: runtime error: invalid memory address or nil pointer dereference [signal SIGSEGV: segmentation violation code=0x1 addr=0x18 pc=0xde0dfa]
    
    goroutine 1 [running]:
    gke-internal.googlesource.com/syllogi/cluster-management/pkg/util.CheckFileExists(0xc001602210, 0x2b, 0xc001602210, 0x2b) pkg/util/util.go:226 +0x9a
    gke-internal.googlesource.com/syllogi/cluster-management/gkectl/pkg/config/util.SetCertsForPrivateRegistry(0xc000053d70, 0x10, 0xc000f06f00, 0x4b4, 0x1, 0xc00015b400)gkectl/pkg/config/util/utils.go:75 +0x85
    ...
    

The issue is that `gkectl prepare` created the private registry certificate directory with a wrong permission.   
**Workaround:** To fix this issue, please run the following commands on the admin workstation:
    
    
    sudo mkdir -p /etc/docker/certs.d/PRIVATE_REGISTRY_ADDRESS
    sudo chmod 0755 /etc/docker/certs.d/PRIVATE_REGISTRY_ADDRESS  
  
Upgrades, Updates | 1.10, 1.11, 1.12, 1.13 | 

### `gkectl repair admin-master` and resumable admin upgrade do not work together

After a failed admin cluster upgrade attempt, don't run `gkectl repair admin-master`. Doing so may cause subsequent admin upgrade attempts to fail with issues such as admin master power on failure or the VM being inaccessible.   
**Workaround:** If you've already encountered this failure scenario, [contact support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support).  
Upgrades, Updates | 1.10, 1.11 | 

### Resumed admin cluster upgrade can lead to missing admin control plane VM template

If the admin control plane machine isn't recreated after a resumed admin cluster upgrade attempt, the admin control plane VM template is deleted. The admin control plane VM template is the template of the admin master that is used to recover the control plane machine with [`gkectl repair admin-master`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/repair-admin-control-plane).   
**Workaround:** The admin control plane VM template will be regenerated during the next admin cluster upgrade.  
Operating system | 1.12, 1.13 | 

### cgroup v2 could affect workloads

In version 1.12.0, cgroup v2 (unified) is enabled by default for Container Optimized OS (COS) nodes. This could potentially cause instability for your workloads in a COS cluster.   
**Workaround:** We switched back to cgroup v1 (hybrid) in version 1.12.1. If you are using COS nodes, we recommend that you upgrade to version 1.12.1 as soon as it is released.  
Identity | 1.10, 1.11, 1.12, 1.13 | 

### ClientConfig custom resource

`gkectl update` reverts any manual changes that you have made to the ClientConfig custom resource.   
**Workaround:** We strongly recommend that you back up the ClientConfig resource after every manual change.  
Installation | 1.10, 1.11, 1.12, 1.13 | 

### `gkectl check-config` validation fails: can't find F5 BIG-IP partitions

Validation fails because F5 BIG-IP partitions can't be found, even though they exist. An issue with the F5 BIG-IP API can cause validation to fail.   
**Workaround:** Try running `gkectl check-config` again.  
Installation | 1.12 | 

### User cluster installation failed because of cert-manager/ca-injector's leader election issue

You might see an installation failure due to `cert-manager-cainjector` in crashloop, when the apiserver/etcd is slow:
    
    
    # These are logs from `cert-manager-cainjector`, from the command
    # `kubectl --kubeconfig USER_CLUSTER_KUBECONFIG -n kube-system
      cert-manager-cainjector-xxx`
    
    I0923 16:19:27.911174       1 leaderelection.go:278] failed to renew lease kube-system/cert-manager-cainjector-leader-election: timed out waiting for the condition
    
    E0923 16:19:27.911110       1 leaderelection.go:321] error retrieving resource lock kube-system/cert-manager-cainjector-leader-election-core:
      Get "https://10.96.0.1:443/api/v1/namespaces/kube-system/configmaps/cert-manager-cainjector-leader-election-core": context deadline exceeded
    
    I0923 16:19:27.911593       1 leaderelection.go:278] failed to renew lease kube-system/cert-manager-cainjector-leader-election-core: timed out waiting for the condition
    
    E0923 16:19:27.911629       1 start.go:163] cert-manager/ca-injector "msg"="error running core-only manager" "error"="leader election lost"
    

  
**Workaround:**

#### View workaround steps

Run the following commands to mitigate the problem. First scale down the `monitoring-operator` so it won't revert the changes to the `cert-manager` Deployment:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG -n kube-system \
        scale deployment monitoring-operator --replicas=0

Edit the `cert-manager-cainjector` Deployment to disable leader election, because we only have one replica running. It isn't required for a single replica:
    
    
    # Add a command line flag for cainjector: `--leader-elect=false`
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG edit \
        -n kube-system deployment cert-manager-cainjector

The relevant YAML snippet for `cert-manager-cainjector` deployment should looks like the following example:
    
    
    ...
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: cert-manager-cainjector
      namespace: kube-system
    ...
    spec:
      ...
      template:
        ...
        spec:
          ...
          containers:
          - name: cert-manager
            image: "gcr.io/gke-on-prem-staging/cert-manager-cainjector:v1.0.3-gke.0"
            args:
            ...
            - --leader-elect=false
    ...
    

Keep `monitoring-operator` replicas at 0 as a mitigation until the installation is finished. Otherwise it will revert the change. After the installation is finished and the cluster is up and running, turn on the `monitoring-operator` for day-2 operations:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG -n kube-system \
        scale deployment monitoring-operator --replicas=1

After each upgrade, the changes are reverted. Perform the same steps again to mitigate the issue until this is fixed in a future release.  
VMware | 1.10, 1.11, 1.12, 1.13 | 

### Restarting or upgrading vCenter for versions lower than 7.0U2

If the vCenter, for versions lower than 7.0U2, is restarted, after an upgrade or otherwise, the network name in vm information from vCenter is incorrect, and results in the machine being in an `Unavailable` state. This eventually leads to the nodes being auto-repaired to create new ones. [Related govmomi bug](https://github.com/vmware/govmomi/issues/2552).   
**Workaround:** This workaround is provided by VMware support:

  1. The issue is fixed in vCenter versions 7.0U2 and above.
  2. For lower versions, right-click the host, and then select **Connection > Disconnect**. Next, reconnect, which forces an update of the VM's portgroup.

  
Operating system | 1.10, 1.11, 1.12, 1.13 | 

### SSH connection closed by remote host

For Google Distributed Cloud version 1.7.2 and above, the Ubuntu OS images are hardened with [ CIS L1 Server Benchmark](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/cis-ubuntu-benchmark). To meet the CIS rule "5.2.16 Ensure SSH Idle Timeout Interval is configured", `/etc/ssh/sshd_config` has the following settings:
    
    
    ClientAliveInterval 300
    ClientAliveCountMax 0
    

The purpose of these settings is to terminate a client session after 5 minutes of idle time. However, the `ClientAliveCountMax 0` value causes unexpected behavior. When you use the ssh session on the admin workstation, or a cluster node, the SSH connection might be disconnected even your ssh client is not idle, such as when running a time-consuming command, and your command could get terminated with the following message:
    
    
    Connection to [IP] closed by remote host.
    Connection to [IP] closed.
    

  
**Workaround:** You can either:

  * Use `nohup` to prevent your command being terminated on SSH disconnection, 
        
        nohup gkectl upgrade admin --config admin-cluster.yaml \
            --kubeconfig kubeconfig

  * Update the `sshd_config` to use a non-zero `ClientAliveCountMax` value. The CIS rule recommends to use a value less than 3: 
        
        sudo sed -i 's/ClientAliveCountMax 0/ClientAliveCountMax 1/g' \
            /etc/ssh/sshd_config
        sudo systemctl restart sshd


Make sure you reconnect your SSH session.  
Installation | 1.10, 1.11, 1.12, 1.13 | 

### Conflicting `cert-manager` installation

In 1.13 releases, `monitoring-operator` will install cert-manager in the `cert-manager` namespace. If for certain reasons, you need to install your own cert-manager, follow the following instructions to avoid conflicts: You only need to apply this work around once for each cluster, and the changes will be preserved across cluster upgrade. Note: One common symptom of installing your own cert-manager is that the `cert-manager` version or image (for example v1.7.2) may revert back to its older version. This is caused by `monitoring-operator` trying to reconcile the `cert-manager`, and reverting the version in the process.   
**Workaround:** Avoid conflicts during upgrade 

  1. Uninstall your version of `cert-manager`. If you defined your own resources, you may want to [backup ](https://cert-manager.io/docs/tutorials/backup/#backup) them.
  2. Perform the [upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).
  3. Follow the following instructions to restore your own `cert-manager`.

**Restore your own cert-manager in user clusters**

  * Scale the `monitoring-operator` Deployment to 0: 
        
        kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
            -n USER_CLUSTER_NAME \
            scale deployment monitoring-operator --replicas=0

  * Scale the `cert-manager` deployments managed by `monitoring-operator` to 0: 
        
        kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
            -n cert-manager scale deployment cert-manager --replicas=0
        kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
            -n cert-manager scale deployment cert-manager-cainjector\
            --replicas=0
        kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
            -n cert-manager scale deployment cert-manager-webhook --replicas=0

  * Reinstall your version of `cert-manager`. [Restore your customized resources](https://cert-manager.io/docs/tutorials/backup/#restore) if you have.
  * You can skip this step if you are using [ upstream default cert-manager installation](https://cert-manager.io/docs/installation/#default-static-install), or you are sure your cert-manager is installed in the `cert-manager` namespace. Otherwise, copy the `metrics-ca` cert-manager.io/v1 Certificate and the `metrics-pki.cluster.local` Issuer resources from `cert-manager` to the cluster resource namespace of your installed cert-manager. 
        
        relevant_fields='
        {
          apiVersion: .apiVersion,
          kind: .kind,
          metadata: {
            name: .metadata.name,
            namespace: "YOUR_INSTALLED_CERT_MANAGER_NAMESPACE"
          },
          spec: .spec
        }
        '
        f1=$(mktemp)
        f2=$(mktemp)
        kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
            get issuer -n cert-manager metrics-pki.cluster.local -o json \
            | jq "${relevant_fields}" > $f1
        kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
            get certificate -n cert-manager metrics-ca -o json \
            | jq "${relevant_fields}" > $f2
        kubectl apply --kubeconfig USER_CLUSTER_KUBECONFIG -f $f1
        kubectl apply --kubeconfig USER_CLUSTER_KUBECONFIG -f $f2


**Restore your own cert-manager in admin clusters** In general, you shouldn't need to re-install cert-manager in admin clusters because admin clusters only run Google Distributed Cloud control plane workloads. In the rare cases that you also need to install your own cert-manager in admin clusters, please follow the following instructions to avoid conflicts. Please note, if you are an Apigee customer and you only need cert-manager for Apigee, you do not need to run the admin cluster commands.

  * Scale the `monitoring-operator` deployment to 0. 
        
        kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
            -n kube-system scale deployment monitoring-operator --replicas=0

  * Scale the `cert-manager` deployments managed by `monitoring-operator` to 0. 
        
        kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
            -n cert-manager scale deployment cert-manager \
            --replicas=0
        
        kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             -n cert-manager scale deployment cert-manager-cainjector \
             --replicas=0
        
        kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
            -n cert-manager scale deployment cert-manager-webhook \
            --replicas=0

  * Reinstall your version of `cert-manager`. [Restore your customized resources](https://cert-manager.io/docs/tutorials/backup/#restore) if you have.
  * You can skip this step if you are using [ upstream default cert-manager installation](https://cert-manager.io/docs/installation/#default-static-install), or you are sure your cert-manager is installed in the `cert-manager` namespace. Otherwise, copy the `metrics-ca` cert-manager.io/v1 Certificate and the `metrics-pki.cluster.local` Issuer resources from `cert-manager` to the cluster resource namespace of your installed cert-manager. 
        
        relevant_fields='
        {
          apiVersion: .apiVersion,
          kind: .kind,
          metadata: {
            name: .metadata.name,
            namespace: "YOUR_INSTALLED_CERT_MANAGER_NAMESPACE"
          },
          spec: .spec
        }
        '
        f3=$(mktemp)
        f4=$(mktemp)
        kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \n
            get issuer -n cert-manager metrics-pki.cluster.local -o json \
            | jq "${relevant_fields}" > $f3
        kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
            get certificate -n cert-manager metrics-ca -o json \
            | jq "${relevant_fields}" > $f4
        kubectl apply --kubeconfig ADMIN_CLUSTER_KUBECONFIG -f $f3
        kubectl apply --kubeconfig ADMIN_CLUSTER_KUBECONFIG -f $f4


  
Operating system | 1.10, 1.11, 1.12, 1.13 | 

### False positives in docker, containerd, and runc vulnerability scanning 

The Docker, containerd, and runc in the Ubuntu OS images shipped with Google Distributed Cloud are pinned to special versions using [Ubuntu PPA](https://launchpad.net/ubuntu/+ppas). This ensures that any container runtime changes will be qualified by Google Distributed Cloud before each release. However, the special versions are unknown to the [Ubuntu CVE Tracker](https://wiki.ubuntu.com/SecurityTeam/UbuntuCVETracker), which is used as the vulnerability feeds by various CVE scanning tools. Therefore, you will see false positives in Docker, containerd, and runc vulnerability scanning results. For example, you might see the following false positives from your CVE scanning results. These CVEs are already fixed in the latest patch versions of Google Distributed Cloud.

  * [ CVE-2019-16884](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16884)
  * [ CVE-2019-19921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19921)
  * [ CVE-2020-15157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15157)
  * [ CVE-2020-15257](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15257)

Refer to the [release notes]](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/release-notes) for any CVE fixes.   
**Workaround:** Canonical is aware of this issue, and the fix is tracked at [ https://github.com/canonical/sec-cvescan/issues/73](https://github.com/canonical/sec-cvescan/issues/73).  
Upgrades, Updates | 1.10, 1.11, 1.12, 1.13 | 

### Network connection between admin and user cluster might be unavailable for a short time during non-HA cluster upgrade

If you are upgrading non-HA clusters from 1.9 to 1.10, you might notice that the `kubectl exec`, `kubectl log` and webhook against user clusters might be unavailable for a short time. This downtime can be up to one minute. This happens because the incoming request (kubectl exec, kubectl log and webhook) is handled by kube-apiserver for the user cluster. User kube-apiserver is a [ Statefulset](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). In a non-HA cluster, there is only one replica for the Statefulset. So during upgrade, there is a chance that the old kube-apiserver is unavailable while the new kube-apiserver is not yet ready.   
**Workaround:** This downtime only happens during upgrade process. If you want a shorter downtime during upgrade, we recommend you to switch to [HA clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/high-availability-disaster-recovery).  
Installation, Upgrades, Updates | 1.10, 1.11, 1.12, 1.13 | 

### Konnectivity readiness check failed in HA cluster diagnose after cluster creation or upgrade

If you are creating or upgrading an HA cluster and notice konnectivity readiness check failed in cluster diagnose, in most cases it will not affect the functionality of Google Distributed Cloud (kubectl exec, kubectl log and webhook). This happens because sometimes one or two of the konnectivity replicas might be unready for a period of time due to unstable networking or other issues.   
**Workaround:** The konnectivity will recover by itself. Wait for 30 minutes to 1 hour and rerun cluster diagnose.  
Operating system | 1.7, 1.8, 1.9, 1.10, 1.11 | 

### `/etc/cron.daily/aide` CPU and memory spike issue

Starting from Google Distributed Cloud version 1.7.2, the Ubuntu OS images are hardened with [CIS L1 Server Benchmark](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/cis-ubuntu-benchmark). As a result, the cron script `/etc/cron.daily/aide` has been installed so that an `aide` check is scheduled so as to ensure that the CIS L1 Server rule "1.4.2 Ensure filesystem integrity is regularly checked" is followed. The cron job runs daily at 6:25 AM UTC. Depending on the number of files on the filesystem, you may experience CPU and memory usage spikes around that time that are caused by this `aide` process.   
**Workaround:** If the spikes are affecting your workload, you can disable the daily cron job:
    
    
    sudo chmod -x /etc/cron.daily/aide  
  
Networking | 1.10, 1.11, 1.12, 1.13 | 

### Load balancers and NSX-T stateful distributed firewall rules interact unpredictably

When deploying Google Distributed Cloud version 1.9 or later, when the deployment has the Seesaw bundled load balancer in an environment that uses NSX-T stateful distributed firewall rules, `stackdriver-operator` might fail to create `gke-metrics-agent-conf` ConfigMap and cause `gke-connect-agent` Pods to be in a crash loop. The underlying issue is that the stateful NSX-T distributed firewall rules terminate the connection from a client to the user cluster API server through the Seesaw load balancer because Seesaw uses asymmetric connection flows. The integration issues with NSX-T distributed firewall rules affect all Google Distributed Cloud releases that use Seesaw. You might see similar connection problems on your own applications when they create large Kubernetes objects whose sizes are bigger than 32K.   
**Workaround:** In the 1.13 version of the documentation, follow [ these instructions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.13/how-to/bundled-load-balance#configuring_stateless_nsx-t_distributed_firewall_policies_for_use_with_seesaw_load_balancer) to disable NSX-T distributed firewall rules, or to use stateless distributed firewall rules for Seesaw VMs. If your clusters use a manual load balancer, follow [ these instructions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance#resetting_connections_to_failed_nodes_recommended) to configure your load balancer to reset client connections when it detects a backend node failure. Without this configuration, clients of the Kubernetes API server might stop responding for several minutes when a server instance goes down.  
Logging and monitoring | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15 | 

### Unexpected monitoring billing 

For Google Distributed Cloud versions 1.10 to 1.15, some customers have found unexpectedly high billing for `Metrics volume` on the **Billing** page. This issue affects you only when all of the following circumstances apply:

  * Application logging and monitoring is enabled (`enableStackdriverForApplications=true`) 
  * Application Pods have the `prometheus.io/scrap=true` annotation. (Installing Cloud Service Mesh can also add this annotation.)

To confirm whether you are affected by this issue, [list your user-defined metrics](https://docs.cloud.google.com/monitoring/docs/metrics-management#view-metrics). If you see billing for unwanted metrics with `external.googleapis.com/prometheus` name prefix and also see `enableStackdriverForApplications` set to true in the response of `kubectl -n kube-system get stackdriver stackdriver -o yaml`, then this issue applies to you.   
**Workaround** If you are affected by this issue, we recommend that you upgrade your clusters to version 1.12 or above, stop using the `enableStackdriverForApplications` flag, and switch to new application monitoring solution [managed-service-for-prometheus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/application-logging-monitoring#enabling_managed_service_for_prometheus_for_user_applications) that no longer relies on the `prometheus.io/scrap=true` annotation. With the new solution, you can also control logs and metrics collection separately for your applications, with the `enableCloudLoggingForApplications` and `enableGMPForApplications` flag, respectively. To stop using the `enableStackdriverForApplications` flag, open the `stackdriver` object for editing:
    
    
    kubectl --kubeconfig=USER_CLUSTER_KUBECONFIG --namespace kube-system edit stackdriver stackdriver
    

Remove the `enableStackdriverForApplications: true` line, save and close the editor. If you can't switch away from the annotation based metrics collection, use the following steps:

  1. Find the source Pods and Services that have the unwanted billed metrics. 
         
         kubectl --kubeconfig KUBECONFIG \
           get pods -A -o yaml | grep 'prometheus.io/scrape: "true"'
         kubectl --kubeconfig KUBECONFIG get \
           services -A -o yaml | grep 'prometheus.io/scrape: "true"'

  2. Remove the `prometheus.io/scrap=true` annotation from the Pod or Service. If the annotation is added by Cloud Service Mesh, consider [configuring Cloud Service Mesh without the Prometheus option](https://docs.cloud.google.com/service-mesh/docs/unified-install/install-anthos-service-mesh#install_dashboards), or [turning off the Istio Metrics Merging feature](https://istio.io/latest/docs/ops/integrations/prometheus/#option-1-metrics-merging).

  
Installation | 1.11, 1.12, 1.13 | 

### Installer fails when creating vSphere datadisk 

The Google Distributed Cloud installer can fail if custom roles are bound at the wrong permissions level. When the role binding is incorrect, creating a vSphere datadisk with `govc` hangs and the disk is created with a size equal to 0. To fix the issue, you should bind the custom role at the vSphere vCenter level (root).   
**Workaround:** If you want to bind the custom role at the DC level (or lower than root), you also need to bind the read-only role to the user at the root vCenter level. For more information on role creation, see [ vCenter user account privileges](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements#vcenter-user-account-privileges).  
Logging and monitoring | 1.9.0-1.9.4, 1.10.0-1.10.1 | 

### High network traffic to monitoring.googleapis.com 

You might see high network traffic to `monitoring.googleapis.com`, even in a new cluster that has no user workloads. This issue affects version 1.10.0-1.10.1 and version 1.9.0-1.9.4. This issue is fixed in version 1.10.2 and 1.9.5.   
**Workaround:**

#### View workaround steps

Upgrade to version 1.10.2/1.9.5 or later. To mitigate this issue for an earlier version:

  1. Scale down `stackdriver-operator`: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
             --namespace kube-system \
             scale deployment stackdriver-operator --replicas=0

Replace USER_CLUSTER_KUBECONFIG with the path of the user cluster kubeconfig file.
  2. Open the `gke-metrics-agent-conf` ConfigMap for editing: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
             --namespace kube-system \
             edit configmap gke-metrics-agent-conf

  3. Increase the probe interval from 0.1 seconds to 13 seconds: 
         
         processors:
             disk_buffer/metrics:
               backend_endpoint: https://monitoring.googleapis.com:443
               buffer_dir: /metrics-data/nsq-metrics-metrics
               probe_interval: 13s
               retention_size_mib: 6144
           disk_buffer/self:
               backend_endpoint: https://monitoring.googleapis.com:443
               buffer_dir: /metrics-data/nsq-metrics-self
               probe_interval: 13s
               retention_size_mib: 200
             disk_buffer/uptime:
               backend_endpoint: https://monitoring.googleapis.com:443
               buffer_dir: /metrics-data/nsq-metrics-uptime
               probe_interval: 13s
               retention_size_mib: 200

  4. Close the editing session.
  5. Change `gke-metrics-agent` DaemonSet version to 1.1.0-anthos.8: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG  \
           --namespace kube-system  set image daemonset/gke-metrics-agent \
           gke-metrics-agent=gcr.io/gke-on-prem-release/gke-metrics-agent:1.1.0-anthos.8


  
Logging and monitoring | 1.10, 1.11 | 

### `gke-metrics-agent` has frequent CrashLoopBackOff errors 

For Google Distributed Cloud version 1.10 and above, `gke-metrics-agent` DaemonSet has frequent CrashLoopBackOff errors when `enableStackdriverForApplications` is set to `true` in the `stackdriver` object.   
**Workaround:** To mitigate this issue, disable application metrics collection by running the following commands. These commands will not disable application logs collection.

  1. To prevent the following changes from reverting, scale down `stackdriver-operator`: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
             --namespace kube-system scale deploy stackdriver-operator \
             --replicas=0

Replace USER_CLUSTER_KUBECONFIG with the path of the user cluster kubeconfig file.
  2. Open the `gke-metrics-agent-conf` ConfigMap for editing: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
             --namespace kube-system edit configmap gke-metrics-agent-conf

  3. Under `services.pipelines`, comment out the entire `metrics/app-metrics` section: 
         
         services:
           pipelines:
             #metrics/app-metrics:
             #  exporters:
             #  - googlecloud/app-metrics
             #  processors:
             #  - resource
             #  - metric_to_resource
             #  - infer_resource
             #  - disk_buffer/app-metrics
             #  receivers:
             #  - prometheus/app-metrics
             metrics/metrics:
               exporters:
               - googlecloud/metrics
               processors:
               - resource
               - metric_to_resource
               - infer_resource
               - disk_buffer/metrics
               receivers:
               - prometheus/metrics

  4. Close the editing session.
  5. Restart the `gke-metrics-agent` DaemonSet: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
             --namespace kube-system rollout restart daemonset gke-metrics-agent


  
Logging and monitoring | 1.11, 1.12, 1.13 | 

### Replace deprecated metrics in dashboard

If deprecated metrics are used in your OOTB dashboards, you will see some empty charts. To find deprecated metrics in the Monitoring dashboards, run the following commands:
    
    
    gcloud monitoring dashboards list > all-dashboard.json
    
    # find deprecated metrics
    cat all-dashboard.json | grep -E \
      'kube_daemonset_updated_number_scheduled\
        |kube_node_status_allocatable_cpu_cores\
        |kube_node_status_allocatable_pods\
        |kube_node_status_capacity_cpu_cores'

The following deprecated metrics should be migrated to their replacements. | Deprecated| Replacement  
---|---  
`kube_daemonset_updated_number_scheduled` | `kube_daemonset_status_updated_number_scheduled`  
`kube_node_status_allocatable_cpu_cores`  
`kube_node_status_allocatable_memory_bytes`  
`kube_node_status_allocatable_pods` | `kube_node_status_allocatable`  
`kube_node_status_capacity_cpu_cores`  
`kube_node_status_capacity_memory_bytes`  
`kube_node_status_capacity_pods` | `kube_node_status_capacity`  
`kube_hpa_status_current_replicas` | `kube_horizontalpodautoscaler_status_current_replicas`  
  


**Workaround:**

To replace the deprecated metrics

  1. Delete "GKE on-prem node status" in the Google Cloud Monitoring dashboard. Reinstall "GKE on-prem node status" following [ these instructions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring#node-status-dashboard).
  2. Delete "GKE on-prem node utilization" in the Google Cloud Monitoring dashboard. Reinstall "GKE on-prem node utilization" following [ these instructions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring#node-utilization-dashboard).
  3. Delete "GKE on-prem vSphere vm health" in the Google Cloud Monitoring dashboard. Reinstall "GKE on-prem vSphere vm health" following [ these instructions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring#vm-health-status-dashboard).

This deprecation is due to the upgrade of [ kube-state-metrics](https://github.com/kubernetes/kube-state-metrics) agent from v1.9 to v2.4, which is required for Kubernetes 1.22. You can replace all deprecated `kube-state-metrics` metrics, which have the prefix `kube_`, in your custom dashboards or alerting policies.


  
Logging and monitoring | 1.10, 1.11, 1.12, 1.13 | 

### Unknown metric data in Cloud Monitoring

For Google Distributed Cloud version 1.10 and above, the data for clusters in Cloud Monitoring may contain irrelevant summary metrics entries such as the following:
    
    
    Unknown metric: kubernetes.io/anthos/go_gc_duration_seconds_summary_percentile
    

Other metrics types that may have irrelevant summary metrics include: 

  * `apiserver_admission_step_admission_duration_seconds_summary`
  * `go_gc_duration_seconds`
  * `scheduler_scheduling_duration_seconds`
  * `gkeconnect_http_request_duration_seconds_summary`
  * `alertmanager_nflog_snapshot_duration_seconds_summary`

While these summary type metrics are in the metrics list, they are not supported by `gke-metrics-agent` at this time.  
Logging and monitoring | 1.10, 1.11, 1.12, 1.13 | 

### Missing metrics on some nodes

You might find that the following metrics are missing on some, but not all, nodes:

  * `kubernetes.io/anthos/container_memory_working_set_bytes`
  * `kubernetes.io/anthos/container_cpu_usage_seconds_total`
  * `kubernetes.io/anthos/container_network_receive_bytes_total`

  
**Workaround:** To fix this issue, perform the following steps as a workaround. For [version 1.9.5+, 1.10.2+, 1.11.0]: increase cpu for gke-metrics-agent by following steps 1 - 4

  1. Open your `stackdriver` resource for editing: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
             --namespace kube-system edit stackdriver stackdriver

  2. To increase the CPU request for `gke-metrics-agent` from `10m` to `50m`, CPU limit from `100m` to `200m` add the following `resourceAttrOverride` section to the `stackdriver` manifest : 
         
         spec:
           resourceAttrOverride:
             gke-metrics-agent/gke-metrics-agent:
               limits:
                 cpu: 100m
                 memory: 4608Mi
               requests:
                 cpu: 10m
                 memory: 200Mi

Your edited resource should look similar to the following: 
         
         spec:
           anthosDistribution: on-prem
           clusterLocation: us-west1-a
           clusterName: my-cluster
           enableStackdriverForApplications: true
           gcpServiceAccountSecretName: ...
           optimizedMetrics: true
           portable: true
           projectID: my-project-191923
           proxyConfigSecretName: ...
           **resourceAttrOverride :
             gke-metrics-agent/gke-metrics-agent:
               limits:
                 cpu: 200m
                 memory: 4608Mi
               requests:
                 cpu: 50m
                 memory: 200Mi**

  3. Save your changes and close the text editor.
  4. To verify your changes have taken effect, run the following command: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
             --namespace kube-system get daemonset gke-metrics-agent -o yaml \
             | grep "cpu: 50m"

The command finds `cpu: 50m` if your edits have taken effect.

  
Logging and monitoring | 1.11.0-1.11.2, 1.12.0 | 

###  Missing scheduler and controller-manager metrics in admin cluster 

If your admin cluster is affected by this issue, scheduler and controller-manager metrics are missing. For example, these two metrics are missing
    
    
    # scheduler metric example
    scheduler_pending_pods
    # controller-manager metric example
    replicaset_controller_rate_limiter_use
    

  
**Workaround:** Upgrade to v1.11.3+, v1.12.1+, or v1.13+.  
| 1.11.0-1.11.2, 1.12.0 | 

### Missing scheduler and controller-manager metrics in user cluster

If your user cluster is affected by this issue, scheduler and controller-manager metrics are missing. For example, these two metrics are missing:
    
    
    # scheduler metric example
    scheduler_pending_pods
    # controller-manager metric example
    replicaset_controller_rate_limiter_use
    

  
**Workaround:** This issue is fixed in Google Distributed Cloud version 1.13.0 and later. Upgrade your cluster to a version with the fix.  
Installation, Upgrades, Updates | 1.10, 1.11, 1.12, 1.13 | 

### Failure to register admin cluster during creation

If you create an admin cluster for version 1.9.x or 1.10.0, and if the admin cluster fails to register with the provided `gkeConnect` spec during its creation, you will get the following error.
    
    
    Failed to create root cluster: failed to register admin cluster: failed to register cluster: failed to apply Hub Membership: Membership API request failed: rpc error:  ode = PermissionDenied desc = Permission 'gkehub.memberships.get' denied on PROJECT_PATH
    

You will still be able to use this admin cluster, but you will get the following error if you later attempt to upgrade the admin cluster to version 1.10.y.
    
    
    failed to migrate to first admin trust chain: failed to parse current version "": invalid version: "" failed to migrate to first admin trust chain: failed to parse current version "": invalid version: ""
    

  
**Workaround:**

#### View workaround steps

If this error occurs, follow these steps to fix the cluster registration issue. After you do this fix, you can then upgrade your admin cluster.

  1. Run `gkectl update admin` to register the admin cluster with the correct service account key.
  2. Create a dedicated service account for patching the `OnPremAdminCluster` custom resource. 
         
         export KUBECONFIG=ADMIN_CLUSTER_KUBECONFIG
         
         # Create Service Account modify-admin
         kubectl apply -f - <<EOF
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: modify-admin
           namespace: kube-system
         EOF
         
         # Create ClusterRole
         kubectl apply -f - <<EOF
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           creationTimestamp: null
           name: modify-admin-role
         rules:
         - apiGroups:
           - "onprem.cluster.gke.io"
           resources:
           - "onpremadminclusters/status"
           verbs:
           - "patch"
         EOF
         
         # Create ClusterRoleBinding for binding the permissions to the modify-admin SA
         
         kubectl apply -f - <<EOF
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           creationTimestamp: null
           name: modify-admin-rolebinding
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: ClusterRole
           name: modify-admin-role
         subjects:
         - kind: ServiceAccount
           name: modify-admin
           namespace: kube-system
         EOF

Replace ADMIN_CLUSTER_KUBECONFIG with the path of your admin cluster kubeconfig file.
  3. Run these commands to update the `OnPremAdminCluster` custom resource. 
         
         export KUBECONFIG=ADMIN_CLUSTER_KUBECONFIG
         
         SERVICE_ACCOUNT=modify-admin
         
         SECRET=$(kubectl get serviceaccount ${SERVICE_ACCOUNT} \
             -n kube-system -o json \
             | jq -Mr '.secrets[].name | select(contains("token"))')
         
         TOKEN=$(kubectl get secret ${SECRET} -n kube-system -o json \
             | jq -Mr '.data.token' | base64 -d)
         
         kubectl get secret ${SECRET} -n kube-system -o json \
             | jq -Mr '.data["ca.crt"]' \
             | base64 -d > /tmp/ca.crt
         
         APISERVER=https://$(kubectl -n default get endpoints kubernetes \
             --no-headers | awk '{ print $2 }')
         
         # Find out the admin cluster name and gkeOnPremVersion from the OnPremAdminCluster CR
         ADMIN_CLUSTER_NAME=$(kubectl get onpremadmincluster -n kube-system \
             --no-headers | awk '{ print $1 }')
         GKE_ON_PREM_VERSION=$(kubectl get onpremadmincluster \
             -n kube-system $ADMIN_CLUSTER_NAME \
             -o=jsonpath='{.spec.gkeOnPremVersion}')
         
         # Create the Status field and set the gkeOnPremVersion in OnPremAdminCluster CR
         curl -H "Accept: application/json" \
             --header "Authorization: Bearer $TOKEN" -XPATCH \
             -H "Content-Type: application/merge-patch+json" \
             --cacert /tmp/ca.crt \
             --data '{"status": {"gkeOnPremVersion": "'$GKE_ON_PREM_VERSION'"}}' \
             $APISERVER/apis/onprem.cluster.gke.io/v1alpha1/namespaces/kube-system/onpremadminclusters/$ADMIN_CLUSTER_NAME/status

  4. Attempt to upgrade the admin cluster again with the `--disable-upgrade-from-checkpoint` flag. 
         
         gkectl upgrade admin --config ADMIN_CLUSTER_CONFIG \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --disable-upgrade-from-checkpoint

Replace ADMIN_CLUSTER_CONFIG with the path of your admin cluster configuration file.

  
Identity | 1.10, 1.11, 1.12, 1.13 | 

### Using GKE Identity Service can cause the Connect Agent to restart unpredictably 

If you are using the [GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/authentication) feature to manage [ GKE Identity Service ClientConfig](https://docs.cloud.google.com/anthos/identity/setup/fleet-cluster), the [ Connect Agent](https://docs.cloud.google.com/anthos/fleet-management/docs/connect-agent) might restart unexpectedly.   
**Workaround:** If you have experienced this issue with an existing cluster, you can do one of the following:

  * Disable GKE Identity Service. If you disable GKE Identity Service, that won't remove the deployed GKE Identity Service binary or remove GKE Identity Service ClientConfig. To disable GKE Identity Service, run this command: 
        
        gcloud container fleet identity-service disable \
            --project PROJECT_ID

Replace PROJECT_ID with the ID of the cluster's [ fleet host project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#fleet_host_project).
  * Update the cluster to version 1.9.3 or later, or version 1.10.1 or later, so as to upgrade the Connect Agent version.

  
Networking | 1.10, 1.11, 1.12, 1.13 | 

### Cisco ACI doesn't work with Direct Server Return (DSR)

Seesaw runs in DSR mode, and by default it doesn't work in Cisco ACI because of data-plane IP learning.   
**Workaround:** A possible workaround is to disable IP learning by adding the Seesaw IP address as a L4-L7 Virtual IP in the Cisco Application Policy Infrastructure Controller (APIC). You can configure the L4-L7 Virtual IP option by going to **Tenant > Application Profiles > Application EPGs** or **uSeg EPGs**. Failure to disable IP learning will result in IP endpoint flapping between different locations in the Cisco API fabric.  
VMware | 1.10, 1.11, 1.12, 1.13 | 

### vSphere 7.0 Update 3 issues

VMWare has recently identified critical issues with the following vSphere 7.0 Update 3 releases:

  * vSphere ESXi 7.0 Update 3 (build 18644231)
  * vSphere ESXi 7.0 Update 3a (build 18825058)
  * vSphere ESXi 7.0 Update 3b (build 18905247)
  * vSphere vCenter 7.0 Update 3b (build 18901211)

  
**Workaround:** VMWare has since removed these releases. You should upgrade the [ESXi](https://www.vmware.com/products/esxi-and-esx.html) and [vCenter Servers](https://www.vmware.com/products/vcenter-server.html) to a newer version.  
Operating system | 1.10, 1.11, 1.12, 1.13 | 

### Failure to mount emptyDir volume as `exec` into Pod running on COS nodes

For Pods running on nodes that use Container-Optimized OS (COS) images, you cannot mount emptyDir volume as `exec`. It mounts as `noexec` and you will get the following error: `exec user process caused: permission denied`. For example, you will see this error message if you deploy the following test Pod:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      creationTimestamp: null
      labels:
        run: test
      name: test
    spec:
      containers:
      - args:
        - sleep
        - "5000"
        image: gcr.io/google-containers/busybox:latest
        name: test
        volumeMounts:
          - name: test-volume
            mountPath: /test-volume
        resources:
          limits:
            cpu: 200m
            memory: 512Mi
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      volumes:
        - emptyDir: {}
          name: test-volume
    

And in the test Pod, if you run `mount | grep test-volume`, it would show noexec option:
    
    
    /dev/sda1 on /test-volume type ext4 (rw,nosuid,nodev,noexec,relatime,commit=30)
    

  
**Workaround:**

#### View workaround steps

Apply a DaemonSet resource, for example:
    
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: fix-cos-noexec
      namespace: kube-system
    spec:
      selector:
        matchLabels:
          app: fix-cos-noexec
      template:
        metadata:
          labels:
            app: fix-cos-noexec
        spec:
          hostIPC: true
          hostPID: true
          containers:
          - name: fix-cos-noexec
            image: ubuntu
            command: ["chroot", "/host", "bash", "-c"]
            args:
            - |
              set -ex
              while true; do
                if ! $(nsenter -a -t 1 findmnt -l | grep -qe "^/var/lib/kubelet\s"); then
                  echo "remounting /var/lib/kubelet with exec"
                  nsenter -a -t 1 mount --bind /var/lib/kubelet /var/lib/kubelet
                  nsenter -a -t 1 mount -o remount,exec /var/lib/kubelet
                fi
                sleep 3600
              done
            volumeMounts:
            - name: host
              mountPath: /host
            securityContext:
              privileged: true
          volumes:
          - name: host
            hostPath:
              path: /
      
  
Upgrades, Updates | 1.10, 1.11, 1.12, 1.13 | 

### Cluster node pool replica update does not work after autoscaling has been disabled on the node pool

Node pool replicas do not update once autoscaling has been enabled and disabled on a node pool.   
**Workaround:** Removing the `cluster.x-k8s.io/cluster-api-autoscaler-node-group-max-size` and `cluster.x-k8s.io/cluster-api-autoscaler-node-group-min-size` annotations from the machine deployment of the corresponding node pool.  
Logging and monitoring | 1.11, 1.12, 1.13 | 

### Windows monitoring dashboards show data from Linux clusters

From version 1.11, on the out-of-the-box monitoring dashboards, the Windows Pod status dashboard and Windows node status dashboard also show data from Linux clusters. This is because the Windows node and Pod metrics are also exposed on Linux clusters.  
Logging and monitoring | 1.10, 1.11, 1.12 | 

### `stackdriver-log-forwarder` in constant CrashLoopBackOff

For Google Distributed Cloud version 1.10, 1.11, and 1.12, `stackdriver-log-forwarder` DaemonSet might have `CrashLoopBackOff` errors when there are broken buffered logs on the disk.   
**Workaround:** To mitigate this issue, we will need to clean up the buffered logs on the node.

  1. To prevent the unexpected behaviour, scale down `stackdriver-log-forwarder`: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
             -n kube-system patch daemonset stackdriver-log-forwarder -p '{"spec": {"template": {"spec": {"nodeSelector": {"non-existing": "true"}}}}}'

Replace USER_CLUSTER_KUBECONFIG with the path of the user cluster kubeconfig file.
  2. Deploy the clean-up DaemonSet to clean up broken chunks: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
             -n kube-system -f - << EOF
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           name: fluent-bit-cleanup
           namespace: kube-system
         spec:
           selector:
             matchLabels:
               app: fluent-bit-cleanup
           template:
             metadata:
               labels:
                 app: fluent-bit-cleanup
             spec:
               containers:
               - name: fluent-bit-cleanup
                 image: debian:10-slim
                 command: ["bash", "-c"]
                 args:
                 - |
                   rm -rf /var/log/fluent-bit-buffers/
                   echo "Fluent Bit local buffer is cleaned up."
                   sleep 3600
                 volumeMounts:
                 - name: varlog
                   mountPath: /var/log
                 securityContext:
                   privileged: true
               tolerations:
               - key: "CriticalAddonsOnly"
                 operator: "Exists"
               - key: node-role.kubernetes.io/master
                 effect: NoSchedule
               - key: node-role.gke.io/observability
                 effect: NoSchedule
               volumes:
               - name: varlog
                 hostPath:
                   path: /var/log
         EOF

  3. To make sure the clean-up DaemonSet has cleaned up all the chunks, you can run the following commands. The output of the two commands should be equal to your node number in the cluster: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
           logs -n kube-system -l app=fluent-bit-cleanup | grep "cleaned up" | wc -l
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
           -n kube-system get pods -l app=fluent-bit-cleanup --no-headers | wc -l

  4. Delete the clean-up DaemonSet: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
           -n kube-system delete ds fluent-bit-cleanup

  5. Resume `stackdriver-log-forwarder`: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
           -n kube-system patch daemonset stackdriver-log-forwarder --type json -p='[{"op": "remove", "path": "/spec/template/spec/nodeSelector/non-existing"}]'


  
Logging and monitoring | 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16 | 

### `stackdriver-log-forwarder` doesn't send logs to Cloud Logging

If you don't see logs in Cloud Logging from your clusters, and you notice the following error in your logs: 
    
    
    2023-06-02T10:53:40.444017427Z [2023/06/02 10:53:40] [error] [input chunk] chunk 1-1685703077.747168499.flb would exceed total limit size in plugin stackdriver.0
    2023-06-02T10:53:40.444028047Z [2023/06/02 10:53:40] [error] [input chunk] no available chunk
          

It's likely the logs input rate exceeds the limit of the logging agent, which causes `stackdriver-log-forwarder` to not send logs. This issue occurs in all Google Distributed Cloud versions. Workaround: To mitigate this issue, you need to increase the resource limit on the logging agent.

  1. Open your `stackdriver` resource for editing: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
             --namespace kube-system edit stackdriver stackdriver

  2. To increase the CPU request for `stackdriver-log-forwarder` , add the following `resourceAttrOverride` section to the `stackdriver` manifest : 
         
         spec:
           resourceAttrOverride:
             stackdriver-log-forwarder/stackdriver-log-forwarder:
               limits:
                 cpu: 1200m
                 memory: 600Mi
               requests:
                 cpu: 600m
                 memory: 600Mi

Your edited resource should look similar to the following: 
         
         spec:
           anthosDistribution: on-prem
           clusterLocation: us-west1-a
           clusterName: my-cluster
           enableStackdriverForApplications: true
           gcpServiceAccountSecretName: ...
           optimizedMetrics: true
           portable: true
           projectID: my-project-191923
           proxyConfigSecretName: ...
           **resourceAttrOverride :
             stackdriver-log-forwarder/stackdriver-log-forwarder:
               limits:
                 cpu: 1200m
                 memory: 600Mi
               requests:
                 cpu: 600m
                 memory: 600Mi**

  3. Save your changes and close the text editor.
  4. To verify your changes have taken effect, run the following command: 
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
             --namespace kube-system get daemonset stackdriver-log-forwarder -o yaml \
             | grep "cpu: 1200m"

The command finds `cpu: 1200m` if your edits have taken effect.

  
Security | 1.13 | 

### Kubelet service will be temporarily unavailable after NodeReady

there is a short period where node is ready but kubelet server certificate is not ready. `kubectl exec` and `kubectl logs` are unavailable during this tens of seconds. This is because it takes time for the new server certificate approver to see the updated valid IPs of the node. This issue affects kubelet server certificate only, it will not affect Pod scheduling.  
Upgrades, Updates | 1.12 | 

### Partial admin cluster upgrade does not block later user cluster upgrade

User cluster upgrade failed with:
    
    
    .LBKind in body is required (Check the status of OnPremUserCluster 'cl-stg-gdl-gke-onprem-mgmt/cl-stg-gdl' and the logs of pod 'kube-system/onprem-user-cluster-controller' for more detailed debugging information.
    

The admin cluster is not fully upgraded, and the status version is still 1.10. User cluster upgrade to 1.12 won't be blocked by any preflight check, and fails with version skew issue.   
**Workaround:** Complete to upgrade the admin cluster to 1.11 first, and then upgrade the user cluster to 1.12.  
Storage | 1.10.0-1.10.5, 1.11.0-1.11.2, 1.12.0 | 

### Datastore incorrectly reports insufficient free space

`gkectl diagnose cluster` command failed with: 
    
    
    Checking VSphere Datastore FreeSpace...FAILURE
        Reason: vCenter datastore: [DATASTORE_NAME] insufficient FreeSpace, requires at least [NUMBER] GB
    

The validation of datastore free space should not be used for existing cluster node pools, and was added in `gkectl diagnose cluster` by mistake.   
**Workaround:** You can ignore the error message or skip the validation using `--skip-validation-infra`.  
Operation, Networking | 1.11, 1.12.0-1.12.1 | 

### Failure to add new user cluster when admin cluster is using MetalLB load balancer

You may not be able to add a new user cluster if your admin cluster is set up with a MetalLB load balancer configuration. The user cluster deletion process may get stuck for some reason which results in an invalidation of the MatalLB ConfigMap. It won't be possible to add a new user cluster in this state.   
**Workaround:** You can [ force delete](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-a-user-cluster#force_delete_a_user_cluster) your user cluster.  
Installation, Operating system | 1.10, 1.11, 1.12, 1.13 | 

### Failure when using Container-Optimized OS (COS) for user cluster

If `osImageType` is using `cos` for admin cluster, and when `gkectl check-config` is executed after admin cluster creation and before user cluster creation, it would fail on: 
    
    
    Failed to create the test VMs: VM failed to get IP addresses on the network.
    

The test VM created for user cluster `check-config` by default uses the same `osImageType` from admin cluster, and currently test VM is not compatible with COS yet.   
**Workaround:** To avoid the slow preflight check which creates the test VM, using `gkectl check-config --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG --fast`.  
Logging and monitoring | 1.12.0-1.12.1 | 

### Grafana in the admin cluster unable to reach user clusters

This issue affects customers using Grafana in the admin cluster to monitor user clusters in Google Distributed Cloud versions 1.12.0 and 1.12.1. It comes from a mismatch of pushprox-client certificates in user clusters and the allowlist in the pushprox-server in the admin cluster. The symptom is pushprox-client in user clusters printing error logs like the following:
    
    
    level=error ts=2022-08-02T13:34:49.41999813Z caller=client.go:166 msg="Error reading request:" err="invalid method \"RBAC:\""
    

  
**Workaround:**

#### View workaround steps

perform the following steps:

  1. Scale down monitoring-operator deployment in admin cluster kube-system namespace. 
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --namespace kube-system scale deploy monitoring-operator \
             --replicas=0

  2. Edit the `pushprox-server-rbac-proxy-config` ConfigMap in admin cluster kube-system namespace. 
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --namespace kube-system edit cm pushprox-server-rbac-proxy-config

Locate the `principals` line for the `external-pushprox-server-auth-proxy` listener and correct the `principal_name` for all user clusters by removing the `kube-system` substring from `pushprox-client.metrics-consumers.kube-system.cluster.` The new config should look like the following: 
         
         permissions:
         - or_rules:
             rules:
             - header: { name: ":path", exact_match: "/poll" }
             - header: { name: ":path", exact_match: "/push" }
         principals: [{"authenticated":{"principal_name":{"exact":"pushprox-client.metrics-consumers.kube-system.cluster.local"}}},{"authenticated":{"principal_name":{"exact":"pushprox-client.metrics-consumers.kube-system.cluster."}}},{"authenticated":{"principal_name":{"exact":"pushprox-client.metrics-consumers.cluster."}}}]
         

  3. Restart the `pushprox-server` deployment in the admin cluster and the `pushprox-client` deployment in affected user clusters: 
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG --namespace kube-system rollout restart deploy pushprox-server
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG --namespace kube-system rollout restart deploy pushprox-client

  4. The preceding steps should resolve the issue. Once the cluster is upgraded to 1.12.2 and later where the issue is fixed, scale up the admin cluster kube-system monitoring-operator so that it can manage the pipeline again. 
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG --namespace kube-system scale deploy monitoring-operator --replicas=1


  
Other | 1.11.3 | 

### `gkectl repair admin-master` does not provide the VM template to be used for recovery

`gkectl repair admin-master` command failed with: 
    
    
    Failed to repair: failed to select the template: no VM templates is available for repairing the admin master (check if the admin cluster version >= 1.4.0 or contact support
    

`gkectl repair admin-master` is not able to fetch the VM template to be used for repairing the admin control plane VM if the name of the admin control plane VM ends with the characters `t`, `m`, `p`, or `l`.   
**Workaround:** Rerun the command with `--skip-validation`.  
Logging and monitoring | 1.11, 1.12, 1.13, 1.14, 1.15, 1.16 | 

### Cloud audit logging failure due to permission denied 

Cloud Audit Logs needs a special permission setup that is currently only automatically performed for user clusters through GKE Hub. It is recommended to have at least one user cluster that uses the same project ID and service account with the admin cluster for Cloud Audit Logs so the admin cluster will have the required permission. However in cases where the admin cluster uses a different project ID or different service account than any user cluster, audit logs from the admin cluster would fail to be injected into Google Cloud. The symptom is a series of `Permission Denied` errors in the `audit-proxy` Pod in the admin cluster. **Workaround:**

#### View workaround steps

To resolve this issue, the permission can be setup by interacting with the `cloudauditlogging` Hub feature:

  1. First check the existing service accounts allowlisted for Cloud Audit Logs in your project: 
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             https://gkehub.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/features/cloudauditlogging

  2. Depend on the response, do one of the following: 
     * If you received a `404 Not_found` error, it means there is no service account allowlisted for this project ID. You can allowlist a service account by enabling the `cloudauditlogging` Hub feature: 
           
           curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
               -H "Content-Type: application/json" \
               https://gkehub.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/features?feature_id=cloudauditlogging -d \
               '{"spec":{"cloudauditlogging":{"allowlistedServiceAccounts":["SERVICE_ACCOUNT_EMAIL"]}}}'

     * If you received a feature spec that contains `"lifecycleState": "ENABLED"` with `"code": "OK"` and a list of service accounts in `allowlistedServiceAccounts`, it means there are existing service accounts allowed for this project, you can either use a service account from this list in your cluster, or add a new service account to the allowlist: 
           
           curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
               -H "Content-Type: application/json" \
               https://gkehub.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/features/cloudauditlogging?update_mask=spec.cloudauditlogging.allowlistedServiceAccounts -d \
               '{"spec":{"cloudauditlogging":{"allowlistedServiceAccounts":["SERVICE_ACCOUNT_EMAIL"]}}}'

     * If you received a feature spec that contains `"lifecycleState": "ENABLED"` with `"code": "FAILED"`, it means the permission setup was not successful. Try to address the issues in the `description` field of the response, or back up the current allowlist, delete the cloudauditlogging hub feature, and re-enable it following step 1 of this section again. You can delete the `cloudauditlogging` Hub feature by: 
           
           curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
               https://gkehub.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/features/cloudauditlogging


In above commands:

  * Replace PROJECT_ID with the cluster's [ audit logging project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#audit_logging_project).
  * Replace SERVICE_ACCOUNT_EMAIL with the email address of the cluster's [ audit logging service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#audit_logging_service_account).

  
Operation, Security | 1.11 | 

### `gkectl diagnose` checking certificates failure

If your work station does not have access to user cluster worker nodes, it will get the following failures when running `gkectl diagnose`:
    
    
    Checking user cluster certificates...FAILURE
        Reason: 3 user cluster certificates error(s).
        Unhealthy Resources:
        Node kubelet CA and certificate on node xxx: failed to verify kubelet certificate on node xxx: dial tcp xxx.xxx.xxx.xxx:10250: connect: connection timed out
        Node kubelet CA and certificate on node xxx: failed to verify kubelet certificate on node xxx: dial tcp xxx.xxx.xxx.xxx:10250: connect: connection timed out
        Node kubelet CA and certificate on node xxx: failed to verify kubelet certificate on node xxx: dial tcp xxx.xxx.xxx.xxx:10250: connect: connection timed out
    

If your work station does not have access to admin cluster worker nodes or admin cluster worker nodes, it will get the following failures when running `gkectl diagnose`:
    
    
    Checking admin cluster certificates...FAILURE
        Reason: 3 admin cluster certificates error(s).
        Unhealthy Resources:
        Node kubelet CA and certificate on node xxx: failed to verify kubelet certificate on node xxx: dial tcp xxx.xxx.xxx.xxx:10250: connect: connection timed out
        Node kubelet CA and certificate on node xxx: failed to verify kubelet certificate on node xxx: dial tcp xxx.xxx.xxx.xxx:10250: connect: connection timed out
        Node kubelet CA and certificate on node xxx: failed to verify kubelet certificate on node xxx: dial tcp xxx.xxx.xxx.xxx:10250: connect: connection timed out
    

  
**Workaround:** If is safe to ignore these messages.  
Operating system | 1.8, 1.9, 1.10, 1.11, 1.12, 1.13 | 

### `/var/log/audit/` filling up disk space on VMs

`/var/log/audit/` is filled with audit logs. You can check the disk usage by running `sudo du -h -d 1 /var/log/audit`. Certain `gkectl` commands on the admin workstation, for example, `gkectl diagnose snapshot` contribute to disk space usage. Since Google Distributed Cloud v1.8, the Ubuntu image is hardened with CIS Level 2 Benchmark. And one of the compliance rules, "4.1.2.2 Ensure audit logs are not automatically deleted", ensures the auditd setting `max_log_file_action = keep_logs`. This results in all the audit rules kept on the disk.   
**Workaround:**

#### View workaround steps

**Admin workstation****** For the admin workstation, you can manually change the auditd settings to rotate the logs automatically, and then restart the auditd service:
    
    
    sed -i 's/max_log_file_action = keep_logs/max_log_file_action = rotate/g' /etc/audit/auditd.conf
    sed -i 's/num_logs = .*/num_logs = 250/g' /etc/audit/auditd.conf
    systemctl restart auditd

The above setting would make auditd automatically rotate its logs once it has generated more than 250 files (each with 8M size). **Cluster nodes****** For cluster nodes, upgrade to 1.11.5+, 1.12.4+, 1.13.2+ or 1.14+. If you can't upgrade to those versions yet, apply the following DaemonSet to your cluster:
    
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: change-auditd-log-action
      namespace: kube-system
    spec:
      selector:
        matchLabels:
          app: change-auditd-log-action
      template:
        metadata:
          labels:
            app: change-auditd-log-action
        spec:
          hostIPC: true
          hostPID: true
          containers:
          - name: update-audit-rule
            image: ubuntu
            command: ["chroot", "/host", "bash", "-c"]
            args:
            - |
              while true; do
                if $(grep -q "max_log_file_action = keep_logs" /etc/audit/auditd.conf); then
                  echo "updating auditd max_log_file_action to rotate with a max of 250 files"
                  sed -i 's/max_log_file_action = keep_logs/max_log_file_action = rotate/g' /etc/audit/auditd.conf
                  sed -i 's/num_logs = .*/num_logs = 250/g' /etc/audit/auditd.conf
                  echo "restarting auditd"
                  systemctl restart auditd
                else
                  echo "auditd setting is expected, skip update"
                fi
                sleep 600
              done
            volumeMounts:
            - name: host
              mountPath: /host
            securityContext:
              privileged: true
          volumes:
          - name: host
            hostPath:
              path: /

Note that making this auditd config change would violate CIS Level 2 rule "4.1.2.2 Ensure audit logs are not automatically deleted".  
Networking | 1.10, 1.11.0-1.11.3, 1.12.0-1.12.2, 1.13.0 | 

### `NetworkGatewayGroup` Floating IP conflicts with node address

Users are unable to create or update `NetworkGatewayGroup` objects because of the following validating webhook error:
    
    
    [1] admission webhook "vnetworkgatewaygroup.kb.io" denied the request: NetworkGatewayGroup.networking.gke.io "default" is invalid: [Spec.FloatingIPs: Invalid value: "10.0.0.100": IP address conflicts with node address with name: "my-node-name"
    

In affected versions, the kubelet can erroneously bind to a floating IP address assigned to the node and report it as a node address in `node.status.addresses`. The validating webhook checks `NetworkGatewayGroup` floating IP addresses against all `node.status.addresses` in the cluster and sees this as a conflict.   
**Workaround:** In the same cluster where create or update of `NetworkGatewayGroup` objects is failing, temporarily disable the ANG validating webhook and submit your change:

  1. Save the webhook config so it can be restored at the end: 
         
         kubectl -n kube-system get validatingwebhookconfiguration \
             ang-validating-webhook-configuration -o yaml > webhook-config.yaml

  2. Edit the webhook config: 
         
         kubectl -n kube-system edit validatingwebhookconfiguration \
             ang-validating-webhook-configuration

  3. Remove the `vnetworkgatewaygroup.kb.io` item from the webhook config list and close to apply the changes.
  4. Create or edit your `NetworkGatewayGroup` object.
  5. Reapply the original webhook config: 
         
         kubectl -n kube-system apply -f webhook-config.yaml


  
Installation, Upgrades, Updates | 1.10.0-1.10.2 | 

### Creating or upgrading admin cluster timeout

During an admin cluster upgrade attempt, the admin control plane VM might get stuck during creation. The admin control plane VM goes into an infinite waiting loop during the boot up, and you will see the following infinite loop error in the `/var/log/cloud-init-output.log` file:
    
    
    + echo 'waiting network configuration is applied'
    waiting network configuration is applied
    ++ get-public-ip
    +++ ip addr show dev ens192 scope global
    +++ head -n 1
    +++ grep -v 192.168.231.1
    +++ grep -Eo 'inet ([0-9]{1,3}\.){3}[0-9]{1,3}'
    +++ awk '{print $2}'
    ++ echo
    + '[' -n '' ']'
    + sleep 1
    + echo 'waiting network configuration is applied'
    waiting network configuration is applied
    ++ get-public-ip
    +++ ip addr show dev ens192 scope global
    +++ grep -Eo 'inet ([0-9]{1,3}\.){3}[0-9]{1,3}'
    +++ awk '{print $2}'
    +++ grep -v 192.168.231.1
    +++ head -n 1
    ++ echo
    + '[' -n '' ']'
    + sleep 1
    

This is because when Google Distributed Cloud tries to get the node IP address in the startup script, it uses `grep -v ADMIN_CONTROL_PLANE_VIP` to skip the admin cluster control-plane VIP which can be assigned to the NIC too. However, the command also skips over any IP address that has a prefix of the control-plane VIP, which causes the startup script to hang. For example, suppose that the admin cluster control-plane VIP is 192.168.1.25. If the IP address of the admin cluster control-plane VM has the same prefix, for example,192.168.1.254, then the control-plane VM will get stuck during creation. This issue can also be triggered if the broadcast address has the same prefix as the control-plane VIP, for example, `192.168.1.255`.   
**Workaround:**

  * If the reason for the admin cluster creation timeout is due to the broadcast IP address, run the following command on the admin cluster control-plane VM: 
        
        ip addr add ${ADMIN_CONTROL_PLANE_NODE_IP}/32 dev ens192

This will create a line without a broadcast address, and unblock the boot up process. After the startup script is unblocked, remove this added line by running the following command: 
        
        ip addr del ${ADMIN_CONTROL_PLANE_NODE_IP}/32 dev ens192

  * However, if the reason for the admin cluster creation timeout is due to the IP address of the control-plane VM, you cannot unblock the startup script. Switch to a different IP address, and recreate or upgrade to version 1.10.3 or later.

  
Operating system, Upgrades, Updates | 1.10.0-1.10.2 | 

### The state of the admin cluster using COS image will get lost upon admin cluster upgrade or admin master repair

DataDisk can't be mounted correctly to admin cluster master node when using COS image and the state of the admin cluster using COS image will get lost upon admin cluster upgrade or admin master repair. (admin cluster using COS image is a preview feature)   
**Workaround:** Re-create admin cluster with osImageType set to ubuntu_containerd After you create the admin cluster with osImageType set to cos, grab the admin cluster SSH key and SSH into admin master node. `df -h` result contains `/dev/sdb1 98G 209M 93G 1% /opt/data`. And `lsblk` result contains `-sdb1 8:17 0 100G 0 part /opt/data`  
Operating system | 1.10 | 

### systemd-resolved failed DNS lookup on `.local` domains

In Google Distributed Cloud version 1.10.0, name resolutions on Ubuntu are routed to local systemd-resolved listening on `127.0.0.53` by default. The reason is that on the Ubuntu 20.04 image used in version 1.10.0, `/etc/resolv.conf` is sym-linked to `/run/systemd/resolve/stub-resolv.conf`, which points to the `127.0.0.53` localhost DNS stub. As a result, the localhost DNS name resolution refuses to check the upstream DNS servers (specified in `/run/systemd/resolve/resolv.conf`) for names with a `.local` suffix, unless the names are specified as search domains. This causes any lookups for `.local` names to fail. For example, during node startup, `kubelet` fails on pulling images from a private registry with a `.local` suffix. Specifying a vCenter address with a `.local` suffix will not work on an admin workstation.   
**Workaround:** You can avoid this issue for cluster nodes if you specify the `searchDomainsForDNS` field in your admin cluster configuration file and the user cluster configuration file to include the domains. Currently `gkectl update` doesn't support updating the `searchDomainsForDNS` field yet. Therefore, if you haven't set up this field before cluster creation, you must SSH into the nodes and bypass the local systemd-resolved stub by changing the symlink of `/etc/resolv.conf` from `/run/systemd/resolve/stub-resolv.conf` (which contains the `127.0.0.53` local stub) to `/run/systemd/resolve/resolv.conf` (which points to the actual upstream DNS): 
    
    
    sudo ln -sf /run/systemd/resolve/resolv.conf /etc/resolv.conf

As for the admin workstation, `gkeadm` doesn't support specifying search domains, so must work around this issue with this manual step. This solution for does not persist across VM re-creations. You must reapply this workaround whenever VMs are re-created.  
Installation, Operating system | 1.10 | 

### Docker bridge IP uses `172.17.0.1/16` instead of `169.254.123.1/24`

Google Distributed Cloud specifies a dedicated subnet for the Docker bridge IP address that uses `--bip=169.254.123.1/24`, so that it won't reserve the default `172.17.0.1/16` subnet. However, in version 1.10.0, there is a bug in Ubuntu OS image that caused the customized Docker config to be ignored. As a result, Docker picks the default `172.17.0.1/16` as its bridge IP address subnet. This might cause an IP address conflict if you already have workload running within that IP address range.   
**Workaround:** To work around this issue, you must rename the following systemd config file for dockerd, and then restart the service:
    
    
    sudo mv /etc/systemd/system/docker.service.d/50-cloudimg-settings.cfg \
        /etc/systemd/system/docker.service.d/50-cloudimg-settings.conf
    
    sudo systemctl daemon-reload
    
    sudo systemctl restart docker

Verify that Docker picks the correct bridge IP address:
    
    
    ip a | grep docker0

This solution does not persist across VM re-creations. You must reapply this workaround whenever VMs are re-created.  
Upgrades, Updates | 1.11 | 

### Upgrade to 1.11 blocked by stackdriver readiness

In Google Distributed Cloud version 1.11.0, there are changes in the definition of custom resources related to logging and monitoring:

  * Group name of the `stackdriver` custom resource changed from `addons.sigs.k8s.io` to `addons.gke.io`;
  * Group name of the `monitoring` and `metricsserver` custom resources changed from `addons.k8s.io` to `addons.gke.io`;
  * The specs of the above resources start to be valiidated against its schema. In particular, [the resourceAttrOverride and storageSizeOverride spec](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring#configuring_stackdriver_component_resources) in the `stackdriver` custom resource need to have string type in the values of the cpu, memory and storage size requests and limits.

The group name changes are made to comply with [CustomResourceDefinition updates in Kubernetes 1.22](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#customresourcedefinition-v122). There is no action required if you do not have additional logic that applies or edits the affected custom resources. The Google Distributed Cloud upgrade process will take care of the migration of the affected resources and keep their existing specs after the group name change. However if you run any logic that applies or edits the affected resources, special attention is needed. First, they need to be referenced with the new group name in your manifest file. For example:
    
    
    apiVersion: addons.gke.io/v1alpha1  ## instead of `addons.sigs.k8s.io/v1alpha1`
    kind: Stackdriver

Secondly, make sure the `resourceAttrOverride` and `storageSizeOverride` spec values are of string type. For example:
    
    
    spec:
      resourceAttrOverride:
        stackdriver-log-forwarder/stackdriver-log-forwarder
          limits:
            cpu: 1000m # or "1"
            # cpu: 1 # integer value like this would not work
            memory: 3000Mi

Otherwise, the applies and edits will not take effect and may lead to unexpected status in logging and monitoring components. Potential symptoms may include:

  * Reconciliation error logs in `onprem-user-cluster-controller`, for example: 
        
        potential reconciliation error: Apply bundle components failed, requeue after 10s, error: failed to apply addon components: failed to apply bundle objects from stackdriver-operator-addon 1.11.2-gke.53 to cluster my-cluster: failed to create typed live object: .spec.resourceAttrOverride.stackdriver-log-forwarder/stackdriver-log-forwarder.limits.cpu: expected string, got &value.valueUnstructured{Value:1}

  * Failure in `kubectl edit stackdriver stackdriver`, for example: 
        
        Error from server (NotFound): stackdrivers.addons.gke.io "stackdriver" not found


If you encounter the above errors, it means an unsupported type under stackdriver CR spec was already present before the upgrade. As a workaround, you could manually edit the stackdriver CR under the old group name `kubectl edit stackdrivers.addons.sigs.k8s.io stackdriver` and do the following: 

  1. Change the resource requests and limits to string type;
  2. Remove any `addons.gke.io/migrated-and-deprecated: true` annotation if present.

Then resume or restart the upgrade process.   
Operating system | 1.7 and later | 

### COS VMs show no IPs when VMs are moved through non-graceful shutdown of the host 

When an ESXi server with vCenter high availability enabled has a fault, the vMotion mechanism moves all virtual machines from the faulty ESXi server to a normal ESXi server, causing migrated COS virtual machines to lose their IP addresses. This issue only affects nodes using a COS OS image type and doesn't impact nodes using an Ubuntu OS image type. **Workaround:** Reboot the virtual machine If the cluster has node auto-repair enabled, unhealthy nodes are automatically detected and re-created. Otherwise, manually reboot or re-create the virtual machine.  
Networking | all versions prior to 1.14.7, 1.15.0-1.15.3, 1.16.0 | 

### GARP reply sent by Seesaw doesn't set target IP

The periodic GARP (Gratuitous ARP) sent by Seesaw every 20s doesn't set the target IP in the ARP header. Some networks might not accept such packets (like Cisco ACI). It can cause longer service down time after a split brain (due to VRRP packet drops) is recovered.  **Workaround:** Trigger a Seeaw failover by running `sudo seesaw -c failover` on either of the Seesaw VMs. This should restore the traffic.  
Operating system | 1.16, 1.28.0-1.28.200 | 

### Kubelet is flooded with logs stating that "/etc/kubernetes/manifests" does not exist on the worker nodes

"staticPodPath" was mistakenly set for worker nodes **Workaround:** Manually create the folder "/etc/kubernetes/manifests"  
  
## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
