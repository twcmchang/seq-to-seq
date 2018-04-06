"""
To run on the latest version of TensorFlow, we have to modify variable names as follow.

Reference: https://github.com/KranthiGV/Pretrained-Show-and-Tell-model/issues/7
"""

print("To run on the latest version of TensorFlow, we are modifying variable names in LSTM.")

OLD_CHECKPOINT_FILE = "save/model.ckpt-990"
NEW_CHECKPOINT_FILE = "save/model.ckpt-990"

import tensorflow as tf
vars_to_rename = {
    "LSTM1/basic_lstm_cell/weights": "LSTM1/basic_lstm_cell/kernel",
    "LSTM1/basic_lstm_cell/biases": "LSTM1/basic_lstm_cell/bias",
    "LSTM2/basic_lstm_cell/weights": "LSTM2/basic_lstm_cell/kernel",
    "LSTM2/basic_lstm_cell/biases": "LSTM2/basic_lstm_cell/bias",
}
new_checkpoint_vars = {}
reader = tf.train.NewCheckpointReader(OLD_CHECKPOINT_FILE)
for old_name in reader.get_variable_to_shape_map():
  if old_name in vars_to_rename:
    new_name = vars_to_rename[old_name]
  else:
    new_name = old_name
  new_checkpoint_vars[new_name] = tf.Variable(reader.get_tensor(old_name))

init = tf.global_variables_initializer()
saver = tf.train.Saver(new_checkpoint_vars)

with tf.Session() as sess:
  sess.run(init)
  saver.save(sess, NEW_CHECKPOINT_FILE)