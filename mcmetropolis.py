"""
8/3/17
Take this code with a pinch of salt, it is the closest fitting implementation
from a quick web search. I haven't edited yet to fit in with our code!

"""


def metropolis(init, iters):
    """
    based on http://www.cs.toronto.edu/~asamir/cifar/rpa-tutorial.pdf
    
    can take several minutes to run with large sample sizes.
    """
    dist = joint_dist()

    # set up empty sample holder
    D = len(init)
    samples = np.zeros((D, iters))

    # initialize state and log-likelihood
    state = init.copy()
    Lp_state = dist.loglike(state)

    accepts = 0
    for i in np.arange(0, iters):
        
        # propose a new state
        prop = np.random.multivariate_normal(state.ravel(), np.eye(10)).reshape(D, 1)

        Lp_prop = dist.loglike(prop)
        rand = np.random.rand()
        if np.log(rand) < (Lp_prop - Lp_state):
            accepts += 1
            state = prop.copy()
            Lp_state = Lp_prop

        samples[:, i] = state.copy().ravel()
        
        # if i % 1000 == 0: print i

    print 'Acceptance ratio', accepts/iters
    return samples
