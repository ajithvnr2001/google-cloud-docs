---
url: https://docs.cloud.google.com/tpu/docs/SAX-on-inference-converter/
title: SAX on Cloud TPU v5e \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:27.160566+00:00
---

# SAX on Cloud TPU v5e  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/SAX-on-inference-converter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SAX on Cloud TPU v5e 

## SAX cluster (SAX cell)

SAX admin server and SAX model server are two essential components that run a SAX cluster.

### SAX admin server

The SAX admin server monitors and coordinates all SAX model servers in a SAX cluster. In a SAX cluster, you can launch multiple SAX admin servers, where only one of the SAX admin server is active through leader election, the others are standby servers. When the active admin server fails, a standby admin server will become active. The active SAX admin server assigns model replicas and inference requests to available SAX model servers.

### SAX admin storage bucket

Each SAX cluster requires a Cloud Storage bucket to store the configurations and locations of SAX admin servers and SAX model servers in the SAX cluster.

### SAX model server

The SAX model server loads a model checkpoint and runs inference with [GSPMD](https://arxiv.org/abs/2105.04663). A SAX model server runs on a single TPU VM worker. Single-host TPU model serving requires a single SAX model server on a single-host TPU VM. Multi-host TPU model serving requires a group of SAX model servers on a multi-host TPU slice. Multi-host model serving is currently not available, but this document does provide an example with a 175B test model for preview.

### SAX model serving

The following section walks through the workflow for serving language models using SAX. It uses the GPT-J 6B model as an example for single-host model serving.

Before starting, install the Cloud TPU SAX Docker images on your TPU VM:
    
    
    sudo usermod -a -G docker ${USER}
    newgrp docker
    
    gcloud auth configure-docker us-docker.pkg.dev
    
    SAX_ADMIN_SERVER_IMAGE_NAME="us-docker.pkg.dev/cloud-tpu-images/inference/sax-admin-server"
    SAX_MODEL_SERVER_IMAGE_NAME="us-docker.pkg.dev/cloud-tpu-images/inference/sax-model-server"
    SAX_UTIL_IMAGE_NAME="us-docker.pkg.dev/cloud-tpu-images/inference/sax-util"
    
    SAX_VERSION=v1.2.0
    
    export SAX_ADMIN_SERVER_IMAGE_URL=${SAX_ADMIN_SERVER_IMAGE_NAME}:${SAX_VERSION}
    export SAX_MODEL_SERVER_IMAGE_URL=${SAX_MODEL_SERVER_IMAGE_NAME}:${SAX_VERSION}
    export SAX_UTIL_IMAGE_URL="${SAX_UTIL_IMAGE_NAME}:${sax_version}"
    
    docker pull ${SAX_ADMIN_SERVER_IMAGE_URL}
    docker pull ${SAX_MODEL_SERVER_IMAGE_URL}
    docker pull ${SAX_UTIL_IMAGE_URL}

Set some other variables you will use later:
    
    
    export SAX_ADMIN_SERVER_DOCKER_NAME="sax-admin-server"
    export SAX_MODEL_SERVER_DOCKER_NAME="sax-model-server"
    export SAX_CELL="/sax/test"

### GPT-J 6B single-host model serving example

Single-host model serving is applicable to single-host TPU slice, that is, v5litepod-1, v5litepod-4 and v5litepod-8.

  1. Create a SAX cluster

     1. Create a Cloud Storage storage bucket for the SAX cluster:
            
            SAX_ADMIN_STORAGE_BUCKET=${your_admin_storage_bucket}
            
            gcloud storage buckets create gs://${SAX_ADMIN_STORAGE_BUCKET} \
            --project=${PROJECT_ID}

You might need another Cloud Storage storage bucket to store the checkpoint.
            
            SAX_DATA_STORAGE_BUCKET=${your_data_storage_bucket}

     2. SSH into your TPU VM in a terminal to launch the SAX admin server:

**Note:** You can also launch your SAX admin server from a local shell instead of a TPU VM.
            
            docker run \
            --name ${SAX_ADMIN_SERVER_DOCKER_NAME} \
            -it \
            -d \
            --rm \
            --network host \
            --env GSBUCKET=${SAX_ADMIN_STORAGE_BUCKET} \
            ${SAX_ADMIN_SERVER_IMAGE_URL}

You can check the docker log by: 
            
            docker logs -f ${SAX_ADMIN_SERVER_DOCKER_NAME}

The output in the log will look similar to the following:
            
            I0829 01:22:31.184198       7 config.go:111] Creating config fs_root: "gs://test_sax_admin/sax-fs-root"
            I0829 01:22:31.347883       7 config.go:115] Created config fs_root: "gs://test_sax_admin/sax-fs-root"
            I0829 01:22:31.360837      24 admin_server.go:44] Starting the server
            I0829 01:22:31.361420      24 ipaddr.go:39] Skipping non-global IP address 127.0.0.1/8.
            I0829 01:22:31.361455      24 ipaddr.go:39] Skipping non-global IP address ::1/128.
            I0829 01:22:31.361462      24 ipaddr.go:39] Skipping non-global IP address fe80::4001:aff:fe8e:fc8/64.
            I0829 01:22:31.361469      24 ipaddr.go:39] Skipping non-global IP address fe80::42:bfff:fef9:1bd3/64.
            I0829 01:22:31.361474      24 ipaddr.go:39] Skipping non-global IP address fe80::20fb:c3ff:fe5b:baac/64.
            I0829 01:22:31.361482      24 ipaddr.go:56] IPNet address 10.142.15.200
            I0829 01:22:31.361488      24 ipaddr.go:56] IPNet address 172.17.0.1
            I0829 01:22:31.456952      24 admin.go:305] Loaded config: fs_root: "gs://test_sax_admin/sax-fs-root"
            I0829 01:22:31.609323      24 addr.go:105] SetAddr /gcs/test_sax_admin/sax-root/sax/test/location.proto "10.142.15.200:10000"
            I0829 01:22:31.656021      24 admin.go:325] Updated config: fs_root: "gs://test_sax_admin/sax-fs-root"
            I0829 01:22:31.773245      24 mgr.go:781] Loaded manager state
            I0829 01:22:31.773260      24 mgr.go:784] Refreshing manager state every 10s
            I0829 01:22:31.773285      24 admin.go:350] Starting the server on port 10000
            I0829 01:22:31.773292      24 cloud.go:506] Starting the HTTP server on port 8080

  2. Launch a single-host SAX model server into the SAX cluster:

At this point, the SAX cluster contains only the SAX admin server. You can connect to your TPU VM over SSH in a second terminal to launch a SAX model server in your SAX cluster:
         
         docker run \
             --privileged  \
             -it \
             -d \
             --rm \
             --network host \
             --name ${SAX_MODEL_SERVER_DOCKER_NAME} \
             --env SAX_ROOT=gs://${SAX_ADMIN_STORAGE_BUCKET}/sax-root \
             ${SAX_MODEL_SERVER_IMAGE_URL} \
                --sax_cell=${SAX_CELL} \
                --port=10001 \
                --platform_chip=tpuv4 \
                --platform_topology=1x1

  3. Convert model checkpoint:

You need to install PyTorch and Transformers to download the GPT-J checkpoint from EleutherAI:
         
         pip3 install accelerate
         pip3 install torch
         pip3 install transformers

To convert the checkpoint to SAX checkpoint, you need to install `paxml`:
         
         pip3 install paxml==1.1.0

The following [script](https://github.com/google/saxml/blob/main/saxml/tools/convert_gptj_ckpt.py) converts the GPT-J checkpoint to SAX checkpoint:
         
         python3 -m convert_gptj_ckpt --base EleutherAI/gpt-j-6b --pax pax_6b

After the conversion is done: 
         
         ls checkpoint_00000000/

You need to create a commit_success file and placed in the sub directories:
         
         gcloud storage cp checkpoint_00000000 ${CHECKPOINT_PATH} --recursive
         
         touch commit_success.txt
         gcloud storage cp commit_success.txt ${CHECKPOINT_PATH}/
         gcloud storage cp commit_success.txt ${CHECKPOINT_PATH}/metadata/
         gcloud storage cp commit_success.txt ${CHECKPOINT_PATH}/state/
         

  4. Publish the model to SAX cluster

You can now publish GPT-J with the checkpoint converted in the previous step.
         
         MODEL_NAME=gptjtokenizedbf16bs32
         MODEL_CONFIG_PATH=saxml.server.pax.lm.params.gptj.GPTJ4TokenizedBF16BS32
         REPLICA=1

To publish the GPT-J (and steps afterward), use SSH to connect to your TPU VM in a third terminal:
         
         docker run \
          ${SAX_UTIL_IMAGE_URL} \
            --sax_root=gs://${SAX_ADMIN_STORAGE_BUCKET}/sax-root \
            publish \
              ${SAX_CELL}/${MODEL_NAME} \
              ${MODEL_CONFIG_PATH} \
              ${CHECKPOINT_PATH} \
              ${REPLICA}

You will see a lot of activity from the model server Docker log until you see something like the following to indicate the model has loaded successfully:
         
         I0829 01:33:49.287459 139865140229696 servable_model.py:697] loading completed.
         

  5. Generate inference results

For GPT-J, input and output must be formatted as a comma separated token ID string. You will need to tokenize the text input.
         
         TEXT = "Below is an instruction that describes a task, paired with
         an input that provides further context. Write a response that
         appropriately completes the request.\n\n### Instruction\:\nSummarize the
         following news article\:\n\n### Input\:\nMarch 10, 2015 . We're truly
         international in scope on Tuesday. We're visiting Italy, Russia, the
         United Arab Emirates, and the Himalayan Mountains. Find out who's
         attempting to circumnavigate the globe in a plane powered partially by the
         sun, and explore the mysterious appearance of craters in northern Asia.
         You'll also get a view of Mount Everest that was previously reserved for
         climbers. On this page you will find today's show Transcript and a place
         for you to request to be on the CNN Student News Roll Call. TRANSCRIPT .
         Click here to access the transcript of today's CNN Student News program.
         Please note that there may be a delay between the time when the video is
         available and when the transcript is published. CNN Student News is
         created by a team of journalists who consider the Common Core State
         Standards, national standards in different subject areas, and state
         standards when producing the show. ROLL CALL . For a chance to be
         mentioned on the next CNN Student News, comment on the bottom of this page
         with your school name, mascot, city and state. We will be selecting
         schools from the comments of the previous show. You must be a teacher or a
         student age 13 or older to request a mention on the CNN Student News Roll
         Call! Thank you for using CNN Student News!\n\n### Response\:

You can obtain the token IDs string through the EleutherAI/gpt-j-6b tokenizer:
         
         from transformers import GPT2Tokenizer
         tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-j-6b")                  :

Tokenize the input text:
         
         encoded_example = tokenizer(TEXT)
         input_ids = encoded_example.input_ids
         INPUT_STR = ",".join([str(input_id) for input_id in input_ids])

You can expect a token ID string similar to the following:
         
         >>> INPUT_STR
         '21106,318,281,12064,326,8477,257,4876,11,20312,351,281,5128,326,3769,2252,4732,13,19430,257,2882,326,20431,32543,262,2581,13,198,198,21017,46486,25,198,13065,3876,1096,262,1708,1705,2708,25,198,198,21017,23412,25,198,16192,838,11,1853,764,775,821,4988,3230,287,8354,319,3431,13,775,821,10013,8031,11,3284,11,262,1578,4498,24880,11,290,262,42438,22931,21124,13,9938,503,508,338,9361,284,2498,4182,615,10055,262,13342,287,257,6614,13232,12387,416,262,4252,11,290,7301,262,11428,5585,286,1067,8605,287,7840,7229,13,921,1183,635,651,257,1570,286,5628,41336,326,373,4271,10395,329,39311,13,1550,428,2443,345,481,1064,1909,338,905,42978,290,257,1295,329,345,284,2581,284,307,319,262,8100,13613,3000,8299,4889,13,48213,6173,46023,764,6914,994,284,1895,262,14687,286,1909,338,8100,13613,3000,1430,13,4222,3465,326,612,743,307,257,5711,1022,262,640,618,262,2008,318,1695,290,618,262,14687,318,3199,13,8100,13613,3000,318,2727,416,257,1074,286,9046,508,2074,262,8070,7231,1812,20130,11,2260,5423,287,1180,2426,3006,11,290,1181,5423,618,9194,262,905,13,15107,3069,42815,764,1114,257,2863,284,307,4750,319,262,1306,8100,13613,3000,11,2912,319,262,4220,286,428,2443,351,534,1524,1438,11,37358,11,1748,290,1181,13,775,481,307,17246,4266,422,262,3651,286,262,2180,905,13,921,1276,307,257,4701,393,257,3710,2479,1511,393,4697,284,2581,257,3068,319,262,8100,13613,3000,8299,4889,0,6952,345,329,1262,8100,13613,3000,0,198,198,21017,18261,25'

To generate a summary for your article:
         
         docker run \
           ${SAX_UTIL_IMAGE_URL} \
             --sax_root=gs://${SAX_ADMIN_STORAGE_BUCKET}/sax-root \
             lm.generate \
               ${SAX_CELL}/${MODEL_NAME} \
               ${INPUT_STR}
         

You can expect something similar to:
         
         +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+
         |                                                                                                                                                    GENERATE                                                                                                                                                    |    SCORE     |
         +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+
         | 1212,2443,3407,262,905,42978,764,198,11041,262,42978,284,1037,2444,351,3555,35915,290,25818,764,198,2953,262,4220,286,262,2443,11,2912,329,257,2863,284,307,4750,319,8100,13613,3000,13,220,921,1276,307,257,4701,393,257,3710,2479,1511,393,4697,284,2581,257,3068,319,262,8100,13613,3000,8299,4889,13,50256 | -0.023136413 |
         | 1212,2443,3407,262,905,42978,764,198,11041,262,42978,284,1037,2444,351,3555,35915,290,25818,764,198,2953,262,4220,286,262,2443,11,2912,329,257,2863,284,307,4750,319,8100,13613,3000,13,220,921,1276,307,257,4701,393,257,3710,2479,1511,393,4697,284,2581,257,3068,319,262,8100,13613,3000,8299,4889,0,50256  |  -0.91842502 |
         | 1212,2443,3407,262,905,42978,764,198,11041,262,42978,284,1037,2444,351,3555,35915,290,25818,764,198,2953,262,4220,286,262,2443,11,2912,329,257,2863,284,307,4750,319,8100,13613,3000,13,921,1276,307,257,4701,393,257,3710,2479,1511,393,4697,284,2581,257,3068,319,262,8100,13613,3000,8299,4889,13,50256     |   -1.1726116 |
         | 1212,2443,3407,262,905,42978,764,198,11041,262,42978,284,1037,2444,351,3555,35915,290,25818,764,198,2953,262,4220,286,262,2443,11,2912,329,257,2863,284,307,4750,319,8100,13613,3000,13,220,921,1276,307,1511,393,4697,284,2581,257,3068,319,262,8100,13613,3000,8299,4889,13,50256                            |   -1.2472695 |
         +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+

To detokenize the output token IDs string:
         
         output_token_ids = [int(token_id) for token_id in OUTPUT_STR.split(',')]
         OUTPUT_TEXT = tokenizer.decode(output_token_ids, skip_special_tokens=True)
         

You can expect the detokenized text as:
         
         >>> OUTPUT_TEXT
         'This page includes the show Transcript.\nUse the Transcript to help
         students with reading comprehension and vocabulary.\nAt the bottom of
         the page, comment for a chance to be mentioned on CNN Student News.
         You must be a teacher or a student age 13 or older to request a mention on the CNN Student News Roll Call.'

  6. Clean up your Docker containers and Cloud Storage storage buckets.




### 175B multi-host model serving preview

Some of the large language models will require a multi-host TPU slice, that is, v5litepod-16 and above. In those cases, all multi-host TPU hosts will need to have a copy of a SAX model server, and all model servers function as a SAX model server group to serve the large model on a multi-host TPU slice.

  1. Create a new SAX cluster

You can follow the same step of Create a SAX cluster in the GPT-J walk through to create a new SAX cluster and a SAX admin server.

Or, if you already have an existing SAX cluster, you can launch a multi-host model server into your SAX cluster.

  2. Launch a multi-host SAX model server into a SAX cluster

Use the same command to create a multi-host TPU slice as you use for a single-host TPU slice, just specify the appropriate multi-host accelerator type:
         
         ACCELERATOR_TYPE=v5litepod-32
         ZONE=us-east1-c
         
         gcloud alpha compute tpus queued-resources create ${QUEUED_RESOURCE_ID} \
           --node-id ${TPU_NAME} \
           --project ${PROJECT_ID} \
           --zone ${ZONE} \
           --accelerator-type ${ACCELERATOR_TYPE} \
           --runtime-version ${RUNTIME_VERSION} \
           --service-account ${SERVICE_ACCOUNT} \
           --reserved
         

To pull the SAX model server image to all TPU hosts/workers and launch them:
         
         gcloud compute tpus tpu-vm ssh ${TPU_NAME} \
           --project ${PROJECT_ID} \
           --zone ${ZONE} \
           --worker=all \
           --command="
             gcloud auth configure-docker \
               us-docker.pkg.dev
             # Pull sax model server image
             docker pull ${SAX_MODEL_SERVER_IMAGE_URL}
             # Run model server
             docker run \
               --privileged  \
               -it \
               -d \
               --rm \
               --network host \
               --name ${SAX_MODEL_SERVER_DOCKER_NAME} \
               --env SAX_ROOT=gs://${SAX_ADMIN_STORAGE_BUCKET}/sax-root \
               ${SAX_MODEL_SERVER_IMAGE_URL} \
                 --sax_cell=${SAX_CELL} \
                 --port=10001 \
                 --platform_chip=tpuv4 \
                 --platform_topology=1x1"
         

  3. Publish the model to SAX cluster

This example uses a [LmCloudSpmd175B32Test](https://github.com/google/saxml/blob/main/saxml/server/pax/lm/params/lm_cloud.py) model:
         
         MODEL_NAME=lmcloudspmd175b32test
         MODEL_CONFIG_PATH=saxml.server.pax.lm.params.lm_cloud.LmCloudSpmd175B32Test
         CHECKPOINT_PATH=None
         REPLICA=1

To publish the test model:
         
         docker run \
          ${SAX_UTIL_IMAGE_URL} \
            --sax_root=gs://${SAX_ADMIN_STORAGE_BUCKET}/sax-root \
            publish \
              ${SAX_CELL}/${MODEL_NAME} \
              ${MODEL_CONFIG_PATH} \
              ${CHECKPOINT_PATH} \
              ${REPLICA}

  4. Generate inference results
         
         docker run \
           ${SAX_UTIL_IMAGE_URL} \
             --sax_root=gs://${SAX_ADMIN_STORAGE_BUCKET}/sax-root \
             lm.generate \
               ${SAX_CELL}/${MODEL_NAME} \
               "Q:  Who is Harry Porter's mother? A\: "
         

Note that since this example uses a test model with random weights, the output may not be meaningful.

  5. Clean Up

Stop the docker containers:
         
         docker stop ${SAX_ADMIN_SERVER_DOCKER_NAME}
         docker stop ${SAX_MODEL_SERVER_DOCKER_NAME}

Delete your Cloud Storage admin storage bucket and any data storage bucket using the gcloud CLI as shown below.
         
         gcloud storage rm gs://${SAX_ADMIN_STORAGE_BUCKET} --recursive --continue-on-error
         gcloud storage rm gs://${SAX_DATA_STORAGE_BUCKET} --recursive --continue-on-error




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
