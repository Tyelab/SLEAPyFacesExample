#%%
%python3 -m pip install sleapyfaces==1.2.0b2.dev10
#%%
from sleapyfaces.base import Project

proj = Project(
    ExperimentEventsFile=("*events.csv", True),
    ExperimentSetupFile=("*.json", True),
    SLEAPFile=("*.h5", True),
    VideoFile=("*.mp4", True),
    base="/Volumes/LaCie/2p/raw/CSE014",
    name="SLEAPyFacesExample"
)

proj.buildColumns(columns=["Mouse"], values=["CSE014"])
proj.buildTrials(TrackedData=["Speaker_on", "LED590_on"], Reduced=[False, True])
proj.visualize(3)

#%%
from sleapyfaces.clustering import FeatureExtractor

fe = FeatureExtractor(proj, base_features=["eye", "ear", "mouth", "nostril", "whisker"])
fe.twoCentroidsDist("eye", "mouth", inplace=True)

#%%
from sleapyfaces.clustering import Cluster

clust = Cluster(fe, prediction_column="Trial")
clust.kmeans()

# %% Example of how to utilizes individual co
from sleapyfaces.utils import into_trial_format
trials = into_trial_format(proj.all_data, trial_types=["sucrose", "airpuff", "sucrose", "sucrose", "led" ...], trial_start_index=[1, 22, 46, 67 ...], trial_end_index=[21, 45, 66, 87 ...])
