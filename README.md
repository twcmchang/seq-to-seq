
# Quick start
- This is the implementation of "Sequence-to-Sequence: Video to Text" in TensorFlow
- To demonstrate the results, there are two videos and the corresponding features in data/testing_data/
- Please run the following script to download my codes and the trained model

```
git clone https://github.com/twcmchang/seq-to-seq.git
```

Download the trained model and test two sampled videos

```
bash run.sh data/sample_testing_id.txt data/testing_data/
```

If you would like to evaluate the BLUE of the generated captions:

```
python3 eval.py --result_file output.json
```




# (1) Train (not support now)
Put training data into data/.
```
python train.py
```
### Default setting
|**Network parameter**| **```n_lstm_step```** | **```n_video_step```** | **```n_caption_step```** | **```dim_image```** | **```dim_hidden```** |
|:-------:|:----:|:----:|:----:|:----:|:----:|
|Default  |  80  |  80  |  20  | 4096 | 1000 |
|**Training parameter** | **```n_epoch```** | **```batch_size```** | **```learning_rate```** | **```grad_clip```** ||
|Default | 1000 |  50  | 0.001 |  10  ||

The model and checkpoint will be stored in save/.

### Schedule sampling (default: 0.0)
Enter an initial sampling probability as follow.
```
python train.py --schedule_sampling 0.01
```
Sampling probability is designed to increase (1+N) times after 50*N epochs.

# (2) Test
```
python test.py
```
|**Argument**| **```testing_file```** | **```testing_path```** | **```result_file```** | **```init_from```** | 
|:-------:|:----:|:----:|:----:|:----:|
|Default  |data/sample_testing_id.txt|data_data/testing_data/|output.json|save/| 

If would like to specify testing_file and testing_path,
```
python test.py --testing_file "your_testing_id.txt" --testing_path "your_testing_feat_path"
```

# (3) Evaluate
```
python eval.py --result_file "your_output_json" --test_label_json "your_answer_json"
```
|**Argument**| **```test_label_json```** | **```result_file```** | 
|:-------:|:----:|:----:|
|Default  |data/testing_public_label.json| output.json|

Current best average BLEU score: 0.274922 after 1000 epochs

### Requirement
- Download [dataset][dataset] and unzip it into hw2/
- Tensorflow r1.0+
