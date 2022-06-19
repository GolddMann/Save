import numpy as np


def sigmoid(x):
    # Наша функция активации: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))


def deriv_sigmoid(x):
    fx = sigmoid(x)
    return fx * (1 - fx)


def mse_loss(y_true, y_pred):
    return ((y_true - y_pred)**2).mean()


class Network:
    def __init__(self):
        self.ws = np.array([np.random.normal() for _ in range(6)])
        self.biases = np.array([np.random.normal() for _ in range(3)])

    def feedforward(self, x):
        hs = [0]*2

        for i in range(2):
            hs[i] = sigmoid(self.ws[i*2] * x[0] +
                            self.ws[i*2 + 1]*x[1] + self.biases[i])

        return sigmoid(self.ws[4] * hs[0] + self.ws[5]*hs[1] + self.biases[2])

    def train(self, data, all_y_trues):
        learn_rate = 0.1
        epochs = 10000
        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                hs = [0]*2
                a_hs = [0]*2

                for i in range(2):
                    hs[i] = self.ws[i*2] * x[0] + \
                        self.ws[i*2+1]*x[1] + self.biases[i]
                    a_hs[i] = sigmoid(hs[i])

                o1 = self.ws[4]*a_hs[0] + self.ws[5]*a_hs[1] + self.biases[2]
                a_o1 = sigmoid(o1)
                y_pred = a_o1

                d_L_d_ypred = -2*(y_true - y_pred)
                d_h_d_w = []

                for i in range(2):
                    a = []
                    for j in range(2):
                        a.append(x[j]*deriv_sigmoid(hs[i]))
                    a.append(deriv_sigmoid(hs[i]))
                    d_h_d_w.append(a)

                d_ypred_d_h = [self.ws[4] *
                               deriv_sigmoid(hs[0]), self.ws[5]*deriv_sigmoid(0), 1]

                d_ypred_d_w = [
                    a_hs[0]*deriv_sigmoid(o1), a_hs[1]*deriv_sigmoid(o1), deriv_sigmoid(o1)]

                for i in range(6):
                    if i < 4:
                        self.ws[i] -= learn_rate*d_L_d_ypred * \
                            d_ypred_d_h[i//2]*d_h_d_w[i//2][i//2]
                    else:
                        self.ws[i] -= learn_rate * \
                            d_L_d_ypred*d_ypred_d_w[(i+1)//3]

                for i in range(3):
                    if i < 2:
                        self.biases[i] -= learn_rate*d_L_d_ypred * \
                            d_ypred_d_h[i]*d_h_d_w[i][2]
                    else:
                        self.biases[i] -= learn_rate*d_L_d_ypred*d_ypred_d_w[i]

            if epoch % 10 == 0:
                y_pred = np.apply_along_axis(self.feedforward, 1, data)
                loss = mse_loss(all_y_trues, y_pred)
                print("Epoch %d loss: %.3f" % (epoch, loss))


if __name__ == "__main__":
    data = np.array([
        [-2, -1],
        [25, 6],
        [17, 4],
        [-15, -6]
    ])

    all_y_trues = np.array([
        1,
        0,
        0,
        1
    ])

    network = Network()
    network.train(data, all_y_trues)

    x = np.array([-2, -1])
    y = np.array([17, 4])
    a_x = network.feedforward(x)
    a_y = network.feedforward(y)
    print(a_x)
    print(a_y)

    if(a_x > 0.9):
        print("it knows that it's a woman")
    else:
        print("They to learn again")

    if(a_y < 0.1):
        print("It knows that it's a man")
    else:
        print("Try to learn again")
