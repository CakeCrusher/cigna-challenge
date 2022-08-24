import pandas as pd
import os

# import data
data_df = pd.read_csv('./data.csv')

# generate the min, max, and avrage for each host and an aggrage for all hosts
data_df_no_dt = data_df.drop(['Date / Time'], axis=1)
mins = data_df_no_dt.min()
all_min = mins.min()
maxs = data_df_no_dt.max()
all_max = mins.max()
means = data_df_no_dt.mean()
all_mean = mins.mean()

# produce a pandas dataframe
columns = ["descriptions", "all"] + list(data_df_no_dt.columns)
data = [
    ["min", all_min] + list(mins),
    ["max", all_max] + list(maxs),
    ["mean", all_mean] + list(means)
]

output_df = pd.DataFrame(data, columns=columns)
output_df = output_df.set_index("descriptions")

# print stdout of output
output_stdout = output_df.to_string()
print(output_stdout)

# format output for json
output_df_json = output_df.reset_index()
output_df_json = output_df_json.to_dict()
def mapped_dict(d):
    return {"min": d[0], "max": d[1], "mean": d[2]}
output_df_json = { k: mapped_dict(output_df_json[k]) for k, v in output_df_json.items()}
output_df_json.pop("descriptions")

# save output as csv and json under outputs directory
if not os.path.exists('./outputs'):
    os.makedirs('./outputs')

output_df.to_csv('./outputs/output.csv')
output_df.to_json('./outputs/output.json')