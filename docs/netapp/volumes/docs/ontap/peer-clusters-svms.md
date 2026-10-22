---
url: https://docs.cloud.google.com/netapp/volumes/docs/ontap/peer-clusters-svms/
title: Peer clusters and SVMs \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:53.562191+00:00
---

# Peer clusters and SVMs  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/ontap/peer-clusters-svms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Peer clusters and SVMs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up peering for the ONTAP storage pool in Google Cloud NetApp Volumes.

Cluster peering and storage virtual machine (SVM) peering connect your Flex Unified ONTAP storage pool to another cluster. This allows services such as SnapMirror and FlexCache to run.

**Note:** Make sure that you complete the one-time configuration to [set up ontap_execute](https://docs.cloud.google.com/netapp/volumes/docs/ontap/common-ontap-mode-procedures#set_up_ontap_execute) before you begin. After you finish, return to this document to continue.

Use the `peer_cluster.py` script to accept an offer and enter a passphrase for an ONTAP-mode pool. For more information, see Cluster peering script.

**Note:** Peer only with clusters that you trust, because peering authorizes SnapMirror and FlexCache traffic between the systems.

## Choose a procedure

Choose one of the following peering procedures based on your setup:

  * **Hybrid peering** : you migrate or replicate from an ONTAP-mode pool to a Default-mode NetApp Volumes volume (Standard, Premium, Extreme, or Flex Unified Default-mode). NetApp Volumes starts peering from the destination. You complete peering on the ONTAP-mode source pool.

  * **Manual peering** : you establish peering yourself and you aren't using a hybrid migration or external replication workflow. Select a scenario:

    * An ONTAP-mode pool and an external ONTAP cluster that's on-premises or outside NetApp Volumes.

    * Two ONTAP-mode pools.




For more information about additional peering options on the external ONTAP cluster, see [NetApp ONTAP documentation](https://docs.netapp.com/us-en/ontap/index.html).

## How cluster peering works on an ONTAP-mode pool

The cluster peering process follows an offer and accept workflow:

  * **Offer** : one cluster initiates peering toward the peer IC-LIF addresses and receives a passphrase.

  * **Accept** : the peer cluster completes peering using the offering cluster's IC-LIF addresses and the passphrase.


**Caution:** Always specify all IC-LIF addresses of the remote cluster in offer and accept steps. Each cluster node has one IC-LIF, and the count depends on the cluster size; for example, two IC-LIFs on a two-node pool. Peering might appear to succeed when only one peer IC-LIF is listed, but you must provide every IC-LIF address for a supported configuration.

The ONTAP CLI proxy isn't interactive. The `cluster peer create -generate-passphrase` command doesn't prompt for input, so you can run the offer on an ONTAP-mode pool by using `ontap_execute`. List all remote IC-LIF addresses as a comma-separated `-peer-addrs` value. The `cluster peer accept` command prompts for the passphrase, so that step fails through the proxy. Use `peer_cluster.py` when an ONTAP-mode pool must accept an offer.

**Note:** The proxy returns `unable to parse command` for the `-initial-allowed-vserver-names` flag on `cluster peer create`. Omit that flag when you offer by using `ontap_execute`.

To peer the clusters, use one of the following scenarios:

  * Scenario A (ONTAP-mode and external ONTAP): run `cluster peer create-generate-passphrase` on the ONTAP-mode pool by using `ontap_execute` with all peer IC-LIF addresses. The external ONTAP administrator runs `cluster peer accept` at the cluster prompt with all ONTAP-mode IC-LIF addresses and enters the passphrase.

  * Scenario B (two ONTAP-mode pools): run `cluster peer create-generate-passphrase` on pool A by using `ontap_execute`, and then run `peer_cluster.py` with `PEER_MODE=accept` on pool B.




Perform SVM peering by running `vserver peer accept` using `ontap_execute` on the ONTAP-mode pool. In Scenario A, the external ONTAP cluster executes `vserver peer create`.

## Replication methods that require peering

The following replication methods require peering:

  * Any ONTAP source to Flex Unified ONTAP-mode (SnapMirror): peer on the ONTAP-mode pool.

  * Flex Unified ONTAP-mode to any ONTAP destination (SnapMirror): peer on the ONTAP-mode pool.

  * ONTAP-mode source to Default-mode NetApp Volumes (volume migration or external replication): use hybrid peering on the ONTAP-mode source pool.




Default-mode volume replication within NetApp Volumes doesn't use ONTAP cluster peering.

## Hybrid peering

Use this section when the source is an ONTAP-mode pool and the destination is a Default-mode volume in NetApp Volumes.

### How NetApp Volumes works

The hybrid peering workflow includes the following steps:

  1. You create a volume migration or external replication on the destination volume in the Google Cloud console or by using Google Cloud CLI. You specify the ONTAP-mode source cluster name, SVM, volume, and source IC-LIF addresses.

  2. If cluster peering isn't already established, NetApp Volumes checks connectivity on the destination, generates a passphrase, and displays peering instructions.

  3. You must perform the remaining peering steps on your ONTAP-mode source pool, because NetApp Volumes doesn't run automated commands on your source pool.




You can't reverse this order. You must create the Default-mode destination first.

### Complete cluster peering on the ONTAP-mode source

Retrieve the passphrase and destination IC-LIF addresses in the Google Cloud console on the Replication or Migration tab or by using Google Cloud CLI:
    
    
     gcloud netapp volumes replications list --volume=DESTINATION_VOLUME --location=LOCATION \
      --format="table(hybridPeeringDetails.command,hybridPeeringDetails.passphrase,hybridPeeringDetails.subnetIp)"
    

On the ONTAP-mode source pool, accept the peering that NetApp Volumes offered on the destination. Set up `ontap_execute` as described in [Common ONTAP-mode procedures](https://docs.cloud.google.com/netapp/volumes/docs/ontap/common-ontap-mode-procedures#set_up_ontap_execute). Set `POOL_NAME` and `LOCATION` for the source pool. List all destination IC-LIF addresses in `PEER_IC_LIF_IPS`, and then run `peer_cluster.py` with `PEER_MODE=accept`:
    
    
     export PROJECT_ID="myproject"
     export LOCATION="us-central1-a"
     export POOL_NAME="ontap-mode-source-pool"
     export PEER_MODE="accept"
     export PEER_IC_LIF_IPS="DESTINATION_IC_LIF_IP_1,DESTINATION_IC_LIF_IP_2"
     export PASSPHRASE="passphrase-from-gcnv-console"
    
     python3 peer_cluster.py
    

Verify the configuration on the source pool:
    
    
     ontap_execute "cluster peer show"
    

### Complete SVM peering on the ONTAP-mode source

If NetApp Volumes doesn't finish SVM peering automatically, it displays a vserver peer command. Run the command by using `ontap_execute`, or accept the pending peer:
    
    
     ontap_execute "vserver peer accept -vserver SOURCE_SVM_NAME -peer-vserver PEER_SVM_NAME"
    

Verify the configuration:
    
    
     ontap_execute "vserver peer show"
    

Return to the hybrid workflow in the Google Cloud console or run `gcloud netapp volumes replications list` to verify that the replication or migration is in progress.

## Manual peering

Use this section when you are establishing peering yourself without a hybrid workflow, for example, before SnapMirror between an ONTAP-mode pool and an external ONTAP cluster, or between two ONTAP-mode pools.

### Before you begin

Complete the following prerequisites:

  1. Confirm that IC-LIFs on the ONTAP-mode pool reach the peer cluster's IC-LIFs. IC-LIFs on ONTAP-mode pools are in IPspace `Gcnv`; on external ONTAP clusters they're in IPspace `Default`. Test ICMP and required intercluster ports.

  2. [Set up ontap_execute](https://docs.cloud.google.com/netapp/volumes/docs/ontap/common-ontap-mode-procedures#set_up_ontap_execute) before you begin.

  3. Collect the cluster name, SVM name, and all peer cluster IC-LIF IP addresses on the ONTAP-mode pool. Provide one address per node, separated by comma. The number of IC-LIFs matches the peer cluster node count.

  4. Share your pool's cluster name, SVM name, and all IC-LIF addresses with the peer cluster administrator.




### Overview

To peer your clusters and SVMs manually, perform the following steps:

  1. [Set up ontap_execute](https://docs.cloud.google.com/netapp/volumes/docs/ontap/common-ontap-mode-procedures#set_up_ontap_execute)

  2. Look up names and IC-LIFs

  3. Verify connectivity

  4. Peer clusters

  5. Peer SVMs

  6. Verify peering




### Look up names and IC-LIFs

On each ONTAP-mode pool, run the lookup commands described in [Common ONTAP-mode procedures](https://docs.cloud.google.com/netapp/volumes/docs/ontap/common-ontap-mode-procedures#look_up_cluster_and_svm_names).

List the IC-LIF addresses, which depend on the pool size, and provide them to the peer cluster administrator.

### Verify connectivity

Run a ping command to peer IC-LIFs from your pool by using the `-vserver Gcnv` flag:
    
    
     ontap_execute "network ping -vserver Gcnv -destination PEER_IC_LIF_IP -lif intercluster-1"
    

Fix routing or firewall issues before you continue. If the ping fails between pools, see [Why your NetApp Volumes can't reach Active Directory (and other networks behind your VPC)](https://community.netapp.com/t5/Tech-ONTAP-Blogs/Why-your-NetApp-Volumes-can-t-reach-Active-Directory-and-other-networks-behind/ba-p/467585) for VPC and partner network guidance.

### Peer clusters

To peer the clusters, use one of the following scenarios:

  * Scenario A: ONTAP-mode pool and external ONTAP

  * Scenario B: Two ONTAP-mode pools




#### Scenario A: ONTAP-mode pool and external ONTAP

To peer an ONTAP-mode pool with an external ONTAP cluster, perform the following steps:

  1. **Offer on the ONTAP-mode pool** : run `cluster peer create -generate-passphrase` command by using `ontap_execute` with all peer IC-LIF addresses. Copy the passphrase from the command output.

  2. **Accept on the external ONTAP** : the peer cluster administrator runs `cluster peer accept` command at the ONTAP prompt with all ONTAP-mode IC-LIF addresses and enters the passphrase.




To offer peering on the ONTAP-mode pool:
    
    
     ontap_execute "cluster peer create -ipspace Gcnv -peer-addrs PEER_IC_LIF_1,PEER_IC_LIF_2 -generate-passphrase"
    

List every IC-LIF address for the peer cluster in the `-peer-addrs` flag, separated by commas. Add additional addresses if the peer cluster has more than two nodes.

ONTAP displays the passphrase in the command output under `Passphrase:`. Copy the passphrase immediately; ONTAP warns that it can't display the passphrase again.

If the command fails or the output doesn't include a passphrase, use `peer_cluster.py` with `PEER_MODE=offer` instead. For more information, see Cluster peering script.

Copy the passphrase and send it to the external ONTAP administrator. Accept the offer within the passphrase validity period, which is one hour by default.

Accept the offer on the external ONTAP cluster at the peer cluster prompt by listing all ONTAP-mode IC-LIF addresses:
    
    
     cluster peer accept -ipspace Default -peer-addrs ONTAP_MODE_IC_LIF_1,ONTAP_MODE_IC_LIF_2
    

Enter the passphrase when ONTAP prompts you. Include every IC-LIF address from the ONTAP-mode pool.

Verify the configuration on the ONTAP-mode pool:
    
    
     ontap_execute "cluster peer show"
    

#### Scenario B: Two ONTAP-mode pools

To peer two ONTAP-mode pools, perform the following steps:

  1. **Offer on pool A** : run `cluster peer create -generate-passphrase` command by using `ontap_execute` on pool A. List all IC-LIF addresses from pool B in `-peer-addrs`. Copy the passphrase.

  2. **Accept on pool B** : run `peer_cluster.py` with `PEER_MODE=accept` on pool B, and list all IC-LIF addresses from pool A in `PEER_IC_LIF_IPS`.




Offer on pool A:
    
    
     ontap_execute "cluster peer create -ipspace Gcnv -peer-addrs POOL_B_IC_LIF_1,POOL_B_IC_LIF_2 -generate-passphrase"
    

List every IC-LIF from pool B, separated by comma. Add additional addresses when pool B has more than two nodes. Copy the `Passphrase:` value from the command output.

If the command fails, use `peer_cluster.py` with `PEER_MODE=offer` on pool A.

Accept on pool B:
    
    
     export PROJECT_ID="myproject"
     export LOCATION="us-west1-b"
     export POOL_NAME="pool-b"
     export PEER_MODE="accept"
     export PEER_IC_LIF_IPS="POOL_A_IC_LIF_1,POOL_A_IC_LIF_2"
     export PASSPHRASE="passphrase-from-pool-a"
    
     python3 peer_cluster.py
    

List every IC-LIF from pool A in `PEER_IC_LIF_IPS`.

Verify the configuration on each pool:
    
    
     ontap_execute "cluster peer show"
    

Confirm that availability is Available and authentication is OK.

### Peer SVMs

After cluster peering succeeds, create an SVM peer for SnapMirror. If you need FlexCache, add it to the `-applications` flag.

#### Scenario A: ONTAP-mode pool and external ONTAP

To peer an ONTAP-mode pool with an external ONTAP cluster, perform the following steps:

  1. **Create on external ONTAP** : the peer cluster administrator runs `vserver peer create` command at the ONTAP prompt.

  2. **Accept on the ONTAP-mode pool** : run the `vserver peer accept` command by using `ontap_execute`.




Create the peer on the external ONTAP cluster at the peer cluster prompt:
    
    
     vserver peer create -vserver PEER_SVM_NAME -peer-vserver ONTAP_MODE_SVM_NAME \
      -peer-cluster ONTAP_MODE_CLUSTER_NAME -applications snapmirror
    

Accept the peer on the ONTAP-mode pool:
    
    
     ontap_execute "vserver peer accept -vserver ONTAP_MODE_SVM_NAME -peer-vserver PEER_SVM_NAME"
    

#### Scenario B: Two ONTAP-mode pools

To peer two ONTAP-mode pools, perform the following steps:

  1. **Create on pool A** : run the `vserver peer create` command by using `ontap_execute` on pool A (or `peer_svm.py` if the create command is unavailable).

  2. **Accept on pool B** : run the `vserver peer accept` command by using `ontap_execute` on pool B.




Create the peer on pool A:
    
    
     ontap_execute "vserver peer create -vserver POOL_A_SVM -peer-vserver POOL_B_SVM -peer-cluster POOL_B_CLUSTER_NAME -applications snapmirror"
    

Accept the peer on pool B:
    
    
     ontap_execute "vserver peer accept -vserver POOL_B_SVM -peer-vserver POOL_A_SVM"
    

Don't create the same SVM peer on both pools.

### Verify peering

To verify peering on the ONTAP-mode pool:
    
    
     ontap_execute "cluster peer show"
     ontap_execute "vserver peer show"
    

Confirm that the cluster peer availability is Available and the SVM peer State is peered.

For Scenario B, repeat the procedure on the second pool. The external ONTAP administrator can verify the configuration by running `cluster peer show` and `vserver peer show` on the peer cluster.

When no cluster peers exist, the `cluster peer show` command returns that the entry doesn't exist.

### Delete peering

Delete SVM peers before cluster peers.

To delete an SVM peer on one pool, delete it to remove the relationship on both sides when pools are reachable.
    
    
     ontap_execute "vserver peer delete -vserver LOCAL_SVM_NAME -peer-vserver PEER_SVM_NAME"
    

The ONTAP CLI proxy doesn't support cluster peer deletion. To delete a cluster peer, delete it by UUID through the REST API.

First, list the peers to find the UUID:
    
    
     TOKEN=$(gcloud auth print-access-token)
     curl -s -H "Authorization: Bearer $TOKEN" \
    
     "https://netapp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/storagePools/POOL_NAME/ontap/api/cluster/peers"
    

Delete each returned UUID:
    
    
     curl -s -X DELETE -H "Authorization: Bearer $TOKEN" \
    
     "https://netapp.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/storagePools/POOL_NAME/ontap/api/cluster/peers/PEER_UUID"
    

Repeat this process on both ONTAP-mode pools in Scenario B. For Scenario A, run `cluster peer delete` on the external ONTAP cluster if needed.

## Cluster peering script

Save the following as `peer_cluster.py`. Use it on an ONTAP-mode pool when that pool must accept a cluster peering offer (`PEER_MODE=accept`). Hybrid peering and Scenario B use `accept` mode. Use `offer` mode (`PEER_MODE=offer`) only if `cluster peer create -generate-passphrase` fails through `ontap_execute` or doesn't return a passphrase. This script requires Python 3.8 or later and the Python standard library.
    
    
     #!/usr/bin/env python3
    """Cluster peer offer or accept on an ONTAP-mode pool through the NetApp Volumes REST proxy."""
    
    import json
    import os
    import subprocess
    import sys
    import time
    import urllib.error
    import urllib.request
    
    REQUIRED = ("PROJECT_ID", "LOCATION", "POOL_NAME", "PEER_MODE")
    missing = [name for name in REQUIRED if not os.environ.get(name)]
    if missing:
        sys.exit(f"Set required environment variables: {', '.join(missing)}")
    
    PROJECT_ID = os.environ["PROJECT_ID"]
    LOCATION = os.environ["LOCATION"]
    POOL_NAME = os.environ["POOL_NAME"]
    PEER_MODE = os.environ["PEER_MODE"].lower()
    POLL_INTERVAL = int(os.environ.get("POLL_INTERVAL", "10"))
    
    API_ROOT = (
        f"https://netapp.googleapis.com/v1/projects/{PROJECT_ID}"
        f"/locations/{LOCATION}/storagePools/{POOL_NAME}/ontap/api"
    )
    
    def parse_ip_list(value: str) -> list:
        return [ip.strip() for ip in value.replace("#", ",").split(",") if ip.strip()]
    
    def get_access_token() -> str:
        return subprocess.check_output(
            ["gcloud", "auth", "print-access-token"], text=True
        ).strip()
    
    def api_request(method: str, path: str, body=None) -> dict:
        headers = {
            "Authorization": f"Bearer {get_access_token()}",
            "Content-Type": "application/json",
        }
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(f"{API_ROOT}{path}", data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode()
            sys.exit(f"API request failed ({exc.code}): {detail}")
    
    def job_record(response: dict) -> dict:
        return response.get("rawResponse") or response.get("body") or response
    
    def job_state(response: dict) -> str:
        return job_record(response).get("state", "")
    
    def format_job_error(response: dict) -> str:
        record = job_record(response)
        message = record.get("message") or record.get("error", {}).get("message")
        if message:
            return message
        return json.dumps(response, indent=2)
    
    def wait_for_job(job_uuid: str) -> None:
        print(f"ONTAP job UUID: {job_uuid}")
        while True:
            response = api_request("GET", f"/cluster/jobs/{job_uuid}")
            state = job_state(response)
            print(f"  Job state: {state}")
            if state == "success":
                return
            if state in ("failure", "error"):
                sys.exit(f"Job failed: {format_job_error(response)}")
            time.sleep(POLL_INTERVAL)
    
    def extract_passphrase(response: dict) -> str:
        body = response.get("body") or response.get("rawResponse") or {}
        records = body.get("records") or []
        if records:
            auth = records[0].get("authentication") or {}
            if auth.get("passphrase"):
                return auth["passphrase"]
        auth = body.get("authentication") or {}
        return auth.get("passphrase", "")
    
    def build_offer_body() -> dict:
        if not os.environ.get("PEER_IC_LIF_IPS"):
            sys.exit("Set PEER_IC_LIF_IPS for offer mode")
    
        payload = {
            "remote": {"ip_addresses": parse_ip_list(os.environ["PEER_IC_LIF_IPS"])},
            "authentication": {"generate_passphrase": True},
            "ipspace": {"name": os.environ.get("IPSPACE", "Gcnv")},
        }
    
        expiry = os.environ.get("EXPIRY_TIME")
        if expiry:
            payload["authentication"]["expiry_time"] = expiry
    
        local_svm = os.environ.get("LOCAL_SVM_NAME")
        if local_svm:
            payload["initial_allowed_svms"] = [{"name": local_svm}]
    
        apps = os.environ.get("PEER_APPLICATIONS", "snapmirror")
        payload["peer_applications"] = [a.strip() for a in apps.split(",") if a.strip()]
    
        encryption = os.environ.get("ENCRYPTION_PROPOSED")
        if encryption:
            payload["encryption"] = {"proposed": encryption}
    
        return {"body": payload}
    
    def build_accept_body() -> dict:
        for name in ("PEER_IC_LIF_IPS", "PASSPHRASE"):
            if not os.environ.get(name):
                sys.exit(f"Set {name} for accept mode")
    
        return {
            "body": {
                "remote": {"ip_addresses": parse_ip_list(os.environ["PEER_IC_LIF_IPS"])},
                "authentication": {"passphrase": os.environ["PASSPHRASE"]},
                "ipspace": {"name": os.environ.get("IPSPACE", "Gcnv")},
            }
        }
    
    def main() -> None:
        if PEER_MODE == "offer":
            body = build_offer_body()
            print("Creating cluster peer offer...")
        elif PEER_MODE == "accept":
            body = build_accept_body()
            print("Accepting cluster peer offer...")
        else:
            sys.exit("PEER_MODE must be 'offer' or 'accept'")
    
        response = api_request("POST", "/cluster/peers?return_records=true", body)
    
        job = (response.get("body") or {}).get("job") or response.get("job")
        if job and job.get("uuid"):
            wait_for_job(job["uuid"])
    
        if PEER_MODE == "offer":
            passphrase = extract_passphrase(response)
            if passphrase:
                print(f"\nPassphrase (provide to the peer pool): {passphrase}")
            else:
                print(json.dumps(response, indent=2))
    
    if __name__ == "__main__":
        main()
    

**Note:** Don't set the `remote.name` field in the offer request. ONTAP discovers the peer cluster name from the IC-LIF addresses.

Optional environment variables: `EXPIRY_TIME`, `PEER_APPLICATIONS` (default `snapmirror`), `ENCRYPTION_PROPOSED`, and `IPSPACE` (default `Gcnv`).

### SVM peering script (fallback)

Use `peer_svm.py` only when `vserver peer create` isn't available through the ONTAP CLI proxy. Instead, use `vserver peer create` and `vserver peer accept` as described in Peer SVMs.
    
    
     #!/usr/bin/env python3
    """Create an SVM peer on an ONTAP-mode pool (fallback when vserver peer create is unavailable)."""
    
    import json
    import os
    import subprocess
    import sys
    import time
    import urllib.error
    import urllib.request
    
    REQUIRED = (
        "PROJECT_ID", "LOCATION", "POOL_NAME",
        "LOCAL_SVM_NAME", "PEER_CLUSTER_NAME", "PEER_SVM_NAME",
    )
    missing = [name for name in REQUIRED if not os.environ.get(name)]
    if missing:
        sys.exit(f"Set required environment variables: {', '.join(missing)}")
    
    PROJECT_ID = os.environ["PROJECT_ID"]
    LOCATION = os.environ["LOCATION"]
    POOL_NAME = os.environ["POOL_NAME"]
    LOCAL_SVM_NAME = os.environ["LOCAL_SVM_NAME"]
    PEER_CLUSTER_NAME = os.environ["PEER_CLUSTER_NAME"]
    PEER_SVM_NAME = os.environ["PEER_SVM_NAME"]
    APPLICATIONS = [
        app.strip()
        for app in os.environ.get("APPLICATIONS", "snapmirror").split(",")
        if app.strip()
    ]
    POLL_INTERVAL = int(os.environ.get("POLL_INTERVAL", "10"))
    
    API_ROOT = (
        f"https://netapp.googleapis.com/v1/projects/{PROJECT_ID}"
        f"/locations/{LOCATION}/storagePools/{POOL_NAME}/ontap/api"
    )
    
    def get_access_token() -> str:
        return subprocess.check_output(
            ["gcloud", "auth", "print-access-token"], text=True
        ).strip()
    
    def api_request(method: str, path: str, body=None) -> dict:
        headers = {
            "Authorization": f"Bearer {get_access_token()}",
            "Content-Type": "application/json",
        }
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(f"{API_ROOT}{path}", data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as exc:
            sys.exit(f"API request failed ({exc.code}): {exc.read().decode()}")
    
    def format_job_error(response: dict) -> str:
        record = response.get("rawResponse") or response.get("body") or response
        message = record.get("message") or record.get("error", {}).get("message")
        return message or json.dumps(response, indent=2)
    
    def wait_for_job(job_uuid: str) -> None:
        while True:
            response = api_request("GET", f"/cluster/jobs/{job_uuid}")
            record = response.get("rawResponse") or response.get("body") or response
            state = record.get("state", "")
            print(f"  Job state: {state}")
            if state == "success":
                print("SVM peer relationship created.")
                return
            if state in ("failure", "error"):
                sys.exit(f"Job failed: {format_job_error(response)}")
            time.sleep(POLL_INTERVAL)
    
    def main() -> None:
        body = {
            "body": {
                "svm": {"name": LOCAL_SVM_NAME},
                "peer": {
                    "cluster": {"name": PEER_CLUSTER_NAME},
                    "svm": {"name": PEER_SVM_NAME},
                },
                "applications": APPLICATIONS,
            }
        }
        response = api_request("POST", "/svm/peers?return_records=true", body)
        job = (response.get("body") or {}).get("job") or response.get("job")
        if not job or not job.get("uuid"):
            print(json.dumps(response, indent=2))
            return
        wait_for_job(job["uuid"])
    
    if __name__ == "__main__":
        main()
    

## What's next

  * Create SnapMirror relationships with `snapmirror create` and `snapmirror initialize` on the ONTAP-mode pool. For more information, see [SnapMirror](https://docs.cloud.google.com/netapp/volumes/docs/discover/features#snapmirror).

  * [Create FlexCache volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/create-flexcache-volume) after you peered with the FlexCache application.

  * For hybrid workflows, return to [Create an external replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/create-external-replication) or [Create a volume migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/create-volume-migration).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
