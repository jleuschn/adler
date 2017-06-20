import demandimport
with demandimport.enabled():
    import tensorflow as tf


def leaky_relu(_x, alpha=0.2, name='leaky_relu'):
    return prelu(_x, init=alpha, name=name, trainable=False)


def prelu(_x, init=0.0, name='prelu', trainable=True):
    with tf.variable_scope(name):
        alphas = tf.get_variable('alphas',
                                 shape=[int(_x.get_shape()[-1])],
                                 initializer=tf.constant_initializer(init),
                                 dtype=tf.float32,
                                 trainable=True)
        pos = tf.nn.relu(_x)
        neg = -alphas * tf.nn.relu(-_x)

        return pos + neg
