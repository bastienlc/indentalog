from time import sleep

from indentalog import ilog


@ilog(name="Training")
def train():
    for epoch in ilog(range(2), name="Epochs"):
        for batch in ilog(range(5), name="Train batches"):
            with ilog(name="Forward pass"):
                # Your code here
                pass
                sleep(0.2)
            with ilog(name="Backward pass"):
                # Your code here
                pass
                sleep(0.2)
            sleep(0.1)

        for batch in ilog(range(5), name="Validation batches"):
            with ilog(name="Forward pass"):
                # Your code here
                pass
                sleep(0.2)
            with ilog(name="Compute metrics"):
                # Your code here
                pass
                sleep(0.2)
            sleep(0.1)


with ilog(name="Initializing model and data"):
    # Your code here
    pass

train()
