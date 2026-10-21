---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/anomaly_detection_iforest/
title: Anomaly Detection with Ensemble Models using Apache Beam (Isolation Forest and LOF) \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:36:07.987648+00:00
---

# Anomaly Detection with Ensemble Models using Apache Beam (Isolation Forest and LOF)  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/anomaly_detection_iforest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Anomaly Detection with Ensemble Models using Apache Beam (Isolation Forest and LOF) Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/anomaly_detection/anomaly_detection_iforest.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/anomaly_detection/anomaly_detection_iforest.ipynb) This notebook demonstrates how to perform anomaly detection on streaming data using the AnomalyDetection PTransform, a new feature introduced in Apache Beam 2.64.0 with more improvement on offline model support in 2.65.0. This notebook is divided into two main sections:

  * Running a Single Offline Model: We will first fetch the data set of Statlog (shuttle) from UCI Machine Learning Repository (cached in gs://apache-beam-samples/anomaly_detection/shuttle/, original link: <https://archive.ics.uci.edu/dataset/148/statlog>+shuttle). This data will be streamed into the pipeline following a periodic impulse. Our Beam pipeline will then apply the AnomalyDetection PTransform with the a pre-trained isolation forest model, compute model metrics.
  * Running an Ensemble of Models: Using the same training data, we now train a second offline model and



## Preparation

### Setting Environment Variables
    
    
    # GCP project id
    PROJECT_ID = 'apache-beam-testing'  # @param {type:'string'}
    
    # Temporary root path, used to store generated files (and temp and staging files if running on Dataflow)
    TEMP_ROOT = 'gs://apache-beam-testing-temp'  # @param {type:'string'}
    
    # Required if running on Dataflow
    REGION = 'us-central1'  # @param {type:'string'}
    
    # TODO: Change this to an official release once 2.65.0 is available
    BEAM_VERSION = '2.65.0rc2'
    
    import random
    SUFFIX = str(random.randint(0, 10000))
    
    
    
    
    
    
    
    from google.colab import auth
    auth.authenticate_user(project_id=PROJECT_ID)
    
    
    
    
    

### Installing Beam and Other Dependencies
    
    
    # For running with local prism runner
    pip install 'apache_beam[interactive]=={BEAM_VERSION}' --quiet
    
    
    # Download the latest prism
    # TODO: We don't need this step once 2.65.0 is available.
     wget https://dist.apache.org/repos/dist/dev/beam/2.65.0/prism/linux/amd64/apache_beam-v2.65.0-prism-linux-amd64.zip
    
    
    
    
    
    
    # Install pyod for offline anomaly detectors
    pip install pyod==2.0.3

## Part 1: Running an Offline Isolation Forest Model

### Model Training
    
    
    # Download the sample data from GCS
    train_data_fn = "./shuttle.trn"
    ! gcloud storage cp "gs://apache-beam-samples/anomaly_detection/shuttle/shuttle.trn" {train_data_fn}
    
    
    
    
    
    
    
    import pandas as pd
    import pyod.models.iforest as iforest
    import pickle
    
    FIELD_NAMES = ["time", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "target"]
    SEP = " "
    df = pd.read_csv(train_data_fn, sep=" ", names=FIELD_NAMES)
    
    # We don't need the time and target field for training.
    train_data = df.drop(['time', 'target'], axis=1)
    train_data_np = train_data.to_numpy()
    
    # Training an isolation forest model
    my_iforest = iforest.IForest(random_state=1234)
    my_iforest.fit(train_data_np)
    
    # Save the model into a file
    iforest_pickled_fn = './iforest_pickled'
    with open(iforest_pickled_fn, 'wb') as fp:
      pickle.dump(my_iforest, fp)
    
    
    
    
    
    
    
    # Upload the pickled model file to GCS
    PICKLED_PATH = TEMP_ROOT + '/anomaly/iforest-notebook-' + SUFFIX + '/pickled'
    iforest_pickled_fn_gcs = PICKLED_PATH + '/iforest.pickled'
    
    ! gcloud storage cp {iforest_pickled_fn} {iforest_pickled_fn_gcs}
    
    
    
    
    

### Defining a Streaming Source and a DoFn for Model Metrics
    
    
    import math
    from typing import Any
    from collections.abc import Sequence
    
    import sklearn
    
    import apache_beam as beam
    from apache_beam.coders import PickleCoder
    from apache_beam.coders import VarIntCoder
    from apache_beam.transforms.periodicsequence import PeriodicImpulse
    from apache_beam.transforms.userstate import ReadModifyWriteStateSpec
    from apache_beam.transforms.window import FixedWindows
    from apache_beam.ml.anomaly.base import AnomalyResult
    
    class SequenceToPeriodicStream(beam.PTransform):
      """ A streaming source that generate periodic event based on a given sequence. """
      def __init__(self, data:Sequence[Any], delay: float = 0.1, repeat: bool = True):
        self._data = data
        self._delay = delay
        self._repeat = repeat
    
      class EmitOne(beam.DoFn):
        INDEX_SPEC = ReadModifyWriteStateSpec('index', VarIntCoder())
    
        def __init__(self, data, repeat):
          self._data = data
          self._repeat = repeat
          self._max_index = len(self._data)
    
        def process(self, element, model_state=beam.DoFn.StateParam(INDEX_SPEC)):
          index = model_state.read() or 0
          if index >= self._max_index:
            return
    
          yield self._data[index]
    
          index += 1
          if self._repeat:
            index %= self._max_index
          model_state.write(index)
    
      def expand(self, input):
        return (input | PeriodicImpulse(fire_interval=self._delay)
            | beam.Map(lambda x: (0, x))
            | beam.ParDo(SequenceToPeriodicStream.EmitOne(self._data, self._repeat))
            | beam.WindowInto(FixedWindows(self._delay)))
    
    
    class ComputeMetrics(beam.DoFn):
        """ A DoFn to compute Area Under Curve (AUC) """
        METRIC_STATE_INDEX = ReadModifyWriteStateSpec('saved_tracker', PickleCoder())
    
        def __init__(self, get_target):
            self._underlying: tuple[list[float], list[int]]
            self._get_target = get_target
    
        def process(self,
                  element: tuple[Any, AnomalyResult],
                  metric_state=beam.DoFn.StateParam(METRIC_STATE_INDEX),
                  **kwargs):
            self._underlying: tuple[list[float], list[int]] = metric_state.read()
            if self._underlying is None:
                scores = []
                labels = []
                targets = []
                self._underlying = (scores, labels, targets)
            else:
                scores, labels, targets = self._underlying
    
            prediction = next(iter(element[1].predictions))
            if math.isnan(prediction.score):
                yield element[0], beam.Row()
            else:
                # buffer the scores and targets for auc computation
                scores.append(prediction.score)
                labels.append(prediction.label)
                targets.append(self._get_target(element[1].example))
    
                accuracy = sklearn.metrics.accuracy_score(targets, labels)
                recall = sklearn.metrics.recall_score(targets, labels)
                precision = sklearn.metrics.precision_score(targets, labels)
                f1 = sklearn.metrics.f1_score(targets, labels)
                fpr, tpr, _ = sklearn.metrics.roc_curve(targets, scores)
                auc = sklearn.metrics.auc(fpr, tpr)
    
                yield element[0], beam.Row(id=element[1].example.id,
                                           target=element[1].example.target,
                                           predicted_label=next(iter(element[1].predictions)).label,
                                           predicted_score=next(iter(element[1].predictions)).score,
                                           accuracy=float(accuracy),
                                           recall=float(recall),
                                           precision=float(precision),
                                           f1=float(f1),
                                           auc=float(auc))
    
            metric_state.write(self._underlying)
    
    
    
    
    

### Preparing Test Data for Streaming
    
    
    # Download the data from GCS
    test_data_fn = "./test.trn"
    ! gcloud storage cp "gs://apache-beam-samples/anomaly_detection/shuttle/shuttle.tst" {test_data_fn}
    
    
    
    
    
    
    
    from apache_beam.io.filesystems import FileSystems
    import pandas as pd
    
    FIELD_NAMES = ["time", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "target"]
    SEP = " "
    with FileSystems().open(test_data_fn) as f:
      df = pd.read_csv(f, sep=" ", names=FIELD_NAMES)
      # just use first 500 instances for demo
      df = df[:500]
      rows = [row.to_dict() for _, row in df.iterrows()]
      for i, row in enumerate(rows):
        row["id"] = i
    
    # Dropping time and target for testing
    test_data_cols = FIELD_NAMES.copy()
    test_data_cols.remove("time")
    test_data_cols.remove("target")
    
    
    
    
    

### Constructing the Pipeline and Running with Prism
    
    
    from apache_beam.ml.anomaly.detectors.pyod_adapter import PyODFactory
    
    # Create detector for PyOd model pickled file
    detector = PyODFactory.create_detector(iforest_pickled_fn_gcs, features=test_data_cols)
    
    
    
    
    
    
    
    import apache_beam as beam
    from apache_beam.options.pipeline_options import PipelineOptions
    from apache_beam.ml.anomaly.transforms import AnomalyDetection
    from apache_beam.transforms.window import GlobalWindows
    from apache_beam.io import fileio
    
    import logging
    logging.getLogger().setLevel(logging.INFO)
    
    # Running the pipeline on prism
    options = PipelineOptions([
        "--streaming",
        "--job_server_timeout=600",
        "--environment_type=LOOPBACK",
        # TODO: remove --prism_location once 2.65 is released
        "--runner=PrismRunner", "--prism_location=./apache_beam-v2.65.0-prism-linux-amd64.zip"
    ])
    
    with beam.Pipeline(options=options) as p:
      _ = (p
           | SequenceToPeriodicStream(rows, delay=1, repeat=True)
           | beam.Map(lambda x: beam.Row(**x))
           | beam.WithKeys(0)
           | AnomalyDetection(detector=detector)
           | beam.WindowInto(GlobalWindows()) # put everything into global window to compute overall auc
           | beam.ParDo(ComputeMetrics(lambda x: 1 if x.target != 1 else 0))
           | beam.LogElements()
      )
    
    
    
    
    

### Alternative: Running the Pipeline with Dataflow Runner
    
    
    # Environment Variables for Dataflow Runner
    TEMP_LOCATION = TEMP_ROOT + '/anomaly/iforest-notebook-' + SUFFIX + '/temp'
    STAGING_LOCATION = TEMP_ROOT + '/anomaly/iforest-notebook-' + SUFFIX + '/staging'
    
    
    
    
    
    
    
    # For running with dataflow runner
    pip install 'apache_beam[gcp, interactive]=={BEAM_VERSION}' --quiet
    
    
    # Running the pipeline on dataflow
    options = PipelineOptions([
      "--runner=DataflowRunner",
      "--temp_location=" + TEMP_LOCATION,
      "--staging_location=" + STAGING_LOCATION,
      "--project=" + PROJECT_ID,
      "--region=" + REGION,
      "--extra_package=gs://shunping-test/anomaly-temp/pyod-2.0.3.tar.gz",
    ])
    
    with beam.Pipeline(options=options) as p:
      _ = (p
           | SequenceToPeriodicStream(rows, delay=1, repeat=True)
           | beam.Map(lambda x: beam.Row(**x))
           | beam.WithKeys(0)
           | AnomalyDetection(detector=detector)
           | beam.WindowInto(GlobalWindows()) # put everything into global window to compute overall auc
           | beam.ParDo(ComputeMetrics(lambda x: 1 if x.target != 1 else 0))
           | beam.LogElements()
      )
    
    
    
    
    

## Part 2: Running an Ensemble of Models

### Another Model Training
    
    
    from pyod.models.loda import LODA
    
    my_lof = LODA()
    my_lof.fit(train_data_np)
    
    
    
    
    
    
    
    # Save the model into a file
    lof_pickled_fn = './lof_pickled'
    with open(lof_pickled_fn, 'wb') as fp:
      pickle.dump(my_lof, fp)
    
    # Write to GCS
    lof_pickled_fn_gcs = PICKLED_PATH + '/lof.pickled'
    
    ! gcloud storage cp {lof_pickled_fn} {lof_pickled_fn_gcs}
    
    
    
    
    
    
    
    # Create detector for PyOd model pickled file
    detector1 = PyODFactory.create_detector(iforest_pickled_fn_gcs, features=test_data_cols, model_id="iforest")
    detector2 = PyODFactory.create_detector(lof_pickled_fn_gcs, features=test_data_cols, model_id="lof")
    
    
    
    
    

### Run an Ensemble Anomaly Detector
    
    
    from apache_beam.ml.anomaly.base import EnsembleAnomalyDetector
    from apache_beam.ml.anomaly.aggregations import AnyVote
    
    # Running the pipeline on prism
    options = PipelineOptions([
        "--streaming",
        "--job_server_timeout=600",
        "--environment_type=LOOPBACK",
        # TODO: remove --prism_location once 2.65 is released
        "--runner=PrismRunner", "--prism_location=./apache_beam-v2.65.0-prism-linux-amd64.zip"
    ])
    
    with beam.Pipeline(options=options) as p:
      _ = (p
           | SequenceToPeriodicStream(rows, delay=1, repeat=True)
           | beam.Map(lambda x: beam.Row(**x))
           | beam.WithKeys(0)
           | AnomalyDetection(detector=EnsembleAnomalyDetector([detector1, detector2],
                                                               aggregation_strategy=AnyVote()))
           | beam.LogElements()
      )
    
    
    
    
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
