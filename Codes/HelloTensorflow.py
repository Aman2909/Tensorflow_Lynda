import tensorflow as tf
msg=tf.string_join(['Hello ',"I'm ", "learning ","TensorFlow!"])

with tf.Session() as sess:
    print(sess.run(msg))