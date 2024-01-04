# beginning of cv model
import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart")

# collects from the user/fiftyone/... file path - run through command line, doesn't like .ipynb

session = fo.launch_app(dataset, port=5151)
session.dataset = dataset


session.wait()