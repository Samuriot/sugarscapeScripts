import json
import sys
import glob
import matplotlib.pyplot as plt

def load_json (filename):
    with open(filename, 'r') as file:
        return json.load(file)

def load_data (json_data):
    timesteps = [entry["timestep"] for entry in json_data]
    population = [entry["population"] for entry in json_data]
    agent_disease_deaths = [entry["agentDiseaseDeaths"] for entry in json_data]
    sick_agents = [entry["sickAgentsPercentage"] for entry in json_data]
    return timesteps, population, agent_disease_deaths, sick_agents

def plot_population (timesteps, population, filename, subdirectory):
    plt.plot(timesteps, population, linestyle='-', label='Population', color="blue")
    plt.xlabel('Timestep')
    plt.ylabel('Population')
    plt.title('Population over Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"./{subdirectory}/{filename}_population.png")
    plt.cla()

def plot_disease_deaths (timesteps, agent_deaths, filename, subdirectory):
    plt.plot(timesteps, agent_deaths, linestyle='-', label='Population', color="red")
    plt.xlabel('Timestep')
    plt.ylabel('Deaths')
    plt.title('Deaths over Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"./{subdirectory}/{filename}_disease_deaths.png")
    plt.cla()

def plot_incidence (timesteps, incidence, filename, subdirectory):
    plt.plot(timesteps, incidence, linestyle='-', label='Population', color="green")
    plt.xlabel('Timestep')
    plt.ylabel('Sick (%)')
    plt.title('Sick Percentage over Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"./{subdirectory}/{filename}_sick_percentage.png")
    plt.cla()

def find_subdirectory (arg):
    if arg == "m":
        return "lessDeadlyResults"
    elif arg == "x":
        return "deadlyDiseaseResults"
    else:
        return "defaultResults"

if __name__ == "__main__":
    subdirectory, startingDiseases = find_subdirectory(sys.argv[2]), sys.argv[1]
    input_file = f"./{subdirectory}/average_log_{startingDiseases}.json"
    
    json = load_json(input_file)
    timesteps, population, agent_deaths, sick_agents = load_data(json)
    plot_population(timesteps, population, startingDiseases, subdirectory) 
    plot_disease_deaths(timesteps, agent_deaths, startingDiseases, subdirectory)
    plot_incidence(timesteps, sick_agents, startingDiseases, subdirectory)