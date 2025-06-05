import sys
import glob
import json

def open_file (filename):
    with open(filename, 'r') as file:
        return json.load(file)

def accumulate (file_list):
    total_map = {}
    for filename in file_list:
        entries = open_file(filename)

        for entry in entries:
            t = entry["timestep"]
            if t not in total_map:
                total_map[t] = {"count": 0}
            total_map[t]["count"] += 1
            
            for k, val in entry.items():
                if k == "timestep":
                    continue
                sum_key = f"{k}_sum"
                total_map[t].setdefault(sum_key, 0)
                total_map[t][sum_key] += val
            
    return total_map

def average (total_results, allowed_keys):
    average_results = []
    for t in sorted(total_results.keys()):
        info = {"timestep": t}
        count = total_results[t]["count"]
        for sum_key, total in total_results[t].items():
            if sum_key == "count":
                continue
            field = sum_key.replace("_sum", "")
            if field in allowed_keys:
                info[field] = total / count
            
        average_results.append(info)
    
    return average_results

def find_subdirectory (arg):
    if arg == "m":
        return "lessDeadlyResults"
    elif arg == "x":
        return "deadlyDiseaseResults"
    else:
        return "defaultResults"

if __name__ == "__main__":
    allowed_keys = {"timestep", "population", "agentDiseaseDeaths", "sickAgentsPercentage"}
    subdirectory, startingDiseases = find_subdirectory(sys.argv[2]), sys.argv[1]
    output_file = f"./{subdirectory}/average_log_{startingDiseases}.json"

    file_list = sorted(glob.glob(f"./{subdirectory}/log_{startingDiseases}_*.json"))
    total_results = accumulate(file_list)
    average_results = average(total_results, allowed_keys)
    with open(output_file, "w") as outfile:
        json.dump(average_results, outfile, indent=2)