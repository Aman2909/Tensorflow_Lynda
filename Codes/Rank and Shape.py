'''Rank
The rank of a tf.Tensor object is its number of dimensions.
Synonyms for rank include order or degree or n-dimension.
Note that rank in TensorFlow is not the same as matrix rank in mathematics.
As the following table shows, each rank in TensorFlow corresponds to a different mathematical entity:

Rank	Math entity
0	Scalar (magnitude only)
1	Vector (magnitude and direction)
2	Matrix (table of numbers)
3	3-Tensor (cube of numbers)
n	n-Tensor (you get the idea)
'''

import  tensorflow as tf
mammal = tf.Variable("Elephant",tf.string)
count = tf.Variable(456,tf.int16)
count2 = tf.Variable(1,tf.int16)
weight= tf.Variable(346.21, tf.float16)
complex = tf.Variable(12.6 - 32j,tf.complex64)

r=tf.rank(mammal)
#t1=count + count2 ERROR!
#r=tf.rank(mammal)

squarish_squares = tf.Variable([ [4, 9], [16, 25] ], tf.int32)
rank_of_squares = tf.rank(squarish_squares)

#t1=tf.zeros([1,2,3,4])
#t1=tf.zeros([1,3,3,4])
#t1=tf.zeros([3,4])
#mymat = tf.Variable([[7],[11]], tf.int16)

with tf.Session() as sess:
    #print(sess.run(r))
    #print(sess.run(t1)) ERROR!
    #print(sess.run(rank_of_squares))
    #print(sess.run(t1))
    #print(sess.run(mymat)) - ERROR!



