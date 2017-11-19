import tensorflow as tf
#tensor is a multidimentinal array/matrix
#build a simple computational graph
#each node takes 0+ tensors as inputs and creates a tensor outputs
#one type of node is a constant- mo input, outputs constant
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)#dtype=tf.float32 automatic

print(node1, node2)
#prints the node, not value

#add/sub nodes
node3 = tf.add(node1, node2)
node4 = tf.subtract(node1, node2)

#constant is boring, placeholders is a promise to provide a value later
#the values entered are fkn tensors
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b
#nested nodes
add_then_trip = 3 * adder_node

#wtf does this have to do with ml? modify the graph to get
#different outputs with the exact same input. Variables time
W = tf.Variable([.3], dtype=tf.float32)
c = tf.Variable([-.3])
x = tf.placeholder(tf.float32)
linear_model=W*x+c
#yay, we got a simple way to caculate .3x + -.3
#thats retarded, lets actually fix the line a bit maybe
#y = correct values, square the diffrences from results, reduce sum sums
#the squared errors to create a single scalar that abstracts the error of all examples using
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model-y)
loss = tf.reduce_sum(squared_deltas)
#thats great, now lets make an Optimizer - slowly changes variables to minimize loss
#simplest = GradientDescent,
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)


#need sesstion to print value
sess = tf.Session()
print(sess.run([node1, node2]))
print(sess.run([node3, node4]))
print(sess.run(adder_node, {a: 1, b: 2}))
print(sess.run(adder_node, {a: [1, 0], b: [2,4]}))
print(sess.run(add_then_trip, {a: 1, b: 2}))
print(sess.run(add_then_trip, {a: [1, 0], b: [2,4]}))
print('let get real :)')
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(linear_model, {x: [1, 2, 3, 4]}))
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))
print('kek, it should be a y = 1 - x duhhh')
fixW = tf.assign(W, [-1.])
fixb = tf.assign(c, [1.])
sess.run([fixW, fixb])
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))
print('lets train this boi')
for i in range(1000):
    sess.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})
print(sess.run([W, c]))
